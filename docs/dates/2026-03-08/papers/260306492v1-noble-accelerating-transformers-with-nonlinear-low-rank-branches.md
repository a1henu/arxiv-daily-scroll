---
layout: default
title: NOBLE: Accelerating Transformers with Nonlinear Low-Rank Branches
---

# NOBLE: Accelerating Transformers with Nonlinear Low-Rank Branches
**arXiv**：[2603.06492v1](https://arxiv.org/abs/2603.06492) · [PDF](https://arxiv.org/pdf/2603.06492.pdf)  
**作者**：Ethan Smith  

**一句话要点**：提出NOBLE架构增强方法，通过非线性低秩分支加速Transformer预训练。

**关键词**：Transformer加速, 非线性低秩分支, 预训练优化, 架构增强, 训练效率

## 3 点简述
- 核心问题：传统Transformer线性层在预训练中效率有限，需提升训练速度与效果。
- 方法要点：添加永久性非线性低秩分支，使用可学习非线性函数如CosNet，增加少量参数。
- 实验或效果：在多种模型上实现训练步骤减少达32%，净墙钟加速达1.22倍，但某些数据增强可能干扰效果。

## 摘要（原文）

> We introduce NOBLE (Nonlinear lOw-rank Branch for Linear Enhancement), an architectural augmentation that adds nonlinear low-rank branches to transformer linear layers. Unlike LoRA and other parameter-efficient fine-tuning (PEFT) methods, NOBLE is designed for pretraining from scratch. The branch is a permanent part of the architecture as opposed to an adapter for finetuning on top of frozen weights. The branch computes σ(xWdown)Wup where σ is a learnable nonlinearity. We evaluate several activation functions and find that CosNet, a two-layer cosine nonlinearity with learnable frequency and phase with a linear projection in between them in the bottleneck space, performs best. NOBLE achieves substantial improvements with minimal overhead: up to 1.47x step speedup to reach baseline eval loss (up to 32% fewer training steps), with as low as 4% additional parameters and 7% step time overhead, resulting in up to 1.22x net wallclock speedup. Experiments on LLMs (250M and 1.5B parameters), BERT, VQGAN, and ViT consistently show improved training efficiency. We identify one caveat: Mixup/CutMix augmentation interferes with NOBLE's benefits in Imagenet classification along with other stochastic augmentations, but when disabled, ViT also improves. This discrepancy is possibly explained by regularization techniques that encourage smoother fits to the target function while NOBLE may specialize more in sharper aspects of the target function.

