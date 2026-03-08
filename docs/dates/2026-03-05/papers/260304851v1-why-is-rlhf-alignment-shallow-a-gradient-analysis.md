---
layout: default
title: Why Is RLHF Alignment Shallow? A Gradient Analysis
---

# Why Is RLHF Alignment Shallow? A Gradient Analysis
**arXiv**：[2603.04851v1](https://arxiv.org/abs/2603.04851) · [PDF](https://arxiv.org/pdf/2603.04851.pdf)  
**作者**：Robin Young  

**一句话要点**：提出基于梯度分析的理论框架，揭示RLHF对齐浅层化的原因并提出改进目标

**关键词**：RLHF对齐, 梯度分析, 鞅分解, 危害信息, KL散度, 数据增强

## 3 点简述
- 核心问题：RLHF对齐为何浅层化，梯度信号集中在危害决定位置
- 方法要点：使用鞅分解和协方差分析，推导对齐梯度的精确表征
- 实验或效果：理论证明标准目标无法实现深度对齐，提出基于恢复惩罚的新目标

## 摘要（原文）

> Why is safety alignment in LLMs shallow? We prove that gradient-based alignment inherently concentrates on positions where harm is decided and vanishes beyond. Using a martingale decomposition of sequence-level harm, we derive an exact characterization of alignment gradients. The gradient at position $t$ equals the covariance between the conditional expected harm and the score function. This implies that positions beyond the harm horizon where the output's harmfulness is already determined receive zero gradient signal during training. This explains empirical observations that KL divergence between aligned and base models concentrates on early tokens. Consequently, standard alignment objectives cannot produce deep alignment, regardless of optimization quality. We introduce the concept of harm information $I_t$, which quantifies each position's influence on harm, and prove that equilibrium KL divergence tracks this quantity. Finally, we derive an objective based on recovery penalties that creates gradient signal at all positions, providing theoretical grounding for empirically successful data augmentation techniques.

