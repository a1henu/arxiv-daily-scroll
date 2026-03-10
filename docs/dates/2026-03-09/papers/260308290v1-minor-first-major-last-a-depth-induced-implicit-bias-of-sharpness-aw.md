---
layout: default
title: Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization
---

# Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization
**arXiv**：[2603.08290v1](https://arxiv.org/abs/2603.08290) · [PDF](https://arxiv.org/pdf/2603.08290.pdf)  
**作者**：Chaewon Moon, Dongkuk Si, Chulhee Yun  

**一句话要点**：揭示SAM在深度线性网络中的隐式偏差，发现其与梯度下降的差异及特征放大现象。

**关键词**：隐式偏差, 锐度感知最小化, 线性网络, 特征放大, 深度学习理论

## 3 点简述
- 研究SAM在线性可分二分类任务中训练L层线性对角网络的隐式偏差。
- 发现ℓ∞-SAM的极限方向依赖初始化，ℓ₂-SAM呈现从次要坐标到主要坐标的序列特征放大。
- 理论分析归因于梯度归一化因子，实验验证了合成和真实数据中的现象。

## 摘要（原文）

> We study the implicit bias of Sharpness-Aware Minimization (SAM) when training $L$-layer linear diagonal networks on linearly separable binary classification. For linear models ($L=1$), both $\ell_\infty$- and $\ell_2$-SAM recover the $\ell_2$ max-margin classifier, matching gradient descent (GD). However, for depth $L = 2$, the behavior changes drastically -- even on a single-example dataset. For $\ell_\infty$-SAM, the limit direction depends critically on initialization and can converge to $\mathbf{0}$ or to any standard basis vector, in stark contrast to GD, whose limit aligns with the basis vector of the dominant data coordinate. For $\ell_2$-SAM, we show that although its limit direction matches the $\ell_1$ max-margin solution as in the case of GD, its finite-time dynamics exhibit a phenomenon we call "sequential feature amplification", in which the predictor initially relies on minor coordinates and gradually shifts to larger ones as training proceeds or initialization increases. Our theoretical analysis attributes this phenomenon to $\ell_2$-SAM's gradient normalization factor applied in its perturbation, which amplifies minor coordinates early and allows major ones to dominate later, giving a concrete example where infinite-time implicit-bias analyses are insufficient. Synthetic and real-data experiments corroborate our findings.

