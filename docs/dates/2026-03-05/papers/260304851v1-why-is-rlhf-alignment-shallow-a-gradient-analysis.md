---
layout: default
title: Why Is RLHF Alignment Shallow? A Gradient Analysis
---

# Why Is RLHF Alignment Shallow? A Gradient Analysis
**arXiv**：[2603.04851v1](https://arxiv.org/abs/2603.04851) · [PDF](https://arxiv.org/pdf/2603.04851.pdf)  
**作者**：Robin Young  

**一句话要点**：提出基于梯度分析揭示RLHF对齐浅层原因，并引入恢复惩罚目标以增强对齐深度

**关键词**：RLHF对齐, 梯度分析, 伤害信息, KL散度, 数据增强, 恢复惩罚

## 3 点简述
- 核心问题：证明基于梯度的对齐方法在伤害决定位置后梯度消失，导致对齐浅层
- 方法要点：通过鞅分解序列级伤害，推导对齐梯度的精确表征，并引入伤害信息量化位置影响
- 实验或效果：理论推导支持数据增强技术，提出恢复惩罚目标在所有位置产生梯度信号

## 摘要（原文）

> Why is safety alignment in LLMs shallow? We prove that gradient-based alignment inherently concentrates on positions where harm is decided and vanishes beyond. Using a martingale decomposition of sequence-level harm, we derive an exact characterization of alignment gradients. The gradient at position $t$ equals the covariance between the conditional expected harm and the score function. This implies that positions beyond the harm horizon where the output's harmfulness is already determined receive zero gradient signal during training. This explains empirical observations that KL divergence between aligned and base models concentrates on early tokens. Consequently, standard alignment objectives cannot produce deep alignment, regardless of optimization quality. We introduce the concept of harm information $I_t$, which quantifies each position's influence on harm, and prove that equilibrium KL divergence tracks this quantity. Finally, we derive an objective based on recovery penalties that creates gradient signal at all positions, providing theoretical grounding for empirically successful data augmentation techniques.

