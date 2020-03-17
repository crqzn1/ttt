# Welcome to Git
## CREATE

 - clone existing repository
`$ git@github.com:crqzn1/ttt.git`
 - create a new local repository
`$ git init`

## LOCAL CHANGES

## HISTORY

## UNDO

## BRANCH & TAGS

## UPDATE & PUBLISH

## MERGE & REBASE

```bash
$ echo "# ttt" > README.md
$ git init
$ ls -a
	.  ..  .git  README.md
$ git status
	On branch master
	Untracked files:
		README.md
		git.png
		git1.png
		kmeans.py
		plot.py
		txdbscan.py
$ git add README.md
$ vi .gitignore
$ cat .gitignore 
	*.png
	*.pdf
	*.[ao]
$ git status
	On branch master
	Changes to be committed:
		new file:   README.md
	Untracked files:
		.gitignore
		kmeans.py
		plot.py
		txdbscan.py
$ git add .
$ git status
	On branch master
	Changes to be committed:
		new file:   .gitignore
		new file:   README.md
		new file:   kmeans.py
		new file:   plot.py
		new file:   txdbscan.py


$ git commit -m 'initial commit'
$ echo "text for 2nd commit" >> README.md
$ git commit -m 'README.md changed for 2nd commit'
$ git log
$ git log -p README.md # detailed log for README.md
$ git log --pretty=oneline
	xxx (HEAD -> master) README.md changed for 2nd commit
	yyy initial commit
$ git branch 
$ echo "kmeans.py uses sklearn package" >> README.md 
$ echo "txdbscan.py is hand coded DBSCAN" >> README.md 
$ git commit -m 'file description added for 3rd commit'


$ vi plot.py
$ git branch test_plotting
$ git checkout test_plotting 
	M	plot.py
	Switched to branch 'test_plotting'
$ git status
	On branch test_plotting
	Changes not staged for commit:
		modified:   plot.py
$ git add plot.py
$ git commit -m '1st commit on branch:plot legend' 
	[test_plotting b658a5e] 1st commit on branch:plot legend
	 1 file changed, 5 insertions(+), 3 deletions(-)
$ git tag 'plot.py_legend'
$ git log --pretty=oneline
	xxx (HEAD -> test_plotting, tag: plot.py_legend) 1st commit on branch:plot legend
	yyy (master) file description added for 3rd commit
	zzz README.md changed for 2nd commit
	aaa initial commit


$ git checkout master
$ git merge test_plotting # merge !!!
	Updating 047564c..b658a5e
	Fast-forward
	 plot.py | 8 +++++---
	 1 file changed, 5 insertions(+), 3 deletions(-)
$ cat plot.py
$ git log --pretty=oneline
	xxx (HEAD -> master, tag: plot.py_legend, test_plotting) 1st commit on branch:plot legend
	yyy file description added for 3rd commit
	zzz README.md changed for 2nd commit
	aaa initial commit
$ git branch -d test_plotting # delete !!!


# https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
$ git branch hotfix
$ echo 'test_plotting branch deleted' >> README.md
$ git add .
$ git commit -m 'delete branch deleted'
$ git checkout hotfix
$ echo 'added by hotfix' >> README.md
$ git commit -a -m '1st commit from hotfix'\
$ git checkout master
$ git merge hotfix 
	Auto-merging README.md
	CONFLICT (content): Merge conflict in README.md
	Automatic merge failed; fix conflicts and then commit the result.'
$ git status
	On branch master
	You have unmerged paths.
	  (fix conflicts and run "git commit")
	  (use "git merge --abort" to abort the merge)
	Unmerged paths:
		both modified:   README.md
$ cat README.md 
	# ttt
	text for 2nd commit
	kmeans.py uses sklearn package
	txdbscan.py is hand coded DBSCAN
	<<<<<<< HEAD
	test_plotting branch deleted
	=======
	added by hotfix
	>>>>>>> hotfix
$ vi README.md
$ git add README.md
$ git commit -m 'conflict resolved'
	[master 28fdb04] conflict resolved
```
