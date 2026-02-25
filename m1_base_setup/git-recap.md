---
layout: default
title: Git Recap
parent: Base Setup
nav_order: 1
---

# Git Recap

Software development requires a safe way to track changes in code. **Version control** helps you answer:

- Who changed the code?
- When was it changed?
- What was changed?
- Can we revert to an earlier version?

Git is the tool we use to manage version control. For a deeper explanation, see the [official Git documentation](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).

---

## Table of Contents

1. [Git vs GitHub](#1-git-vs-github)
2. [Core Concepts](#2-core-concepts)
   - [What Does Git Track?](#21-what-does-git-track)
   - [Repositories: Local and Remote](#22-repositories-local-and-remote)
   - [Forks and Upstream](#23-forks-and-upstream)
   - [The Three Stages of Git](#24-the-three-stages-of-git)
3. [Getting Code](#3-getting-code)
   - [clone](#31-clone)
   - [fetch](#32-fetch)
   - [pull](#33-pull)
4. [Making Changes](#4-making-changes)
   - [status](#41-status)
   - [add](#42-add)
   - [stash and stash pop](#43-stash-and-stash-pop)
   - [commit](#44-commit)
5. [Sharing Changes](#5-sharing-changes)
   - [push](#51-push)
   - [merge](#52-merge)
6. [Navigating History](#6-navigating-history)
   - [checkout](#61-checkout)

---

## 1. Git vs GitHub

It is important to understand the difference:

- **Git** → A version control tool installed on your computer.
- **GitHub** → A website that hosts Git repositories online.

In this course, we use Git locally (in the terminal) and GitHub to store and share code. You are expected to create a public GitHub repository and use Git to upload your work.

---

## 2. Core Concepts

### 2.1 What Does Git Track?

Git tracks changes to files inside a project folder. Specifically, it tracks new files, modified files, deleted files, and the full history of all changes.

> **Important:** Git does NOT automatically track everything — files must be explicitly added first.

---

### 2.2 Repositories: Local and Remote

A **repository** (or *repo*) is a project folder that Git tracks. It contains your project files and a hidden `.git` folder that stores the full version history.

There are two types:

- **Local repository** → On your computer
- **Remote repository** → Hosted online (e.g., on GitHub)

**What is a remote and what is `origin`?**

A *remote* is a named reference to a repository hosted somewhere else (typically GitHub). When you clone a repository, Git automatically creates a remote called **`origin`** that points back to the URL you cloned from.

```bash
git remote -v
# origin  https://github.com/marco-saretta/python-workshop.git (fetch)
# origin  https://github.com/marco-saretta/python-workshop.git (push)
```

You can have multiple remotes. `origin` is just the conventional name for the primary one.

---

### 2.3 Forks and Upstream

A **fork** is your personal copy of someone else's repository, hosted on your own GitHub account. Forks are useful when you want to contribute to a project you don't own.

When you fork and then clone, you typically have two remotes:

| Remote | Points to |
|--------|-----------|
| `origin` | Your fork on GitHub |
| `upstream` | The original repository you forked from |

You set up `upstream` manually so you can pull in changes from the original project:

```bash
git remote add upstream https://github.com/original-author/python-workshop.git
git remote -v
# origin    https://github.com/your-username/python-workshop.git (fetch)
# upstream  https://github.com/original-author/python-workshop.git (fetch)
```

To sync your fork with the latest changes from the original:

```bash
git fetch upstream
git merge upstream/main
```

---

### 2.4 The Three Stages of Git

Git works in three main steps:

```
Working Directory  →  Staging Area (Index)  →  Commit (History)
   (edit files)         (git add)               (git commit)
```

1. **Working Directory** — Where you edit files freely.
2. **Staging Area (Index)** — Where you prepare a set of changes before saving them.
3. **Commit** — A permanent snapshot of your staged changes, stored in history.

This separation gives you control: you can edit many files but only commit a specific subset of them.

---

## 3. Getting Code

### 3.1 Clone

`git clone` downloads a remote repository to your computer. You can clone using **HTTPS** or **SSH**:

| Method | URL format | Requires |
|--------|-----------|----------|
| HTTPS | `https://github.com/user/repo.git` | GitHub username + password/token |
| SSH | `git@github.com:user/repo.git` | SSH key configured on GitHub |

HTTPS is simpler to start with. SSH is preferred for regular work because it doesn't require entering credentials each time.

**Example — clone the workshop repository with HTTPS:**

Open a terminal (preferably Git Bash on Windows, or any terminal on Mac/Linux) and run:

```bash
git clone https://github.com/marco-saretta/python-workshop.git
cd python-workshop
```

After cloning, `cd python-workshop` moves you into the new local folder. You now have a complete local copy of the repository, and Git has automatically set `origin` to point to the GitHub URL.

---

### 3.2 Fetch

`git fetch` downloads the latest changes from a remote **without applying them** to your working directory. It updates your local knowledge of what exists remotely, but leaves your files untouched.

```bash
git fetch origin
```

Think of it as "check what's new on the remote, but don't change anything yet." This is useful for inspecting remote changes before deciding to merge them.

---

### 3.3 Pull

`git pull` downloads the latest changes from the remote **and immediately applies them** to your current branch. It is effectively `git fetch` followed by `git merge`.

```bash
git pull origin main
```

**When to use `fetch` vs `pull`:**

- Use `fetch` when you want to inspect changes before integrating them.
- Use `pull` when you're confident you want to apply the latest changes right away.

> **Warning:** If you have local uncommitted changes that conflict with the incoming changes, `git pull` may fail. Use `git stash` first (see [Section 4.3](#43-stash-and-stash-pop)).

---

## 4. Making Changes

### 4.1 Status

`git status` is your most important command for understanding what is happening in your repository. It shows:

- Which files have been **modified** (but not staged)
- Which files are **staged** (ready to commit)
- Which files are **untracked** (Git doesn't know about them yet)

```bash
git status
```

Example output:

```
On branch main
Changes not staged for commit:
  modified:   app.py

Untracked files:
  new_script.py
```

Run `git status` frequently — before and after every other command — to stay oriented.

---

### 4.2 Add

`git add` moves changes from the working directory to the **staging area**. Only staged changes will be included in the next commit.

```bash
# Stage a single file
git add app.py

# Stage multiple files
git add app.py utils.py

# Stage all changed and new files in the current directory
git add .
```

> **Tip:** Prefer staging specific files rather than `git add .` — it forces you to review what you're actually committing.

---

### 4.3 Stash and Stash Pop

`git stash` temporarily shelves your uncommitted changes so you can switch context (e.g., pull updates or switch branches) without losing work or committing unfinished code.

```bash
# Save current changes to the stash
git stash

# Your working directory is now clean
git status  # nothing to commit

# ... do other work (e.g., git pull, git checkout another-branch) ...

# Restore your stashed changes
git stash pop
```

`git stash pop` restores the most recently stashed changes and removes them from the stash. If you want to keep the stash entry after restoring, use `git stash apply` instead.

You can view all stashed entries with:

```bash
git stash list
# stash@{0}: WIP on main: abc1234 Add login validation
```

---

### 4.4 Commit

`git commit` saves a permanent snapshot of your staged changes to the repository's history.

```bash
git commit -m "Add login validation"
```

The `-m` flag lets you write a short commit message inline. This message should describe *what* changed and *why*, not how.

**Good commit messages:**

```bash
git commit -m "Fix off-by-one error in date parser"
git commit -m "Add unit tests for user authentication"
git commit -m "Remove unused import in config.py"
```

**Bad commit messages:**

```bash
git commit -m "fix"
git commit -m "changes"
git commit -m "asdfgh"
```

> **Note:** A commit only includes what you have staged with `git add`. Unstaged changes remain in your working directory and will not be included.

**Full example — the typical edit → stage → commit cycle:**

```bash
# 1. Edit your file
# (make changes to app.py in your editor)

# 2. Check what changed
git status

# 3. Stage the file
git add app.py

# 4. Confirm what is staged
git status

# 5. Commit
git commit -m "Add login validation"
```

---

## 5. Sharing Changes

### 5.1 Push

`git push` uploads your local commits to a remote repository, making them available to others.

```bash
git push origin main
```

This pushes your `main` branch to the remote named `origin`. If you are working on a different branch, replace `main` with your branch name:

```bash
git push origin my-feature-branch
```

> **Tip:** Before pushing, it's good practice to run `git pull` first to make sure your local branch is up to date with the remote. This reduces the chance of conflicts.

---

### 5.2 Merge

`git merge` integrates changes from one branch into another. The most common use case is merging a feature branch back into `main` once work is complete.

```bash
# Switch to the branch you want to merge INTO
git checkout main

# Merge the feature branch into main
git merge my-feature-branch
```

**What happens during a merge:**

- If the branches have no conflicting changes, Git performs a **fast-forward merge** automatically.
- If the same lines were changed in both branches, Git reports a **merge conflict**. You must manually edit the conflicting files, then stage and commit the resolution:

```bash
# After resolving conflicts in your editor:
git add conflicted-file.py
git commit -m "Resolve merge conflict in conflicted-file.py"
```

---

## 6. Navigating History

### 6.1 Checkout

`git checkout` is used to switch between branches or restore files to a previous state.

**Switch to an existing branch:**

```bash
git checkout main
git checkout my-feature-branch
```

**Create and switch to a new branch in one step:**

```bash
git checkout -b new-feature
```

This is the most common way to start new work — branch off from `main`, make your changes, then merge back when done.

**Restore a single file to its last committed state** (discard local changes):

```bash
git checkout -- app.py
```

> **Warning:** `git checkout -- <file>` permanently discards your unsaved changes to that file. There is no undo.

> **Note:** In newer versions of Git, `git switch` is the preferred command for switching branches, and `git restore` for discarding file changes. `git checkout` still works and remains widely used.