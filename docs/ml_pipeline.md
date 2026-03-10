# Machine Learning Pipeline

The ML pipeline consists of the following stages:

1. **Data ingestion** – load raw building and sensor data via
   `src/data_pipeline/data_loader.py`.
2. **Data cleaning** – remove invalid records and enforce types (`data_cleaning.py`).
3. **Feature engineering** – derive time‑based and occupancy features
   (`feature_engineering.py`).
4. **Model training** – energy, comfort, and occupancy models implemented in
   `src/training/*.py` or custom notebooks.
5. **Evaluation** – compute metrics on held‑out sets; placeholder code prints
   coefficients and shapes.
6. **Inference** – use `src/inference/*` utilities or the API to obtain predictions.

Each stage is modular and can be replaced with more sophisticated components
(e.g. `sklearn` pipelines, PyTorch datasets, streaming ingestion).
