FROM node:18 AS development

WORKDIR /app
COPY angular-app/package.json angular-app/package-lock.json ./
RUN npm install

COPY angular-app .

EXPOSE 4200
CMD ["npm", "start"]

FROM development AS test
CMD ["npm", "run", "test"]
