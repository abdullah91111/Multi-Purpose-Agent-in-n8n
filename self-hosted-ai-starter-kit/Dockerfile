# Use the base image for n8n
FROM n8nio/n8n:latest

# Switch to root to install packages
USER root

# Set environment variable to ensure Puppeteer downloads Chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=false

# Set the environment variable to point to system-wide Chromium
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Install Bash and necessary dependencies
RUN apk update && apk add --no-cache \
    bash \
    python3 \
    py3-pip \
    build-base \
    pkgconfig \
    pixman-dev \
    cairo-dev \
    pango-dev \
    jpeg-dev \
    giflib-dev \
    nodejs \
    npm

# Install additional dependencies for Chromium and Puppeteer
RUN apk add --no-cache \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    dbus-libs \
    libx11 \
    libxcomposite \
    libxdamage \
    libxtst \
    libxrandr \
    libxi \
    udev \
    ttf-dejavu

# Install required npm packages globally
RUN npm install -g axios url file-type neo4j-driver @mozilla/readability \
    jsdom marked pdf.js-extract pdf-parse-fork tiktoken firebase-admin \
    canvas json5 katex marked-katex-extension pdfjs-dist ioredis amqplib \
    pdf-img-convert flexsearch puppeteer turndown sanitize-html \
    commonmark path


# Set the NODE_PATH environment variable to ensure global modules can be accessed
ENV NODE_PATH=/usr/local/lib/node_modules

# Switch back to node user
USER node

# Set the entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]

