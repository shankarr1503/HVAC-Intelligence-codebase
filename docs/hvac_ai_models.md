# HVAC AI Models

This document describes the machine learning models used in the project.

## Thermal Comfort Model
A regression model that predicts a comfort score based on environmental features
such as temperature, humidity, and time of day. The placeholder implementation
uses a linear equation but can be extended to neural networks or gradient-boosted
trees.

## Energy Consumption Predictor
Estimates the energy usage of HVAC based on current state and control signals.
Currently implemented as a linear predictor; more sophisticated approaches can
leverage historical data and physical models.

## State Estimator
Keeps track of the HVAC system and building state by fusing incoming sensor
measurements. Useful as input to controllers and optimizers.

## Extensibility
All models conform to simple `fit/train` and `predict` interfaces, enabling
plug-and-play replacements. Future work may integrate PyTorch modules or scikit-
learn pipelines.
