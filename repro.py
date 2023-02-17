import requests

response: requests.Response = requests.get(url="https://www.google.com")

with response as r:
    chunks: list[bytes] = []
    chunks_length: int = 0
    iter: int = 0
    for chunk in r.iter_content(chunk_size=200):
        iter += 1
        chunks.append(chunk)
        chunks_length += len(chunk)

print(f"done: {iter}")
