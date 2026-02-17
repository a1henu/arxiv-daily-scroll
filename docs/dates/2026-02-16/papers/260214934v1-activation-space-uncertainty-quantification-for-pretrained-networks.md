---
layout: default
title: Activation-Space Uncertainty Quantification for Pretrained Networks
---

# Activation-Space Uncertainty Quantification for Pretrained Networks
**arXiv**：[2602.14934v1](https://arxiv.org/abs/2602.14934) · [PDF](https://arxiv.org/pdf/2602.14934.pdf)  
**作者**：Richard Bergna, Stefan Depeweg, Sergio Calvo-Ordoñez, Jonathan Plenk, Alvaro Cartea, Jose Miguel Hernández-Lobato  

**一句话要点**：提出GAPA方法，通过激活空间贝叶斯建模为预训练网络提供高效不确定性量化

**关键词**：不确定性量化, 预训练网络, 激活空间建模, 高斯过程, 后处理方法, 高效推理

## 3 点简述
- 核心问题：预训练模型的不确定性量化常需重训练或高计算成本，可能改变预测
- 方法要点：将贝叶斯建模从权重移至激活空间，用高斯过程激活替换非线性层，保持预测不变
- 实验或效果：在回归、分类等任务中，校准和分布外检测匹配或优于基线，测试时高效

## 摘要（原文）

> Reliable uncertainty estimates are crucial for deploying pretrained models; yet, many strong methods for quantifying uncertainty require retraining, Monte Carlo sampling, or expensive second-order computations and may alter a frozen backbone's predictions. To address this, we introduce Gaussian Process Activations (GAPA), a post-hoc method that shifts Bayesian modeling from weights to activations. GAPA replaces standard nonlinearities with Gaussian-process activations whose posterior mean exactly matches the original activation, preserving the backbone's point predictions by construction while providing closed-form epistemic variances in activation space. To scale to modern architectures, we use a sparse variational inducing-point approximation over cached training activations, combined with local k-nearest-neighbor subset conditioning, enabling deterministic single-pass uncertainty propagation without sampling, backpropagation, or second-order information. Across regression, classification, image segmentation, and language modeling, GAPA matches or outperforms strong post-hoc baselines in calibration and out-of-distribution detection while remaining efficient at test time.

