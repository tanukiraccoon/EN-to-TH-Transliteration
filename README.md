# EN-to-TH-Transliteration [![Build Status](https://app.travis-ci.com/tanukiraccoon/EN-to-TH-Transliteration.svg?branch=main)](https://app.travis-ci.com/tanukiraccoon/EN-to-TH-Transliteration)
This is my final project in university.
## Installation
Install with [docker](https://www.docker.com/):
1. Clone the GitHub repository to an empty folder on your local machine:
    ```shell
    git clone https://github.com/tanukiraccoon/en-to-th-transliteration.git .
    ```
2. Build
    ```shell
    docker build -t tanukiraccoon/en-to-th-transliteration .
    ```
3. Run
    ```shell
    docker run -d -p 5000:5000 tanukiraccoon/en-to-th-transliteration
    ```
4. Stop and Remove
    ```shell
    docker container rm -f tanukiraccoon/en-to-th-transliteration
    ```
## Features
  * Transliterate English Words to Thai Words
  * Dictionary ([Longdo Dict API](https://dict.longdo.com/page/api))
