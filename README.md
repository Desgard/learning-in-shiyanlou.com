# learning-in-shiyanlou.com

## Description

Learning Programming in shiyanlou.com. And I write a python shell to manage the folders structure, which can create folders by chapters of courses. ⌨️ ⌨️

## syltools.py -h

```bash
$ python3 syltool.py -h
usage: syltool.py [-h] [-g GETT] [-cc] [-cs] [-s] [-p PORT] [-u USER] [-a ADDRESS]

optional arguments:
  -h, --help            show this help message and exit
  -g GETT, --gett GETT  get the name of course by course code. [given a number]
  -cc, --cf-c           create a folder in default path in client.
  -cs, --cf-s           create a folder in default path in server.
  -s, --scp             scp the files to server folder
  -p PORT, --port PORT  ssh connect to server - port
  -u USER, --user USER  ssh connect to server - user
  -a ADDRESS, --address ADDRESS ssh connect to server - ip
```

### etc.

I was learning the Course [<Git 实战教程>](https://www.shiyanlou.com/courses/4) whose course code is `4`. So I can use following command to make folder in default folder:

```bash
$ python3 syltool.py -g 4 -cc
```

And you will see the folder structure:

```bash
Git 实战教程
.
├── git介绍
├── 基本用法（上）
├── 基本用法（下）
├── 中级技能（上）
├── 中级技能（下）
└── 高级技能
```

Very convenient. 😊 
