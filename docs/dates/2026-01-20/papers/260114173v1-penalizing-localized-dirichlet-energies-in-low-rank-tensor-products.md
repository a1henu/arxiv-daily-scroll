---
layout: default
title: Penalizing Localized Dirichlet Energies in Low Rank Tensor Products
---

# Penalizing Localized Dirichlet Energies in Low Rank Tensor Products
**arXiv**：[2601.14173v1](https://arxiv.org/abs/2601.14173) · [PDF](https://arxiv.org/pdf/2601.14173.pdf)  
**作者**：Paris A. Karakasis, Nicholas D. Sidiropoulos  

**一句话要点**：提出局部狄利克雷能量正则化策略，以解决张量积B样条模型在回归任务中全局正则化失效的问题。

**关键词**：张量积B样条, 狄利克雷能量, 正则化策略, 回归任务, 过拟合控制

## 3 点简述
- 研究低秩张量积B样条模型，发现全局狄利克雷能量正则化在完美插值场景下可能失效。
- 提出基于训练点局部超立方体的局部狄利克雷能量正则化方法，增强模型平滑性控制。
- 实验显示张量积B样条模型在过拟合场景下优于神经网络，且对正则化更鲁棒。

## 摘要（原文）

> We study low-rank tensor-product B-spline (TPBS) models for regression tasks and investigate Dirichlet energy as a measure of smoothness. We show that TPBS models admit a closed-form expression for the Dirichlet energy, and reveal scenarios where perfect interpolation is possible with exponentially small Dirichlet energy. This renders global Dirichlet energy-based regularization ineffective. To address this limitation, we propose a novel regularization strategy based on local Dirichlet energies defined on small hypercubes centered at the training points. Leveraging pretrained TPBS models, we also introduce two estimators for inference from incomplete samples. Comparative experiments with neural networks demonstrate that TPBS models outperform neural networks in the overfitting regime for most datasets, and maintain competitive performance otherwise. Overall, TPBS models exhibit greater robustness to overfitting and consistently benefit from regularization, while neural networks are more sensitive to overfitting and less effective in leveraging regularization.

