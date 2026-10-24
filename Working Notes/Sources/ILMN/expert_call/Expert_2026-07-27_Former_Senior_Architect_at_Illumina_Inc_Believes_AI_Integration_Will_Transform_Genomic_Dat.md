

COMPANY DEEP-DIVE 

# **Former Senior Architect at Illumina Inc Believes AI Integration Will Transform Genomic Data Analytics** 

DATE PUBLISHED INTERVIEW DATE EXPERT PERSPECTIVE ANALYST PERSPECTIVE PRIMARY COMPANY 29 Jul 2026 27 Jul 2026 Former Investor-Led (Buy-Side) ILMN 

##### **SMART SUMMARY** 

## **Summary** 

The conversation covered the expert's experience in developing data analytics and AI/LLM solutions for genomic data, the challenges and opportunities of integrating AI into customer-facing platforms, and the evolving value proposition in the genomics industry from hardware to advanced analytics and software services. 

##### EXPERT BACKGROUND 

- Former senior software architect with over a decade of experience leading and developing data analytics and algorithmic solutions for DNA and RNA sequencing data at a major genomics company, including integration of AI and LLM technologies. 

##### EXPERT SENTIMENT 

- Strong belief that empowering customers with direct access to their own data via AI/LLM tools is transformative for research and product development. 

- Optimistic about the shift from fixed algorithms to flexible, AI-driven data exploration, but emphasizes the critical need for validation due to the non-deterministic nature of LLMs. 

- Predicts that the long-term value in genomics will shift from sequencing hardware to advanced data analytics and integrated software platforms. 

##### TAKEAWAYS 

- The expert developed a proof-of-concept AI agent that allowed users to query massive genomic datasets in natural language, translating queries to SQL and returning results in seconds. 

- Management was enthusiastic about the AI/LLM integration, pushing the project to pre-alpha production, with a focus on empowering clients to explore their own data beyond pre-defined algorithms. Validation and accuracy of AI-generated queries are crucial, as LLMs can produce incorrect or unintended results; user education is necessary to mitigate risks of hallucination. 

- The expert sees future competitive advantage in providing an integrated, user-friendly platform akin to 'the Amazon for DNA,' where clients can easily store, access, and analyze their data. 

- The expert believes that as sequencing becomes commoditized, the primary value and revenue opportunities will shift to data analytics, software integration, and enabling customer-driven research. 

AlphaSense Assistant is AI Generated 

## **Table of Contents** 

Introduction and Background 

AI Integration and Proof of Concept 

Challenges and Validation of AI Models 

Data Management and Optimization 

Future Directions and Competitive Strategies 

Final Thoughts and Insights 

## **Expert Bio** 

Adjunct Faculty Big Data Modeling and Analytics at University Leavey School of Business. The expert is responsible for teaching distributed computing and scale-out architectures, developing course materials and labs, and instructing students on technologies including MapReduce, Spark, PySpark, Amazon Athena, and Google BigQuery, with hands-on PySpark exercises for large-scale data analysis. Prior to Santa Clara University, the expert was the Senior Architect at Illumina (left August 2025). Reporting to the Director, the expert was responsible for designing, implementing, and deploying scalable genomics algorithms and production pipelines for DNA and generelationship analysis, including validation and verification. The expert can speak to Spark and PySpark architecture and optimization, 

Page 1 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

Snowflake and Amazon Athena for analytics, MapReduce/Hadoop design patterns, large-scale genomic data analytics and DNA sequencing pipelines. 

## **Interview Transcript** 

Client 00:00:00 Thanks for taking the call. I'm looking forward to chatting with you about Illumina and competitors and what's going on with their latest technology. I always say this is like meeting a curious friend for coffee. We'll focus on your areas of expertise. Can you tell me more about your background? 

Expert 00:00:22 

Yes. I worked at Illumina for 12 years, and I was a chief software architect for their data analytics, data generated from the sequencers. We will ingest those data. I was part of the connected data analytics team. Before that, I was working at NextBio for three years, which was acquired by Illumina. My main expertise is the data analytics using DNA and RNA data, and developing algorithms based on the data generated for the DNA and RNA and those kind of data. Do you want more detail? If you have any specific question, I can address that. 

Client 00:01:04 

Can you expand on what you did while working at the company, and what that was like? 

