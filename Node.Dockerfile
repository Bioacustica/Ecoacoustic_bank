FROM node:14.17.4-alpine
WORKDIR /bioacustica-front
ENV PATH="/bioacustica-front/node_modules/.bin:$PATH"
COPY . ./
RUN npm run build
CMD ["npm","start"]