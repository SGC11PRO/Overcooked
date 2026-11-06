# Project Workflow (Git & GitHub)
This guide defines our collaboration rules, naming conventions, and daily workflow for the project.

## Branch Naming Convention
To keep the repository clean and organized, branch names must follow the format category/short-description:

- feature/ : For new features or parts of the project (e.g., feature/player-movement).

- fix/ : For bug fixes or error corrections (e.g., fix/collision-bug).

- docs/ : For documentation or text files (e.g., docs/update-readme).

- refactor/ : For code restructuring or clean-up without adding new features (e.g., refactor/clean-classes).

## Commit Message Standards (Conventional Commits)
Commit messages must start with a lowercase type, followed by a colon and a clear description in the imperative mood:

- feat: add ingredient chopping logic

- fix: fix timer countdown bug

- docs: update installation instructions

- style: format code in player.py

- refactor: simplify scoring function

## Daily Workflow (Step-by-Step)
1. **When starting work (Update)**
Make sure you have the latest version of the main branch before starting your task:

```Bash
git checkout main # Change to the main branch
git pull origin main # Update your local project with the latest version of the repositorie
```

2. **Create your feature branch**
Create a new branch specifically for the task you are working on:

```Bash
git checkout -b feature/your-task-name # Create and change to new branch
```

3. **During the workday (Save changes)**
Write your code, save your files, and make frequent commits. 
> Note that the `git add .` command must be executed from the root folder of the project (not from subfolders inside)

```Bash
git add . # Add the current folder to the commit
git commit -m "feat: brief description of what you just did" # Add a msg to the commit
git push origin feature/your-task-name # Save your commit on cloud (updating your branch)
```

4. **When finishing the task (Integrate into main)**
1. Push your final changes to GitHub (`git push` from previous step).
2. Go to the repository's website on GitHub and click Compare & pull request.
3. Review the changes, create the Pull Request, and click Merge pull request.

5. **Local clean-up**
Once merged on GitHub, return to your terminal to update and delete your local branch:

```Bash
git checkout main # Change back to main branch
git pull origin main # update your local project
git branch -d feature/your-task-name # delete your branch
```

> Doing the `git pull origin main` again in the final step is useful when we have both updated the project files, so you can also download my changes on your local computer.