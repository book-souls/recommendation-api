from app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_SERVER_PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
