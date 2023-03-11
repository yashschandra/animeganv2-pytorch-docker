from flask import Flask, request, jsonify
from PIL import Image
import torch
import os
from io import BytesIO
import base64
import json

app = Flask(__name__)


@app.route("/", methods = ['POST'])
def main():
    model = torch.hub.load("/app/animegan2-pytorch-main", "generator", source = "local", pretrained=request.json['pretrained'])
    face2paint = torch.hub.load("/app/animegan2-pytorch-main", "face2paint", source = "local", size=512)
    input = Image.open(BytesIO(base64.b64decode(request.json['input']))).convert("RGB")
    output = face2paint(model, input)
    buffered = BytesIO()
    output.save(buffered, "JPEG")
    output_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return jsonify({'output': output_data})