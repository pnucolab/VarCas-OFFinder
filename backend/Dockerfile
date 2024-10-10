
FROM ubuntu:22.04

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip libvcflib-tools libvcflib-dev nano\
    samtools ocl-icd-libopencl1 ocl-icd-opencl-dev nvidia-opencl-dev tabix bcftools && \
    rm -rf /var/lib/apt/lists/*
# Copy the requirements.txt file into the container
ENV PATH="$PATH:/usr/lib/vcflib/bin"
COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app
EXPOSE 8000

# Command to run the application
#CMD ["sleep", "infinity"]
#CMD ["/usr/bin/supervisord"]