FROM python:3.9
ADD program1.py .
ADD boolean_gui.py .
ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV DISPLAY=host.docker.internal:0.0

CMD ["python", "./boolean_gui.py"]