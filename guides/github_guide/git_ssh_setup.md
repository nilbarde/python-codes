# Setting Up SSH Key for GitHub on Ubuntu

This guide walks you through the process of setting up an SSH key for authenticating with GitHub on Ubuntu.

## Table of Contents

1. [Check for Existing SSH Keys](#1-check-for-existing-ssh-keys)
2. [Generate a New SSH Key](#2-generate-a-new-ssh-key)
3. [Add the SSH Key to the SSH Agent](#3-add-the-ssh-key-to-the-ssh-agent)
4. [Add the SSH Key to Your GitHub Account](#4-add-the-ssh-key-to-your-github-account)
5. [Test the SSH Connection](#5-test-the-ssh-connection)
6. [Conclusion](#6-conclusion)

## 1. Check for Existing SSH Keys

Before generating a new SSH key, check if you already have existing keys. Open a terminal and run:

```bash
ls -al ~/.ssh
```

Look for existing keys, typically `id_rsa` and `id_rsa.pub`.

## 2. Generate a New SSH Key

If you don't have an existing SSH key, generate a new one:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Follow the on-screen prompts, and you can leave the passphrase empty for simplicity.

## 3. Add the SSH Key to the SSH Agent

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add your SSH key to the agent:

```bash
ssh-add ~/.ssh/id_rsa
```

## 4. Add the SSH Key to Your GitHub Account

Copy the SSH key to your clipboard:

```bash
xclip -sel clip < ~/.ssh/id_rsa.pub
```

if xclip is not installed then
Display the SSH key:

```bash
cat ~/.ssh/id_rsa.pub
```

Copy the displayed key.

Go to your GitHub account > Settings > SSH and GPG keys > New SSH key, and paste the copied key.

## 5. Test the SSH Connection

Test the SSH connection to GitHub:

```bash
ssh -T git@github.com
```

If successful, you'll see a message indicating authentication.

## 6. Conclusion

You have successfully set up an SSH key for GitHub on Ubuntu. This allows secure and convenient authentication when interacting with GitHub repositories.

This guide covers the key steps to set up and configure an SSH key for GitHub on Ubuntu. Users can follow the instructions to ensure a secure and seamless authentication process when interacting with GitHub repositories

---

Go back to [GitHub Guide](README.md).

Visit other [Developer Guides](../README.md).
