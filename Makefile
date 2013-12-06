python = /usr/bin/python
venus_path = $(HOME)/src/venus

public:
	$(python) $(venus_path)/planet.py planet.ini

s3: public
	s3cmd sync --acl-public public/ s3://tempura.8-p.info/

test:
	python -m unittest discover
