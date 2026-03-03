Updating your local repository on the Raspberry Pi is a straightforward process. Since you've already made changes on GitHub, you essentially need to tell your Pi to "go grab the new stuff."

Here is the quickest way to get it done using the terminal.

### ---

**1\. Navigate to your project folder**

First, make sure you are inside the directory of your local repository.

Bash

cd path/to/your/repository

### **2\. Pull the changes**

The most common command for this is git pull. This command fetches the changes from GitHub and immediately merges them into your local files.

Bash

git pull origin main

**Note:** If your primary branch is named master instead of main, use git pull origin master instead.

### ---

**Potential Roadblocks (and how to fix them)**

Sometimes Git might get a little protective if you have unsaved changes on your Raspberry Pi that conflict with what you added on GitHub.

* **"Please commit your changes or stash them..."**  
  If you’ve been tinkering with files on the Pi and haven't saved them to Git yet, Git won't want to overwrite them. You can "hide" your local changes temporarily, pull the update, and then bring your changes back:  
  Bash  
  git stash  
  git pull origin main  
  git stash pop

* **Authentication Issues**  
  If it’s been a while, GitHub might ask for your credentials. Since GitHub deprecated password authentication for Git operations, you’ll likely need to use a **Personal Access Token (PAT)** or an **SSH Key**.

### ---

**Summary of Commands**

| Action | Command |
| :---- | :---- |
| **Check Status** | git status |
| **Download & Merge** | git pull origin main |
| **Download only (no merge)** | git fetch |

Would you like me to walk you through setting up an SSH key on your Raspberry Pi so you don't have to type in a token every time you pull?