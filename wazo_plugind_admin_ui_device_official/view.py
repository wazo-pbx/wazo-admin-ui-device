# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import jsonify, request
from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import DeviceForm


class DeviceView(BaseView):
    form = DeviceForm
    resource = 'device'

    @classy_menu_item('.devices', l_('Devices'), order=5, icon="phone-square")
    def index(self):
        return super().index()


class DeviceListingView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        devices = self.service.list(**params)
        results = [{'id': device['id'], 'text': device['mac']} for device in devices['items']]
        return jsonify(build_select2_response(results, devices['total'], params))
