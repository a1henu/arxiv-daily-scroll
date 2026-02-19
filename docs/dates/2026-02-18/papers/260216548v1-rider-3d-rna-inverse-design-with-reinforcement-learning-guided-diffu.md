---
layout: default
title: RIDER: 3D RNA Inverse Design with Reinforcement Learning-Guided Diffusion
---

# RIDER: 3D RNA Inverse Design with Reinforcement Learning-Guided Diffusion
**arXiv**：[2602.16548v1](https://arxiv.org/abs/2602.16548) · [PDF](https://arxiv.org/pdf/2602.16548.pdf)  
**作者**：Tianmeng Hu, Yongzheng Cui, Biao Luo, Ke Li  

**一句话要点**：提出RIDER框架，通过强化学习引导扩散模型直接优化3D结构相似性，以解决RNA逆设计中序列恢复与结构保真度不匹配的问题。

**关键词**：RNA逆设计, 3D结构相似性, 强化学习, 扩散模型, 图神经网络, 策略梯度

## 3 点简述
- 核心问题：RNA逆设计现有方法依赖序列恢复作为代理指标，但高恢复率不一定保证正确折叠，结构保真度评估不足。
- 方法要点：先预训练基于GNN的条件扩散模型生成序列，再通过改进策略梯度算法和3D自洽奖励函数进行微调。
- 实验或效果：RIDER在结构相似性指标上提升超过100%，并生成与原生序列不同的设计，优于现有方法。

## 摘要（原文）

> The inverse design of RNA three-dimensional (3D) structures is crucial for engineering functional RNAs in synthetic biology and therapeutics. While recent deep learning approaches have advanced this field, they are typically optimized and evaluated using native sequence recovery, which is a limited surrogate for structural fidelity, since different sequences can fold into similar 3D structures and high recovery does not necessarily indicate correct folding. To address this limitation, we propose RIDER, an RNA Inverse DEsign framework with Reinforcement learning that directly optimizes for 3D structural similarity. First, we develop and pre-train a GNN-based generative diffusion model conditioned on the target 3D structure, achieving a 9% improvement in native sequence recovery over state-of-the-art methods. Then, we fine-tune the model with an improved policy gradient algorithm using four task-specific reward functions based on 3D self-consistency metrics. Experimental results show that RIDER improves structural similarity by over 100% across all metrics and discovers designs that are distinct from native sequences.

