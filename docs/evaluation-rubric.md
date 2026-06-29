PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git init
Reinitialized existing Git repository in C:/Users/USER/OneDrive/Documents/Desktop/llm-response-evaluation/.git/
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        LICENSE
        README.md
        data/
        docs/
        examples/
        notebook/
        requirements.txt
        src/

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git remote -v
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git branch -M main        
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git branch
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git remote add origin https://github.com/kevinnjogu-dev/llm-response-evaluation.git
error: remote origin already exists.
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git remote -v
origin  https://github.com/kevinnjogu-dev/llm-response-evaluation.git (fetch)
origin  https://github.com/kevinnjogu-dev/llm-response-evaluation.git (push)
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git add .
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git commit -m "Initial project structure"
[main (root-commit) 29e06f0] Initial project structure
 15 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 data/prompts.json
 create mode 100644 data/sample_responses.json
 create mode 100644 docs/evaluation-rubric.md
 create mode 100644 docs/methodology.md
 create mode 100644 examples/average_response.md
 create mode 100644 examples/good_response.md
 create mode 100644 examples/poor_response.md
 create mode 100644 notebook/evaluation_demo.ipynb
 create mode 100644 requirements.txt
 create mode 100644 src/evaluator.py
 create mode 100644 src/scoring.py
 create mode 100644 src/utils.py
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git push -u origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 767 bytes | 191.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/kevinnjogu-dev/llm-response-evaluation.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git add .
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git commit -m "Add project documentation"
[main 478cef4] Add project documentation
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {notebook => notebooks}/evaluation_demo.ipynb (100%)
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 238 bytes | 238.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/kevinnjogu-dev/llm-response-evaluation.git
   29e06f0..478cef4  main -> main
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git add .
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git commit -m "Add project documentation"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git push
Everything up-to-date
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git add README.md
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git commit -m "Update README with project overview"
[main 7c19991] Update README with project overview
 1 file changed, 66 insertions(+)
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 832 bytes | 208.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/kevinnjogu-dev/llm-response-evaluation.git
   478cef4..7c19991  main -> main
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git add docs/evaluation-rubric.md
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git commit -m "Add evaluation rubric"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git push
Everything up-to-date
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\USER\OneDrive\Documents\Desktop\llm-response-evaluation> 