Expert 00:01:10 

I have had two paths in the Illumina. One area was about maybe three to four years, I was managing a team of five people developing algorithms for DNA and for the customers. I think that was about maybe three, four years. For eight, nine years, I was an individual contributor in a big team. Basically, I was acting as a software architect on how to manage the software, how to manage data, and how to develop scalable data algorithms which we can run on any number of samples, and it will be scalable. 

Client 00:01:43 What do you think about these roles? Did you enjoy particular aspects of it more than others? What was challenging? What was easy? What was fun? 

Expert 00:01:57 

I think I truly enjoyed it because at every aspect of the development, we involved the clients and customers to give us feedback while we are developing these algorithms. We were not developing ad hoc algorithms because we wanted. We wanted to develop algorithms based on the data so that the clients and consumers can use them and deploy them in a production environment. It was not a, "Because I like this algorithm, I'll develop that." No. It was based on the requirements given by us by many different clients and whoever was going to use these algorithms. This was it. Sometimes it was challenging, because even at some time, the clients didn't know what they are looking for. That was the challenging part. 

Client 00:02:45 

Even the clients didn't know what they were looking for. Could you tell me more about that? 

Expert 00:02:51 

For example, they were interested in finding the rare variants and developing some algorithm, finding the patterns, but they did not have a clear idea how they are going to use them and how they are going to deploy them. For some well-known algorithms, they knew it, but for the ones which they were unsure, they did not know what to do. I think one aspect, which I believe it was missing, and with the innovation of the AI and the LLM it has to happen, is that we just not only develop them algorithms so that they can be deployed, but also open the API platform so that they can explore the data that they have, and they can ask maybe some intelligent questions based on their data. 

I think the era of developing the fixed set of algorithms is going to go away. For a fixed set of algorithms that they are well-known, then no problem, but the consumers, as I see these days, they should have access to their own data by using AI LLM. Also, that will require the validation and standardization, so those has to be also in place as well. 

Client 00:03:57 

That's very interesting. I'm wondering, is the company doing all it can to create solutions or functions, features that the customer will want without knowing that they want those things. 

Page 2 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

Expert 00:04:09 

I see. That's a good point. That's a very good point. Just one year before I left on August of 2025, I developed a POC, proof of concept, for using the AI LLM integration into a set of data. This was not for a particular customer. I gave a demo to managers and senior managers that, "Okay, you have this data sitting there, and what we can do with that?" One aspect is that, yes, there are well-known algorithms. We can develop them and deploy them, and they can click it and use it. That's fine. 

In my POC, I demoed that the data is beyond those existing algorithms. I was able to develop AI LLM agents, a very simple one. Basically, they will ask their questions in English, and then that will be translated to SQL, and then that SQL will be executed and validated. They will run it, and then they will see the result. Of course, the queries that we run on POC and also the customer, because we have a massive amount of data, we are talking about maybe six trillion data points, and the queries will run between five seconds to 20 seconds. It is not like a real-time system that you can get the answer in a second or two seconds. 

I think the enthusiasm of the management, I was not expecting that they will embrace this idea. Actually, they embraced the idea, and then before I left, I was able to push that component to the pre-alpha to the production. Basically, what this has to enable is that the customer, they know their data, they know what is in there, so they should be able to ask the intelligent questions and then get the results. Of course, this will take some time until they master it, and, first, there will be errors and all those things. Eventually, they will get it, and then the platform will be much more useful to the clients, and also, it will benefit Illumina. Am I making sense? 

#### Client 00:06:19 

That makes sense. Just thinking for a second about these comments. You built this proof-of-concept AI agent that took plain English questions, converted them to SQL, validated the code, queried the database. You ran queries against six trillion data points with results returning in five to 20 seconds. Illumina management embraced the project and pushed it to pre-alpha production before you left. Am I saying that right? 

Expert 00:06:49 

That's very correct, yes. 

Client 00:06:51 

Can you tell me a little bit more about the value proposition here? 

#### Expert 00:06:57 

The value proposition is that the researchers and the clients, they are not bound by just a set of well-defined algorithms that we give them. If they have new requirements, if they are looking for new things, we give them metadata, meaning everything represented as tables. The table has name and columns. Basically, we enable them to view their own data. Not the volume, I'm talking about the metadata. By looking at the metadata, they can ask very intelligent questions. 

