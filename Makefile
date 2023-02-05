IMG_NAME=10k_fastapi
RUN_NAME=10k_fastapi_run
OPENAI_KEY=${OPENAI_API_KEY}

rmi:
	docker rm "${RUN_NAME}"
	docker rmi -f "${IMG_NAME}"

build:
	docker image build --tag "${IMG_NAME}" .

run:
	docker container run --publish 80:80 \
	-e "OPENAI_API_KEY=${OPENAI_KEY}" \
	--name "${RUN_NAME}" "${IMG_NAME}"


.PHONY: rmi build run