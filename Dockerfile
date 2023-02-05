FROM python:3.11

WORKDIR /code

# COPY ./requirements.txt /code/requirements.txt
COPY pyproject.toml /code/pyproject.toml


# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev


# 
COPY ./main.py /code/
COPY ./langchain_utils.py /code/

RUN mkdir /code/data
COPY ./data/*.pkl /code/data

ENV OPENAI_API_KEY=$OPENAI_API_KEY

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]