# Insurance Data Analysis and Modeling

## **Overview**
This project aims to analyze historical insurance claim data to optimize marketing strategies and identify "low-risk" customer segments. The tasks span data exploration, hypothesis testing, and statistical modeling to derive actionable insights and build predictive models.

---

## **Project Structure**
```
.
├── data/                   # Contains the datasets used for analysis
├── scripts/                # Modularized Python scripts for data processing and modeling
├── notebook/               # Jupyter Notebooks for interactive analysis and reporting
├── outputs/                # Generated visualizations and reports
├── requirements.txt        # Python dependencies
├── .dvc/                   # DVC configuration for data versioning
├── .github/workflows/      # CI/CD configuration for GitHub Actions
└── README.md               # Project documentation
```

---

## **Setup and Installation**

### Prerequisites
- Python 3.8 or above
- Git
- DVC

### Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### Set Up the Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize DVC:
   ```bash
   dvc init
   ```
4. Pull data from the remote storage:
   ```bash
   dvc pull
   ```

---

## **Workflow**

### Task 1: Data Understanding and EDA
- Summarized data structure, quality, and distributions.
- Visualized relationships and trends using histograms, bar charts, and scatter plots.

### Task 2: Data Version Control
- Used DVC to version datasets.
- Configured local remote storage for reproducibility.

### Task 3: A/B Hypothesis Testing
- Tested hypotheses regarding risk and profitability differences across provinces, zip codes, and genders.
- Performed statistical tests (t-tests, chi-square tests) to validate hypotheses.

### Task 4: Statistical Modeling
- Built and evaluated predictive models (Linear Regression, Random Forests, XGBoost).
- Used SHAP for feature importance analysis and interpretability.

---

## **Key Features**
1. **Data Analysis:**
   - Performed exploratory data analysis to uncover insights.
2. **Hypothesis Testing:**
   - Validated risk and profit margin differences across various demographics.
3. **Predictive Modeling:**
   - Built and evaluated machine learning models to predict `TotalClaims`.
4. **Data Versioning:**
   - Ensured reproducibility with DVC.

---

## **Results and Recommendations**

### Insights
- Significant risk variations across provinces and zip codes.
- No significant risk differences between genders.
- High-profit zip codes identified for targeted marketing.

### Recommendations
- Focus marketing campaigns on low-risk regions.
- Offer premium discounts in high-margin zip codes.
- Maintain gender-neutral pricing for fairness and compliance.

---

## **Running the Project**

### Step 1: Run Notebooks
Navigate to the `notebook/` folder and execute the notebooks step by step to replicate the analysis.

### Step 2: Run Scripts
Use the modularized scripts for reusable functionalities:
- Data Preparation:
  ```python
  from scripts.data_preparation import handle_missing_data, encode_categorical_data, split_data
  ```
- Statistical Modeling:
  ```python
  from scripts.modeling import build_linear_regression, build_random_forest, build_xgboost
  ```

### Step 3: Unit Tests
Ensure everything works correctly by running unit tests:
```bash
pytest
```

---

## **Continuous Integration (CI)**
This project uses GitHub Actions to run unit tests automatically. The configuration is in `.github/workflows/unittest.yml`.

---

## **Technologies Used**
- **Languages:** Python
- **Libraries:**
  - pandas, numpy, matplotlib, seaborn
  - scikit-learn, xgboost, shap
- **Version Control:** Git, DVC
- **CI/CD:** GitHub Actions

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For questions or collaboration opportunities, please contact:
- **Name:** Gebriel Admasu
- **Email:** [Your Email Address]
