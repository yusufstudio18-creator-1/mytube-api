from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
VIDEOS_FILE = "videos.json"

def load_videos():
    if not os.path.exists(VIDEOS_FILE):
        return []
    with open(VIDEOS_FILE, "r") as f:
        return json.load(f)

def save_videos(videos):
    with open(VIDEOS_FILE, "w") as f:
        json.dump(videos, f, indent=2)

@app.route("/videos", methods=["GET"])
def get_videos():
    return jsonify(load_videos())

@app.route("/videos", methods=["POST"])
def add_video():
    data = request.json
    if "link" not in data:
        return jsonify({"error":"Link required"}), 400
    videos = load_videos()
    videos.append({"link": data["link"]})
    save_videos(videos)
    return jsonify({"success": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)