# GitHub For krsmith436

<mark>Never use "sudo" for git commands.</mark>

### DAILY COMMANDS
- git pull: Grab the latest changes from GitHub to your Pi.
- git add . : Tell Git to track the changes you just made.
- git commit -m "Fixed a bug": Save those changes locally with a note.
- git push: Send those saved changes up to GitHub.
- git log --oneline: Clean list of every "save point" you’ve created so far.

### CREATE REPOSITORY
Before you touch the Pi, GitHub needs to know where the code is going.
1. Log into GitHub and click the + icon in the top right -> New repository.
2. Give it a name (it doesn't have to match your folder name, but it helps).
3. Important: Do not check "Initialize this repository with a README, .gitignore, or license." Leave it completely empty.
4. Click Create repository.
5. On your empty GitHub repository page, make sure the SSH button is selected (not HTTPS). The URL should look like `git@github.com:krsmith436/repo-name.git`.
6. Create a file named ".gitignore" in your project's root directory.
``` Bash
nano .gitignore 
```

7. Paste the content below and exit/save (^X).
``` 
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual Environments
venv/
env/
.env

# Raspberry Pi / OS specific
.DS_Store
Thumbs.db

# Distribution / packaging
dist/
build/
*.egg-info/

# Log files
*.log

# Any other files/folders 
```

8. Go to your pi and enter these commands:
``` Bash
cd ~/your-project-folder
git init                        # This creates a hidden ".git" folder that starts tracking your changes.
git add .                       # Add all files in the current folder, don't forget '.' at the end
git commit -m "Initial commit"
git branch -M main              # Rename your default branch to main
git remote add origin git@github.com:krsmith436/your-repo-name.git
git push -u origin main 
```
- NOTE 1: The "-u" flag remembers your preferences, so next time you want to upload changes, you only have to type "git push".
- NOTE 2: If there is a problem with pushing due to permission, <br>
a) verify USER is not owner of all files being pushed. <br>
b) change ownership of all files to USER.
``` Bash
sudo chown -R $USER:$USER .     # Don't forget '.' at the end 
```

### CREATE AND SWITCH TO A NEW BRANCH
1. Instead of working on main, create a "feature" branch. Let’s call it ble-fix.
``` Bash
git checkout -b ble-fix
```
- The `-b` flag tells Git to **create** the branch.
- `checkout` tells Git to **switch** your workspace to that branch.

2. Make Your Changes<br>
Now, modify your Python scripts.
``` Bash
# After editing your files...
git add .
git commit -m "Testing new Bluetooth connection logic"
```

3. Switch Back to Main<br>
Once you’re happy with the changes and have verified the script works, you need to return to the **main** branch to bring those changes over.
``` Bash
git checkout main
```
**Note:** If you look at your files now, your changes will "disappear." Don't panic! They are safely tucked away in the **ble-fix** branch.

4. Merge the Changes<br>
Now, pull the work from **ble-fix** into **main**.
``` Bash
git merge ble-fix
```

Git will usually perform a "Fast-forward" merge, essentially sliding the **main** pointer up to where your **ble-fix** pointer is.

5. Clean Up and Push<br>
Since the **ble-fix** branch is now part of **main**, you don't really need the "side-car" branch anymore.
``` Bash
# Delete the local feature branch
git branch -d ble-fix

# Push the updated main branch to GitHub
git push origin main
```

### INSTALL GIT
``` Bash
sudo apt update
sudo apt install git -y
git --version
```

### CONFIG
``` Bash
git config --global user.name "krsmith436"
git config --global user.email "krsmith436@att.net" 
```

### SETUP SSH
1. Check for existing keys
``` Bash
ls -al ~/.ssh 
```

2. Generate a new key: `ssh-keygen -t ed25519 -C "krsmith436@att.net"`<br>
(Press Enter to accept the default file location and skip the passphrase if you want it to be easy).

3. Add your key to the SSH Agent:
``` Bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519 
```

4. Copy your public key:
``` Bash
cat ~/.ssh/id_ed25519.pub 
```

5. Add it to GitHub: https://github.com/settings/keys
6. Click New SSH Key, give it a title (like "My Raspberry Pi").
7. Paste the text you copied from your terminal
8. Click Add SSH key.
9. Test the connection
``` Bash
ssh -T git@github.com 
```

You’ll see a warning about the authenticity of the host.<br>
Type `yes` and hit **Enter**. All is well if you see:
> *"Hi [YourUsername]! You've successfully authenticated..."*

### IF YOU ACCIDENTALLY ADDED "HTTPS" URL INSTEAD OF "SSH"
``` Bash
git remote set-url origin git@github.com:krsmith436/your-repo-name.git 
```

