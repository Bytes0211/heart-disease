# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
Machine learning project predicting heart disease using k-Nearest Neighbors (k-NN) classification. The analysis pipeline includes data cleaning, EDA, feature engineering, hyperparameter tuning via GridSearchCV, and comprehensive model evaluation with ROC curves, confusion matrices, and cross-validation.

## Environment Setup

### Virtual Environment
The project uses a Python virtual environment named `.hdVenv` (default location). To set up:

```bash
make setup    # Creates venv and installs dependencies
make activate # Activates existing venv or creates new one
```

### Python Version
Python 3.8+ required (3.12.3 currently used)

### Dependencies
Install via: `pip install -r requirements.txt`

Key libraries:
- `pandas`, `numpy` - Data manipulation
- `matplotlib`, `seaborn` - Visualization
- `scikit-learn` - ML algorithms (KNeighborsClassifier, GridSearchCV, StandardScaler, SimpleImputer, evaluation metrics)
- `scipy`, `statsmodels` - Statistical computing

## Development Commands

### Running Analysis
```bash
jupyter notebook heart-disease.ipynb
```

### Cleanup
```bash
make clean  # Removes build/, dist/, __pycache__, etc.
```

## Dataset
- **File**: `heart-disease.csv` (918 samples, 12 features)
- **Target**: Binary classification (HeartDisease: 1=disease, 0=normal)
- **Class Distribution**: 55.3% disease (508) vs 44.7% normal (410)
- **Features**: Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope

## ML Architecture

### Pipeline Stages
1. **Data Cleaning**: Invalid value detection (172 zero cholesterols, 1 zero RestingBP) → median imputation via `SimpleImputer`
2. **EDA**: Distribution analysis, correlation heatmaps, cross-tabulations
3. **Feature Engineering**: Label encoding for categorical variables, StandardScaler for normalization
4. **Train/Test Split**: 80/20 with stratification to maintain class balance
5. **Hyperparameter Tuning**: GridSearchCV with 5-fold CV testing n_neighbors (1-30), weights (uniform/distance), metric (euclidean/manhattan)
6. **Evaluation**: Confusion matrix, sensitivity/specificity, precision/recall/F1, ROC/AUC, 10-fold CV

### k-NN Algorithm Choice
- **Why k-NN**: Non-parametric, models clinical "similar patients" concept, handles non-linear relationships, interpretable
- **Critical Preprocessing**: StandardScaler required (distance-based algorithm)
- **Stratification**: Maintains class balance in splits

### Evaluation Metrics Priority
For medical ML, prioritize:
- **Sensitivity (Recall)** - Critical: false negatives (missed disease) are dangerous
- **AUC** - Threshold-independent performance measure
- **Cross-validation** - Confirms generalization and stability

### Model Files
Analysis is contained entirely in `heart-disease.ipynb`. No separate Python modules/scripts.

## Git Configuration
Default editor for commits: WARP (per user preferences)

## Ignored Files
- `.hdVenv/` - Virtual environment
- `KNN_METHODOLOGY_GUIDE.md` - Educational documentation (not for version control)
- `heart-disease-old.ipynb` - Backup notebook
- Standard Python/Jupyter ignores (`.ipynb_checkpoints/`, `__pycache__/`)

## Git Commit Convention

Use conventional commit format: `type(scope): brief description`

### Commit Types
- **feat**: New feature or functionality
- **fix**: Bug fix
- **docs**: Documentation changes
- **refactor**: Code refactoring without functionality change
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (dependencies, config, infrastructure)
- **perf**: Performance improvements
- **style**: Code style/formatting changes

### Project Scopes
- **notebook**: Jupyter notebook updates
- **ml**: Machine learning model changes
- **data**: Dataset and preprocessing
- **sklearn**: Scikit-learn configuration
- **eda**: Exploratory data analysis

### Guidelines
- Keep first line under 72 characters
- Use imperative mood ("add" not "added")
- Always include: `Co-Authored-By: Warp <agent@warp.dev>`
- Scope is optional but recommended
- Reference issues when applicable: `fix(ml): improve k-NN hyperparameter tuning (#123)`
