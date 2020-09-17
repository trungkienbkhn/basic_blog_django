# Basic blog with Django

## Các chức năng chính

1. Đăng nhập, đăng xuất, xem, chỉnh sửa profile người dùng 
   (p/s: chức năng edit user đang bị lỗi)
2. Sau khi đăng nhập có thể xem, xóa sửa hoặc tạo bài viết mới
3. Bình luận bài viết

## Requirements

- Mysql
- Python3
- Django
- mysqlclient

## Installing

> Hệ điều hành: Ubuntu, Window

### Clone

```bash
git clone https://github.com/trungkienbkhn/basic_blog_django
```

### Create database

>Ubuntu

```bash 
mysql -u root -p
mysql>create database blogdb;
```
>Win

- Tự tạo hoặc có thể sử dụng MySQL Workbench

### Database setup

- Trong thư mục Basic_blog/settings.py 

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'your_db'',  
        'USER':'root',  
        'PASSWORD':'your_pw'',  
        'HOST':'localhost',  
        'PORT':'3306'  
    }  
} 

- Sửa your_db thành blogdb hoặc tùy chọn, sửa your_pw bằng password mysql
- Chạy migration

```bash
cd Basic_blog
python3 manage.py migrations
python3 manage.py makemigrations blog
python3 manage.py migrate
```

### Run

```bash
python3 manage.py runserver
```

## Author

- Nguyễn Trung Kiên
- Link github: https://github.com/trungkienbkhn