For example, if they are looking for a rare variant of chromosome 17, a SNP of allele of A, or something, they are looking for a specific thing for a rare variant, they should be able to ask those questions without clicking the algorithm that I have developed them many years ago. They should be able to explore new horizons based on their data. I think that will be very valuable for the new research, for the new product creation, and for anything which belongs to them. I think with this, the customer, the client, will have a feeling that they are empowered, and they can do more. They will learn more about their own data and then ask intelligent questions. 

I always found that our clients and customers, they are very intelligent. They're asking the right questions. Sometimes if we are developing the algorithms, it is taking some time, and they don't have access to their own infrastructure. By enabling this POC of the AI LLM agent, they will have access to their own data and ask questions. Of course, it takes a learning process to ask the right questions, but eventually, they'll get it. 

#### Client 00:08:35 

I'm wondering what could be a game changer from here. Is it something to do with LLMs? We have China and their open source models, we have ChatGPT, we've got Claude. 

#### Expert 00:08:47 

The AI LLM that we use, it was a Snowflake platform. We used the AI LLM of the Snowflake. We did not use any other, such as OpenAI or Anthropic or anything like that. At that time, it was not even available for us to integrate, but we used the AI LLM of the Snowflake. I think this will be quite a game changer, first, it will enable the trust between the Illumina and their customers, that they have full access to their data, and they can ask any question about their data. 

Page 3 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

Second, the scientists in the customer area, the scientists and the researchers will be able to test new algorithms without going seven, eight weeks of telling us what they want. They can just do it on their own data by asking the questions, and we generate the SQL and run that for them. That will be amazing turnaround time for the research and the development. 

Client 00:09:44 

### It's bypassing engineering delays and empowering clients to query their own data correctly. 

Expert 00:09:51 Absolutely. One thing which we have to involve the clients and customers, to tell them that even though the SQL is generated and it is getting the right result, but validation is the key, the accuracy. AI LLM can generate SQL and runs and generates results, but is that the intended result? Those are the things that the clients and customers, with working with the Illumina, they have to find the platform for the validation and authentication of those data to make sure that it is what is intended. Of course, getting the data is not the whole thing, but getting the right data out of the database is the correct thing. Can I add one more thing? 

Client 00:10:33 Yes. 

Expert 00:10:34 

As you know and you're aware, that these AI LLM models are probabilistic models, they are not 100% deterministic. That's why the validation is crucial. 

Client 00:10:46 

Going from seven to eight-week development cycles, that drops to seconds, but it still requires validation. Maybe that adds some time on top. Am I saying that right? 

Expert 00:10:58 

Yes. If I was the customer of Illumina, I will demand this feature. 

Client 00:11:05 

Rather than using LLMs, where you have to potentially expose sensitive data to that LLM, instead, the more appropriate way of doing things is with Snowflake, they have a data lake, and then use their own embedded LLM. Am I saying that right? 

Expert 00:11:22 

You're right. Also, we expose only the data which belongs to them. Unless other data is shared, they are bound to their own data. Security is very important in this kind of data because you don't want to open the data from another customer to another customer. The security was very important, and we were able to implement the features so that the customer can only access their own data, but also, there was some part of the data which was a public data, and all of the customers can access that. 

Client 00:11:55 

Can you tell me more about the challenges of LLMs being non-deterministic and being more of a pattern-matching engine. Is that really understood properly when thinking about what it could mean for the future of Illumina? 

Expert 00:12:08 

Let me tell you one example. I might ask a question that give me some information about the patients. If the SQL uses a left join versus the inner join, the results will be completely different. I don't know if you are familiar with the join operations in SQL. 

Client 00:12:25 Can you tell me more about those? 

Page 4 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

#### Expert 00:12:28 

All of the data is represented in tables. I don't know what's your background in relational databases, but imagine you have many different spreadsheets. I'm just resembling it. When you are joining the tables, you are joining on common elements. If you don't join properly or use different kind of ID for the join, you will get some results, but it is not the intended result. The AI LLM can generate SQL which will generate the output, but is that the intention of the client which asked that question? That is not 100%. Basically, that is called validation of the generated SQL from AI LLM must be validated before you can trust the output. 

Client 00:13:15 

