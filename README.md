# 🔐 Ransomware Detection Using Machine Learning

This project explores multiple machine learning models to detect ransomware from a dataset of system behaviors. We primarily used the **Random Forest** algorithm and compared its effectiveness to **K-Nearest Neighbors (KNN)**, **Logistic Regression**, and **Linear Regression**. The goal was to classify files as either benign or ransomware with high accuracy and low error.

---

## 👩‍💻 Authors

- **Aniyah Hall**  
  Bachelor of Science in Computer Technology  
  Health Technology & Cybersecurity, Bowie State University

- **Dajah Gordon**  
  Bachelor of Science in Computer Technology  
  Bowie State University

---

## 🧠 Algorithms Used

| Algorithm            | Accuracy (Train / Test) | Loss (Train / Test) | Notes                                  |
|----------------------|--------------------------|----------------------|----------------------------------------|
| Random Forest        | ~100% / 99.67–99.70%     | Very Low             | Best performing; efficient with 100 trees |
| K-Nearest Neighbors  | 99.46% / 99.18%          | 0.0121 / 0.1311      | Strong performance and low error       |
| Logistic Regression  | 86.55% / 87.27%          | 0.3248 / 0.3094      | Moderate performance                   |
| Linear Regression    | 46.23% / 48.31%          | 0.1322 / 0.1267      | Not suitable for classification        |

---

## 🧪 Dataset

- **Total Samples:** ~62,485  
  - **Training:** 49,988  
  - **Testing:** 12,497  
- The dataset was loaded into Python (via PyCharm) and used to train/test all models.
- Labels: `benign` or `ransomware`

---

## 📊 Evaluation Metrics

- **Accuracy**
- **Loss**
- **Confusion Matrix** — showed minimal false positives/negatives for best models

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `ransomware_detection_random_forest.py` | Random Forest implementation |
| `ransomware_detection_knn.py` | K-Nearest Neighbors implementation |
| `ransomware_detection_logistic.py` | Logistic Regression |
| `ransomware_detection_linear.py` | Linear Regression |
| `plot_results.py` | Code for generating accuracy/loss graphs |
| `data/` | Folder for dataset (or sample if original is too large) |
| `README.md` | Project overview and instructions |
| `requirements.txt` | Python dependencies |
| `report.pdf` | (Optional) Your final report formatted as PDF |

---

## 📦 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/ransomware-detection.git
cd ransomware-detection

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run a Model (Example: Random Forest)
python ransomware_detection_random_forest.py

### 4. Output
Accuracy & loss will be printed
Confusion matrix and plots may be saved to /results/ folder
