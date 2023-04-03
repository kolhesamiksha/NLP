#  **Get started with Streamlit App**

### End to End Practical guide to Publish your first Streamlit app, here at Katonic platform.

### 

### **Overview**

This article will show you how to publish a Python App using Streamlit
on Katonic Platform.

In this tutorial you will learn:

-   Spin a workspace environment with the necessary dependencies to
    publish a Streamlit App.

-   Setup and create a sample Streamlit app.

-   Host your App directly to the Katonic Deployment Launchpad.

Let's publish your first Streamlit App on Katonic Platform.

## **Setting-up your Workspace**

To run any python code, First it's necessary to setup the environment to
work on. Create a VS Code workspace to run your Python App.

1.  From the platform, Select **Workspace** and then click on **Create
    Workspace**.

2.  Fill the following details under workspace:

    -   **Name:** fill your workspace name.

    -   **Select Environment:** select VSCode environment.

    -   **Webapp:** Select Streamlit.

    -   **Image:** Select Streamlit version.

    -   **Additional Port:** Select port where you want to run your app.
        It\'s necessary during the Launch of your App.

    -   **Resources:** Desired compute resource for workspace.

    -   Click on **Create**

3.  You will be directed to the Workspace overview window, where you can
    see your workspace under processing.

4.  It will take approximately 2-3 minutes to get this workspace ready.
    Try to Refresh the page.

Note: Refresh the page, if it'll be in processing even after 2-3 mins.

5.  You can connect to your workspace, when the processing tab changes
    to running.

6.  Click on the C**onnect** to use this Workspace for App building.

## 

Now, you're done with workspace setup, Let's create a sample app.

## **Required GitHub instructions and setup**

Follow these instructions to download the sample App code from github.
If you wish to code by yourself, you can directly create an app.py file
to start coding the app.

Follow this
[Link](https://github.com/kolhe-samiksha/katonic_streamlit_guide/tree/main)
to download the sample code from github.

1.  Go on terminal in VS Code, use Ctrl+Shift+\`

2.  Run git clone url_of_repo (from above Link).

3.  Your Code will get downloaded.

## For more info about how to use git. Follow this [Link](https://github.com/katonic-dev/Examples)

## **Start the app development**

1.  Write your sample app.py code there or copy below sample code.

Note: Always define the routes as given in sample code, routes =
os.environ\[\"ROUTE\"\]

## 

## 

## **Test your app**

1.  Create the **requirements.txt** file with all required dependency.

2.  Here is the **requirements.txt** code used in above app.

> **altair**\
> **pandas**\
> **streamlit**

Note: Type the following commands into the Bash.

> **pip install -r requirements.txt**\
> **streamlit run app.py \--server.port=8050 \--server.address=0.0.0.0**

Note: keep the path relative to your folder structure.\
Note: keep your app name as \_\_app.py\_\_ and requirement file as
\_\_requirements.txt\_\_

To test the App on your local browser, follow further steps.

1.  After running that streamlit run app.py command, you'll received a
    local url e.g. http://0.0.0.0/8050.

2.  Now, copy the workspace URL from search bar of your browser.

3.  Paste on new tab and remove the query part e.g.

**URL**:
https://dev-release-test.katonic.ai/ws-61df0429-d0f6-4c76-bcbf-7da63e2b2d43-641adea97dab73d68f9fe8e7/vscode/?folder=/home/katonic/workspace"

Do the changes to the URL like below methods:

"https://dev-release-test.katonic.ai/ws-61df0429-d0f6-4c76-bcbf-7da63e2b2d43-641adea97dab73d68f9fe8e7/8050/"

Or

"https://dev-release-test.katonic.ai/ws-61df0429-d0f6-4c76-bcbf-7da63e2b2d43-641adea97dab73d68f9fe8e7/8050/?folder=/home/katonic/workspace"

3\. Go back to the Workspaces.

Your App will automatically get hosted on Katonic Platform.

4\. Click on the Live app to see your app.

5\. Your app will open on the new tab.

6\. You can also monitor your running workspace usage by clicking on
**Usage** on right corner.

7\. To see the how app got hosted on katonic platform, click **Logs** on
right corner.

Finally commit and push your code to the GitHub. Follow the
[Link](https://docs.katonic.ai/UserGuide/Git-Integration) for
instructions required to commit and push in the VSCode.

## **Deploy your App**

1.  To deploy your app, go to the **Deploy tab** and click on the **+App
    Deployment** button.

Fill the details as follow:

-   **App Name**: your app name.

-   **Select Environment**: your app environment.

-   **Github Token**: your github token.

-   **Username**: your github account user-name.

-   **Account Type**: Select your account personal or organisation.

-   **App Visibility: S**elect visibility as public or private.

-   **Repository**: Select the app repository where you app code is
    present.

-   **Revision Type:** branch or tags. Further mentioned the respective
    branch_name or tag_name as per your github repo.

-   **Main_file Path:** app.py file name

-   **Resources**: choose desired compute resources.

-   **Pod_Range**: keep that 1-2 pods only.

-   **+Add Environment variable**: if you've used any os
    dependencies\...you can add this here.

2.  Click on the Deploy button, it will take you to the Deploy window
    again.

3.  Here you can see your App deployment status **processing**.

4.  After few minutes status will change to **running**.

5.  check the logs.

6.  you can view the current status and check if the deployed app is
    ready to go.

```{=html}
<!-- -->
```
7.  To launch your app, click on **App URL**.

8.  The app will launch in a new tab.

**You can share the App Url to showcase your work.**
