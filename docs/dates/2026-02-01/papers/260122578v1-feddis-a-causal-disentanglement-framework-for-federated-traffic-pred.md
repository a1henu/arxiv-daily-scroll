---
layout: default
title: FedDis: A Causal Disentanglement Framework for Federated Traffic Prediction
---

# FedDis: A Causal Disentanglement Framework for Federated Traffic Prediction
**arXiv**：[2601.22578v1](https://arxiv.org/abs/2601.22578) · [PDF](https://arxiv.org/pdf/2601.22578.pdf)  
**作者**：Chengyang Zhou, Zijian Zhang, Chunxu Zhang, Hao Miao, Yulin Zhang, Kedi Lyu, Juncheng Hu  

**一句话要点**：提出FedDis框架，通过因果解耦解决联邦交通预测中的数据异构问题

**关键词**：联邦学习, 交通预测, 因果解耦, 数据异构, 时空模式, 互信息最小化

## 3 点简述
- 核心问题：联邦学习中非独立同分布交通数据导致性能下降，现有方法难以分离全局与局部模式
- 方法要点：采用双分支设计，个性化银行捕获客户端特定因素，全局模式银行提取共同知识，通过互信息最小化实现解耦
- 实验或效果：在四个真实数据集上验证，FedDis实现最优性能，并具备高效性和可扩展性

## 摘要（原文）

> Federated learning offers a promising paradigm for privacy-preserving traffic prediction, yet its performance is often challenged by the non-identically and independently distributed (non-IID) nature of decentralized traffic data. Existing federated methods frequently struggle with this data heterogeneity, typically entangling globally shared patterns with client-specific local dynamics within a single representation. In this work, we postulate that this heterogeneity stems from the entanglement of two distinct generative sources: client-specific localized dynamics and cross-client global spatial-temporal patterns. Motivated by this perspective, we introduce FedDis, a novel framework that, to the best of our knowledge, is the first to leverage causal disentanglement for federated spatial-temporal prediction. Architecturally, FedDis comprises a dual-branch design wherein a Personalized Bank learns to capture client-specific factors, while a Global Pattern Bank distills common knowledge. This separation enables robust cross-client knowledge transfer while preserving high adaptability to unique local environments. Crucially, a mutual information minimization objective is employed to enforce informational orthogonality between the two branches, thereby ensuring effective disentanglement. Comprehensive experiments conducted on four real-world benchmark datasets demonstrate that FedDis consistently achieves state-of-the-art performance, promising efficiency, and superior expandability.

