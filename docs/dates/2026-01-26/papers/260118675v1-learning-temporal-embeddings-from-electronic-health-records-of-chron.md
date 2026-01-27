---
layout: default
title: Learning temporal embeddings from electronic health records of chronic kidney disease patients
---

# Learning temporal embeddings from electronic health records of chronic kidney disease patients
**arXiv**：[2601.18675v1](https://arxiv.org/abs/2601.18675) · [PDF](https://arxiv.org/pdf/2601.18675.pdf)  
**作者**：Aditya Kumar, Mario A. Cypko, Oliver Amft  

**一句话要点**：提出时间感知LSTM从电子健康记录学习慢性肾病患者的时序嵌入，提升临床表示质量与预测性能。

**关键词**：时序嵌入学习, 电子健康记录, 慢性肾病, 循环神经网络, 临床预测模型, 表示学习

## 3 点简述
- 研究核心问题：时序嵌入模型能否从纵向电子健康记录中学习临床有意义的表示，而不损害预测性能。
- 方法要点：比较三种循环架构（普通LSTM、注意力增强LSTM、时间感知LSTM），训练为嵌入模型和端到端预测器。
- 实验效果：时间感知LSTM产生更结构化的嵌入，在CKD阶段聚类和ICU死亡率预测中表现最佳，嵌入模型优于端到端预测器。

## 摘要（原文）

> We investigate whether temporal embedding models trained on longitudinal electronic health records can learn clinically meaningful representations without compromising predictive performance, and how architectural choices affect embedding quality. Model-guided medicine requires representations that capture disease dynamics while remaining transparent and task agnostic, whereas most clinical prediction models are optimised for a single task. Representation learning facilitates learning embeddings that generalise across downstream tasks, and recurrent architectures are well-suited for modelling temporal structure in observational clinical data. Using the MIMIC-IV dataset, we study patients with chronic kidney disease (CKD) and compare three recurrent architectures: a vanilla LSTM, an attention-augmented LSTM, and a time-aware LSTM (T-LSTM). All models are trained both as embedding models and as direct end-to-end predictors. Embedding quality is evaluated via CKD stage clustering and in-ICU mortality prediction. The T-LSTM produces more structured embeddings, achieving a lower Davies-Bouldin Index (DBI = 9.91) and higher CKD stage classification accuracy (0.74) than the vanilla LSTM (DBI = 15.85, accuracy = 0.63) and attention-augmented LSTM (DBI = 20.72, accuracy = 0.67). For in-ICU mortality prediction, embedding models consistently outperform end-to-end predictors, improving accuracy from 0.72-0.75 to 0.82-0.83, which indicates that learning embeddings as an intermediate step is more effective than direct end-to-end learning.

