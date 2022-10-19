FROM node:14.17.4-alpine
WORKDIR /bioacustica
ENV PATH="./node_modules/.bin:$PATH"
COPY . .
RUN npm run build
CMD ["npm","start"]