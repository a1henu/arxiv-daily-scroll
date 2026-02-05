---
layout: default
title: Generative Neural Operators through Diffusion Last Layer
---

# Generative Neural Operators through Diffusion Last Layer
**arXiv**：[2602.04139v1](https://arxiv.org/abs/2602.04139) · [PDF](https://arxiv.org/pdf/2602.04139.pdf)  
**作者**：Sungwon Park, Anthony Zhou, Hongjoong Kim, Amir Barati Farimani  

**一句话要点**：提出扩散最后一层以增强神经算子的不确定性建模能力

**关键词**：神经算子, 不确定性量化, 扩散模型, 函数空间建模, 随机偏微分方程

## 3 点简述
- 神经算子缺乏对随机系统的概率建模，需不确定性量化
- 扩散最后一层作为轻量级概率头，通过低秩展开在函数空间参数化输出分布
- 在随机PDE基准中提升泛化与不确定性预测，增强确定性场景的稳定性

## 摘要（原文）

> Neural operators have emerged as a powerful paradigm for learning discretization-invariant function-to-function mappings in scientific computing. However, many practical systems are inherently stochastic, making principled uncertainty quantification essential for reliable deployment. To address this, we introduce a simple add-on, the diffusion last layer (DLL), a lightweight probabilistic head that can be attached to arbitrary neural operator backbones to model predictive uncertainty. Motivated by the relative smoothness and low-dimensional structure often exhibited by PDE solution distributions, DLL parameterizes the conditional output distribution directly in function space through a low-rank Karhunen-Loève expansion, enabling efficient and expressive uncertainty modeling. Across stochastic PDE operator learning benchmarks, DLL improves generalization and uncertainty-aware prediction. Moreover, even in deterministic long-horizon rollout settings, DLL enhances rollout stability and provides meaningful estimates of epistemic uncertainty for backbone neural operators.

