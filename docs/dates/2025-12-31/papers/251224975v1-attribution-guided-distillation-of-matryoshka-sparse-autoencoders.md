---
layout: default
title: Attribution-Guided Distillation of Matryoshka Sparse Autoencoders
---

# Attribution-Guided Distillation of Matryoshka Sparse Autoencoders
**arXiv**：[2512.24975v1](https://arxiv.org/abs/2512.24975) · [PDF](https://arxiv.org/pdf/2512.24975.pdf)  
**作者**：Cristina P. Martin-Linares, Jonathan P. Ling  

**一句话要点**：提出蒸馏嵌套稀疏自编码器以解决稀疏自编码器特征冗余和可转移性问题

**关键词**：稀疏自编码器, 特征蒸馏, 归因引导, 模型解释, 可转移特征

## 3 点简述
- 稀疏自编码器特征冗余且训练不稳定，导致解释难以复用
- 通过迭代蒸馏循环，基于梯度激活归因选择核心特征并跨周期重用
- 在Gemma-2-2B模型上实验，蒸馏核心提升SAEBench指标，实现特征跨稀疏度转移

## 摘要（原文）

> Sparse autoencoders (SAEs) aim to disentangle model activations into monosemantic, human-interpretable features. In practice, learned features are often redundant and vary across training runs and sparsity levels, which makes interpretations difficult to transfer and reuse. We introduce Distilled Matryoshka Sparse Autoencoders (DMSAEs), a training pipeline that distills a compact core of consistently useful features and reuses it to train new SAEs. DMSAEs run an iterative distillation cycle: train a Matryoshka SAE with a shared core, use gradient X activation to measure each feature's contribution to next-token loss in the most nested reconstruction, and keep only the smallest subset that explains a fixed fraction of the attribution. Only the core encoder weight vectors are transferred across cycles; the core decoder and all non-core latents are reinitialized each time. On Gemma-2-2B layer 12 residual stream activations, seven cycles of distillation (500M tokens, 65k width) yielded a distilled core of 197 features that were repeatedly selected. Training using this distilled core improves several SAEBench metrics and demonstrates that consistent sets of latent features can be transferred across sparsity levels

