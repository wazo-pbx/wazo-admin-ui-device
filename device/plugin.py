# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.destination import register_listing_url

from .service import DeviceService
from .view import DeviceDestinationView

device = create_blueprint('device', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        config = dependencies['config']

        DeviceDestinationView.service = DeviceService(config['confd'])
        DeviceDestinationView.register(device, route_base='/devices_listing')

        register_listing_url('device', 'device.DeviceDestinationView:list_json')

        core.register_blueprint(device)
