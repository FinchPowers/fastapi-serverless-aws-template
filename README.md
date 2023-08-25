# FastAPI - Serverless - AWS - template

Working FastAPI template that can be deployed to AWS through serverless. The mangum python library
is used to route incoming API Gateway to FastAPI routes.

### Requirements

* Python >= 3.10
* Node >= 14

### Commands

* **Install**: `poetry install`
* **Format code**: `make format`
* **Lint code**: `make lint`
* **Test**: `make test`

### Deploy

This assumes you have a working AWS environment to deploy to.

This is a template, so placeholder values need to be replaced. The best thing to do is to run `git
grep TODO` to find them all. Once done, the project can be deployed with `npm exec -- sls deploy
--stage <STAGE>`.
