---
layout: default
title: Knowledge-Aware Evolution for Streaming Federated Continual Learning with Category Overlap and without Task Identifiers
---

# Knowledge-Aware Evolution for Streaming Federated Continual Learning with Category Overlap and without Task Identifiers
**arXiv**：[2601.19788v1](https://arxiv.org/abs/2601.19788) · [PDF](https://arxiv.org/pdf/2601.19788.pdf)  
**作者**：Sixing Tan, Xianmin Liu  

**一句话要点**：提出FedKACE以解决流式联邦持续学习中类别重叠和无任务标识符的问题

**关键词**：流式联邦持续学习, 类别重叠, 无任务标识符, 自适应推理, 梯度平衡重放, 核谱边界缓冲区

## 3 点简述
- 核心问题：流式场景下类别重叠和无任务标识符导致新旧知识混淆与任务分配不确定
- 方法要点：自适应推理模型切换、梯度平衡重放和核谱边界缓冲区维护
- 实验或效果：多场景实验和遗憾分析验证了FedKACE的有效性

## 摘要（原文）

> Federated Continual Learning (FCL) leverages inter-client collaboration to balance new knowledge acquisition and prior knowledge retention in non-stationary data. However, existing batch-based FCL methods lack adaptability to streaming scenarios featuring category overlap between old and new data and absent task identifiers, leading to indistinguishability of old and new knowledge, uncertain task assignments for samples, and knowledge confusion.To address this, we propose streaming federated continual learning setting: per federated learning (FL) round, clients process streaming data with disjoint samples and potentially overlapping categories without task identifiers, necessitating sustained inference capability for all prior categories after each FL round.Next, we introduce FedKACE: 1) an adaptive inference model switching mechanism that enables unidirectional switching from local model to global model to achieve a trade-off between personalization and generalization; 2) a adaptive gradient-balanced replay scheme that reconciles new knowledge learning and old knowledge retention under overlapping-class scenarios; 3) a kernel spectral boundary buffer maintenance that preserves high-information and high-boundary-influence samples to optimize cross-round knowledge retention. Experiments across multiple scenarios and regret analysis demonstrate the effectiveness of FedKACE.

