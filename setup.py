import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'ETE_Disease_Classification'
AUTHOR_USERNAME = 'RiteshYennuwar'
SRC_REPO = 'src'
AUTHOR_EMAIL = 'yennuwarritesh@hotmail.com'

setuptools.setup(
    name = REPO_NAME,
    version= __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = 'A package for project disease classification',
    long_description = long_description,
    long_description_content = 'text/markdown',
    url = f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker' : f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues', 
    },
    package_dir={'' : 'src'},
    packages = setuptools.find_packages(where='src')
)