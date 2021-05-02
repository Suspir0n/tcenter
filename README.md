# Tcenter for Python

A Python library for centralization of title. In this `0.1.4.4` version of tcenter, it allows you to center the title with a number of specific spaces.

## Installation

The latest stable version [is available on PyPI](https://pypi.org/project/tcenter/). Either add `tcenter` to your `requirements.txt` file or install with pip:

    pip install tcenter

## Usage

After you have installed it, to use it is very simple, just import the library and use it this way:

```python
from tcenter.center import to_center

receive = to_center('Hello world', 20)
```

The function `to_center`, it receives a maximum of three parameters and a minimum of two. if you run the `help ()` command you will receive more information about:

```python
help(to_center)
```

He will return this to you at the terminal:

```python
Help on function to_center in module tcenter.center:

to_center(title, space, object='')
    This function is reponsible for centralizing the title. accepted at least two vestments.
    :param title: receive any title, only string.
    :param space: receive any value, only numbers.
    :param object: receive any object, ex: - . = ~ < > _ | between others.
    :return: The title centralized.
```

there are 3 ways for you to pass the data to `to_center`:

```python
from tcenter.center import to_center

receive_one = to_center('Hello world', 20)
receive_two = to_center('Hello world', '20')
receive_three = to_center('Hello world', 20, '=')

print(receive_one)
print(receive_two)
print(receive_three)
```

This way the output would be like this:

```python
       Hello World
       Hello World
=======Hello World=======
```

if you notice, the first two have no difference, but the third, it allows your title to be in the middle of the objects.
