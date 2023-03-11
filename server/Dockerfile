FROM alpine/curl:3.14 AS builder

WORKDIR /tmp

RUN curl -L -o main.zip https://github.com/bryandlee/animegan2-pytorch/archive/refs/heads/main.zip
RUN unzip main.zip

FROM tiangolo/uwsgi-nginx-flask:python3.8 AS final

ENV LISTEN_PORT 8080
EXPOSE 8080

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt
COPY --from=builder /tmp/animegan2-pytorch-main/hubconf.py /app/animegan2-pytorch-main/
COPY --from=builder /tmp/animegan2-pytorch-main/model.py /app/animegan2-pytorch-main/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/face_paint_512_v2.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/face_paint_512_v1.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/celeba_distill.pt /root/.cache/torch/hub/checkpoints/
COPY --from=builder /tmp/animegan2-pytorch-main/weights/paprika.pt /root/.cache/torch/hub/checkpoints/
COPY server.py /app/
COPY uwsgi.ini /app/
