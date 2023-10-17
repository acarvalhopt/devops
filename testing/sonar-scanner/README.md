### Dockerfile with manual installation of sonar-scanner on python image.


### To run locally with the sonar-scanner image:
```
docker run \                                                                                                                          
    --rm \        
    -e SONAR_HOST_URL=<SONAR_URL> \
    -e SONAR_LOGIN=<SONAR_AUTH_TOKEN> \
    -e SONAR_PROJECT_KEY=<PYTHON_PROJECT> \
    -v "<PATH_TO_MY_PYTHON_PROJECT>:/usr/src" \
    sonarsource/sonar-scanner-cli
```