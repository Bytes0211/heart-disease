# Heart Disease Prediction Analysis 🫀

A comprehensive machine learning project for predicting heart disease using k-Nearest Neighbors (k-NN) classification. This notebook demonstrates a complete ML pipeline from data cleaning through model evaluation, following industry best practices.

## ✨ Features

- **Data Cleaning** 🧹: Systematic handling of missing values and invalid data points
- **Exploratory Data Analysis** 📊: Comprehensive analysis of numerical and categorical features
- **Feature Engineering** 🔧: Label encoding and standardization for optimal model performance
- **k-NN Classification** 🤖: Implementation and hyperparameter tuning of k-Nearest Neighbors
- **Model Evaluation** 📈: Multiple metrics including ROC curves, confusion matrices, and cross-validation
- **Visualization** 📉: Distribution plots, correlation heatmaps, and performance visualizations

## 📥 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Usage

The main analysis is contained in the Jupyter notebook:

```bash
jupyter notebook heart-disease.ipynb
```

### Analysis Pipeline

The notebook follows a complete machine learning workflow:

1. **Data Loading & Inspection**: Import and examine the dataset structure
2. **Data Cleaning**: Handle invalid values and missing data
3. **Exploratory Data Analysis**: Visualize distributions and relationships
4. **Feature Engineering**: Prepare data for modeling
5. **Model Training**: Train k-NN classifier with baseline parameters
6. **Hyperparameter Tuning**: Optimize k, weights, and distance metrics
7. **Model Evaluation**: Assess performance using multiple metrics

## 📊 Dataset

The project analyzes a heart disease dataset (`heart-disease.csv`) with **918 samples** and **12 features**:

### Features

1. **Age**: Patient age in years
2. **Sex**: M (Male) or F (Female)
3. **ChestPainType**: TA (Typical Angina), ATA (Atypical Angina), NAP (Non-Anginal Pain), ASY (Asymptomatic)
4. **RestingBP**: Resting blood pressure [mm Hg]
5. **Cholesterol**: Serum cholesterol [mm/dl]
6. **FastingBS**: Fasting blood sugar [1: >120 mg/dl, 0: otherwise]
7. **RestingECG**: Resting electrocardiogram results [Normal, ST, LVH]
8. **MaxHR**: Maximum heart rate achieved [60-202]
9. **ExerciseAngina**: Exercise-induced angina [Y: Yes, N: No]
10. **Oldpeak**: ST depression induced by exercise
11. **ST_Slope**: Slope of peak exercise ST segment [Up, Flat, Down]
12. **HeartDisease**: Target variable [1: disease, 0: normal]

### Data Characteristics

- **Class Distribution**: 55.3% disease (508) vs 44.7% no disease (410)
- **Data Quality Issues**: 172 zero values in Cholesterol, 1 in RestingBP (handled via median imputation)
- **No Missing Values**: After cleaning, all 918 samples are complete

## 📁 Project Structure

