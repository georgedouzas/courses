"""
Functions that evaluate model performance in various settings.
"""

import numpy as np

from sklearn.base import clone
from sklearn.utils import check_random_state
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.metrics import SCORERS


def training_score(estimator, scoring, X, y, rnd_seed, **kwargs):
    """Calculate training score."""
    estimator = clone(estimator).set_params(random_state=rnd_seed).fit(X, y)   
    return SCORERS[scoring](estimator, X, y)


def validation_score(estimator, scoring, X, y, rnd_seed, **kwargs):
    """Calculate validation score."""
    X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=rnd_seed)
    estimator = clone(estimator).set_params(random_state=rnd_seed).fit(X_train, y_train)    
    return SCORERS[scoring](estimator, X_val, y_val)


def cross_validation_score(estimator, scoring, X, y, cv, rnd_seed, **kwargs):
    """Calculate cross-validation score."""
    estimator = clone(estimator).set_params(random_state=rnd_seed)
    return cross_val_score(estimator, X, y, scoring=scoring).mean()


def cross_validation_param_grid_score(estimator, scoring, X, y, cv, param_grid, rnd_seed):
    """Calculate highest cross-validation score for a parameter grid."""
    estimator = clone(estimator).set_params(random_state=rnd_seed)
    gscv = GridSearchCV(estimator, param_grid, scoring=scoring, cv=cv).fit(X, y)
    return gscv.best_score_


def nested_cross_validation_param_grid_score(estimator, scoring, X, y, cv, param_grid, rnd_seed):
    """Calculate nested cross-validation score for a parameter grid."""
    estimator = clone(estimator).set_params(random_state=rnd_seed)
    gscv = GridSearchCV(estimator, param_grid, scoring=scoring, cv=cv).fit(X, y)
    return cross_val_score(gscv, X, y, cv=cv, scoring=scoring).mean()


class Score:
    """
    Main class that returns the average score for a number of runs.
    """

    score_functions = {
        'training': training_score,
        'validation': validation_score,
        'cv': cross_validation_score,
        'cv_param_grid': cross_validation_param_grid_score,
        'nested_cv_param_grid': nested_cross_validation_param_grid_score
    }

    def __init__(self, estimator, scoring, X, y, cv=None, param_grid=None, rnd_seed=None):
        self.estimator = estimator
        self.scoring = scoring
        self.X = X
        self.y = y

    def calculate(self, kind, rnd_seed=None, cv=None, param_grid={}, n_runs=10):
        random_state = check_random_state(rnd_seed)
        rnd_seeds = [random_state.randint(0, 2 ** 32 - 1) for _ in range(n_runs)]
        scores = []
        for rnd_seed in rnd_seeds:
            scores.append(
                self.score_functions[kind](
                    self.estimator, self.scoring, self.X, self.y, cv=cv, param_grid=param_grid, rnd_seed=rnd_seed
                ) 
            )
        return np.mean(scores)

