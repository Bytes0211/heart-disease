# Heart Disease Analysis 🫀

A Python-based data analysis and visualization project for exploring heart disease datasets using Pandas, Bokeh, and statistical analysis tools.

## ✨ Features

- **Data Analysis** 📊: Central tendency calculations (mean, median, mode, min, max)
- **Missing Data Visualization** 🔍: Interactive heat map showing missing data patterns
- **Gender Distribution** 👥: Male vs Female count visualization
- **Interactive Visualizations** 📈: Bokeh-based interactive charts and plots
- **Statistical Insights** 📉: Comprehensive numerical analysis of health metrics

## 📥 Installation

```bash path=null start=null
pip install -r requirements.txt
```

## 🚀 Usage

### Central Tendencies Analysis

Calculate mean, median, mode, min, and max for all numerical columns:

```python path=null start=null
python central_tendencies.py
```

This generates a formatted table showing statistical measures for each numerical feature in the dataset.

### Missing Data Analysis

Generate an interactive heat map visualization showing missing data percentages:

```python path=null start=null
python heat-map.py
```

**Output:** Creates `heat-map.html` with an interactive bar chart showing:
- Missing data count per column
- Missing data percentage
- Color-coded visualization (green = complete, red = missing)

### Gender Distribution Visualization

Create a bar chart showing male vs female distribution:

```python path=null start=null
python sex_counts_viz.py
```

**Output:** Creates `sex_counts_visualization.html` with an interactive bar chart displaying gender counts.

## 📊 Dataset

The project analyzes a heart disease dataset (`heart-disease.csv`) containing various health metrics and patient information including:

- **Demographic data**: Age, Sex
- **Clinical measurements**: RestingBP, Cholesterol, MaxHR, Oldpeak
- **Health indicators**: ChestPainType, FastingBS, RestingECG, ExerciseAngina, ST_Slope
- **Target variable**: HeartDisease (presence or absence)

## 📁 Project Structure

```bash path=null start=null
heart-disease/
├── central_tendencies.py      # Statistical analysis of numerical columns
├── heat-map.py                # Missing data visualization
├── sex_counts_viz.py          # Gender distribution chart
├── viz1.py                    # Categorical variable visualizations
├── bokeh-example.py           # Bokeh examples and demos
├── bokeh-embed.py             # Bokeh embedding examples
├── viz1-bokeh.py              # Additional Bokeh visualizations
├── fixed_code.py              # Code fixes and improvements
├── sandbox.py                 # Experimental code
├── requirements.txt           # Project dependencies
├── test.md                    # Test markdown file
└── heart-disease.csv          # Dataset (required)
```

## 📋 Requirements

The project uses the following key libraries:

- **pandas** (2.3.3): Data manipulation and analysis
- **bokeh** (3.8.0): Interactive visualizations
- **numpy** (2.3.4): Numerical computing
- **scikit-learn** (1.7.2): Machine learning tools
- **statsmodels** (0.14.5): Statistical modeling
- **matplotlib-inline**: Inline plotting support
- **tabulate** (0.9.0): Pretty-print tabular data
- **scipy** (1.16.2): Scientific computing

See [requirements.txt](requirements.txt) for full dependency list.

## 🎨 Visualization Features

### Bokeh Visualizations

All Bokeh visualizations include:
- Interactive tooltips with detailed information
- Pan, zoom, and reset controls
- Dark minimal theme support
- Responsive design
- HTML export for easy sharing

### Heat Map Features

The missing data heat map includes:
- Color gradient from green (no missing data) to red (high missing data)
- Hover tooltips showing exact counts and percentages
- Column names on x-axis (rotated 45° for readability)
- Missing percentage on y-axis

### Gender Distribution Features

The sex distribution chart includes:
- Color-coded bars (blue for male, red for female)
- Count labels displayed on each bar
- Clean, minimal design without grid lines

## 💡 Best Practices

### 📊 Data Analysis

- Always check for missing data before analysis using `heat-map.py`
- Use `central_tendencies.py` to understand data distributions
- Verify data types and ranges before statistical operations

### 🎨 Visualization

- Use Bokeh for interactive web-based visualizations
- Export visualizations as HTML for easy sharing
- Apply consistent color schemes across related charts
- Include tooltips for better user experience

### 🔬 Statistical Analysis

- Calculate multiple measures of central tendency (not just mean)
- Consider outliers when interpreting min/max values
- Document any data preprocessing or cleaning steps

## 🛠️ Development

The project includes several experimental and development files:
- `sandbox.py`: Testing ground for new features
- `fixed_code.py`: Corrected implementations
- `bokeh-example.py` and `bokeh-embed.py`: Learning resources for Bokeh

## ⚠️ Requirements

- Python 3.8+ recommended
- Dataset file `heart-disease.csv` must be present in project root
- Modern web browser for viewing Bokeh HTML outputs

## 📄 License

This project is intended for personal/educational use.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows existing patterns
- Visualizations are tested in a browser
- Statistical calculations are verified
- Documentation is updated

## 💬 Support

For issues related to:
- **Bokeh**: Consult the [Bokeh Documentation](https://docs.bokeh.org/)
- **Pandas**: Refer to the [Pandas Documentation](https://pandas.pydata.org/docs/)
- **Statistical Analysis**: See the [SciPy](https://scipy.org/) and [Statsmodels](https://www.statsmodels.org/) documentation
