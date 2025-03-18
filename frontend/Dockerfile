FROM node:18

WORKDIR /app
COPY angular-app/package.json angular-app/package-lock.json ./
RUN npm install

COPY angular-app .
EXPOSE 4200

CMD ["npm", "start"]
