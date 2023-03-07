from setuptools import setup, find_packages

setup(
    name='Cinemate App',
    version='1.0',
    author='Roman Nikolaichuk',
    author_email='roma1111181@gmail.com',
    description='This is a simple app to manage movie reviews',
    url='https://github.com/Nikolaichukr/Cinemate',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.2.3',
        'Flask-Migrate==4.0.4',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==3.0.3',
        'Flask-WTF==1.1.1',
        'mysql-connector-python==8.0.32',
    ]
)
