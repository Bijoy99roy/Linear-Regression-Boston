
# End-to-end Linear Regresson implementation

This project predicts the house price of Boston.


# 📜 Dataset
The Dataset used is the boston housing price Dataset from
sklearn.
You can get the Dataset from code below -
```python
from sklearn.datasets import load_boston
boston = load_boston()
bos = pd.DataFrame(boston.data, columns = boston.feature_names)
bos['MEDV'] = boston.target
```



## 🖥Installation

### 🛠 Requirements
- Python 3.7+
- Flask
- Pandas
- Numpy
- Pickle



  
## ⚙Installation

Install all the requirements using requirements.txt file run -

```cmd
pip install -r requirements.txt
```
    