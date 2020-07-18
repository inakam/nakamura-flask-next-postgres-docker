FROM node:14-stretch-slim AS base
WORKDIR /usr/src/app

COPY ["package.json", "yarn.lock", "./"]
RUN yarn install

FROM base AS dev
ENTRYPOINT [ "yarn", "dev" ]

FROM base AS prod
COPY . .
RUN yarn build
ENTRYPOINT [ "yarn", "start" ] 