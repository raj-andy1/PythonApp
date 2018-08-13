#Dockerfile for mypythonapp


FROM centos:centos7
MAINTAINER Andy Rajagopalan <ranandthirth@gmail.com>

RUN yum -y update && yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-release-7-2.noarch.rpm
RUN yum -y install git httpd mod_wsgi python-pip
RUN pip install --upgrade pip && pip install flask flask-mysql \
&& mkdir /var/www/mypythonapp \
&& git clone https://github.com/raj-andy1/PythonApp.git /var/www/mypythonapp