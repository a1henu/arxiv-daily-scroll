---
layout: default
title: Entropy-Guided Data-Efficient Training for Multimodal Reasoning Reward Models
---

# Entropy-Guided Data-Efficient Training for Multimodal Reasoning Reward Models
**arXiv**：[2602.01884v1](https://arxiv.org/abs/2602.01884) · [PDF](https://arxiv.org/pdf/2602.01884.pdf)  
**作者**：Shidong Yang, Tongwen Huang, Hao Wen, Yong Wang, Li Chen, Xiangxiang Chu  

**一句话要点**：提出熵引导训练方法以提升多模态推理奖励模型的数据效率和性能

**关键词**：多模态推理, 奖励模型, 熵引导训练, 数据效率, 样本难度, 噪声缓解

## 3 点简述
- 核心问题：多模态奖励模型训练受数据集噪声和样本难度差异影响，导致性能下降和效率低下。
- 方法要点：基于响应熵与准确性的强相关性，设计熵引导数据筛选和渐进训练策略，减少噪声并优化学习过程。
- 实验或效果：在三个基准测试中，该方法训练的模型持续优于现有最佳多模态奖励模型。

## 摘要（原文）

> Multimodal reward models are crucial for aligning multimodal large language models with human preferences. Recent works have incorporated reasoning capabilities into these models, achieving promising results. However, training these models suffers from two critical challenges: (1) the inherent noise in preference datasets, which degrades model performance, and (2) the inefficiency of conventional training methods, which ignore the differences in sample difficulty. In this paper, we identify a strong correlation between response entropy and accuracy, indicating that entropy can serve as a reliable and unsupervised proxy for annotation noise and sample difficulty. Based on this insight, we propose a novel Entropy-Guided Training (EGT) approach for multimodal reasoning reward models, which combines two strategies: (1) entropy-guided data curation to mitigate the impact of unreliable samples, and (2) an entropy-guided training strategy that progressively introduces more complex examples. Extensive experiments across three benchmarks show that the EGT-trained model consistently outperforms state-of-the-art multimodal reward models.

