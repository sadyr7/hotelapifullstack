FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/

EXPOSE 80
#
#RUN mkdir -p /usr/src/app/static
#RUN chmod -R 755 /usr/src/app/static


#FROM nginx:latest
#
#RUN apt-get update && apt-get install -y procps
#RUN mkdir -p /home/app/staticfiles
#RUN chmod -R 755 /home/app/staticfiles