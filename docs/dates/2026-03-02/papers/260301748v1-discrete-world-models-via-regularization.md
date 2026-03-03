---
layout: default
title: Discrete World Models via Regularization
---

# Discrete World Models via Regularization
**arXiv**：[2603.01748v1](https://arxiv.org/abs/2603.01748) · [PDF](https://arxiv.org/pdf/2603.01748.pdf)  
**作者**：Davide Bizzaro, Luciano Serafini  

**一句话要点**：提出DWMR方法，通过正则化实现无监督布尔世界模型学习，无需重建或对比信号。

**关键词**：布尔世界模型, 无监督学习, 正则化方法, 潜在空间表示, 稀疏动作建模

## 3 点简述
- 核心问题：现有世界模型依赖重建或对比信号保持潜在空间信息，限制了布尔表示的独立性和稀疏性。
- 方法要点：引入耦合潜在预测与正则化的损失函数，最大化熵和独立性，并强制稀疏动作变化的局部性先验。
- 实验或效果：在组合结构基准上，DWMR比基于重建的方法学习到更准确的表示和转移，结合重建解码器可进一步提升性能。

## 摘要（原文）

> World models aim to capture the states and dynamics of an environment in a compact latent space. Moreover, using Boolean state representations is particularly useful for search heuristics and symbolic reasoning and planning. Existing approaches keep latents informative via decoder-based reconstruction, or instead via contrastive or reward signals. In this work, we introduce Discrete World Models via Regularization (DWMR): a reconstruction-free and contrastive-free method for unsupervised Boolean world-model learning. In particular, we introduce a novel world-modeling loss that couples latent prediction with specialized regularizers. Such regularizers maximize the entropy and independence of the representation bits through variance, correlation, and coskewness penalties, while simultaneously enforcing a locality prior for sparse action changes. To enable effective optimization, we also introduce a novel training scheme improving robustness to discrete roll-outs. Experiments on two benchmarks with underlying combinatorial structure show that DWMR learns more accurate representations and transitions than reconstruction-based alternatives. Finally, DWMR can also be paired with an auxiliary reconstruction decoder, and this combination yields additional gains.

