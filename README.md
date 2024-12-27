# 🌐 Multi-Site Scraper Project

## 🛠️ Overview
This is a small project designed to scrape as many websites as you need with minimal developer effort. 🚀 The project structure is intentionally simple and efficient to streamline the creation of new scrapers. It's just a starting point, and you can customize it to fit your needs. 🌟

---

## 🏗️ Project Structure
The workflow is designed to minimize complexity and focus on daily tasks:

1️⃣ **Index Page Handling**  
   - Obtain an index URL and work on it daily. A new day means a new index page to scrape. 📅  
   - Process a collection of data using tools like `BeautifulSoup` (bs4) or other scraping/crawling libraries. 🕸️  

2️⃣ **Field Selectors Setup**  
   - Define field selectors using XPath or BS4 selectors for each data field (e.g., `Bus` fields or other entities).  
   - Ensure detailed pages are processed effectively. ✅  

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
