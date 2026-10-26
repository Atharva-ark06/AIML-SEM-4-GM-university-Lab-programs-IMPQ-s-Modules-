# Time-aware validation

Random splitting can leak future information into past predictions.

For forecasting, order observations by time and train on earlier periods while validating on later periods. Consider rolling-origin evaluation and seasonality. Fit scalers and feature transformations using each training window only.

Record the forecast horizon and ensure features would actually be available at the prediction timestamp.