The AI agent, it's translating natural language queries sometimes incorrectly, and causing problems for you, the human. 

#### Expert 00:13:23 

I can give you hundreds of examples which will generate wrong. There are many reasons why it will generate wrong. One is that the asker, the client, is not asking proper question or not giving proper environment to the AI LLM, which if you give least amount of information to the AI LLM, it will hallucinate and give you wrong answer. If your prompt is proper, and if your metadata is proper, and all of those are done, the chances are over 90% you will get the correct result, but that 10% is a problem. You need to still validate. There are no AI LLM models which can give you 100% correct answers. None. 

Client 00:14:04 For you personally, when thinking about this, any big epiphanies or revelations when thinking about the value of LLM in general, even beyond Illumina? 

#### Expert 00:14:13 

Even with my demo, even with my POC, I showed five AI LLM questions which got it right and five AI LLM question which got it wrong. All those 10 generated output, and if you don't know SQL, you might think, "Oh, I got the result. It's beautiful," but some of those, five of them were wrong. I think the education to the client and customers are the key. They need to understand that when we are deploying AI LLM to the clients, AI LLM can hallucinate, and sometimes it can give you wrong answer. The more you know about the SQL, the more you know about your metadata, you can catch those errors. 

Client 00:14:53 

I'm just thinking about your background, chief architect at Illumina. What's the next step for this technology? What's on the roadmap in terms of what would be a game changer? 

#### Expert 00:15:05 

One of the problems which I saw at Illumina, when the data is generated from the sequencers, the data goes to ingestion. For example, if it's a DNA sample, it has five million rows, and then when you are ingesting it, you are generating 30 million records from five million rows of data. Five million rows of DNA data becomes 30 million records which can be interpreted and queried. One of the major problems Illumina needs to fix is that they need to generate these data right on the source so that we don't need to ingest data later on. Do you understand what I'm saying? 

Client 00:15:42 

Can you expand on that? 

#### Expert 00:15:44 

Let's say that a sequencer knows what any of the machines that's generating, that are spitting the DNA data. For one DNA sample, it will generate five million records. That data comes to the data analytics team. We get that data for one sample, and then we run ingestion algorithms to expand every row to maybe five, six rows. That becomes maybe about 30 million rows that is suitable for the data analytics and querying. 

What I'm saying is that we should bypass this. The sequencer should add some modules to the sequencer to generate all these 30 million records so that the analytics team do not have to do all these ingestions. That will be a time saver because each of these ingestion can take between 15-20 minutes of time in a cluster environment. That will be a big optimization. 

Page 5 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

Client 00:16:38 

I'm just thinking for a second. What do you think about pricing and where we're headed? Do you think their technology, their solutions become less expensive over time? Some of them can be very expensive, including some test work that's done. 

Expert 00:16:55 

I think the sequencers are becoming cheaper, I mean the data generation. Also, we see some competition from different companies such as Roche or other companies. They are generating the short reads, long reads, and all those things. My opinion is that in a long run, the value of DNA data will be in the data analytics, not in the generation of that. What is the meaning of the data and the algorithms and the queries that you run on these data? It is premature maybe, but I think in the long run, between five to 10 years, Illumina should think about how to generate revenue from the data analytics components rather than the sequencers because the value will be there. 

For example, if you can analyze the data from a mother who is pregnant and find out more about the baby, that will be amazingly powerful that if there is a disease or problem, they can fix it at the root rather than later. I think the data analytics will answer all of those beautifully. In long run, as I see, the sequencers and data generation will be commodities. Anybody can generate that. An analysis and providing a platform, providing LLM, providing AI for the data queries and finding out that if this DNA has autism genes and those things, that will be more valuable. 

#### Client 00:18:18 

What about the value of the software and integration and ease of use? To what extent does the company have a competitive advantage? 

Expert 00:18:28 

Absolutely. Those are the foundations. Suppose you generated all of the data in the world, and you don't have environment to analyze and view your data, then the data is useless. For example, if you look at the Amazon, Amazon provides the data integrations for any services. Illumina has to be the Amazon for the DNA data, so that the clients and customers can come and find out the services, and pick and select the services they want for their data, and then they should be paying accordingly based on the usage. 

They have to find some formula, that how they are using the data. It can be by megabyte, terabyte, or those things. In a long run, in order for Illumina to be successful, they need to think about that, how can I be the Amazon for the DNA? 

