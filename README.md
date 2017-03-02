# learning-in-shiyanlou.com

## Description

Learning Programming in shiyanlou.com. And I write a python shell to manage the folders structure, which can create folders by chapters of courses. ⌨️ ⌨️

## syltools.py -h

```bash
$ python3 syltool.py -h
usage: syltool.py [-h] [-g GETT] [-cc] [-cs] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -g GETT, --gett GETT  get the name of course by course code. [given a
                        number]
  -cc, --cf-c           create a folder in default path in client.
  -cs, --cf-s           create a folder in default path in server.
  -s, --scp             scp the files to server folder
```

### etc.

I was learning the Course [<Git 实战教程>](https://www.shiyanlou.com/courses/4) whose course code is `4`. So I can use following command to make folder in default folder:

```bash
$ python3 syltool.py -g 4 -cc
```

Very convenient. 😊 
