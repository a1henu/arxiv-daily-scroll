---
layout: default
title: Semantic-Guided Dynamic Sparsification for Pre-Trained Model-based Class-Incremental Learning
---

# Semantic-Guided Dynamic Sparsification for Pre-Trained Model-based Class-Incremental Learning
**arXiv**：[2601.21345v1](https://arxiv.org/abs/2601.21345) · [PDF](https://arxiv.org/pdf/2601.21345.pdf)  
**作者**：Ruiqi Liu, Boyu Diao, Zijia An, Runjie Shao, Zhulin An, Fei Wang, Yongjun Xu  

**一句话要点**：提出语义引导动态稀疏化方法，以解决类增量学习中预训练模型适配器的可塑性受限问题。

**关键词**：类增量学习, 预训练模型, 动态稀疏化, 激活空间, 知识迁移, 干扰防止

## 3 点简述
- 核心问题：类增量学习中，冻结预训练模型并使用正交约束的轻量适配器会损害模型的可塑性。
- 方法要点：通过语义引导动态稀疏化，在激活空间中塑造类特定稀疏子空间，促进相似类间知识迁移并防止干扰。
- 实验或效果：在多个基准数据集上实验，SGDS方法实现了最先进的性能表现。

## 摘要（原文）

> Class-Incremental Learning (CIL) requires a model to continually learn new classes without forgetting old ones. A common and efficient solution freezes a pre-trained model and employs lightweight adapters, whose parameters are often forced to be orthogonal to prevent inter-task interference. However, we argue that this parameter-constraining method is detrimental to plasticity. To this end, we propose Semantic-Guided Dynamic Sparsification (SGDS), a novel method that proactively guides the activation space by governing the orientation and rank of its subspaces through targeted sparsification. Specifically, SGDS promotes knowledge transfer by encouraging similar classes to share a compact activation subspace, while simultaneously preventing interference by assigning non-overlapping activation subspaces to dissimilar classes. By sculpting class-specific sparse subspaces in the activation space, SGDS effectively mitigates interference without imposing rigid constraints on the parameter space. Extensive experiments on various benchmark datasets demonstrate the state-of-the-art performance of SGDS.