```
heart-disease/
├── heart-disease.ipynb        # Main analysis notebook
├── heart-disease.csv          # Dataset
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 📋 Requirements

The project uses the following key libraries:

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Static visualizations
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning algorithms and tools
  - `KNeighborsClassifier`: k-NN implementation
  - `GridSearchCV`: Hyperparameter optimization
  - `StandardScaler`: Feature normalization
  - `SimpleImputer`: Missing value handling
  - Evaluation metrics: confusion_matrix, roc_curve, classification_report
- **scipy**: Statistical computing

See [requirements.txt](requirements.txt) for full dependency list.

## 🔬 Analysis Methodology

### 1. Data Cleaning

- **Invalid Values**: Identified and replaced 172 zero values in Cholesterol and 1 in RestingBP with NaN
- **Imputation**: Applied median imputation using `SimpleImputer` for missing numerical values
- **Duplicates**: Removed duplicate records
- **Final Dataset**: 918 complete samples with no missing values

### 2. Exploratory Data Analysis

**Target Variable Analysis:**
- Balanced binary classification with slight skew (55.3% disease)
- Visualized with bar charts and pie charts

**Numerical Features:**
- Histogram distributions with mean/median indicators
- Box plots for outlier detection stratified by disease status
- Features: Age, RestingBP, Cholesterol, MaxHR, Oldpeak

**Categorical Features:**
- Cross-tabulation with target variable
- Features: Sex, ChestPainType, FastingBS, RestingECG, ExerciseAngina, ST_Slope

**Correlation Analysis:**
- Label encoding applied to categorical variables
- Heatmap visualization of feature correlations
- Identified relationships between predictors and target

### 3. Model Building

**k-Nearest Neighbors (k-NN) Classifier:**
- **Train/Test Split**: 80/20 with stratification to maintain class balance
- **Feature Scaling**: `StandardScaler` applied (critical for distance-based algorithms)
- **Baseline Model**: k=5 neighbors as starting point

**Why k-NN?**
- Non-parametric algorithm suitable for complex decision boundaries
- No assumptions about data distribution
- Effective for binary classification tasks
- Interpretable results based on similarity

### 4. Hyperparameter Tuning

**GridSearchCV Configuration:**
- **n_neighbors**: 1 to 30 (finding optimal k)
- **weights**: ['uniform', 'distance'] (equal vs distance-weighted voting)
- **metric**: ['euclidean', 'manhattan'] (distance calculation methods)
- **Cross-Validation**: 5-fold CV for robust parameter selection

**Optimization Goal:** Maximize classification accuracy while avoiding overfitting

### 5. Model Evaluation

**Performance Metrics:**
- **Confusion Matrix**: TP, TN, FP, FN breakdown
- **Sensitivity (Recall)**: True positive rate
- **Specificity**: True negative rate
- **Precision**: Positive predictive value
- **F1-Score**: Harmonic mean of precision and recall
- **ROC Curve**: TPR vs FPR visualization
- **AUC Score**: Overall discrimination ability
- **Cross-Validation**: 10-fold CV for generalization assessment

**k vs Accuracy Plot:**
- Visualizes model performance across different k values
- Identifies optimal balance between bias and variance
- Shows overfitting (low k) and underfitting (high k) regions

## 💡 Key Takeaways

### Model Performance

- k-NN classifier successfully trained for binary heart disease prediction
- Hyperparameter tuning identified optimal configuration
- Multiple evaluation metrics provide comprehensive performance view
- Cross-validation confirms model generalization capability

### Technical Highlights

1. **Proper Data Preprocessing**: Systematic cleaning with median imputation
2. **Feature Scaling**: Essential for distance-based k-NN algorithm
3. **Stratified Splitting**: Maintains class balance in train/test sets
4. **Grid Search**: Exhaustive hyperparameter optimization
5. **Multiple Metrics**: Comprehensive evaluation beyond simple accuracy
6. **Cross-Validation**: Robust assessment of model generalization

### Clinical Relevance

- Binary classification suitable for disease screening
- Interpretable results based on patient similarity
- Multiple health metrics considered (demographic, clinical, diagnostic)
- Balanced dataset reduces bias toward either class

## 🎯 Best Practices Demonstrated

### Data Preparation
- ✅ Handle invalid/impossible values (e.g., zero cholesterol)
- ✅ Use appropriate imputation strategies (median for skewed data)
- ✅ Check for and remove duplicates
- ✅ Verify data quality before modeling

### Feature Engineering
- ✅ Label encode categorical variables for correlation analysis
- ✅ Apply standardization for distance-based algorithms
- ✅ Stratify train/test split to maintain class distribution

### Model Development
- ✅ Start with baseline model before optimization
- ✅ Use cross-validation for hyperparameter tuning
- ✅ Test multiple parameter combinations systematically
- ✅ Evaluate on held-out test set

### Evaluation
- ✅ Use multiple metrics (accuracy, precision, recall, F1, AUC)
- ✅ Visualize performance (ROC curves, confusion matrix)
- ✅ Assess generalization with cross-validation
- ✅ Consider both false positives and false negatives

## 🔮 Future Improvements

- Compare k-NN with other algorithms (Random Forest, SVM, Logistic Regression)
- Feature importance analysis to identify key predictors
- SMOTE or other techniques for handling class imbalance
- Ensemble methods for improved performance
- External validation on independent dataset
- Pipeline implementation for production deployment

## ⚠️ Requirements

- Python 3.8+ recommended
- Jupyter Notebook or JupyterLab
- Dataset file `heart-disease.csv` must be present in project root

## 📄 License

This project is intended for personal/educational use.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing notebook structure
- New analyses include proper documentation
- Visualizations are clear and informative
- Model evaluations are comprehensive

## 💬 Resources

For more information:
- **Scikit-learn k-NN**: [Documentation](https://scikit-learn.org/stable/modules/neighbors.html)
- **Model Evaluation**: [Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
- **Pandas**: [Documentation](https://pandas.pydata.org/docs/)
- **Seaborn**: [Visualization Gallery](https://seaborn.pydata.org/examples/index.html)
