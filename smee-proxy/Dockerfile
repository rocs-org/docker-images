FROM node:lts-alpine
RUN apk update && apk add --no-cache bash curl
RUN npm install -g smee-client-proxy==1.3.0

# Expose port for health check
EXPOSE 3000

ENTRYPOINT ["smee"]
CMD ["--help"]
