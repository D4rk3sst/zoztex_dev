# -*- coding: utf-8 -*-
from setuptools import setup

packages = [
    "base.Engine.zoztex",
    "base.Engine.zoztex.exceptions",
    "base.Engine.zoztex.http",
    "base.Engine.zoztex.utils",
    "base.Engine.zoztex.ws",
    "base.Engine.zoztex.ws.channels",
    "base.Engine.zoztex.ws.objects",
]

package_data = {"": ["*"]}

install_requires = [
    "beautifulsoup4==4.11.2",
    "certifi==2022.12.7",
    "greenlet>=2.0.1",
    "undetected-chromedriver>=3.5.5",
    "pyOpenSSL>=23.1.1",
    "pytz>=2023.3",
    "requests-toolbelt>=1.0.0",
    "requests>=2.31.0",
    "urllib3>=2.0.5",
    "websocket-client==1.6.3",
    "websockets==11.0.3",
]

setup_kwargs = {
    "name": "zoztex",
    "version": "1.0.0",
    "description": "Trading bot",
    "author": "D4rk3st",
    "author_email": "d4rk3sst@proton.me",
    "maintainer": "None",
    "maintainer_email": "None",
    "url": "no url",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.10,<3.13",
}


setup(**setup_kwargs)
