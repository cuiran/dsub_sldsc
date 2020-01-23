FROM google/cloud-sdk:slim

RUN apt-get update && apt-get install -y \
    build-essential \
    bzip2 \
    ca-certificates \
    git \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    mysql-client \
    wget \
    zlib1g-dev

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.10.1-Linux-x86_64.sh && \
    /bin/bash /Miniconda3-3.10.1-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-3.10.1-Linux-x86_64.sh && \
    /opt/conda/bin/conda install --yes conda==3.14.1
ENV PATH /opt/conda/bin:$PATH

RUN conda install -c daler \
    pip \
    cython \
    matplotlib \
    nose \
    numpydoc \
    pip \
    pandas \
    pyyaml \
    sphinx \
    pysam
RUN conda install -c daler \
    tabix \
    bedtools=2.25.0

RUN conda install --channel conda-forge --channel bioconda pybedtools

COPY requirements.txt /home/
RUN pip2 install -r /home/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /home/requirements.txt
COPY ./pyscripts /home/pyscripts/
RUN chmod 777 -R /home/pyscripts/

VOLUME ["/root/.config"]
CMD [ "/bin/bash" ]
