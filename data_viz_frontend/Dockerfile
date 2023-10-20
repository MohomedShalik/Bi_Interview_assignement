FROM node:20.8-alpine


WORKDIR /data_viz_frontend

COPY package.json .
# RUN npm install vite -g
RUN npm install 


COPY . .

EXPOSE 3000


CMD ["npm" , "run" ,"dev"]