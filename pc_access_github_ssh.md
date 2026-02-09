# Windows 11 pc Access github.com Using SSH
### 1. Generate an SSH key
Open PowerShell or Command Prompt and run:
```
bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter to accept the default file location ('C:\Users\YourUsername\.ssh\id_ed25519'), then optionally set a passphrase.
### 2. Start the SSH agent
```
bash
# Start the service
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent

# Add your key
ssh-add ~\.ssh\id_ed25519
```
### 3. Copy your public key
```
bash
cat ~\.ssh\id_ed25519.pub
```
Copy the entire output (starts with 'ssh-ed25519').
### 4. Add the key to GitHub
- Go to GitHub.com → Settings → SSH and GPG keys
- Click "New SSH key"
- Paste your public key and give it a title
- Click "Add SSH key"
### 5. Test the connection
```
bash
ssh -T git@github.com
```
You should see: 'Hi username! You've successfully authenticated...'
### 6. Use SSH for repositories
When cloning, use the SSH URL:
```
bash
git clone git@github.com:username/repository.git
```
For existing repos using HTTPS, switch to SSH:
```
bash
git remote set-url origin git@github.com:username/repository.git
```
That's it! You're now set up to use SSH with GitHub on Windows 11.

