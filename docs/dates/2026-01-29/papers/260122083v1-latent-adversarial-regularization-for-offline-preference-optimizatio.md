---
layout: default
title: Latent Adversarial Regularization for Offline Preference Optimization
---

# Latent Adversarial Regularization for Offline Preference Optimization
**arXiv**：[2601.22083v1](https://arxiv.org/abs/2601.22083) · [PDF](https://arxiv.org/pdf/2601.22083.pdf)  
**作者**：Enyi Jiang, Yibo Jacky Zhang, Yinglun Xu, Andreas Haupt, Nancy Amato, Sanmi Koyejo  

**一句话要点**：提出GANPO，通过潜在空间对抗正则化改进离线偏好优化，解决语言模型语义相似性挑战。

**关键词**：离线偏好优化, 潜在空间正则化, 对抗训练, 语言模型, 语义相似性, 分布偏移

## 3 点简述
- 核心问题：语言模型偏好优化中，词元级相似性不代表语义或行为相似性，导致优化困难。
- 方法要点：引入GANPO，利用对抗方法最小化策略模型与参考模型内部表示的差异，实现潜在空间正则化。
- 实验或效果：在多种模型架构和任务上验证，GANPO在分布偏移和噪声下提供更稳健反馈，计算开销小。

## 摘要（原文）

> Learning from human feedback typically relies on preference optimization that constrains policy updates through token-level regularization. However, preference optimization for language models is particularly challenging because token-space similarity does not imply semantic or behavioral similarity. To address this challenge, we leverage latent-space regularization for language model preference optimization. We introduce GANPO, which achieves latent-space regularization by penalizing divergence between the internal representations of a policy model and a reference model. Given that latent representations are not associated with explicit probability densities, we adopt an adversarial approach inspired by GANs to minimize latent-space divergence. We integrate GANPO as a regularizer into existing offline preference optimization objectives. Experiments across multiple model architectures and tasks show consistent improvements from latent-space regularization. Further, by comparing GANPO-induced inferential biases with those from token-level regularization, we find that GANPO provides more robust structural feedback under distributional shift and noise while maintaining comparable downstream performance with minor computational overhead.

