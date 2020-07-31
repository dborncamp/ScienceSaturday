# Science Saturday
Welcome to the repo for the Science Saturday Team.
The goal of this repo is to collaborate to publish a paper for April 1, 2018 archive papers.

Here we have the Data, programs to make plots, and latex manuscript of paper.

## To collaborate
If there is something you want to have a discussion about, open an issue about it and we can discuss it.

Otherwise if there is something you want to contribute, create a new branch and file a PR to merge it to master.
Get someone else to review the PR and it will be merged and made into the final paper.
It is good practice to have someone look over what you merge to master before you just push it straight to master (looking at you, almost everyone at ST with bad git practices).


## Analysis Environment
I assume that most people attending Science Saturday are best in Python so I have included some Python notebooks with my initial work.
And since not everyone is able to use Docker or something like that I have included a txt file that includes all of the packages I used to do the analysis.
To install the conta environment from the file use:

`conda env create --file scilib-env.txt`


If there is something that you need to add, please use conda and update the environment file so that we can all have what you needed for your code/plot.
You can do this by using:

`conda list --explicit > scilib-env.txt`

As much as I *REALLY* hate using notebooks (and I think they should never be used for anything beyond a tutorial) that is probably what everyone else is most comfortable with so I have started putting in notebooks in the repo for everyone to get things started.


## The Data
I have cleaned the data from the google sheet (https://docs.google.com/spreadsheets/d/1clTSVXBHpFB_4yqkAQhzvsDoVax4SZUYpGdbCy7FZ6U/edit#gid=329859720) a little and it should be easily readable using a Pandas dataframe.
See the Python notebooks in `lib` to do this.

## Future Science Saturdays
Below are some ideas that have been floated for future Science Saturday adventures:

- Cold red wine same as white wine? (reverse of SS1)
- Should we test different priced vodkas?
- Let's test chocolate!
- Coffee coffee coffee
