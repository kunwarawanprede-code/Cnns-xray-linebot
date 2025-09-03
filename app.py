from flask import Flask, request, jsonify
import requests
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)
model = load_model("lung_cnn_model.h5")  

def predict_image(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction, axis=1)[0]
    return ["Normal", "Pneumonia", "Tuberculosis"][class_index]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    image_url = data["events"][0]["message"]["image"]["url"]
    reply_token = data["events"][0]["replyToken"]

    image_data = requests.get(image_url).content
    image_path = "temp.jpg"
    with open(image_path, "wb") as f:
        f.write(image_data)

    result = predict_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {raJV7rrLap/W7Mbo+UGSh5OHSQ6NMsYtnzA6RMptVqXUljc57GppR4jpwGKuzE1hQXIrU7CJvVbEU9hkIG3uWKAXjqF25U9JWm8gNon1iYjLii4C5fkrg+fdtFjP0HikTSqWqEpK9Nr4k0eTDwMDjgdB04t89/1O/w1cDnyilFU=}"
    }

    payload = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": f"ผลการทำนาย: {result}"}]
    }

    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()
