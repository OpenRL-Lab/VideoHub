from pathlib import Path

import requests


class Client:
    def __init__(self, base_url: str, api_key: str = "sk-"):
        self.base_url = base_url
        self.api_key = api_key

    def generate(self, model: str, video_path: str, prompt: str) -> dict:
        assert Path(video_path).exists(), f"Video file {video_path} does not exist."

        headers = {"Authorization": f"Bearer {self.api_key}"}
        video_file = open(video_path, "rb")
        data = {
            "model": (None, model),
            "question": (None, prompt),
            "video": ("filename.mp4", video_file, "video/mp4"),
        }
        response = requests.post(self.base_url, files=data, headers=headers)
        video_file.close()

        result = {}
        if response.status_code != 200:
            result["status"] = "error"
            result["content"] = response.text
        else:
            response = response.json()
            if "answer" in response:
                result["status"] = "success"
                result["content"] = response["answer"]
            else:
                # something wrong!
                result["status"] = "error"
                result["content"] = response

        return result
