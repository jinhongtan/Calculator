# Calculator
### This program inlcude 7 calculation operations: Addition, subtraction, multiply, divide, square root, squre

1. We have three python files, read_data.py, calculator.py, test.py
2. calculator.py has the functions for different operations
3. read_data.py has functions for read data from csv file for testing
4. test.py is the program for testing
5. In the bottom is the screenshot of successful run of the testing

#### create images

1. clone this program

```shell
$> git clone https://github.com/jinhongtan/Calculator.git
```

2. go to Dockerfile directory (cd Dockerfile)

```shell
# switch to Dockerfile directory
$> cd Calculator/
```

3. run docker bulid command

```shell
$> docker build -t <imageName>:<tagName>
```

#### run image

```shell
$> docker run -it <imageName>:<tagName>
```

![alt text](https://github.com/jinhongtan/Calculator/blob/858e28bad3a9fc5d935865d7072a7e3cc6b08159/test%20run%20success.png)
