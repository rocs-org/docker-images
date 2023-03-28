FROM node:lts-alpine
RUN apk update && apk add --no-cache bash curl
RUN npm install -g smee-client-proxy
ENTRYPOINT ["smee"]
CMD ["--help"]
