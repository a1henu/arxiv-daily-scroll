---
layout: default
title: LoopViT: Scaling Visual ARC with Looped Transformers
---

# LoopViT: Scaling Visual ARC with Looped Transformers
**arXiv**：[2602.02156v1](https://arxiv.org/abs/2602.02156) · [PDF](https://arxiv.org/pdf/2602.02156.pdf)  
**作者**：Wen-Jie Shu, Xuerui Qiu, Rui-Jie Zhu, Harold Haodong Chen, Yexin Liu, Harry Yang  

**一句话要点**：提出LoopViT，通过循环Transformer解决视觉推理中计算深度与参数规模耦合的问题。

**关键词**：视觉推理, 循环Transformer, 动态退出机制, ARC-AGI基准, 权重共享

## 3 点简述
- 核心问题：前馈架构在视觉推理中计算深度受限于参数规模，难以模拟人类归纳的迭代算法特性。
- 方法要点：采用权重共享的循环架构，结合局部卷积和全局注意力，并引入基于预测熵的动态退出机制。
- 实验或效果：在ARC-AGI-1基准上，18M参数模型达到65.8%准确率，优于73M参数集成模型。

## 摘要（原文）

> Recent advances in visual reasoning have leveraged vision transformers to tackle the ARC-AGI benchmark. However, we argue that the feed-forward architecture, where computational depth is strictly bound to parameter size, falls short of capturing the iterative, algorithmic nature of human induction. In this work, we propose a recursive architecture called Loop-ViT, which decouples reasoning depth from model capacity through weight-tied recurrence. Loop-ViT iterates a weight-tied Hybrid Block, combining local convolutions and global attention, to form a latent chain of thought. Crucially, we introduce a parameter-free Dynamic Exit mechanism based on predictive entropy: the model halts inference when its internal state ``crystallizes" into a low-uncertainty attractor. Empirical results on the ARC-AGI-1 benchmark validate this perspective: our 18M model achieves 65.8% accuracy, outperforming massive 73M-parameter ensembles. These findings demonstrate that adaptive iterative computation offers a far more efficient scaling axis for visual reasoning than simply increasing network width. The code is available at https://github.com/WenjieShu/LoopViT.

