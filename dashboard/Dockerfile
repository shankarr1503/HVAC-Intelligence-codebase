FROM node:18-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
ARG REACT_APP_TELEMETRY_URL=ws://localhost:5000/ws/telemetry
ENV REACT_APP_TELEMETRY_URL=$REACT_APP_TELEMETRY_URL
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
