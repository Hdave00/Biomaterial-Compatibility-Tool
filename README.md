# Biomaterial-Selection-and-Bioinformatics-Tool

## NOTE-- This README is incomplete as of now, basic operational instructions only, complete details coming very soon!

A modern Streamlit-based biomaterials intelligence platform combining:

* **Local database search** (details coming soon...)
* **Materials Project API integration** (real-time crystal structure, elasticity, magnetism, bonding, oxidation, and thermodynamic data) details coming soon
* **3D structure visualization** using **py3Dmol**
    - Visualisation not yet implemented for 3D Structures of elements/materials, more details coming soon...
* **Machine-learning pipelines** for structure prediction (details coming ...)

This project is part of a larger effort to build an intelligent decision-support system for materials science and biomaterials engineering.

It is meant to be a working prototype for a vision of merging the highly interconnected and interdisciplinary domains of Bioinformatics, Biofabrication and Biotechnology. Using the foundational principles of Material Science, Rheology, Biomedical Engineering, Machine Learning, Data Science/Data Modelling and Computer Engineering, the project aims to provide a link between rapid prototyping & research, and the eventual project structuring phase for ALL 3 primary domains by providing a platform that unifies a researcher/student/professional's workflow.
This platform is being built from the ground up, taking into account the amount of time lost in pruning data, building models, querying multiple different platforms for the same purpose, having to create multiple online accounts and the hassle that comes in the world of research & academia to find a unified workflow for a specific domain, for researchers and students alike. 
Think of it as different limbs of a single body, being able to have "minds of their own", rather than multiple different bodies inefficiently trying to communicate for one singular purpose. 

By combining inter-related domains that are highly relevant and co-dependant on each of the 3 domains of Bioinformatics, Material Science Research and Biotechnology, the platform is unified in its purpose to only provide the data, machine learning tools, journaling and data modelling/data visualisation related to those fields that are shaping our future in not only a theoretical sense, but a tangible way that aids humanity greatly through the combined efforts of many.

It comprises of being able to provide cleaned datasets for query and data visualization, machine learning models for predictions and live compatibility confirmations accross all 3 domains. 

This is but a fraction of what those 3 "parent domains" are concerned with, there is much more to each one of those domains. For example, Biotechnology has sub domains in more than just the medical sense, the emergence of novel food sciences and sustainable advances in lab farming for better yeilds in the challenging climate we face today are also due to the immense efforts made by people in that field, and that domain too could be integrated in such a platform to streamline research and create relevant tools which could greatly aid that domain, if it was to be scaled up using a different framework.


---

Platform is live on Streamlit!

