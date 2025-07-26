# README Programmer Debates
<img width="320" alt="image" src="https://github.com/user-attachments/assets/d1afc348-7619-4754-b54a-a11a12c33383" />
<img width="320" alt="image" src="https://github.com/user-attachments/assets/726730ef-8c0f-46da-a3b8-627dba14ab99" />
<img width="320" alt="image" src="https://github.com/user-attachments/assets/c2ff1c2f-aaea-49b5-b2d7-ff44f4895889" />

**This is a fun little section to put on a readme, which allows viewers to vote on a controversial programming debate.**

Every 8 hours, a Github Action is set to pick a new question and reset the counts. There are buttons to vote, which send a request to a remote server, which manages the counts.

Your vote may not appear instantly, due to Github Image caching. A Github Action force resets the cache every 30 minutes, otherwise wait a few minutes and it may appear.

## Usage
1. Fork this repository.
2. Use [Nest](https://hackclub.app) or similar to host `server.py` (a flask app)
3. Update all references to `https://froggerapi.madavidcoder.hackclub.app` within `updater.py` and the below snippet, to the url that your flask app listens to.
4. Add the below snippet into your `README.md` file, to display the questions:
    ```Markdown
    ## Programmer Debate
    ### <!-- Question starts -->Questions will appear here!<!-- Question ends -->
    #### Vote
    [<kbd> <br> <!-- Option 1 starts -->Option 1!<!-- Option 1 ends --> <br> </kbd>][Option 1]
    [<kbd> <br> <!-- Option 2 starts -->Option 2!<!-- Option 2 ends --> <br> </kbd>][Option 2]
    #### Here's what the internet thinks!
    <!-- Results 1 starts -->
    Results will appear here!
    <!-- Results 1 ends -->
    <!-- Results 2 starts -->
    Results will appear here!
    <!-- Results 2 ends -->
    ---
    <sup><sub>A new question will appear every six hours, check [MadAvidCoder/ReadmeProgrammerDebates](https://github.com/MadAvidCoder/ReadmeProgrammerDebates) to see how it works!</sub></sub>

    <!-- Links -->
    [Option 1]: https://<your-server-url>/option-1
    [Option 2]: https://<your-server-url/option-2
    ```
5. Add `build.yml` and `reset.yml` to your `.github/workflows` folder, so that the questions and results will automatically update.
