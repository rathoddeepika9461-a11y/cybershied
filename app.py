from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def analyze_url(url: str) -> dict:
    score = 0
    warnings = []
    
    if re.search(r'https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        score += 40
        warnings.append("Warning: URL contains a raw IP address instead of a domain name.")
        
    if url.count('-') > 3:
        score += 25
        warnings.append("Warning: Excessive hyphens found, a common phishing tactic.")
        
    if url.count('.') > 4:
        score += 20
        warnings.append("Warning: High number of subdomains detected.")
        
    if '@' in url:
        score += 35
        warnings.append("Warning: Contains '@' symbol which can hide the true destination.")

    risk_score = min(score, 100)
    
    if risk_score >= 50:
        status = "High Risk (Phishing Suspected)"
    elif risk_score > 0:
        status = "Medium Risk (Suspicious)"
    else:
        status = "Low Risk (Likely Safe)"
        
    return {
        "url": url,
        "risk_score": risk_score,
        "status": status,
        "warnings": warnings if warnings else ["No major suspicious patterns detected."]
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "No URL provided."}), 400
    result = analyze_url(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)