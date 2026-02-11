---
layout: default
title: Predictive Query Language: A Domain-Specific Language for Predictive Modeling on Relational Databases
---

# Predictive Query Language: A Domain-Specific Language for Predictive Modeling on Relational Databases
**arXiv**：[2602.09572v1](https://arxiv.org/abs/2602.09572) · [PDF](https://arxiv.org/pdf/2602.09572.pdf)  
**作者**：Vid Kocijan, Jinu Sunil, Jan Eric Lenssen, Viman Deb, Xinwei Xe, Federco Reyes Gomez, Matthias Fey, Jure Leskovec  

**一句话要点**：提出预测查询语言以简化关系数据库上的预测建模任务定义

**关键词**：预测建模, 关系数据库, 声明式语言, 机器学习任务, 自动标签生成, 预测AI平台

## 3 点简述
- 核心问题：关系数据预测建模需手动提取训练样本，过程缓慢易错
- 方法要点：PQL为声明式语言，单查询定义任务，自动计算训练标签
- 实验或效果：已集成于预测AI平台，应用于欺诈检测、推荐等用例

## 摘要（原文）

> The purpose of predictive modeling on relational data is to predict future or missing values in a relational database, for example, future purchases of a user, risk of readmission of the patient, or the likelihood that a financial transaction is fraudulent. Typically powered by machine learning methods, predictive models are used in recommendations, financial fraud detection, supply chain optimization, and other systems, providing billions of predictions every day. However, training a machine learning model requires manual work to extract the required training examples - prediction entities and target labels - from the database, which is slow, laborious, and prone to mistakes. Here, we present the Predictive Query Language (PQL), a SQL-inspired declarative language for defining predictive tasks on relational databases. PQL allows specifying a predictive task in a single declarative query, enabling the automatic computation training labels for a large variety of machine learning tasks, such as regression, classification, time-series forecasting, and recommender systems. PQL is already successfully integrated and used in a collection of use cases as part of a predictive AI platform. The versatility of the language can be demonstrated through its many ongoing use cases, including financial fraud, item recommendations, and workload prediction. We demonstrate its versatile design through two implementations; one for small-scale, low-latency use and one that can handle large-scale databases.

