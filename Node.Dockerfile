FROM node:14.17.4-alpine
# ENV NODE_OPTIONS --openssl-legacy-provider
WORKDIR /bioacustica
COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .
# RUN npm run build
CMD ["npm","start"]