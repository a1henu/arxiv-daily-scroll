---
layout: default
title: Self-Supervised Learning from Structural Invariance
---

# Self-Supervised Learning from Structural Invariance
**arXiv**：[2602.02381v1](https://arxiv.org/abs/2602.02381) · [PDF](https://arxiv.org/pdf/2602.02381.pdf)  
**作者**：Yipeng Zhang, Hafez Ghaemi, Jungyoon Lee, Shahab Bakhtiari, Eilif B. Muller, Laurent Charlin  

**一句话要点**：提出AdaSSL以解决自监督学习中一对多映射的不确定性建模问题

**关键词**：自监督学习, 一对多映射, 变分推理, 对比学习, 蒸馏学习, 视频理解

## 3 点简述
- 核心问题：自监督学习在处理一对多映射时难以灵活捕捉条件不确定性
- 方法要点：引入潜变量建模不确定性，推导变分下界并正则化标准目标
- 实验或效果：在因果表示学习、细粒度图像理解和视频世界建模中验证通用性

## 摘要（原文）

> Joint-embedding self-supervised learning (SSL), the key paradigm for unsupervised representation learning from visual data, learns from invariances between semantically-related data pairs. We study the one-to-many mapping problem in SSL, where each datum may be mapped to multiple valid targets. This arises when data pairs come from naturally occurring generative processes, e.g., successive video frames. We show that existing methods struggle to flexibly capture this conditional uncertainty. As a remedy, we introduce a latent variable to account for this uncertainty and derive a variational lower bound on the mutual information between paired embeddings. Our derivation yields a simple regularization term for standard SSL objectives. The resulting method, which we call AdaSSL, applies to both contrastive and distillation-based SSL objectives, and we empirically show its versatility in causal representation learning, fine-grained image understanding, and world modeling on videos.

