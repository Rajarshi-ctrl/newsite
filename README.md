# Personal Data Analytics Portfolio Website

## Overview
This is the codebase for my personal data analytics portfolio website. The site showcases my data analytics projects, skills, certifications, and professional experience in an interactive and visually appealing format.

## Live Site
🌐 [Visit Live Portfolio](https://drajarshi.vercel.app)

## Tech Stack

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

## Folder Structure

```
newsite/
│
├── mainapp/              # Main Django application
├── staticfiles/static/   # Static assets (CSS, JS, images)
├── website/              # Django project configuration
├── .env                  # Environment variables
├── build_files.sh        # Build script for deployment
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── vercel.json           # Vercel deployment configuration
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/Rajarshi-ctrl/newsite.git
cd newsite
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
- Configure your `.env` file with necessary credentials

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Access the site**
- Open your browser and navigate to `http://127.0.0.1:8000/`

## Main Features

✨ **Key Highlights:**
- **Responsive Design**: Mobile-first, fully responsive layout
- **Project Showcase**: Interactive gallery of data analytics projects
- **Skills & Certifications**: Comprehensive display of technical skills and professional certifications
- **Dynamic Content**: Django-powered backend for easy content management
- **Professional Portfolio**: Clean, modern UI showcasing professional experience
- **Performance Optimized**: Fast loading times with optimized static files
- **SEO Friendly**: Structured metadata and semantic HTML

## Screenshots

![Portfolio Preview](screenshot.png)
*Coming Soon: Add screenshot of the portfolio homepage*

## Deployment

The site is deployed on Vercel with automatic deployments from the master branch.

## License

This project is licensed under the MIT License - feel free to use this code for your own portfolio with attribution.

---

**Developed by Rajarshi Dutta** | [GitHub](https://github.com/Rajarshi-ctrl) | [Live Site](https://rajarshi.vercel.app/)
