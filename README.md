# CNNs X-Ray Linebot

This project is a LINE bot designed to predict lung diseases from X-ray images using AI. The bot classifies images into three categories:
- Normal
- Pneumonia
- Tuberculosis

## Requirements
- Flask
- TensorFlow
- Requests
- Gunicorn

## Instructions
1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Deploy to a cloud platform such as Render or Heroku.
4. Configure the LINE Developers account and use the provided access token and secret for the bot.

## Usage
Send an X-ray image to the bot, and it will classify the image into one of the three categories.

git add your_model.h5
git commit -m "Add model file"
git push
