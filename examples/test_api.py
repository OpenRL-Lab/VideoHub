from videohub import Client


def main():
    client = Client(base_url="http://172.19.128.69:12345/video_qa", api_key="sk-")
    print(
        client.generate(
            model="CogVLM",
            video_path="../test_data/ikun.mp4",
            prompt="When does the man begin to play basketball?",
        )
    )


if __name__ == "__main__":
    main()
