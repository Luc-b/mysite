# Django Blog
A simple blog web application built with the Django framework. The application allows users to create, edit, delete, and publish blog posts, as well as add comments.

## Features
- **User Authentication**: Login and logout
- **Create, Edit, and Delete Posts**
- **Publish and Save Posts as Drafts**
- **Add Comments to Posts**
- **Approve and Remove Comments**
- **View a List of Published and Draft Posts**

## Technologies Used
- Python 3
- Django
- SQLite3
- HTML/CSS

## Installation and Setup
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
   ```
4. (Optional) Create an admin user:
   ```bash
   python manage.py createsuperuser  
   ```
5. Start the development server:
   ```bash
   python manage.py runserver  
   ```
6. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Routes and URLs

### Blog
- **Home (Post List)**: `/`
- **About Page**: `/about/`
- **Post Detail**: `/post/<post_id>/`
- **Create Post**: `/post/new/`
- **Edit Post**: `/post/<post_id>/edit/`
- **Delete Post**: `/post/<post_id>/remove/`
- **Draft Posts**: `/drafts/`
- **Publish Post**: `/post/<post_id>/publish/`

### Comments
- **Add Comment**: `/post/<post_id>/comment/`
- **Approve Comment**: `/comment/<comment_id>/approve/`
- **Remove Comment**: `/comment/<comment_id>/remove/`

### Authentication
- **Login**: `/accounts/login/`
- **Logout**: `/accounts/logout/`

## Project Structure
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

## Planned Improvements
- **User Authorization**: Restrict editing and deleting posts to the author only.
- **Advanced Comments**: Enable replies to comments.
- **Pagination**: Split posts into multiple pages.

## Author
Luc-b

