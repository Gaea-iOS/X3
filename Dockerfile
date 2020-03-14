FROM node:12

RUN npm install --save-dev @babel/plugin-transform-flow-strip-types
RUN npm install --save-dev @babel/core 
RUN npm install --save-dev danger

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]