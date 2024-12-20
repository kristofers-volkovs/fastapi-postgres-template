# Fastapi template

## System requirements
- Docker
- Make
- [uv](https://docs.astral.sh/uv/)

## Development

### Setup

1. Create `.env` by copying `.env.template`
    ```shell
    cp .env.template .env
    ```

2. Run the project
    ```shell
    make dev
    ```

### Running Tests

To run tests and see the test code coverage run:
```shell
make test
```

### Container shell

To connect to the dev containers shell run:
```shell
make shell-dev
```

To connect to any running container run:
```shell
docker exec -it <container_id> bash
```

### Code style

The code is formatted and checked using - ruff and mypy

To format & check the code execute:
```shell
make check
```

### Commiting code

Pre-commit hooks are set up to check the code on commits - [configuration file](.pre-commit-config.yaml). To run the checks before committing, run:
```shell
pre-commit run
```

To install pre-commit hooks run `pre-commit install`. More info [here](https://pre-commit.com/).

## Production

To build a small docker image for prod run:
```shell
make prod
```
