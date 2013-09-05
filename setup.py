#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from distutils.core import setup

setup(
    name='xivo-cloud-ivr-client',
    version='1.0',
    description='Script to generating IVR from XiVO unified cloud.',
    maintainer='Sylvain Boily',
    maintainer_email='sboily@proformatique.com',
    url='http://www.avencall.com/',
    license='GPLv3',
    scripts=['bin/xivo-cloud-ivr-client'],
    data_files=[('/etc/pf-xivo', ['etc/xivo-cloud.conf']),
                ('/etc/asterisk/extensions_extra.d/',
                 ['extensions/xivo-cloud-ivr.conf'])]
)
