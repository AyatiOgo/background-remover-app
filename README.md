# 🖼️ Background Remover App 

A simple **background remover web app** built with **Django** (backend), **Tailwind CSS** (frontend), and **[rembg](https://github.com/danielgatis/rembg)** (background removal engine).  

This app allows users to upload images and automatically remove their backgrounds with just one click.  

---

## 🚀 Features  
- Upload images and remove backgrounds instantly.  
- Powered by the **rembg** Python library (U²-Net AI model).  
- Clean and responsive **Tailwind CSS UI**.  
- Download processed images with transparent backgrounds.  
- Built with **Django** for scalability and extensibility.  

---

## 🛠️ Tech Stack  
- **Backend:** Django, Python  
- **Frontend:** Tailwind CSS  
- **Background Removal:** rembg (U²-Net)  

---

## 📦 Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/AyatiOgo/background-remover-app.git 
cd bg-remove
```
### 2. Create and activate virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3. Install dependencies 
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```
### 5. Start the development server
```bash
python manage.py runserver
```

## 📂 Project Structure  
bg-remove/
│── manage.py
│── requirements.txt
│── README.md
│
├── bg_remove/ # Django project files
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── removerApp/ # Main app (handles uploads & background removal)
│ ├── views.py
│ ├── models.py
│ ├── templates/
│ └── static/

## 📸 Screenshots
<img width="1920" height="903" alt="Screenshot 2025-08-25 215318" src="https://github.com/user-attachments/assets/b276deb5-654a-47cf-bc86-0d815354a76a" />

## 🔮 Future Improvements
- Add drag & drop support for image uploads.
- Support batch image background removal.
- User authentication & saved history.
- API endpoints for third-party integration.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests.




