# jumbler-python

A python library for jumbling letters within words. For background information, see section "Background" at the bottom of this page.

This README explains how to:

1. Create a virtual environment,
1. Execute unit tests,
1. Build a Python package from the source code of this repository,
1. Import a Python package (tarball and wheel archive) and use the objects of the package's module,
1. Dispose of the virtual environment you created.

Make sure you use Python 3.8 or higher. The Python binary used was downloaded and installed from the download section of the official [Python website](https://www.python.org/downloads/).

The contents of this repository where developed on macOS 10.14.8.

For details about how to code using Python and packaging Python projects, see the following two links:

- [Python 3.8.2 Documentation](https://docs.python.org/3.8/),
- [Python Packaging User Guide](https://packaging.python.org).

# Installation

## Python Version

Make sure the binary `python` is aliased to `python3.8`.

```
$ python --version
Python 3.8.2
```

## Build the Package from the Source Code Provided in this Repository

First, clone the GitHub repository.

```
$ mkdir <my-test-dir>
$ cd <my-test-dir>
$ git clone https://github.com/mglavitsch/jumbler-python.git
$ cd jumbler-python
```

In order to have a safe environment with a local Python binary and locally installed Python libraries, we first create a virtual environment and get the versions of `pip`, `setuptools` and `wheel` which the packaging and installation process was successfully tested with.

```
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install pip==20.3.3
(venv) $ pip install setuptools==46.0.0
(venv) $ pip install wheel==0.34.2
```

Run the unit tests using [Test Discovery](https://docs.python.org/3.8/library/unittest.html#unittest-test-discovery).

```
(venv) $ python -m unittest -v
test_indices (tests.test_jumble.Jumbler) ... ok
test_jumble (tests.test_jumble.Jumbler) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Build the packages by creating in directory `dist` both a tarball `.tar.gz` and a wheel archive `.whl`.

```
(venv) $ python setup.py sdist bdist_wheel
```

Either, install the tarball,

```
(venv) $ pip install dist/jumblepkg-mglavitsch-0.0.1.tar.gz
<...>
Successfully installed jumblepkg-mglavitsch-0.0.1
```

Or, install the wheel archive.

```
(venv) $ pip install dist/jumblepkg_mglavitsch-0.0.1-py3-none-any.whl
<...>
Successfully installed jumblepkg-mglavitsch-0.0.1
```

List the installed packages.

```
(venv) $ pip list
Package              Version
-------------------- -------
jumblepkg-mglavitsch 0.0.1
pip                  20.3.3
setuptools           46.0.0
wheel                0.34.2
```

## Test the Package `jumblepkg` Containing the Module `jumble`

By calling `help(Jumbler)`, you display the Docstring content of class `Jumbler`.

```
(env) $ python
>>> from jumblepkg.jumble import Jumbler
>>> help(Jumbler)
<docstring content>
>>> jumbler = Jumbler("Zaphod Beeblebrox")
>>> print(jumbler.get_indices())
[[0, 5], [7, 16]]
>>> print(jumbler.get_jumbled_text(True, 1000))
Zohapd Bbeeboelrx
>>> exit()
```

## Cleanup

Deactivate your virtual environment.

```
(venv) $ deactivate
```

You might want to remove the directory `venv` you created with command `python -m venv venv` in directory `<my-test-dir>/jumbler-python` .

# Background

## Hypothesis

It doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind does not read every letter by itself, but the word as a whole.

## Example

The jumbling of the words of the hypothesis stated above might end up in the following result:

"It doesn't matetr in what order the letrets in a word are, the only imonarptt thing is that the first and last letetr be at the right place. The rest can be a total mess and you can still read it wihuott prbelom. This is beasuce the human mind does not read every letetr by itslef, but the word as a whole."

## Reference

This statement goes back to Graham Ernest Rawlinson: "The Significance of Letter Position in Word Recognition", PhD Thesis, 1976, University of Nottingham
