---
layout: default
title: Decoding Fake Narratives in Spreading Hateful Stories: A Dual-Head RoBERTa Model with Multi-Task Learning
---

# Decoding Fake Narratives in Spreading Hateful Stories: A Dual-Head RoBERTa Model with Multi-Task Learning
**arXiv**：[2512.16147v1](https://arxiv.org/abs/2512.16147) · [PDF](https://arxiv.org/pdf/2512.16147.pdf)  
**作者**：Yash Bhaskar, Sankalp Bahad, Parameswari Krishnamurthy  

**一句话要点**：提出双头RoBERTa模型与多任务学习，以检测印英混合社交媒体中的虚假仇恨叙事。

**关键词**：虚假仇恨检测, 多任务学习, RoBERTa模型, 印英混合文本, 社交媒体分析

## 3 点简述
- 核心问题：社交媒体中虚假叙事驱动的仇恨言论检测，针对印英混合文本。
- 方法要点：采用双头RoBERTa模型，结合多任务学习处理二元分类与目标严重性预测。
- 实验或效果：在Faux-Hate共享任务中取得竞争性结果，验证了方法的有效性。

## 摘要（原文）

> Social media platforms, while enabling global connectivity, have become hubs for the rapid spread of harmful content, including hate speech and fake narratives \cite{davidson2017automated, shu2017fake}. The Faux-Hate shared task focuses on detecting a specific phenomenon: the generation of hate speech driven by fake narratives, termed Faux-Hate. Participants are challenged to identify such instances in code-mixed Hindi-English social media text. This paper describes our system developed for the shared task, addressing two primary sub-tasks: (a) Binary Faux-Hate detection, involving fake and hate speech classification, and (b) Target and Severity prediction, categorizing the intended target and severity of hateful content. Our approach combines advanced natural language processing techniques with domain-specific pretraining to enhance performance across both tasks. The system achieved competitive results, demonstrating the efficacy of leveraging multi-task learning for this complex problem.

