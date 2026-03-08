---
layout: default
title: FedAFD: Multimodal Federated Learning via Adversarial Fusion and Distillation
---

# FedAFD: Multimodal Federated Learning via Adversarial Fusion and Distillation
**arXiv**：[2603.04890v1](https://arxiv.org/abs/2603.04890) · [PDF](https://arxiv.org/pdf/2603.04890.pdf)  
**作者**：Min Tan, Junchao Ma, Yinfu Feng, Jiajun Ding, Wenwen Pan, Tingting Han, Qian Zheng, Zhenzhong Kuang, Zhou Yu  

**一句话要点**：提出FedAFD框架，通过对抗融合与蒸馏解决多模态联邦学习中的个性化与异构性问题。

**关键词**：多模态联邦学习, 对抗对齐, 知识蒸馏, 个性化学习, 模型异构性, 隐私保护

## 3 点简述
- 核心问题：多模态联邦学习中存在模态/任务差异、模型异构性，影响个性化性能。
- 方法要点：客户端采用双层对抗对齐和粒度感知融合，服务器端基于相似性引导的集成蒸馏。
- 实验或效果：在IID和非IID设置下，FedAFD在客户端和服务器端均实现优越性能与效率。

## 摘要（原文）

> Multimodal Federated Learning (MFL) enables clients with heterogeneous data modalities to collaboratively train models without sharing raw data, offering a privacy-preserving framework that leverages complementary cross-modal information. However, existing methods often overlook personalized client performance and struggle with modality/task discrepancies, as well as model heterogeneity. To address these challenges, we propose FedAFD, a unified MFL framework that enhances client and server learning. On the client side, we introduce a bi-level adversarial alignment strategy to align local and global representations within and across modalities, mitigating modality and task gaps. We further design a granularity-aware fusion module to integrate global knowledge into the personalized features adaptively. On the server side, to handle model heterogeneity, we propose a similarity-guided ensemble distillation mechanism that aggregates client representations on shared public data based on feature similarity and distills the fused knowledge into the global model. Extensive experiments conducted under both IID and non-IID settings demonstrate that FedAFD achieves superior performance and efficiency for both the client and the server.

