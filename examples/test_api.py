from videohub import Client
client = Client(base_url="http://172.19.128.69:12345/video_qa", api_key="sk-")
response = client.generate(
        model="CogVLM2-Video",
        video_path="../test_data/ikun.mp4",
        # prompt="When does the man begin to play basketball?",
        prompt="How old are you?",
        temperature=0.1,
    )
print(response)