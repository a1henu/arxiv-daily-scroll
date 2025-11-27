---
layout: default
title: RIA: A Ranking-Infused Approach for Optimized listwise CTR Prediction
---

# RIA: A Ranking-Infused Approach for Optimized listwise CTR Prediction
**arXiv**：[2511.21394v1](https://arxiv.org/abs/2511.21394) · [PDF](https://arxiv.org/pdf/2511.21394.pdf)  
**作者**：Guoxiao Zhang, Tan Qu, Ao Li, DongLin Ni, Qianlong Xie, Xingxing Wang  

**一句话要点**：提出RIA统一框架以优化列表式CTR预测，解决排序与重排序解耦问题。

**关键词**：CTR预测, 重排序, 端到端学习, Transformer架构, 广告系统优化

## 3 点简述
- 核心问题：现有方法解耦排序与重排序，导致列表式模型稀疏且表示能力弱。
- 方法要点：集成点式和列表式评估，引入UCDT、CUHT、LMH和EC模块。
- 实验效果：在公开和工业数据集上AUC和LogLoss提升，在线CTR和CPM显著增长。

## 摘要（原文）

> Reranking improves recommendation quality by modeling item interactions. However, existing methods often decouple ranking and reranking, leading to weak listwise evaluation models that suffer from combinatorial sparsity and limited representational power under strict latency constraints. In this paper, we propose RIA (Ranking-Infused Architecture), a unified, end-to-end framework that seamlessly integrates pointwise and listwise evaluation. RIA introduces four key components: (1) the User and Candidate DualTransformer (UCDT) for fine-grained user-item-context modeling; (2) the Context-aware User History and Target (CUHT) module for position-sensitive preference learning; (3) the Listwise Multi-HSTU (LMH) module to capture hierarchical item dependencies; and (4) the Embedding Cache (EC) module to bridge efficiency and effectiveness during inference. By sharing representations across ranking and reranking, RIA enables rich contextual knowledge transfer while maintaining low latency. Extensive experiments show that RIA outperforms state-of-the-art models on both public and industrial datasets, achieving significant gains in AUC and LogLoss. Deployed in Meituan advertising system, RIA yields a +1.69% improvement in Click-Through Rate (CTR) and a +4.54% increase in Cost Per Mille (CPM) in online A/B tests.

