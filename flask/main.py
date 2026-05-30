from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
feedback_db = []


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.route("/practice-areas", methods=["GET"])
def list_practice_areas():
    areas = []
    for item in feedback_db:
        if item.get("type") == "practice_area":
            areas.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "description": item.get("description", ""),
            })
    return jsonify({"practice_areas": areas}), 200


@app.route("/attorneys", methods=["GET"])
def list_attorneys():
    bios = []
    for item in feedback_db:
        if item.get("type") == "attorney":
            bios.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "title": item.get("title", ""),
                "bio": item.get("bio", ""),
                "practice_areas": item.get("practice_areas", []),
            })
    return jsonify({"attorneys": bios}), 200


@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()
    inquiry_type = (data.get("type") or "inquiry").strip()
    if not message:
        return jsonify(error="message is required"), 400
    item = {
        "id": len(feedback_db) + 1,
        "type": inquiry_type,
        "name": name,
        "email": email,
        "message": message,
    }
    feedback_db.append(item)
    return jsonify(item), 201


@app.route("/feedback/<int:feedback_id>", methods=["GET"])
def get_feedback(feedback_id):
    item = next((x for x in feedback_db if x.get("id") == feedback_id), None)
    if not item:
        return jsonify(error="not found"), 404
    return jsonify(item), 200


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(".", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5005)
