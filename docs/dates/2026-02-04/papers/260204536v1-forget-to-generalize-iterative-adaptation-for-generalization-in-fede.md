---
layout: default
title: Forget to Generalize: Iterative Adaptation for Generalization in Federated Learning
---

# Forget to Generalize: Iterative Adaptation for Generalization in Federated Learning
**arXiv**：[2602.04536v1](https://arxiv.org/abs/2602.04536) · [PDF](https://arxiv.org/pdf/2602.04536.pdf)  
**作者**：Abdulrahman Alotaibi, Irene Tenison, Miriam Kim, Isaac Lee, Lalana Kagal  

**一句话要点**：提出迭代联邦适应以解决非独立同分布联邦学习中的泛化问题

**关键词**：联邦学习, 非独立同分布, 泛化增强, 迭代适应, 参数重置

## 3 点简述
- 核心问题：联邦学习在非独立同分布客户端数据下性能严重下降
- 方法要点：通过分代训练，随机或选择性地重置部分模型参数以逃离局部最优
- 实验或效果：在多个数据集上平均提升21.5%的全局准确率

## 摘要（原文）

> The Web is naturally heterogeneous with user devices, geographic regions, browsing patterns, and contexts all leading to highly diverse, unique datasets. Federated Learning (FL) is an important paradigm for the Web because it enables privacy-preserving, collaborative machine learning across diverse user devices, web services and clients without needing to centralize sensitive data. However, its performance degrades severely under non-IID client distributions that is prevalent in real-world web systems. In this work, we propose a new training paradigm - Iterative Federated Adaptation (IFA) - that enhances generalization in heterogeneous federated settings through generation-wise forget and evolve strategy. Specifically, we divide training into multiple generations and, at the end of each, select a fraction of model parameters (a) randomly or (b) from the later layers of the model and reinitialize them. This iterative forget and evolve schedule allows the model to escape local minima and preserve globally relevant representations. Extensive experiments on CIFAR-10, MIT-Indoors, and Stanford Dogs datasets show that the proposed approach improves global accuracy, especially when the data cross clients are Non-IID. This method can be implemented on top any federated algorithm to improve its generalization performance. We observe an average of 21.5%improvement across datasets. This work advances the vision of scalable, privacy-preserving intelligence for real-world heterogeneous and distributed web systems.

