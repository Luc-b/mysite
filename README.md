
# Django Blog  

A simple blog web application built with the Django framework. The application allows users to create, edit, delete, and publish blog posts, as well as add comments.  

## **Features**  
- User registration and login  
- Create, edit, and delete blog posts  
- Publish and save posts as drafts  
- Add comments to posts  
- View a list of published and draft posts  

## **Technologies Used**  
- Python 3  
- Django  
- SQLite3   
- HTML/CSS  

## **Installation and Setup**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Luc-b/mysite.git
   cd mysite
   ```  
2. Create a virtual environment and install dependencies:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   pip install -r requirements.txt  
   ```  
3. Run database migrations:  
   ```bash
   python manage.py migrate  
   python manage.py createsuperuser  # If you want admin access  
   ```  
4. Start the development server:  
   ```bash
   python manage.py runserver  
   ```  
5. Open the application in your browser:  
   ```
   http://127.0.0.1:8000/
   ```  

## **Project Structure**  
```
mysite/
│── blog/                 # Blog application  
│   ├── migrations/       # Database migrations  
│   ├── static/css/       # Styles for the site  
│   ├── templates/blog/   # HTML templates  
│   ├── views.py          # Page rendering logic  
│   ├── models.py         # Database models  
│   ├── forms.py          # Django forms  
│   ├── urls.py           # App routes  
│── mysite/               # Project configuration  
│── db.sqlite3            # SQLite database  
│── manage.py             # Main management script  
```

## **Planned Improvements**  
- **User Authorization**: Restrict editing and deleting posts to the author only.  
- **Advanced Comments**: Enable replies to comments.  
- **Pagination**: Split posts into multiple pages.  

## **Author**  
Luc-b  

