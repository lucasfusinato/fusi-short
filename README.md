# FusiShort

🔗 FusiShort is a Python URL shortener application.

![Funcionamento da aplicação](./docs/example.gif).

## About

This is a playground application created with goal of applying full cycle software development using popular technologies like Python, Redis, Docker and Kubernetes.

## Running locally

1. Build applications:

```
$ docker-compose build
```

2. Run applications:

```
$ docker-compose up -d
```

That's all! API can be accessed on [this link](http://localhost:8000/docs) and web server [here](http://localhost:8501).

2.1. [After tests] Stop running:

```
$ docker-compose down
```

## Built with

- [Redis](https://redis.io/): in-memory database;
- [FastAPI](https://fastapi.tiangolo.com/): back-end API framwork;
- [PyTest](https://docs.pytest.org/en/7.0.x/): Python unit test library;
- [Streamlit](https://streamlit.io/): front-end WEB framework;
- [Docker](https://www.docker.com/): containerization platofrm;
- [Kubernetes](https://kubernetes.io/pt-br/): container orchestration platform.

## Author

- **Lucas Fusinato Wilhelm Chiodini Zanis** - [lucasfusinato](https://github.com/lucasfusinato)

## License

This project is licensed under the MIT license.