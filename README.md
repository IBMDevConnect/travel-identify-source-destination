# Identifying correct source and destination of travel using Watson Knowledge Studio, Watson Natural Language Understanding and Watson Assistant.

Contributors: Rajesh Gudikoti & Riya Mary Roy

* Build a custom model in Watson Knowledge Studio.
* Import that model into Watson Natural Language Understanding.
* Invoke Watson Assistant, which internally uses NLU to identify the source and destination in user queries.

### Watson Assistant response to user query with and without NLU(custom model)

## Technical Architecture

![](images/architecture.png)

The process is as follows:

* We create a Watson Natural Language Understanding service from an IBM Cloud account.
* Create Cloud Functions to extract source and destination in user query.
* We create Watson Assistant and invokes Cloud Functions.

## Included Components
* [Watson Natural Language Understanding](https://console.bluemix.net/catalog/services/natural-language-understanding): A cognitive search and content analytics engine for applications to identify patterns, trends, and actionable insights.
* [Watson Assistant](https://console.bluemix.net/catalog/services/watson-assistant-formerly-conversation): With the IBM Watson Assistant service, you can build a solution that understands natural-language input and uses machine learning to respond to customers in a way that simulates a conversation between humans.
* [IBM Cloud Functions](https://console.bluemix.net/openwhisk): IBM Cloud Functions (based on Apache OpenWhisk) is a Function-as-a-Service (FaaS) platform which executes functions in response to incoming events and costs nothing when not in use.

# Steps

1. [Clone the repo](#1-clone-the-repo)
2. [Create IBM Cloud services](#2-create-ibm-cloud-services)
3. [Create Watson Natural Language Understanding (NLU)](#)
4. [Configure IBM Cloud Functions (Serverless)](#4-configure-ibm-cloud-functions-serverless)
5. [Configure Watson Assistant](#5-configure-watson-assistant)

## 1. Clone the repo

```
git clone https://github.com/IBMDevConnect/travel-identify-source-destination
```

## 2. Create IBM Cloud account (Ignore this step if you have account)

https://console.ng.bluemix.net/registration/

Create the following IBM Cloud Services:

## 3. Create Watson Natural Language Understanding (NLU)

Note: Keep the credentials(username and password) of NLU service handy, they will be used later in Watson Assistant.

## 4. Configure IBM Cloud Functions (Serverless)
* Navigate to root of the cloned project(travel-identify-source-destination folder) on Terminal
* Execute below command

```
ibmcloud fn action create extractLocation --docker ragudiko/python_nltk_location_extract-22 __main__.py
```

Response should be "ok: created action extractLocation".

Note: The action name 'extractLocation' will be used in Watson Assistant, so keep it handy.

Click the Hamburger to open the menu

![](images/1-screenshot.png)


Select Functions from menu

![](images/2-screenshot.png)


Take note of Current Namespace and API Key (required in later steps)

![](images/3-screenshot.png)

From left navigation menu click Actions, verify the action 'extractLocation' is listed.


## 5. Configure Watson Assistant

Navigate to Catalog > AI > Watson Assistant

![](images/8-screenshot.png)


Create Watson Assistant Service

![](images/9-screenshot.png)


Launch Tool

![](images/10-screenshot.png)


Import Workspace by clicking on Upload icon

![](images/11-screenshot.png)


Choose JSON file [workspace-dc5ee9e6-a979-4cd4-a548-520252772a61.json](https://github.com/IBMDevConnect/travel-identify-source-destination/tree/master/watson-assistant-workspace) from the folder and click on Import

![](images/12-screenshot.png)


Within Dialog Tab, click on book flight that has country/state mentioned node

![](images/13-screenshot.png)


Within JSON Editor, update IBM Cloud Functions username, password, namespace and action name (credentials which was saved earlier )
NOTE: From the API Key-The segment before the colon (:) is your IBM Cloud Functions Username & segment after the colon is your IBM Cloud Functions Password

Also, update Natural Language Understanding service username,password

![](images/14-screenshot.png)


## Sample Output

You can test it out in Try it Out panel of Watson Assistant!

![](images/sample-output.png)

# Links
* [Watson Natural Language Understanding](https://www.ibm.com/watson/services/natural-language-understading/)
* [Watson Assistant](https://www.ibm.com/watson/services/conversation/)
* [IBM Cloud Functions](https://www.ibm.com/cloud/functions)

# Learn more

* **Artificial Intelligence Code Patterns**: Enjoyed this Code Pattern? Check out our other [AI Code Patterns](https://developer.ibm.com/code/technologies/artificial-intelligence/).
* **AI and Data Code Pattern Playlist**: Bookmark our [playlist](https://www.youtube.com/playlist?list=PLzUbsvIyrNfknNewObx5N7uGZ5FKH0Fde) with all of our Code Pattern videos
* **With Watson**: Want to take your Watson app to the next level? Looking to utilize Watson Brand assets? [Join the With Watson program](https://www.ibm.com/watson/with-watson/) to leverage exclusive brand, marketing, and tech resources to amplify and accelerate your Watson embedded commercial solution.

# License

[Apache 2.0](LICENSE)
