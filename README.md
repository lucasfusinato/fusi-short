# FusiShort

🔗 FusiShort is a Python URL shortener application.

## About

This is a playground application created with goal of applying full cycle software development, including analysis, design, development, testing, deployment and maintence, using popular technologies like Python, Redis, Docker and Kubernetes.

## Orientações para execução local

1. Gerar o *build* das aplicações:

```
$ docker-compose build
```

2. Executar as aplicações:

```
$ docker-compose up -d
```

E pronto! A API poderá ser acessada através [deste link](http://localhost:8000/docs) e o servidor WEB [neste link](http://localhost:8501).

2.1. Finalizar a execução:

```
$ docker-compose down
```

## Build with

- [Redis](https://redis.io/): in-memory database;
- [FastAPI](https://fastapi.tiangolo.com/): back-end API framwork;
- [Streamlit](https://streamlit.io/): front-end WEB framework;
- [Docker](https://www.docker.com/): containerization platofrm;
- [Kubernetes](https://kubernetes.io/pt-br/): container orchestration platform.

## Author

- **Lucas Fusinato Wilhelm Chiodini Zanis** - [lucasfusinato](https://github.com/lucasfusinato)

## License

This project is licensed under the MIT license.