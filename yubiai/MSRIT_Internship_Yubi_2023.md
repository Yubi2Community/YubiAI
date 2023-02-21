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
    1. Data collection task to train a model like chatgpt but for fintech queries
    2. We need to collect as many questions and answers which are Finance, business, and fintech related and create a corpus.
</br>
</br>
2. Model hallucination + Factual text generation model for FinTech (Summary, NER)</br>
    1. Generative AI can not answer deterministically .. it generally hallucinates the next text to be generated. </br>
    2. But for Fintech we need factual information to be present in let's say Summary Or NER generation tasks.</br>
    3. We need to study this hallucination part of model learning and make sure that fine-tuned models always output factual information.</br>
</br>
</br>
3. Better Skew Detection and correction in uploaded Fintech Documents</br>
</br>
</br>
4. Better Noise Removal from noisy agents/customer calls</br>
</br>
</br>
5. Creating a signature for each user based on his/her speech patterns</br>
    1. There is a need to identify one speaker from another </br>
    2. Also, a speech dimerisation task where we need to know who spoke when</br>
    3. Another use-case for agent calls over the call or in an actual visit … we need to check if the agent actually spoke or someone else. </br>
    4. To tackle these problems we need to create a signature for each user so that we can identify them.</br>
</br>
</br>
6. Create/Collect summarisation datasets in the fintech domain</br>
    1. News summary generation - data collection/curation task</br>
    2. We need to collect as much News and Its summary corpus as possible .. only specific to Finance, business, and fintech.</br>
    3. It will be used in summary generation models</br>
</br>
</br>
7. Speech/Voice sentiment analysis of agent/customer calls</br>
    1. During the call, agents can misspeak or speak rudely with customers</br>
    2. Customers can also reply back with NSFW language</br>
    3. Also, there is a need to understand the Customer's reply and detect their intent</br>
    4. We plan to work on this project from a Text perspective and also on Speech directly</br>
</br>
</br>
8. NER for fintech - Data Collection, Tagging and Model training</br>
    1. Data collection/curation task for NER model training</br>
    2. We need as much data as possible from Fintech + Indian regional text perspective tagged as NER. </br>
    3. Open-ended problem</br>
</br>
</br>
9. Table-to-Text Summary generation</br>
    1. Give a table of information we need to put down in readable text</br>
    2. Like providing a summary of the given table </br>
    3. Open-Ended problem</br>
</br>
</br>
10. Write test cases for “YubiAI git repository” AND Maintain features/issues for  “YubiAI git repository”</br>
</br>
</br>
11. Text-2-Speech → Data, model, open-source benchmarks</br>
    1. There is a use-case where we want to create a speech bot and let it respond back.</br>
    2. So TTS capability is required </br>
    3. It should have support for Indian regional languages as well</br>
</br>
</br>
12. Model optimisation for inference (Quantisation, teacher-student)</br>
</br>
</br>
13. Edge device DL model development and deployment</br>
</br>
</br>
14. Faster model training (Single gpu Latge Model training)</br>
    1. Large Deep learning model training requires many GPUs and workstations</br>
    2. We need to figure out a way to train such models on smaller or even single GPUs</br>
    3. Open-ended problem</br>
</br>
</br>
15. ChatGPT Analysis - Report on strength, what use cases to use and the guardrails required</br>
</br>
</br>
16. Twitter Or Web Sentiment Analysis for companies and CXOs real-time</br>
    1. Given a feed of news about the company or its CXOs.. we need to identify its sentiment</br>
    2. Twitter is just one example .. it can be any social media platform</br>
</br>
</br>
17. Collections Sentiment Analysis/ Top reasons for complaints </br>
    1. Check if data is available publicly such as Twitter </br>
    2. Search for loan collection, scrape the data</br>
    3. Store and analyze and perform graphs/top reasons for complaints </br>
</br>
</br>
18. News/Title/Feed sentiment analysis</br>
</br>
</br>
19. Data Augmentation for training - Ex: Driving License, PID replacement (in-painting)</br>
    1. Take a standard DL or any card-based document </br>
    2. Create a synthetic pipeline around it i.e example scramble letters, remove few letters and create the same with alternate names </br>
    3. Geometrically place text/part of the items in different 3d space example DOB placed in different positions</br>
    4. Create the entire pipeline to generate N data points as required </br>
</br>
</br>