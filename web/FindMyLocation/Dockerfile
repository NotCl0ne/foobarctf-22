FROM node:12-buster-slim

WORKDIR /app

COPY package*.json ./

ENV PORT 9999
ENV NODE_ENV production
RUN npm install

COPY . .

EXPOSE 9999

CMD ["node","/app/index.js"]
