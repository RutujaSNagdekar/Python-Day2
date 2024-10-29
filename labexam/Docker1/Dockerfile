#Dockerfile for Apache server
FROM httpd:2.4
COPY ./index.html .
EXPOSE 9091
ENTRYPOINT [ "usr/src" , "./index.html" ] 
                              
