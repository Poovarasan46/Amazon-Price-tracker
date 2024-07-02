# Amazon-Price-tracker

## Overview
This Python script tracks prices of products on Amazon and notifies users via email when a product's price drops below a specified threshold.

## Features
- Monitors product prices on Amazon using product links.
- Sends email notifications when a product's price drops below a specified threshold.
- Easy setup and configuration.

## Installation
1. Clone the repository:
git clone https://github.com/your-username/amazon-price-tracker.git
2. Install dependencies:
pip install -r requirements.txt
## Usage
1. Set up your email credentials and desired product link and price threshold in `config.py`.
2. Run the script:
3. python amazon_price_tracker.py
## Configuration
To configure the Amazon Price Tracker, edit the `main.py` file with the following details:

- **Product URL**: Replace `product_url` with the Amazon product URL you want to track.
  ```python
  product_url = 'https://www.amazon.com/dp/B07VFFC1Q3/'
1.Target Price: Set target_price to the price threshold below which you want to receive notifications.
2.Email Settings: Update sender_email, receiver_email, and email_password with appropriate values.
