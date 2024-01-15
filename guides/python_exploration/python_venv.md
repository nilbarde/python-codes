# Creating and Using Python Virtual Environment Guide

This guide provides step-by-step instructions for creating and using Python virtual environments on Ubuntu. Virtual environments are useful for isolating Python projects and managing dependencies.

## Table of Contents

1. [Installing Python](#1-installing-python)
2. [Installing `venv` Module](#2-installing-venv-module)
3. [Creating a Virtual Environment](#3-creating-a-virtual-environment)
4. [Activating the Virtual Environment](#4-activating-the-virtual-environment)
5. [Deactivating the Virtual Environment](#5-deactivating-the-virtual-environment)
6. [Installing Packages in the Virtual Environment](#6-installing-packages-in-the-virtual-environment)
7. [Listing Installed Packages](#7-listing-installed-packages)
8. [Using the Virtual Environment in a Script](#8-using-the-virtual-environment-in-a-script)

## 1. Installing Python

Ensure Python is installed on your system. If not, install it using:

```bash
sudo apt update
sudo apt install python3
```

## 2. Installing `venv` Module

Check if the `venv` module is installed:

```bash
python3 -m venv --help
```

If not installed, install it:

```bash
sudo apt install python3-venv
```

## 3. Creating a Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
python3 -m venv venv_workspace
```

This command creates a virtual environment named `venv_workspace` in your project directory.

## 4. Activating the Virtual Environment

Activate the virtual environment:

```bash
source venv_workspace/bin/activate
```

Your terminal prompt will change, indicating the virtual environment is active.

## 5. Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:

```bash
deactivate
```

Your prompt will return to the original state.

## 6. Installing Packages in the Virtual Environment

While the virtual environment is active, use `pip` to install packages:

```bash
pip install package_name
```

## 7. Listing Installed Packages

List installed packages in the virtual environment:

```bash
pip list
```

## 8. Using the Virtual Environment in a Script

To use the virtual environment in a script, add the following line at the beginning of your script:

```python
#!/path/to/venv_workspace/bin/python
```

This ensures the script uses the Python interpreter from the virtual environment.
