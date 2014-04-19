pip install -r requirements.txt
pip install pylint
pip install coverage
pip install /var/cache/pip/http%3A%2F%2Feffbot.org%2Fmedia%2Fdownloads%2FPIL-1.1.7.tar.gz
coverage run --source=$WORKSPACE/ manage.py test cms
coverage xml
coverage html
pylint -f parseable cms/ | tee pylint.out
pep8 --first cms/ | tee pep8.txt

