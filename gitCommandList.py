#first time working with git
1. Download git from git_scm.com

2. git version      check version of git

3. config git to set name and email before start using git
    git config --global user.name "Sonthaya Deelua"         create name  of user
    git config --golbal email "sdeelua@hotmail.com"         create email of user 
    git config --global --list                              will show name and email which just create
    cat ~/.gitconfig                                        will show name and email same as above

4. Create new file and open file in git
    echo "Hello" > gitLearn.md                              create new file "gitLearn.md" and that file contain the word "Hello"
    code .                                                  Open that repo with VSCode

5. Then we will create git repository
    git init        create Git Repository and will show below detail
        Reinitialized existing Git repository in C:/Users/sdeel/OneDrive/เอกสาร/Github/.git/

6. If we could not see .git file in folder we have to set up at Control Panel of our computer
    Select the Start button, then select Control Panel > Appearance and Personalization. 
    Select Folder Options, then select the View tab. Under Advanced settings, select Show hidden files, 
    folders, and drives, and then select OK.

6.1 if we want to exclude any file in repo from commit . we will create .gitignore file and put all file name that we want to exclude and also *.log to exclude all log file

7. git add gitLearn.md                              will add gitLearn.md file into staging area
   if file name has space like git learn. 
   git add "git learn"      we can use double qoute 

8. After git add if we have any update or edit in the file we can use "git diff" it will show differnce between "working directory" and "staging area"

9. git commit -m"message" to commit 
        git commit      keep permanent from staging area into repository
            $ git commit -m"my first commit"
            [master c4a083c] my first commit
            1 file changed, 2 insertions(+)
            create mode 100644 lerningGit.md

        git log         will show all commit history 
            $ git log
                commit c4a083c8adc33186ac195bd9cda71e71b1d72c7a (HEAD -> master)
                Author: Sonthaya Deelua <sdeelua@hotmail.com>
                Date:   Sun Jun 19 12:49:40 2022 -0400

                my first commit

                commit cbb5e733b14fc0d14fdadfa66bb3f1633cbbd900
                Author: sonthaya deelua <sdeelua@hotmail.com>
                Date:   Sun Jun 19 08:50:26 2022 -0400

                add other local repo

        git log --oneline --graph --decorate --all          Will see shorter message from git log
                $ git log --oneline --graph --decorate --all
                * c4a083c (HEAD -> master) my first commit
                * cbb5e73 add other local repo
                * 8bee080 (origin/master) Testlocalrepo
        git log --pretty=oneline        will show only one line per log


10.   git status      check status of working directory and staging area. Sometime we add new line into working directory but has not do "git add" yet
      git add         add working directory into staging area
      git diff        show difference detail between working directory and staging area
      git commit      keep permanent from staging area into repository
      git log         show all commit

11. ถ้าเราเผลอลบข้อมูลในไฟล์ออกไป หรือใช้คำสั่งเพื่อลบข้อมูลในไฟล์ที่ commit แล้วไป
    echo "" > lerningGit.md       ข้อมูลในไฟล์จะถูกลบออกไปทั้งหมด

12. git show HEAD      Will show the latest update version from git which have all data in file
        commit c4a083c8adc33186ac195bd9cda71e71b1d72c7a (HEAD -> master)
        Author: Sonthaya Deelua <sdeelua@hotmail.com>
        Date:   Sun Jun 19 12:49:40 2022 -0400

        my first commit

        diff --git a/lerningGit.md b/lerningGit.md
        new file mode 100644
        index 0000000..934cf4c
        --- /dev/null
        +++ b/lerningGit.md
        @@ -0,0 +1,2 @@
        +##add after git add to learn
        +###add after git add##

13. git checkout HEAD lerningGit.md     This will resume all data (same latest commit) back to file     
  
#BRANCH  การจัดการไฟล์ส่วนใหญ่จะทำที่ master Branch แต่ถ้าเราจะทำงานกับ ไฟล์ ส่วนใหญ่จะต้องสร้าง branch แยกไปทำงาน แล้วค่อย merce กล้บ

14.  git branch     to check how many branch we have and which branch we are

15.  git branch workingBr      create new branch with name "workingBr"

16. git branch    again will show
        $ git branch
        * master    (* show which branch we are)
          workingBr

17. git checkout workingBr          When we want to swith to work at new branch
        Switched to branch 'workingBr'
18. git branch
     master
     * workingBr

