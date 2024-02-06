#!/usr/bin/env python3

import json

from icecream import ic

from devices import Inventory


def read_device_list():
    with open("test/list-devices.json", encoding="utf-8", mode="r") as f:
        data = json.load(f)
    return data


device_list = read_device_list()
devices = Inventory(device_list)

ic(devices.get_device_id_by_asset_tag("00000"))
ic(devices.macs)
ic(devices.blueprints)
ic(devices.device_count)
ic(devices.get_device_ids_by_user("user1"))
ic(devices.get_device_id_by_device_name("test iphone"))
