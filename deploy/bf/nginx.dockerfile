FROM nginx:1.19.6-alpine
WORKDIR /etc/nginx
ADD deploy/bf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8082
CMD ["nginx","-g", "daemon off;"]
