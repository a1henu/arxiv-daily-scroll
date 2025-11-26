---
layout: default
title: Adaptive Hopfield Network: Rethinking Similarities in Associative Memory
---

# Adaptive Hopfield Network: Rethinking Similarities in Associative Memory
**arXiv**：[2511.20609v1](https://arxiv.org/abs/2511.20609) · [PDF](https://arxiv.org/pdf/2511.20609.pdf)  
**作者**：Shurong Wang, Yuqi Pan, Zhuoyang Shen, Meng Zhang, Hongwei Wang, Guoqi Li  

**一句话要点**：提出自适应相似性机制以解决关联记忆中检索正确性问题

**关键词**：关联记忆, 自适应相似性, Hopfield网络, 后验概率, 变体分布, 多任务学习

## 3 点简述
- 现有模型基于邻近性评估检索质量，无法保证最强关联，导致检索错误
- 引入自适应相似性，学习近似查询生成似然，实现正确检索
- 理论证明在噪声、掩码和偏差变体下最优，实验显示多任务SOTA性能

## 摘要（原文）

> Associative memory models are content-addressable memory systems fundamental to biological intelligence and are notable for their high interpretability. However, existing models evaluate the quality of retrieval based on proximity, which cannot guarantee that the retrieved pattern has the strongest association with the query, failing correctness. We reframe this problem by proposing that a query is a generative variant of a stored memory pattern, and define a variant distribution to model this subtle context-dependent generative process. Consequently, correct retrieval should return the memory pattern with the maximum a posteriori probability of being the query's origin. This perspective reveals that an ideal similarity measure should approximate the likelihood of each stored pattern generating the query in accordance with variant distribution, which is impossible for fixed and pre-defined similarities used by existing associative memories. To this end, we develop adaptive similarity, a novel mechanism that learns to approximate this insightful but unknown likelihood from samples drawn from context, aiming for correct retrieval. We theoretically prove that our proposed adaptive similarity achieves optimal correct retrieval under three canonical and widely applicable types of variants: noisy, masked, and biased. We integrate this mechanism into a novel adaptive Hopfield network (A-Hop), and empirical results show that it achieves state-of-the-art performance across diverse tasks, including memory retrieval, tabular classification, image classification, and multiple instance learning.

