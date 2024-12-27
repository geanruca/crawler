# 🌐 Multi-Site Scraper Project

## 🛠️ Overview
This is a small project designed to scrape as many websites as you need with minimal developer effort. 🚀 The project structure is intentionally simple and efficient to streamline the creation of new scrapers. It's just a starting point, and you can customize it to fit your needs. 🌟

---

## 🏗️ Project Structure
The workflow is designed to minimize complexity and focus on daily tasks:

1️⃣ **Django Components**
   - `crawler` app containing models and scraping logic. Here is where developers can work on the scraping logic. 🕷️
   - Admin interface for data management
   - Database migrations for bus and image data
   - The scraper runs as a Django management command (`python manage.py scrap`)
   - Data is automatically stored in SQLite database (configurable in settings.py)
   - Access and manage scraped data through Django admin interface
   - Extend models by adding fields and running migrations

---

## ⚠️ Considerations
- Works best for websites with an **index page** and corresponding **detail pages**. 🖱️➡️📄  
- The Bus model includes 3 scraped fields as an example. You can easily expand this by adding more fields as needed. 🛠️  
- The scraper is designed to **run manually** in two stages:  
  1️⃣ Scraping all index pages first to gather detail URLs.  
  2️⃣ Scraping all detail pages to retrieve additional information.

---

🎯 **Start scraping smarter, not harder!** Happy coding! 💻✨

---

## 🚀 Installation

1️⃣ **Set up your virtual environment**  
   Generate a virtual environment to isolate project dependencies:
   ```bash
   python3 -m venv venv
   ```

2️⃣ **Activate the virtual environment**  
   Activate it using the following command:
   ```bash
   source venv/bin/activate
   ```

3️⃣ **Install dependencies**  
   Install all required libraries from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4️⃣ **Setup Django**  
   Initialize the database and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```


4️⃣ **Run the scraper**  
   Use the following command to execute the scraper:
   ```bash
   python3 manage.py scrap
   ```

---
## 🚀 Visualizations

5️⃣ **Run the server**
    ```bash
    python3 manage.py runserver
    ```
6️⃣ **Open the browser and go to the following link**
    ```bash
    http://localhost:8000/admin
    ```

🚀 🚀 Now you can login with the superuser credentials, and review the Bus scrapped data 🚀 🚀


🌟 Enjoy building powerful scrapers with ease! If you encounter any issues or want to suggest improvements, feel free to contribute! 🚀✨
