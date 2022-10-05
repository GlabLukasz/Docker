FROM node
# we are using image of node program for our container

WORKDIR /app
# WORKDIR is a directory where all additional files will be executed from

COPY package.json /app/
# First we are copying package.jason to install it with "npm install" to optimaze
# (get faster) another image build

RUN npm install
# After copying all files to /app dir, "npm install" will instal all dependencies from the folder
# We use RUN for start something in the image

COPY . /app
# We are copying all files from the main directory (first ".") to the /app directory (subfolder)
# To copy files to the root directory as well, instead of /app we need to put another "."
# Eg. COPY . .

EXPOSE 80
# We are highliting internal docker container port (last line in "server.js")
# We will communicate with our container through this (80) port
# It is optional to put EXPOSE in Dockerfile but it's best practise to do it
# as we still need to know on which port our container is running and we need -p to conecti with it.

CMD ["node", "server.js"]
# CMD is for running application as a container (in the container)
# So we first start "node" (from image) and than server "server.js" from copied files
# CMD command is used as the very last one in Dockerfile
# docker build . - we are creating container from our Dockerfile
# "." means our Dockerfile is in root dir
# docker run -p 3000:80 container_id - we are running container on local machine
# port 3000 (-p is for publish) through our container port 80