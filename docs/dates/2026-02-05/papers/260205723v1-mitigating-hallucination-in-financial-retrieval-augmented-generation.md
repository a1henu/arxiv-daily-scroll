---
layout: default
title: Mitigating Hallucination in Financial Retrieval-Augmented Generation via Fine-Grained Knowledge Verification
---

# Mitigating Hallucination in Financial Retrieval-Augmented Generation via Fine-Grained Knowledge Verification
**arXiv**：[2602.05723v1](https://arxiv.org/abs/2602.05723) · [PDF](https://arxiv.org/pdf/2602.05723.pdf)  
**作者**：Taoye Yin, Haoyuan Hu, Yaxin Fan, Xinhao Chen, Xinya Wu, Kai Deng, Kezun Zhang, Feng Wang  

**一句话要点**：提出RLFKV框架，通过细粒度知识验证缓解金融RAG系统中的幻觉问题。

**关键词**：检索增强生成, 幻觉缓解, 强化学习, 细粒度验证, 金融领域

## 3 点简述
- 金融RAG系统因时间敏感性依赖检索文档，但生成响应仍存在与检索信息矛盾的幻觉。
- 方法将响应分解为原子知识单元，计算细粒度忠实度奖励，并加入信息量奖励防止奖励黑客。
- 在FDD任务和新数据集FDD-ANT上实验，显示方法能一致提升性能，验证有效性。

## 摘要（原文）

> In financial Retrieval-Augmented Generation (RAG) systems, models frequently rely on retrieved documents to generate accurate responses due to the time-sensitive nature of the financial domain. While retrieved documents help address knowledge gaps, model-generated responses still suffer from hallucinations that contradict the retrieved information. To mitigate this inconsistency, we propose a Reinforcement Learning framework enhanced with Fine-grained Knowledge Verification (RLFKV). Our method decomposes financial responses into atomic knowledge units and assesses the correctness of each unit to compute the fine-grained faithful reward. This reward offers more precise optimization signals, thereby improving alignment with the retrieved documents. Additionally, to prevent reward hacking (e.g., overly concise replies), we incorporate an informativeness reward that encourages the policy model to retain at least as many knowledge units as the base model. Experiments conducted on the public Financial Data Description (FDD) task and our newly proposed FDD-ANT dataset demonstrate consistent improvements, confirming the effectiveness of our approach.

