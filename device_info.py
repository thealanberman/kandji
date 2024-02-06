from api import API


class DeviceInfo(API):
    def __init__(self, api_key):
        super().__init__(api_key)

    def list_devices(self):
        return self.get("/v1/devices")

    def get_info(self, device_id):
        return self.get(f"/v1/devices/{device_id}")

    def get_details(self, device_id):
        return self.get(f"/v1/devices/{device_id}/details")

    def get_lost_mode_details(self, device_id):
        return self.get(f"/v1/devices/{device_id}/details/lostmode")

    def cancel_lost_mode(self, device_id):
        return self.delete(f"/v1/devices/{device_id}/details/lostmode")

    def get_activity(self, device_id, limit=300, offset=0):
        """
        Get activity for a device

        Args:
            device_id (str): Device ID
            limit (int, optional): Number of results to return. Defaults to 300.
            offset (int, optional): Offset to start at. Defaults to 0.

        Returns:
            dict: Activity data
        """
        return self.get(
            f"/v1/devices/{device_id}/activity?limit={limit}&offset={offset}"
        )

    def get_all_activity(self, device_id) -> list[dict]:
        """Get all activity for a device"""
        offset = 0
        results = []
        while self.get_activity(device_id, limit=300, offset=offset)["activity"][
            "next"
        ]:
            results.append(
                self.get_activity(device_id, limit=300, offset=offset)["activity"][
                    "results"
                ]
            )
            offset += 300
        return results

        # return self.get(f"/v1/devices/{device_id}/activity/all")
