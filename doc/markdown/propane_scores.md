# Propane Scores

Scores in Propane are contained the propane_scores.txt file. Yeah we know what your thinking "Have you ever heard of a database loser???". Yes we have, and while we are making many changes to Propane from its base of NetKoTH, there are somethings we just don't want to change. One of those things is how NetKoTH has this cool parser that lets you handle scoring without needing a heavy and complex database system. Also not having a "real" database means one less input vector if some mean rule breaker wants to attack the score box.


All in all Propane should never be run in a directory accessible to users in any way shape or form (covered more in setup.md which is coming soon!). Propane therefore can do funky things that make life easy, like write easy to parse score data to a text file, and make system calls, without worrying about security implications because if you set up the scoring server correctly this doesn't matter (besides if they get into the scoring server what kind of behind the scenes stuff Propane is doing is meaningless). So we chose simplicity, elegance, and cool text parsing > clunky database dependency. It was one of the things we thought made the original NetKoTH great so it's here to stay!


So how to we use the propane_scores.txt?


Well there really isn't anything you have to do! This file by default is BLANK and gets initialized dynamically, but normally this is how it might look in different scenarios:


## Initialized No Scores:

```
[TotalScores]

[linuxScores]

[windoosScores]

```


## Scores:

```
[TotalScores]
myntal = 60
3ndg4me = 40

[linuxScores]
myntal = 60

[windoosScores]
3ndg4me = 40

```


The scoring engine takes care of all of this for you. It's the primary functionality of Propane. However this documentation is here because it is important to understand the format of the propane_scores.txt file and note that you can edit scores dynamically.


Want to penalize a player and deduct points? Simply change their score in the propane_scores.txt file in real time as the game is running! Want to merge team names/points cause someone accidentally mistyped their team name on a box and now have two different scores? You can do that too!


## Examples:


### Change Score

**Before**
```
[TotalScores]
myntal = 60
3ndg4me = 40

[linuxScores]
myntal = 60

[windoosScores]
3ndg4me = 40

```


**After**
```
[TotalScores]
myntal = 60
3ndg4me = 70

[linuxScores]
myntal = 60

[windoosScores]
3ndg4me = 70

```

### Merge users

**Before**
```
[TotalScores]
myntal = 60
3ndg4me = 40
mintal = 10

[linuxScores]
myntal = 60

[windoosScores]
3ndg4me = 40
mintal = 10

```

**After**
```
[TotalScores]
myntal = 70
3ndg4me = 40

[linuxScores]
myntal = 60

[windoosScores]
3ndg4me = 40
myntal = 10

```


As an administrator you have full control over teams and scores, and all you have to do is make simple edits to the propane_scores.txt file.
