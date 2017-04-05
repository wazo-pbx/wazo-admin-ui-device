install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/device.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-device
	rm /etc/wazo-admin-ui/conf.d/device.yml
	systemctl restart wazo-admin-ui
