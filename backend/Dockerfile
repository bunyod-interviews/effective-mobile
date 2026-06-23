FROM python:3.14-alpine

RUN addgroup -S my_group && adduser -S non_root_user -G my_group

WORKDIR /app

COPY app.py load_env.py ./

RUN chown -R non_root_user:my_group /app

USER non_root_user

EXPOSE 8080

CMD ["python", "app.py"]