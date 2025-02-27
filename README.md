# Air Quality Index Prediction Model

This repository contains code for predicting the Air Quality Index (AQI) using historical air quality and weather data. The model is built using Python and leverages machine learning techniques to provide predictions.

## Data Collection

The `data_collection.py` script collects historical air quality data from the OpenAQ platform and weather data from the OpenWeatherMap API.

### Usage

1. Install the required libraries:
    ```bash
    pip install requests pandas
    ```

2. Set your OpenWeatherMap API key and run the script:
    ```bash
    python data_collection.py
    ```

The script will save the collected data to a CSV file named `air_quality_weather_data.csv`.

## Model Development

The `model_development.py` script preprocesses the collected data, builds, trains, and evaluates a RandomForestRegressor model to predict AQI values.

### Usage

1. Install the required libraries:
    ```bash
    pip install pandas scikit-learn joblib
    ```

2. Run the script:
    ```bash
    python model_development.py
    ```

The script will save the trained model to a file named `aqi_prediction_model.pkl`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License.