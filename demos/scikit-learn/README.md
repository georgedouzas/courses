# Description

Various examples of Scikit-Learn's functionality.

### Model Evaluation

Import the main class:

```python
from model_evaluation import Score
```

Create a score object using an estimator, a name for the scorer, the input data X and the target y:

```python
from sklearn.tree import DecisionTreeClassifier
score = Score(DecisionTreeClassifier(), 'accuracy', X, y)
```

Calculate the average score for a number of runs:

```python
score.calculate(kind='training')
```

The available kinds of scores are 'training', 'validation', 'cv', 'cv_param_grid' and 'nested_cv_param_grid'.
