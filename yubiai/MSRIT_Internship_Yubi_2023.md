# Open Source Projects for Students

Following is the list of some of the projects to which students can contribute. The list is ever-growing and limited only by imagination. We will discuss each of these projects in detail once finalised.

| ID | Project                                                                                                | Priority  | Complexity |
|:--:|--------------------------------------------------------------------------------------------------------|:---------:|:----------:|
| 19 | Data Augmentation for training - Ex: Driving License , PID replacement (in-painting)                   |    High   |   Medium   |
| 9  | Table-to-Text Summary generation                                                                       |    High   |    High    |
| 6  | Create/Collect summarisation datasets in the fintech domain                                            |    High   |     Low    |
| 8  | NER for fintech - Data Collection, Tagging and Model training                                          |    High   |   Medium   |
| 16 | Twitter Or Web Sentiment Analysis for companies and CXOs real-time                                     |    High   |   Medium   |
| 17 | Collections Sentiment Analysis - if data is available publicly                                         |    High   |   Medium   |
| 18 | News/Title/Feed sentiment analysis                                                                     |    Low    |   Medium   |
| 4  | Better Noise Removal from noisy agent/customer calls                                                   |    Low    |    High    |
| 13 | Edge device DL model development and deployment                                                        |    Low    |    High    |
| 3  | Better Skew Detection and correction in uploaded Fintech Documents                                     |    Low    |   Medium   |
| 11 | Text-2-Speech → Data, model, open-source benchmarks                                                    |    Low    |   Medium   |
| 12 | Model optimisation for inference (Quantisation, teacher-student)                                       |    Low    |   Medium   |
| 15 | ChatGPT Analysis - Report on strength, what use cases to use and the guardrails required               |    Low    |     Low    |
| 2  | Model hallucination + Factual text generation model for FinTech (Summary, NER)                         |   Medium  |    High    |
| 5  | Creating a signature for each user based on his/her speech patterns                                    |   Medium  |    High    |
| 7  | Speech/Voice sentiment analysis of agent/customer calls                                                |   Medium  |    High    |
| 14 | Faster model training (Single gpu LLMs)                                                                |   Medium  |    High    |
| 1  | Create/Collect QnA dataset for Fintech Chatbot or Auto-QnA system                                      |   Medium  |     Low    |
| 10 | Write test cases for “YubiAI git repository” AND Maintain features/issues for  “YubiAI git repository” |   Medium  |     Low    |

## Project Briefs

1. Create/Collect QnA dataset for Fintech Chatbot or Auto-QnA system
&emsp;&emsp;* Data collection task to train a model like chatgpt but for fintech queries
&emsp;&emsp;* We need to collect as many questions and answers which are Finance, business, and fintech related and create a corpus.
</br>
2. Model hallucination + Factual text generation model for FinTech (Summary, NER)</br>
&emsp;&emsp;* Generative AI can not answer deterministically .. it generally hallucinates the next text to be generated. </br>
&emsp;&emsp;* But for Fintech we need factual information to be present in let's say Summary Or NER generation tasks.</br>
&emsp;&emsp;* We need to study this hallucination part of model learning and make sure that fine-tuned models always output factual information.</br>
</br>
3. Better Skew Detection and correction in uploaded Fintech Documents</br>
</br>
4. Better Noise Removal from noisy agents/customer calls</br>
</br>
5. Creating a signature for each user based on his/her speech patterns</br>
&emsp;&emsp;* There is a need to identify one speaker from another </br>
&emsp;&emsp;* Also, a speech dimerisation task where we need to know who spoke when</br>
&emsp;&emsp;* Another use-case for agent calls over the call or in an actual visit … we need to check if the agent actually spoke or someone else. </br>
&emsp;&emsp;* To tackle these problems we need to create a signature for each user so that we can identify them.</br>
</br>
6. Create/Collect summarisation datasets in the fintech domain</br>
&emsp;&emsp;* News summary generation - data collection/curation task</br>
&emsp;&emsp;* We need to collect as much News and Its summary corpus as possible .. only specific to Finance, business, and fintech.</br>
&emsp;&emsp;* It will be used in summary generation models</br>
</br>
7. Speech/Voice sentiment analysis of agent/customer calls</br>
&emsp;&emsp;* During the call, agents can misspeak or speak rudely with customers</br>
&emsp;&emsp;* Customers can also reply back with NSFW language</br>
&emsp;&emsp;* Also, there is a need to understand the Customer's reply and detect their intent</br>
&emsp;&emsp;* We plan to work on this project from a Text perspective and also on Speech directly</br>
</br>
8. NER for fintech - Data Collection, Tagging and Model training</br>
&emsp;&emsp;* Data collection/curation task for NER model training</br>
&emsp;&emsp;* We need as much data as possible from Fintech + Indian regional text perspective tagged as NER. </br>
&emsp;&emsp;* Open-ended problem</br>
</br>
9. Table-to-Text Summary generation</br>
&emsp;&emsp;* Give a table of information we need to put down in readable text</br>
&emsp;&emsp;* Like providing a summary of the given table </br>
&emsp;&emsp;* Open-Ended problem</br>
</br>
10. Write test cases for “YubiAI git repository” AND Maintain features/issues for  “YubiAI git repository”</br>
</br>
11. Text-2-Speech → Data, model, open-source benchmarks</br>
&emsp;&emsp;* There is a use-case where we want to create a speech bot and let it respond back.</br>
&emsp;&emsp;* So TTS capability is required </br>
&emsp;&emsp;* It should have support for Indian regional languages as well</br>
</br>
12. Model optimisation for inference (Quantisation, teacher-student)</br>
</br>
13. Edge device DL model development and deployment</br>
</br>
14. Faster model training (Single gpu Latge Model training)</br>
&emsp;&emsp;* Large Deep learning model training requires many GPUs and workstations</br>
&emsp;&emsp;* We need to figure out a way to train such models on smaller or even single GPUs</br>
&emsp;&emsp;* Open-ended problem</br>
</br>
15. ChatGPT Analysis - Report on strength, what use cases to use and the guardrails required</br>
</br>
16. Twitter Or Web Sentiment Analysis for companies and CXOs real-time</br>
&emsp;&emsp;* Given a feed of news about the company or its CXOs.. we need to identify its sentiment</br>
&emsp;&emsp;* Twitter is just one example .. it can be any social media platform</br>
</br>
17. Collections Sentiment Analysis/ Top reasons for complaints </br>
&emsp;&emsp;* Check if data is available publicly such as Twitter </br>
&emsp;&emsp;* Search for loan collection, scrape the data</br>
&emsp;&emsp;* Store and analyze and perform graphs/top reasons for complaints </br>
</br>
18. News/Title/Feed sentiment analysis</br>
</br>
19. Data Augmentation for training - Ex: Driving License, PID replacement (in-painting)</br>
&emsp;&emsp;* Take a standard DL or any card-based document </br>
&emsp;&emsp;* Create a synthetic pipeline around it i.e example scramble letters, remove few letters and create the same with alternate names </br>
&emsp;&emsp;* Geometrically place text/part of the items in different 3d space example DOB placed in different positions</br>
&emsp;&emsp;* Create the entire pipeline to generate N data points as required </br>
</br>