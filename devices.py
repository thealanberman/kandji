"""Kandji Device Inventory"""

from dataclasses import dataclass


@dataclass
class Device:
    agent_installed: bool
    agent_version: str
    asset_tag: str
    blueprint_id: str
    blueprint_name: str
    device_id: str
    device_name: str
    first_enrollment: str
    is_missing: bool
    is_removed: bool
    last_check_in: str
    last_enrollment: str
    lost_mode_status: str
    mdm_enabled: bool
    model: str
    os_version: str
    platform: str
    serial_number: str
    supplemental_build_version: str
    supplemental_os_version_extra: str
    user: str


@dataclass
class Inventory:
    devices: list[Device]

    def __init__(self, device_dicts: list[dict]):
        self.load(device_dicts)

    def load(self, device_dicts: list[dict]):
        self.devices = [Device(**device_dict) for device_dict in device_dicts]

    @property
    def device_count(self):
        return len(self.devices)

    @property
    def macs(self):
        return [device for device in self.devices if device.platform == "Mac"]

    @property
    def iphones(self):
        return [device for device in self.devices if device.platform == "iPhone"]

    @property
    def ipads(self):
        return [device for device in self.devices if device.platform == "iPad"]

    @property
    def blueprints(self):
        # return a list of unique blueprint names
        return list(set(device.blueprint_name for device in self.devices))

    def get_device_ids_by_user(self, user: str) -> list[str]:
        return [device.device_id for device in self.devices if device.user == user]

    def get_device_id_by_asset_tag(self, asset_tag):
        for device in self.devices:
            if device.asset_tag == asset_tag:
                return device.device_id
        raise ValueError(f"Asset tag {asset_tag} not found in device list")

    def get_device_id_by_serial(self, serial_number):
        for device in self.devices:
            if device.serial_number == serial_number:
                return device.device_id
        raise ValueError(f"Serial number {serial_number} not found in device list")

    def get_device_id_by_device_name(self, device_name):
        for device in self.devices:
            if device.device_name == device_name:
                return device.device_id
        raise ValueError(f"Device name {device_name} not found in device list")

    def get_device_user_by_asset_tag(self, asset_tag):
        for device in self.devices:
            if device.asset_tag == asset_tag:
                return device.user
        raise ValueError(f"Asset tag {asset_tag} not found in device list")

    def get_device_user_by_serial(self, serial_number):
        for device in self.devices:
            if device.serial_number == serial_number:
                return device.user
        raise ValueError(f"Serial number {serial_number} not found in device list")

    def get_device_hostname_by_asset_tag(self, asset_tag):
        for device in self.devices:
            if device.asset_tag == asset_tag:
                return device.device_name
        raise ValueError(f"Asset tag {asset_tag} not found in device list")

    def get_device_hostname_by_serial(self, serial_number):
        for device in self.devices:
            if device.serial_number == serial_number:
                return device.device_name
        raise ValueError(f"Serial number {serial_number} not found in device list")

    def get_devices_by_user(self, user):
        return [device for device in self.devices if device.user == user]

    def get_blueprint_id_by_name(self, blueprint_name):
        for device in self.devices:
            if device.blueprint_name == blueprint_name:
                return device.blueprint_id
        raise ValueError(f"Blueprint name {blueprint_name} not found in device list")
