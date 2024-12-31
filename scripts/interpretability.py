import shap

def explain_model(model, X):
    """
    Use SHAP to explain the model's predictions.
    """
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)
    shap.summary_plot(shap_values, X)
