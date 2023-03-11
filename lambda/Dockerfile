FROM alpine/curl:3.14 AS builder

WORKDIR /tmp

RUN curl -L -o main.zip https://github.com/bryandlee/animegan2-pytorch/archive/refs/heads/main.zip
RUN unzip main.zip

FROM public.ecr.aws/lambda/python:3.8 AS final

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY --from=builder /tmp/animegan2-pytorch-main/hubconf.py "${LAMBDA_TASK_ROOT}"/animegan2-pytorch-main/
COPY --from=builder /tmp/animegan2-pytorch-main/model.py "${LAMBDA_TASK_ROOT}"/animegan2-pytorch-main/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/face_paint_512_v2.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/face_paint_512_v1.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/celeba_distill.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/paprika.pt /root/.cache/torch/hub/checkpoints/

COPY lambda.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda.main" ]

