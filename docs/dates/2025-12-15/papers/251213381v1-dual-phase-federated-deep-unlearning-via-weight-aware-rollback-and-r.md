---
layout: default
title: Dual-Phase Federated Deep Unlearning via Weight-Aware Rollback and Reconstruction
---

# Dual-Phase Federated Deep Unlearning via Weight-Aware Rollback and Reconstruction
**arXiv**：[2512.13381v1](https://arxiv.org/abs/2512.13381) · [PDF](https://arxiv.org/pdf/2512.13381.pdf)  
**作者**：Changjun Zhou, Jintao Zheng, Leyou Yang, Pengfei Wang  

**一句话要点**：提出双阶段联邦深度遗忘方法，通过权重感知回滚与重建解决隐私泄露问题

**关键词**：联邦学习, 隐私保护, 深度遗忘, 权重回滚, 变分自编码器, 模型重建

## 3 点简述
- 核心问题：现有联邦遗忘方法依赖服务器端知识蒸馏，仅移除目标客户端更新，忽略其他客户端贡献中的隐私，可能导致隐私泄露。
- 方法要点：基于权重感知，回滚高权重参数，利用变分自编码器重建并消除低权重参数，结合投影技术恢复模型。
- 实验或效果：在四个数据集上验证，相比基线方法，准确率提升1%-5%，时间成本降低高达12倍。

## 摘要（原文）

> Federated Unlearning (FUL) focuses on client data and computing power to offer a privacy-preserving solution. However, high computational demands, complex incentive mechanisms, and disparities in client-side computing power often lead to long times and higher costs. To address these challenges, many existing methods rely on server-side knowledge distillation that solely removes the updates of the target client, overlooking the privacy embedded in the contributions of other clients, which can lead to privacy leakage. In this work, we introduce DPUL, a novel server-side unlearning method that deeply unlearns all influential weights to prevent privacy pitfalls. Our approach comprises three components: (i) identifying high-weight parameters by filtering client update magnitudes, and rolling them back to ensure deep removal. (ii) leveraging the variational autoencoder (VAE) to reconstruct and eliminate low-weight parameters. (iii) utilizing a projection-based technique to recover the model. Experimental results on four datasets demonstrate that DPUL surpasses state-of-the-art baselines, providing a 1%-5% improvement in accuracy and up to 12x reduction in time cost.

