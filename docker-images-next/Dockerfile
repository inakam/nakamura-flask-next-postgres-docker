FROM node:14-stretch-slim
WORKDIR /usr/src/app

COPY ["package.json", "yarn.lock", "./"]
RUN yarn install
COPY . .

ENTRYPOINT [ "yarn", "dev" ]