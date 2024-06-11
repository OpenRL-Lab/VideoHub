# VideoHub

VideoHub API

## Install
    
```shell
pip install videohub
```

## Usage

```python
from videohub import Client
client = Client(base_url="http://ip:port/video_qa", api_key="sk-")
print(
    client.generate(
        model="CogVLM",
        video_path="test.mp4",
        prompt="When does the man begin to jump?",
    )
)
```