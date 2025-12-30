---
layout: default
title: Scoring, Reasoning, and Selecting the Best! Ensembling Large Language Models via a Peer-Review Process
---

# Scoring, Reasoning, and Selecting the Best! Ensembling Large Language Models via a Peer-Review Process
**arXiv**：[2512.23213v1](https://arxiv.org/abs/2512.23213) · [PDF](https://arxiv.org/pdf/2512.23213.pdf)  
**作者**：Zhijun Chen, Zeyu Ji, Qianren Mao, Junhang Cheng, Bangjie Qin, Hao Wu, Zhuoran Li, Jingzheng Li, Kai Sun, Zizhe Wang, Yikun Ban, Zhu Sun, Xiangyang Ji, Hailong Sun  

**一句话要点**：提出LLM-PeerReview，一种无监督大语言模型集成方法，通过同行评审机制选择最佳响应。

**关键词**：大语言模型集成, 无监督学习, 同行评审机制, LLM-as-a-Judge, 图形模型推理, 响应选择

## 3 点简述
- 核心问题：如何从多个大语言模型生成的候选响应中无监督地选择最理想答案。
- 方法要点：采用三阶段框架，包括评分、推理和选择，利用LLM-as-a-Judge技术和图形模型或平均策略。
- 实验或效果：在两个变体上，在四个数据集上表现强劲，分别超越Smoothie-Global模型6.9%和7.3%。

## 摘要（原文）

> We propose LLM-PeerReview, an unsupervised LLM Ensemble method that selects the most ideal response from multiple LLM-generated candidates for each query, harnessing the collective wisdom of multiple models with diverse strengths. LLM-PeerReview is built on a novel, peer-review-inspired framework that offers a clear and interpretable mechanism, while remaining fully unsupervised for flexible adaptability and generalization. Specifically, it operates in three stages: For scoring, we use the emerging LLM-as-a-Judge technique to evaluate each response by reusing multiple LLMs at hand; For reasoning, we can apply a principled graphical model-based truth inference algorithm or a straightforward averaging strategy to aggregate multiple scores to produce a final score for each response; Finally, the highest-scoring response is selected as the best ensemble output. LLM-PeerReview is conceptually simple and empirically powerful. The two variants of the proposed approach obtain strong results across four datasets, including outperforming the recent advanced model Smoothie-Global by 6.9% and 7.3% points, respectively.

