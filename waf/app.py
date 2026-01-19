from flask import Flask, request, abort
import pickle
from feature_extraction import extract_features_from_json

app = Flask(__name__)

with open("waf_model.pkl", "rb") as f:
    model = pickle.load(f)

print(f"✅ Model loaded successfully")
print(f"Model type: {type(model)}")
print(f"Model classes: {model.classes_ if hasattr(model, 'classes_') else 'Not available'}")
print(f"Number of features expected: {model.n_features_in_ if hasattr(model, 'n_features_in_') else 'Not available'}")

@app.route("/", methods=["GET", "POST"])
@app.route("/<path:subpath>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def waf(subpath=""):
    req_json = {
        "method": request.method,
        "url": request.full_path,
        "headers": dict(request.headers),
        "dataset": request.get_data(as_text=True)
    }

    print(f"\n📨 Request received:")
    print(f"   Method: {req_json['method']}")
    print(f"   URL: {req_json['url']}")
    print(f"   Headers: {req_json['headers']}")
    print(f"   Data: {req_json['dataset'][:100]}...")

    features = extract_features_from_json(req_json)
    print(f"   Extracted features: {features}")

    if hasattr(model, 'n_features_in_'):
        if len(features) != model.n_features_in_:
            print(f"   ⚠️ Warning: Expected {model.n_features_in_} features, got {len(features)}")




    prediction = model.predict([features])[0]
    print(f"   Prediction: {prediction} (0=legitimate, 1=malicious)")

    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba([features])[0]
        print(f"   Probability: {proba}")




    if prediction == 1:
        print("🚫 Blocked malicious request")
        abort(403)

    print("✅ Allowed request")
    return "Request allowed by ML WAF"

if __name__ == "__main__":
    app.run(port=8080, debug=True)