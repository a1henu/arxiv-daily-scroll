---
layout: default
title: Using Large Language Models to Create Personalized Networks From Therapy Sessions
---

# Using Large Language Models to Create Personalized Networks From Therapy Sessions
**arXiv**：[2512.05836v1](https://arxiv.org/abs/2512.05836) · [PDF](https://arxiv.org/pdf/2512.05836.pdf)  
**作者**：Clarissa W. Ong, Hiba Arnaout, Kate Sheehan, Estella Fox, Eugen Owtscharow, Iryna Gurevych  

**一句话要点**：提出基于大语言模型的个性化网络生成方法，用于心理治疗会话分析以支持案例概念化。

**关键词**：大语言模型应用, 心理治疗个性化, 网络生成, 上下文学习, 案例概念化

## 3 点简述
- 核心问题：个性化网络估计通常需要密集纵向数据，限制了治疗个性化的可扩展性。
- 方法要点：利用上下文学习从治疗转录本中自动识别心理过程，并通过两步法构建临床意义网络。
- 实验或效果：专家评估显示，该方法在临床效用和可解释性上优于直接提示，偏好率高达90%。

## 摘要（原文）

> Recent advances in psychotherapy have focused on treatment personalization, such as by selecting treatment modules based on personalized networks. However, estimating personalized networks typically requires intensive longitudinal data, which is not always feasible. A solution to facilitate scalability of network-driven treatment personalization is leveraging LLMs. In this study, we present an end-to-end pipeline for automatically generating client networks from 77 therapy transcripts to support case conceptualization and treatment planning. We annotated 3364 psychological processes and their corresponding dimensions in therapy transcripts. Using these data, we applied in-context learning to jointly identify psychological processes and their dimensions. The method achieved high performance even with a few training examples. To organize the processes into networks, we introduced a two-step method that grouped them into clinically meaningful clusters. We then generated explanation-augmented relationships between clusters. Experts found that networks produced by our multi-step approach outperformed those built with direct prompting for clinical utility and interpretability, with up to 90% preferring our approach. In addition, the networks were rated favorably by experts, with scores for clinical relevance, novelty, and usefulness ranging from 72-75%. Our findings provide a proof of concept for using LLMs to create clinically relevant networks from therapy transcripts. Advantages of our approach include bottom-up case conceptualization from client utterances in therapy sessions and identification of latent themes. Networks generated from our pipeline may be used in clinical settings and supervision and training. Future research should examine whether these networks improve treatment outcomes relative to other methods of treatment personalization, including statistically estimated networks.

