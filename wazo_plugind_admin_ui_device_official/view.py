# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import (
    jsonify,
    request,
    flash
)
from flask_babel import (
    gettext as _,
    lazy_gettext as l_
)
from flask_menu.classy import classy_menu_item
from requests.exceptions import HTTPError

from wazo_admin_ui.helpers.classful import BaseView, LoginRequiredView
from wazo_admin_ui.helpers.classful import extract_select2_params, build_select2_response

from .form import DeviceForm


class DeviceView(BaseView):
    form = DeviceForm
    resource = 'device'

    @classy_menu_item('.devices', l_('Devices'), order=5, icon="phone-square")
    def index(self):
        return super().index()

    def autoprov(self, device_id):
        try:
            self.service.autoprov(device_id)
        except HTTPError as error:
            self._flash_http_error(error)
            return self._redirect_for('index')

        flash(_('%(resource)s: Resource has been reset to autoprov', resource=self.resource), 'success')
        return self._redirect_for('index')

    def synchronize(self, device_id):
        try:
            self.service.synchronize(device_id)
        except HTTPError as error:
            self._flash_http_error(error)
            return self._redirect_for('index')

        flash(_('%(resource)s: Resource has been synchronized', resource=self.resource), 'success')
        return self._redirect_for('index')


class DeviceListingView(LoginRequiredView):

    def list_json(self):
        params = extract_select2_params(request.args)
        devices = self.service.list(**params)
        results = [{'id': device['id'], 'text': device['mac']} for device in devices['items']]
        return jsonify(build_select2_response(results, devices['total'], params))
