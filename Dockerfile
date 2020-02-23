FROM node:12

RUN buildDeps='npm install --save-dev @babel/plugin-transform-flow-strip-types' \
    npm install --save-dev @babel/core \
    npm install --save-dev danger &buildDeps

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]