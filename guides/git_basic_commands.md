# Basic Git Commands Guide

This guide provides a quick reference for basic Git commands on Ubuntu. Git is a powerful version control system widely used for collaborative development.

## Table of Contents

1. [Setting Up Git](#1-setting-up-git)
2. [Cloning a Repository](#2-cloning-a-repository)
3. [Checking Repository Status](#3-checking-repository-status)
4. [Making Changes](#4-making-changes)
5. [Committing Changes](#5-committing-changes)
6. [Branching](#6-branching)
7. [Merging](#7-merging)
8. [Pushing Changes](#8-pushing-changes)
9. [Pulling Changes](#9-pulling-changes)
10. [Viewing Commit History](#10-viewing-commit-history)

## 1. Setting Up Git

Install Git on Ubuntu:

```bash
sudo apt update
sudo apt install git
```

Configure your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 2. Cloning a Repository

Clone a remote repository to your local machine:

```bash
git clone https://github.com/username/repository.git
```

## 3. Checking Repository Status

Check the status of your local repository:

```bash
git status
```

## 4. Making Changes

Create or modify files in your working directory.

## 5. Committing Changes

Stage changes for commit:

```bash
git add filename
```

Commit changes with a descriptive message:

```bash
git commit -m "Your commit message"
```

## 6. Branching

Create a new branch:

```bash
git branch new-branch
```

Switch to the new branch:

```bash
git checkout new-branch
```

## 7. Merging

Merge changes from one branch into another:

```bash
git checkout target-branch
git merge source-branch
```

## 8. Pushing Changes

Push changes to a remote repository:

```bash
git push origin branch-name
```

## 9. Pulling Changes

Pull changes from a remote repository:

```bash
git pull origin branch-name
```

## 10. Viewing Commit History

View commit history:

```bash
git log
```

These are some basic Git commands to get you started. Explore more Git functionalities as you continue with your development projects.
