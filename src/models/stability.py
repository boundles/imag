import requests


def txt2image(prompt):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": f"Bearer sk-Wi4lfzCtRhgGSwyQJIdGjzS3HX59KOFn8CzjCENi8qfem2nw",
            "accept": "application/json"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "png",
            "size": "512*512"
        },
    )

    return response.content
