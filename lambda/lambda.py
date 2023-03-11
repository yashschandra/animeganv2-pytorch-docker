from PIL import Image
import torch
import os
from io import BytesIO
import base64

def main(event, context):
    task_root = os.environ['LAMBDA_TASK_ROOT']
    model = torch.hub.load(task_root + "/animegan2-pytorch-main", "generator", source = "local", pretrained=event['pretrained'])
    face2paint = torch.hub.load(task_root + "/animegan2-pytorch-main", "face2paint", source = "local", size=512)
    input = Image.open(BytesIO(base64.b64decode(event['input']))).convert("RGB")
    output = face2paint(model, input)
    buffered = BytesIO()
    output.save(buffered, "JPEG")
    output_data = base64.b64encode(buffered.getvalue())
    return {'output': output_data}