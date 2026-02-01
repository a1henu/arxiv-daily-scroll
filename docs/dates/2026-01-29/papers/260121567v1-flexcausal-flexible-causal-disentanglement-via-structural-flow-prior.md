---
layout: default
title: FlexCausal: Flexible Causal Disentanglement via Structural Flow Priors and Manifold-Aware Interventions
---

# FlexCausal: Flexible Causal Disentanglement via Structural Flow Priors and Manifold-Aware Interventions
**arXiv**：[2601.21567v1](https://arxiv.org/abs/2601.21567) · [PDF](https://arxiv.org/pdf/2601.21567.pdf)  
**作者**：Yutao Jin, Yuang Tao, Junyong Zhai  

**一句话要点**：提出FlexCausal框架以解决因果解耦表示学习中后验协方差对角化和先验噪声高斯假设的局限性

**关键词**：因果解耦表示学习, 块对角协方差VAE, 因子化流先验, 反事实一致性, 流形感知干预, 非高斯噪声建模

## 3 点简述
- 现有方法依赖对角后验协方差和高斯先验，无法处理真实世界因果因素的非高斯复杂统计特性
- 采用块对角协方差VAE和因子化流先验，分离因果机制与分布统计学习，结合对齐目标和反事实约束
- 在合成和真实数据集上实验显示，FlexCausal显著优于其他方法，实现高保真生成

## 摘要（原文）

> Causal Disentangled Representation Learning(CDRL) aims to learn and disentangle low dimensional representations and their underlying causal structure from observations. However, existing disentanglement methods rely on a standard mean-field approximation with a diagonal posterior covariance, which decorrelates all latent dimensions. Additionally, these methods often assume isotropic Gaussian priors for exogenous noise, failing to capture the complex, non-Gaussian statistical properties prevalent in real-world causal factors. Therefore, we propose FlexCausal, a novel CDRL framework based on a block-diagonal covariance VAE. FlexCausal utilizes a Factorized Flow-based Prior to realistically model the complex densities of exogenous noise, effectively decoupling the learning of causal mechanisms from distributional statistics. By integrating supervised alignment objectives with counterfactual consistency constraints, our framework ensures a precise structural correspondence between the learned latent subspaces and the ground-truth causal relations. Finally, we introduce a manifold-aware relative intervention strategy to ensure high-fidelity generation. Experimental results on both synthetic and real-world datasets demonstrate that FlexCausal significantly outperforms other methods.

