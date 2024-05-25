FROM centos
WORKDIR  /app
COPY . /app
#RUN apt-get clean
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN cd ..
RUN cd ..
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum install msodbcsql17-17.4.1.1-1 -y
RUN yum -y install wget make gcc openssl-devel bzip2-devel -y
RUN cd /tmp/
RUN wget https://www.python.org/ftp/python/3.6.12/Python-3.6.12.tgz
RUN tar xzf Python-3.6.12.tgz
RUN cd Python-3.6.12
RUN ./configure --enable-optimizations
RUN make altinstall
RUN ln -sfn /usr/local/bin/python3.6 /usr/bin/python3.6
RUN ln -sfn /usr/local/bin/pip3.6 /usr/bin/pip3.6

RUN yum install unixODBC unixODBC-devel
RUN yum install gcc-c++
RUN dnf install python3-devel -y
RUN pip install -U pip setuptools
RUN pip3 install -r requirements.txt
CMD ["python3", "testconn.py"]