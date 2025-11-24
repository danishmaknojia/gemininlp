# Push to GitHub - Quick Guide

## Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Repository name: `gemininlp` (or your preferred name)
3. Choose Public or Private
4. **DO NOT** check "Add a README file" (we already have one)
5. Click "Create repository"

## Step 2: Push Your Code

After creating the repo, GitHub will show you commands. Use these:

```bash
# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/gemininlp.git

# Rename branch to main if needed (GitHub uses 'main' by default)
git branch -M main

# Push your code
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/gemininlp.git
git branch -M main
git push -u origin main
```

## If you need to authenticate:
- GitHub no longer accepts passwords for HTTPS
- Use a Personal Access Token instead:
  1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate a new token with `repo` permissions
  3. Use the token as your password when prompted

