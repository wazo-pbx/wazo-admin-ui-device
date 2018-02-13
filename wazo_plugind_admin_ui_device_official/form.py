# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    SubmitField,
    StringField,
    SelectField,
    FormField,
    BooleanField
)
from wtforms.validators import IPAddress, MacAddress

from wazo_admin_ui.helpers.form import BaseForm


class DeviceOptionsForm(BaseForm):
    switchboard = BooleanField(l_('Switchboard'), default=False)


class DeviceForm(BaseForm):
    # template_id = StringField(l_('Template')) # TODO to implemented
    ip = StringField(l_('IP'), validators=[IPAddress()])
    mac = StringField(l_('MAC'), validators=[MacAddress()])
    model = StringField(l_('Model'))
    plugin = StringField(l_('Plugin'))
    vendor = StringField(l_('Vendor'))
    version = StringField(l_('Version'))
    sn = StringField(l_('Serial Number'))
    status = SelectField(l_('Status'), choices=[
        ('autoprov', l_('Autoprov')),
        ('configured', l_('Configured')),
        ('not_configured', l_('Not configured')),
    ])
    options = FormField(DeviceOptionsForm)
    description = StringField(l_('Description'))
    submit = SubmitField()