[Visit The app on Streamlit](https://biomat-test-inuxwupzxu4apppplsy93ya2.streamlit.app/)

---

## Datasets and citation

The datasets for this project can be found mainly at [Kaggle](https://www.kaggle.com/). I have used different datasets for different purposes, mainly the two domains of Machine Learning and a Search/Lookup functionality of data representation and visualisation.

1. [Young's Modulus of Metals](https://www.kaggle.com/datasets/kanchana1990/youngs-modulus-of-metals) dataset for gathering and training the ML model to perform a regression task on predicting the potential young's modulus of metals given the following input parameters:
  - Density (g/cm³)
  - Hardness (BHN)
  - Tensile Strength (MPa)
  - Yield Strength (MPa)
  - Elongation (%)
  - Poisson’s Ratio
  - Hardness (HV)
  - Shear Modulus (GPa)

2. [RCSB_PDB Human Macromolecular Structure Dataset](https://www.kaggle.com/datasets/samiraalipour/rcsb-pdb-macromolecular-structure-dataset/data) for a protein structure database, used in the Oligomeric State Prediction task. This is a multi-task supervised learning model that performs classification and regression simultaneously to predict the oligomeric state (monomer, dimer, trimer, etc.) for a protein, given the following features of a protein:
  - Number of Chains: The number of distinct chains in the protein structure.
  - Helix Count: The number of alpha helices in the protein structure.
  - Coil Count: The number of coil (random coil) regions in the protein structure.
  - Molecular Weight per Deposited Model: The molecular weight of the entire protein structure, including all chains.
  - Stoichiometry: The ratio of components in the protein assembly.

3. [Materials and Their Mechanical Properties](https://www.kaggle.com/datasets/purushottamnawale/materials/data) is used to feed data to lookup table, and a machine learning model, the model learns to predict properties of a metal, given certain data points/parameters. This dataset mainly includes industrial alloys for Machine Design and their mechanical properties. This can still be adapted quite aptly for machine learning tasks and especially, given the detailed and complete nature of the dataset, for material selection in a myriad of contexts including material compatibility with biological specimen.

4. [High Entropy Alloys](https://www.kaggle.com/datasets/sethpointaverage/high-entropy-alloys-properties), is a more complicated dataset because of the nature of what High Entropy Alloys are. They are included both in the lookup pipeline, and in the ML architecture to infer from. This is because, HEA are quite dependant on their manufacturing technique, which in turn determines almost every aspect of the alloy. Whereas traditional alloys are mainly Binary or Trinary, HEA are atleast alloys of 5 or more elements. There are some properties of HEA like the microstructure, grain size, density, and gas content (Oxygen, Nitrogen and Carbon). These aspects/properties of HEA are again, not only dependant on the alloys themselves but also the processing method. This unique crystal lattice structure and the "uniformly random" atomic matrix, makes them a very viable avenue for Biomaterial usage (due to highly tunable density, molecular structure and control over gasses trapped within the lattice) and for the discovery of not only newer alloys, but also inter-mingling them with different families of materials such as polymers and elemental metals to find more use cases in other domains of material science.
These novel materials break the traditional logic of materials in a quite a fundamental way, and allow us to change the approach to how we view materials. For example, HEA can be hard, but not really brittle, rather flexible. Metal that can be ductile enough to conform into shape, but be able to score tempered glass. Some HEA can even be created in a specific environment with specific methods to even be Super-Paramagnetic or also be tuned to become Nano particle Catalysts. This is why, it is important to consider HEA and design the material ML pipeline to infer and predict the properties of such materials in various contexts. Some of the properties listed in the dataset are:

- Microstructure: The experimentally observed phases (e.g. FCC, BCC, B2). Any phases that were not BCC, FCC, HCP, L12, B2, or Laves were labeled as “Sec. = secondary” or “Other”.
- Processing method: The conditions under which the alloy was synthesized. CAST = as-cast or directional casting. POWDER = gas atomization, mechanical alloying, sintering, spark plasma sintering, or vacuum hot pressing. WROUGHT = cold-rolled, hot-rolled, or hot-forged. ANNEAL = annealed, homogenized, or aged. OTHER = additive manufacturing, hot isostatic pressing, or severe plastic deformation.
- Grain size (μm): The average grain size of the alloy.
- Exp. Density (g/cm3): Experimentally reported density.
- Calculated Density (g/cm3): Density estimated using the rule of mixtures (ROM):
where xi, Mi, Vi are the atomic fraction, molar mass and molar volume of the element i. Elemental density values were obtained via Pymatgen22.
- Test temperature (°C): Temperature at which mechanical testing was performed.
- Exp. Young’s modulus (GPa): The experimental Young’s modulus, when reported.
- Calculated Young’s modulus (GPa) Young’s modulus calculated using the rule of mixtures (ROM) for single phase solid solutions only:
where xi, Vi, and Ei are the atomic fraction, molar volume, and Young’s modulus of the alloy element i. Elemental Young’s modulus values were obtained via Pymatgen22.
- O content (wppm): Measured oxygen content.
- N content (wppm): Measured nitrogen content.
- C content (wppm): Measured carbon content.

5. 


---

---
## Machine Learning Architecture, libraries and methodology of predictions.

Explanation of why I chose the architecture, prediction methodology and the reasoning behind each machine learning pipeline.

### Main in use machine learning pipelines under src/ml_pipelines:

#### QSAR Pipeline for Ionic-Liquid Cytotoxicity

This module implements a fully automated **Quantitative Structure–Activity Relationship (QSAR)** pipeline for predicting the cytotoxicity of ionic liquids using multiple curated CSV datasets. It supports both **regression (CC50 prediction)** and **binary toxicity classification**, and produces all required molecular fingerprints, physicochemical descriptors, metadata encodings, and trained machine-learning artifacts.

---

**1 Architectural Overview**


Full documentation for the implementation details of the ML architecture and code:
**[See the QSAR Notebook](notebooks/qsar_docs.ipynb)**


---

## **Features**

### 🔍 **Local Database Search**

* Query materials stored in your local CSV or database.
* Fast and cached lookup.
* Returns full material metadata.

---

### 🌐 **Materials Project Integration**

* Live lookup of:

  * Structure summaries
  * Elasticity data (when available)
  * Magnetism
  * Bonding information
  * Oxidation states
  * Surface properties
  * Thermodynamics (when available)
* Handles missing MP data gracefully.

---

### 🧪 **3D Structure Viewer** (not yet implemented...)

* Interactive **py3Dmol** molecular visualizer. (details coming soon...)
* Supports rotation, zoom, and style changes.
* Automatically loads valid MP structures.

---

### 🧮 **ML Prediction Pipelines**

* Details coming soon ...

---

### 🖥️ **Modern Streamlit Dashboard**

* Clean UI with custom CSS.
* Uses `st.session_state` for stable navigation.
* Mobile-aware responsive design.

---

## **Project Structure** (full structure explained soon...)

```
project/
│
├── streamlit_app.py           # Main multi-page Streamlit entrypoint
├── visualization.py           # MP API data visualization tab
├── mp_integration.py          # API integration helper functions
├── data/                      # Local datasets
├── models/                    # Trained ML models
├── utils/
│   ├── ml_pipelines/
│   │   └── crystalline_structure_predictor.py
│   └── ...
└── README.md
```

---

## **Installation**

### **1. Clone the repo**

```bash
git clone <https://github.com/Hdave00/Biomat-test>
cd project
```

### **2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **Environment Variables**

Create a `.env` file in the project root:

```
MP_API_KEY=your_materials_project_api_key_here
```

This key is loaded in `mp_integration.py` using **python-dotenv**.

---

## **Running the App**

```bash
streamlit run streamlit_app.py
```

---

## **Usage Overview**

### **Local Search**

1. Navigate to **Local Search** tab.
2. Type a material name or ID.
3. Results appear instantly by caching.

### **Materials Project Lookup**

1. Select an element → structure → MP Entry ID.
2. View:

   * Material summary
   * Bonding + magnetism
   * Elasticity (when available)


---
### **ML Prediction**

1. Navigate to **Prediction** tab. (more details coming soon...)

---

## **Future Roadmap (Coming Soon...)**

* ML-enhanced materials recommendation engine
* Implant-specific constraints (shear force, cytotoxicity, budget, lifespan)
* Automated structure report PDF generator
* WASM-powered C modules for simulation
* User profiles & saved searches

---

## **Troubleshooting**

### **No elasticity data**

Some MP entries simply do not contain elasticity measurements.
The UI will show:

> *“No elasticity data available for this entry.”*

### **Sub-types not appearing**

This happens if MP returns **no structures** for your element.
Try selecting another element or refresh the tab.

---

## **License**

MIT


---
