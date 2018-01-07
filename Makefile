init:
	pip install -r requirements.txt

package:
	rm -rf dist/*
	pip install wheel
	python setup.py sdist
	python setup.py bdist_wheel --universal
	gpg --detach-sign -a dist/*.gz
	twine upload dist/*.gz dist/*.gz.asc