19. git checkout -b branchname      if we want to create new branch and work with it immediately
    (Another way of crate new branch name by using git checkout instead of git branch "branch name"

When we create new branch, All file from Master will show in new branch also

20. Test to create new file into "workingBr" branch
     echo "I add new file into workingBr" >> WorkingInBr.md

21. Then will to do git add  and git commit in this branch as mormal. This file here will not show in master branch.

#To add this file into Master brach

22. git checkout master      switch to work at master branch
    git merge workingBr      Merge workingBr branch into master branch

    $ git merge workingBr
    Updating c4a083c..41750a6
    Fast-forward
    WorkingInBr.md | 1 +
    1 file changed, 1 insertion(+)
    create mode 100644 WorkingInBr.md

23. git log         will show all commit from both branch in master
    $ git log
    commit 41750a6b47cb1aa97f4aea0be3bd23077a74d695 (HEAD -> master, workingBr)
    Author: Sonthaya Deelua <sdeelua@hotmail.com>
    Date:   Sun Jun 19 13:43:24 2022 -0400

    commit WorkingInBr file

    commit c4a083c8adc33186ac195bd9cda71e71b1d72c7a
    Author: Sonthaya Deelua <sdeelua@hotmail.com>
    Date:   Sun Jun 19 12:49:40 2022 -0400

    my first commit

    commit cbb5e733b14fc0d14fdadfa66bb3f1633cbbd900
    Author: sonthaya deelua <sdeelua@hotmail.com>
    Date:   Sun Jun 19 08:50:26 2022 -0400

    add other local repo

24. git branch -d workingBr         After merge, we use this command to delete branch that we dont need anymore  

####All above are git working in our local only -- Now we are going to connect to github######

25. In github --> profile --> your repository --> Create new repo and fill all data and copy SSH

26. Back in Documents in locat in git : git clone git@github.com:SonthayaDeelua/Jun19Repo.git       This will clone all data from github (remote repo) into local
27. After cloning --> repo which clone from github
28  git remote -v  will show remote address both fetch and push
        origin  git@github.com:SonthayaDeelua/TE-Module-2.git (fetch)
        origin  git@github.com:SonthayaDeelua/TE-Module-2.git (push)
29. git fetch   when we want to check if any update at remote repository and will show if found anything difference
30. git status  will show that local is 1 commit behind to remote and will recommend to use git pull to pull data from remote to local
31. git merge origin/master     will merge data from remote into local
32. git pull origin/master is the same as git fetch & git merge combined
33. If we work at local and we want to push it to keep at remote
    git add
    git commit -m "massage"
    git push -u origin main  (New version of github change from master to be main)

34. When we edit file we also can use 
    git commit -am "massege"       -am mean add all and commit use when want to short cut without git add
    
35. git reset --hard c10047a63a2482db4b770440ed2732c063161e58       when we want to reset back to that version of our commit

36. git reset --hard origin/main        When we want to reset to be the same as we are at github now (same as latest version on github)

37. Fork  is the way to copy other people's repo to be our own repo (For studying purpose :)

38. Pull request : When we fork some github repo and we develop some good thing and want orignal repo to be updated same as our repo
    We will do "pull request" to submit our version to all contributor in that Original Repo to review and accept. If everybody agree and will do pull request

39. Set up our repo to be website or git page
     39.1  create new repo with this name rule  :  SonthayaDeelua.github.io
     When we clone it to our local , then we can create out website under github server. but space is limited

40. git help config  / git config --help     Will go the help if need  

41. For those local repo that have not been connected to github yet we can use this command to connect to github
    git config --global user.username + our github username

42. In case we already created some file in out local and already do git add and git commit but not yet connect to remote /git hub
    First : create repo in the hub with same repo name as local repo
    Then link our remot repository from github by
    git remote add  origin + our SSH link from github
    to check if it connect correctly
    git remote -v  will show remote address both fetch and push
        origin  git@github.com:SonthayaDeelua/TE-Module-2.git (fetch)
        origin  git@github.com:SonthayaDeelua/TE-Module-2.git (push)


43. We can use git push to push repo to remote
44. To create file via gitbash
    touch filename.filetype  for example touch  workspace.txt
45. To open above txt file via notepad
    notepad master.txt
46. ls -ltr     will show more file detail inside repo

47. if we already have 5 commit but we want to get back to commit 3 to re-write or add something but we still want to keep commit 4-5 to be the same
    git reset --soft + commit 3 id (longgggg)

    latest commit number will be commit3 , commit 4-5 history will be disappear but what changed in commit 4-5 stil be there.
    This is when do it in local only. 
48. If we already push 5 commit to remote server but we want to delete commit3 out from history
    The logic to do that is, we use
    git revert   + commit3 ID  (revert can do one commit at a time)

    git will create commit6 to remove commit3 but commit3 still show in the history

49. Normally we work with branch at local level only and delete after we already merge into master
    BUT if we want to push that minor branch into remote server also we can use
    git push -u origin + minor branch name

    And once we already merge it into master Branch in local and we push the master to remote server already and we want to delete branch at remote server
    git push origin --delete minor branch name

    git branch -av , git branch -v      list all git branch
    git branch -D + branch name         Delete branch

50. git log --merge     Producing list of commits that are causing the conflict
51. git reset --mixed   to undo the change to the working directory and staging area
52. git merge --abort   exiting merge process and return back to the state before the merging begun

53. When we have merge conflict
    git pull --rebase origin main/master    will show detail where conflict happend

    git mergetool           will open vi command and show detail in file where difference, Once we do manual fix we save by type "wq" to save the final file


    