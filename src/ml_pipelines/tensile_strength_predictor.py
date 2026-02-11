"""
Tensile & Yield Strength Prediction Pipeline (Su, Sy) - Corrected ANN

Dataset:
data/materials_data/material.csv

Inputs:
- E  (Young's Modulus)
- G  (Shear Modulus)
- mu (Poisson Ratio)
- Ro (Density)

Targets:
- Su (Ultimate Tensile Strength)
- Sy (Yield Strength)

Models:
- RandomForestRegressor
- Multi-Layer Perceptron (MLP, corrected)

Artifacts Saved:
- models/tensile_rf_model.pkl
- models/tensile_mlp_model.keras
- models/tensile_x_scaler.pkl
- models/tensile_y_scaler.pkl
- models/tensile_features.json

Plots Saved:
- plots/tensile_parity_*.png
- plots/tensile_residual_*.png
"""

import pandas as pd
import numpy as np
import joblib
import os
import json
import logging
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor

from keras import layers, models, callbacks, optimizers

# -----------------------------
# CONFIG
# -----------------------------

DATA_PATH = "data/materials_data/material.csv"

MODEL_RF_PATH = "models/tensile_rf_model.pkl"
MODEL_MLP_PATH = "models/tensile_mlp_model.keras"
X_SCALER_PATH = "models/tensile_x_scaler.pkl"
Y_SCALER_PATH = "models/tensile_y_scaler.pkl"
FEATURE_PATH = "models/tensile_features.json"

PLOT_DIR = "plots"

os.makedirs("models", exist_ok=True)
os.makedirs(PLOT_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# -----------------------------
# LOAD & CLEAN
# -----------------------------

def load_and_prepare_data():
    df = pd.read_csv(DATA_PATH)
    log.info(f"Loaded dataset: {df.shape[0]} rows")

    # Drop duplicates
    df = df.drop_duplicates()

    # Features / Targets
    feature_cols = ["E", "G", "mu", "Ro"]
    target_cols = ["Su", "Sy"]

    df = df.dropna(subset=feature_cols + target_cols)

    X = df[feature_cols].astype(float)
    y = df[target_cols].astype(float)

    log.info(f"Training using {len(X)} samples")
    return X, y, feature_cols, target_cols

# -----------------------------
# RANDOM FOREST MODEL
# -----------------------------

def train_random_forest(X_train, X_test, y_train, y_test):
    rf = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    for i, col in enumerate(y_train.columns):
        mae = mean_absolute_error(y_test.iloc[:, i], y_pred[:, i])
        r2 = r2_score(y_test.iloc[:, i], y_pred[:, i])
        log.info(f"RF {col}: MAE = {mae:.2f}, R² = {r2:.3f}")

    joblib.dump(rf, MODEL_RF_PATH)
    log.info(f"Saved Random Forest → {MODEL_RF_PATH}")
    return y_pred

# -----------------------------
# CORRECTED MLP MODEL
# -----------------------------

def build_mlp(n_in, h1=128, h2=64, dropout=0.2, lr=1e-3):
    model = models.Sequential([
        layers.Input(shape=(n_in,)),
        layers.Dense(h1, activation='relu'),
        layers.Dropout(dropout),
        layers.Dense(h2, activation='relu'),
        layers.Dense(2)  # Two targets: Su, Sy
    ])
    model.compile(optimizer=optimizers.Adam(learning_rate=lr), loss='mae')
    return model

def train_mlp(X_train, X_test, y_train, y_test):
    # --- Scale X properly ---
    x_scaler = StandardScaler().fit(X_train)
    Xtr = x_scaler.transform(X_train)
    Xte = x_scaler.transform(X_test)

    # --- Scale y to [0,1] ---
    y_scaler = MinMaxScaler().fit(y_train)
    ytr = y_scaler.transform(y_train)
    yte = y_scaler.transform(y_test)

    mlp = build_mlp(Xtr.shape[1])

    early_stop = callbacks.EarlyStopping(
        monitor='val_loss',
        patience=20,
        restore_best_weights=True
    )

    history = mlp.fit(
        Xtr, ytr,
        validation_data=(Xte, yte),
        epochs=500,
        batch_size=32,
        callbacks=[early_stop],
        verbose=0
    )

    y_pred_scaled = mlp.predict(Xte)
    y_pred = y_scaler.inverse_transform(y_pred_scaled)

    for i, col in enumerate(y_train.columns):
        mae = mean_absolute_error(y_test.iloc[:, i], y_pred[:, i])
        r2 = r2_score(y_test.iloc[:, i], y_pred[:, i])
        log.info(f"MLP {col}: MAE = {mae:.2f}, R² = {r2:.3f}")

    # Save models and scalers
    mlp.save(MODEL_MLP_PATH)
    joblib.dump(x_scaler, X_SCALER_PATH)
    joblib.dump(y_scaler, Y_SCALER_PATH)
    log.info(f"Saved MLP → {MODEL_MLP_PATH}")
    log.info(f"Saved X Scaler → {X_SCALER_PATH}")
    log.info(f"Saved Y Scaler → {Y_SCALER_PATH}")

    return y_pred

# -----------------------------
# VISUALIZATION
# -----------------------------

def parity_plot(y_true, y_pred, title, filename):
    plt.figure(figsize=(6, 5))
    plt.scatter(y_true, y_pred, alpha=0.6)
    plt.plot([y_true.min(), y_true.max()],
             [y_true.min(), y_true.max()],
             'r--')
    plt.title(title)
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def residual_plot(y_true, y_pred, title, filename):
    residuals = y_true - y_pred
    plt.figure(figsize=(6, 5))
    plt.scatter(y_true, residuals, alpha=0.6)
    plt.axhline(0, color='r', linestyle='--')
    plt.title(title)
    plt.xlabel("True")
    plt.ylabel("Residual")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    X, y, feature_cols, target_cols = load_and_prepare_data()

    # Save feature list
    with open(FEATURE_PATH, "w") as f:
        json.dump(feature_cols, f)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------- Random Forest --------
    rf_preds = train_random_forest(X_train, X_test, y_train, y_test)

    # -------- Corrected MLP --------
    mlp_preds = train_mlp(X_train, X_test, y_train, y_test)

    # -------- Plots --------
    for i, col in enumerate(target_cols):
        parity_plot(
            y_test.iloc[:, i].values,
            mlp_preds[:, i],
            title=f"{col} — MLP Parity Plot",
            filename=f"{PLOT_DIR}/tensile_parity_{col}.png"
        )
        residual_plot(
            y_test.iloc[:, i].values,
            mlp_preds[:, i],
            title=f"{col} — MLP Residual Plot",
            filename=f"{PLOT_DIR}/tensile_residual_{col}.png"
        )

    # Optional: MAPE / Accuracy summary
    for i, col in enumerate(target_cols):
        mape = mean_absolute_percentage_error(y_test.iloc[:, i], mlp_preds[:, i]) * 100
        acc = 100 - mape
        log.info(f"MAPE for {col}: {mape:.2f}% → Accuracy: {acc:.2f}%")

    log.info("Tensile strength training complete.")