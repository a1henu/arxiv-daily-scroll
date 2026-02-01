---
layout: default
title: Latent Adversarial Regularization for Offline Preference Optimization
---

# Latent Adversarial Regularization for Offline Preference Optimization
**arXiv**：[2601.22083v1](https://arxiv.org/abs/2601.22083) · [PDF](https://arxiv.org/pdf/2601.22083.pdf)  
**作者**：Enyi Jiang, Yibo Jacky Zhang, Yinglun Xu, Andreas Haupt, Nancy Amato, Sanmi Koyejo  

**一句话要点**：提出GANPO以解决语言模型偏好优化中语义相似性不足的问题

**关键词**：语言模型偏好优化, 潜在空间正则化, 对抗性训练, 离线学习, 语义相似性

## 3 点简述
- 核心问题：基于token级正则化的偏好优化难以捕捉语义或行为相似性。
- 方法要点：通过对抗性方法在潜在空间正则化，惩罚策略模型与参考模型内部表示的差异。
- 实验或效果：在多个模型和任务中提升性能，提供更稳健的结构反馈，计算开销小。

## 摘要（原文）

> Learning from human feedback typically relies on preference optimization that constrains policy updates through token-level regularization. However, preference optimization for language models is particularly challenging because token-space similarity does not imply semantic or behavioral similarity. To address this challenge, we leverage latent-space regularization for language model preference optimization. We introduce GANPO, which achieves latent-space regularization by penalizing divergence between the internal representations of a policy model and a reference model. Given that latent representations are not associated with explicit probability densities, we adopt an adversarial approach inspired by GANs to minimize latent-space divergence. We integrate GANPO as a regularizer into existing offline preference optimization objectives. Experiments across multiple model architectures and tasks show consistent improvements from latent-space regularization. Further, by comparing GANPO-induced inferential biases with those from token-level regularization, we find that GANPO provides more robust structural feedback under distributional shift and noise while maintaining comparable downstream performance with minor computational overhead.

