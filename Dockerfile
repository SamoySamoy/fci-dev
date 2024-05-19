# ================================== BUILDER ===================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-PYTHON_VERSION_NOT_SET}
ARG INSTALL_NODE_VERSION=${INSTALL_NODE_VERSION:-NODE_VERSION_NOT_SET}

FROM node:${INSTALL_NODE_VERSION}-bullseye-slim AS node
FROM python:${INSTALL_PYTHON_VERSION}-slim-bullseye AS builder


WORKDIR /app

COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/lib/ /usr/lib/
# See https://github.com/moby/moby/issues/37965
RUN true
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY requirements requirements
RUN pip install --no-cache -r requirements/prod.txt


COPY package.json ./
RUN npm install

COPY webpack.config.js autoapp.py ./
COPY flask_boilerplate flask_boilerplate
COPY assets assets
COPY .env.example .env
RUN npm run-script build



# ================================= DEVELOPMENT ================================
FROM builder AS development
RUN pip install PyMySQL
RUN pip install --no-cache -r requirements/dev.txt
EXPOSE 2992
EXPOSE 5000
COPY . .
CMD [ "npm", "start" ]
