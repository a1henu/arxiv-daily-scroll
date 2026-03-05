---
layout: default
title: DisenReason: Behavior Disentanglement and Latent Reasoning for Shared-Account Sequential Recommendation
---

# DisenReason: Behavior Disentanglement and Latent Reasoning for Shared-Account Sequential Recommendation
**arXiv**：[2603.03782v1](https://arxiv.org/abs/2603.03782) · [PDF](https://arxiv.org/pdf/2603.03782.pdf)  
**作者**：Jiawei Cheng, Min Gao, Zongwei Wang, Xiaofei Zhu, Zhiyi Liu, Wentao Li, Wei Li, Huan Wu  

**一句话要点**：提出DisenReason方法，通过行为解耦和潜在推理解决共享账户序列推荐问题。

**关键词**：共享账户序列推荐, 行为解耦, 潜在推理, 频域分析, 推荐系统

## 3 点简述
- 核心问题：共享账户中多用户行为混杂，现有方法假设固定潜在用户数，限制推荐准确性。
- 方法要点：两阶段推理，先频域行为解耦构建统一账户表示，再潜在用户推理推断用户数。
- 实验或效果：在四个基准数据集上优于现有方法，MRR@5和Recall@20相对提升最高达12.56%和6.06%。

## 摘要（原文）

> Shared-account usage is common on streaming and e-commerce platforms, where multiple users share one account. Existing shared-account sequential recommendation (SSR) methods often assume a fixed number of latent users per account, limiting their ability to adapt to diverse sharing patterns and reducing recommendation accuracy. Recent latent reasoning technique applied in sequential recommendation (SR) generate intermediate embeddings from the user embedding (e.g, last item embedding) to uncover users' potential interests, which inspires us to treat the problem of inferring the number of latent users as generating a series of intermediate embeddings, shifting from inferring preferences behind user to inferring the users behind account. However, the last item cannot be directly used for reasoning in SSR, as it can only represent the behavior of the most recent latent user, rather than the collective behavior of the entire account. To address this, we propose DisenReason, a two-stage reasoning method tailored to SSR. DisenReason combines behavior disentanglement stage from frequency-domain perspective to create a collective and unified account behavior representation, which serves as a pivot for latent user reasoning stage to infer the number of users behind the account. Experiments on four benchmark datasets show that DisenReason consistently outperforms all state-of-the-art baselines across four benchmark datasets, achieving relative improvements of up to 12.56\% in MRR@5 and 6.06\% in Recall@20.