Client 00:19:17 

How can they be the Amazon for the DNA? 

#### Expert 00:19:22 

I think they can be by, first, putting the data to the repository should be as easy as Amazon services. It should be basically painless. To put the data, view the data, analyze data, all of these should be transparent to the customers. That will take developing an integrated environment, reliably integrated environment, so that the customers can trust and put their data, and also maybe bring other data which the Illumina doesn't have. 

They should be enablers and bring all the things that they have and put it there, and then analyze and enable the AI LLM for them to basically examine their own data and see what they can do with that data. If we just provide applications and well-defined algorithms that they can come and click and use it, eventually, there are going to be things that they want to do on their own rather than relying on the Illumina. I think that giving the full access to their own data is the first fundamental rule in keeping the customers. 

#### Client 00:20:22 

Given your software background and chief architect, is there something really unique or special about the software that maybe only you would appreciate because of the experience you've had with this company? Is there something not talked about as much as it should? 

Expert 00:20:37 

Are you talking about algorithms or data? Which? 

Client 00:20:41 

I'm thinking about the data or the software or the algorithms, the integrations, things that customer prefers, maybe not appreciate. 

Page 6 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

Expert 00:20:51 I understand. There are some algorithms of that. For example, if I want to find the relationship of the hundreds of thousands of DNA samples, find the mother, father, child, there is parent-sibling relationship, those are very well-defined algorithms, and those cannot be done by just an AI LLM agent in a very simple manner. Those need to be developed and deployed, so that it can be used by many clients. 

There are some also ad hoc queries that the client can think about them and use them, and they should be also available. In most of the situations, if there is no AI LLM integration, how they can access those data? For some well-defined algorithms, of course, that will take long time and long-term development cycle and testing, but there are also many things that the client should be able to ask and explore without being complex. They can ask simple question. 

For example, they can ask, "How many of my patients are between age 10 and 20, and they are Hispanic?" Those kind of things and those kind of questions, and which ones have the chromosome one with allele of a specific alleles and those kind of things, some of those questions can be answered quickly by the customer requirements. Even in speech, they don't need even to type. They can ask it by using the speech recognition software and ask those questions and get answers immediately. They don't need to come to Illumina or any other company to develop those algorithms. 

Client 00:22:21 

Great getting your thoughts on all of this. I was just thinking for a second about some of your comments. 

#### Expert 00:22:30 

Sure. I remember one set of samples that we got from Stanford University. This was the autism data. It was 5,000 samples. This was small data, to my opinion, 5,000 x 30 million, that will be 15 billion data points. If you open that data with AI LLM to the researchers, they can do wonders. They can ask tremendous amount of questions, and they would love that by AI LLM, rather than giving them fixed set of algorithms. 

Client 00:23:00 

Very interesting, that makes me curious because I have autism. I discovered it very late in life, in my early 50s. I'm always curious about could that be changed or improved upon with some type of therapy, but without losing the advantages at the same time. 

#### Expert 00:23:19 

Sure. I think so. My opinion, I have started working on AI LLM for the past four years right now. My background is I have a PhD in computer science, and I understand those very well, how those LLM models are built. I believe that opening those kind of data for the researchers, that will open a new avenue for finding the, it can be cure, or it can be medicine, or it can be anything. That will open a new avenue for finding things that it was impossible by the just well-developed algorithms that we develop. 

First of all, the computer scientist doesn't know the domain very well. I'm a computer scientist. I know the DNA, RNA, and all those, the data, but the domain knowledge is with the researchers and scientists. Once they have the access to this data, they can eventually get it and ask proper questions about this data. 

Client 00:24:15 

Any final last words? Anything to add or highlight? 

#### Expert 00:24:20 

We touched on the AI LLM a little bit. I would like to leave with you the impression is that validation of the AI-generated code or SQL is the key in using the AI LLM in anywhere. If it is not validated, we can hallucinate and get the wrong answers. 

Client 00:24:39 

Got it. Those are all the questions that I had. Thanks so much for your time. Have a great day. 

Page 7 of 7 

©2026, AlphaSense, Inc. All Rights Reserved. AlphaSense is a service mark of AlphaSense, Inc. All other trademarks mentioned belong to their respective owners. 

