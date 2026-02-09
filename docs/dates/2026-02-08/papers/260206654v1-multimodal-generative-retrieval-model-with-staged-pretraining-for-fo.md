---
layout: default
title: Multimodal Generative Retrieval Model with Staged Pretraining for Food Delivery on Meituan
---

# Multimodal Generative Retrieval Model with Staged Pretraining for Food Delivery on Meituan
**arXiv**：[2602.06654v1](https://arxiv.org/abs/2602.06654) · [PDF](https://arxiv.org/pdf/2602.06654.pdf)  
**作者**：Boyu Chen, Tai Guo, Weiyu Cui, Yuqing Li, Xingxing Wang, Chuan Shi, Cheng Yang  

**一句话要点**：提出分阶段预训练策略以解决多模态检索中的模态主导与训练不一致问题，应用于美团外卖场景。

**关键词**：多模态检索, 分阶段预训练, 语义ID, 生成任务, 判别任务, 外卖推荐

## 3 点简述
- 核心问题：联合优化导致模态主导和训练速度不一致，引发一周期问题。
- 方法要点：采用分阶段预训练，每阶段专注特定任务，并设计生成与判别任务利用语义ID。
- 实验或效果：在美团数据上提升召回率和归一化折扣累积增益，线上A/B测试增加收入和点击率。

## 摘要（原文）

> Multimodal retrieval models are becoming increasingly important in scenarios such as food delivery, where rich multimodal features can meet diverse user needs and enable precise retrieval. Mainstream approaches typically employ a dual-tower architecture between queries and items, and perform joint optimization of intra-tower and inter-tower tasks. However, we observe that joint optimization often leads to certain modalities dominating the training process, while other modalities are neglected. In addition, inconsistent training speeds across modalities can easily result in the one-epoch problem. To address these challenges, we propose a staged pretraining strategy, which guides the model to focus on specialized tasks at each stage, enabling it to effectively attend to and utilize multimodal features, and allowing flexible control over the training process at each stage to avoid the one-epoch problem. Furthermore, to better utilize the semantic IDs that compress high-dimensional multimodal embeddings, we design both generative and discriminative tasks to help the model understand the associations between SIDs, queries, and item features, thereby improving overall performance. Extensive experiments on large-scale real-world Meituan data demonstrate that our method achieves improvements of 3.80%, 2.64%, and 2.17% on R@5, R@10, and R@20, and 5.10%, 4.22%, and 2.09% on N@5, N@10, and N@20 compared to mainstream baselines. Online A/B testing on the Meituan platform shows that our approach achieves a 1.12% increase in revenue and a 1.02% increase in click-through rate, validating the effectiveness and superiority of our method in practical applications.

