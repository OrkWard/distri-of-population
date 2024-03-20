import pandas as pd
import numpy as np
from config import DATA_DIR
from os import path
import math

diabetes = pd.read_csv(path.join(DATA_DIR, "PlayTennis.csv"))


def calculate_entropy(data: pd.DataFrame, target_column: str):
    total_rows = len(data)
    target_values = data[target_column].unique()

    entropy = 0.0
    for value in target_values:
        # Calculate the proportion of instances with the current value
        value_count = len(data[data[target_column] == value])
        proportion = value_count / total_rows
        entropy -= proportion * math.log2(proportion) if proportion != 0 else 0.0

    return entropy


entropy_outcome = calculate_entropy(diabetes, "Outcome")


def calculate_information_gain(data, feature, target_column):
    # Calculate weighted average entropy for the feature
    unique_values = data[feature].unique()
    weighted_entropy = 0

    for value in unique_values:
        subset = data[data[feature] == value]
        proportion = len(subset) / len(data)
        weighted_entropy += proportion * calculate_entropy(subset, target_column)

    # Calculate information gain
    information_gain = entropy_outcome - weighted_entropy

    return information_gain


for column in diabetes.columns[:-1]:
    entropy = calculate_entropy(diabetes, column)
    information_gain = calculate_information_gain(diabetes, column, "Outcome")
    print(
        f"{column} - Entropy: {entropy:.3f}, Information Gain: {information_gain:.3f}"
    )


def id3(data, target_column, features):
    if len(data[target_column].unique()) == 1:
        return data[target_column].iloc[0]

    if len(features) == 0:
        return data[target_column].mode().iloc[0]

    best_feature = max(
        features, key=lambda x: calculate_information_gain(data, x, target_column)
    )

    tree = {best_feature: {}}

    features = [f for f in features if f != best_feature]

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        tree[best_feature][value] = id3(subset, target_column, features)

    return tree


id3(diabetes, "Outcome", diabetes.columns)
