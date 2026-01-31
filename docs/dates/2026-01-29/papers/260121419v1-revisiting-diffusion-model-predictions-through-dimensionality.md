---
layout: default
title: Revisiting Diffusion Model Predictions Through Dimensionality
---

# Revisiting Diffusion Model Predictions Through Dimensionality
**arXiv**：[2601.21419v1](https://arxiv.org/abs/2601.21419) · [PDF](https://arxiv.org/pdf/2601.21419.pdf)  
**作者**：Qing Jin, Chaoyang Wang  

**一句话要点**：提出k-Diff框架，基于数据维度理论优化扩散模型预测目标，提升生成性能。

**关键词**：扩散模型, 预测目标优化, 数据维度理论, 生成模型, 图像生成, 自动化学习

## 3 点简述
- 核心问题：扩散模型中预测目标（如噪声、速度、数据）的选择缺乏理论依据，尤其在数据维度影响下。
- 方法要点：建立广义预测理论框架，分析数据几何与最优目标关系，提出k-Diff自动学习最优预测参数。
- 实验或效果：在潜空间和像素空间图像生成中，k-Diff优于固定目标基线，验证了理论并实现自动化提升。

## 摘要（原文）

> Recent advances in diffusion and flow matching models have highlighted a shift in the preferred prediction target -- moving from noise ($\varepsilon$) and velocity (v) to direct data (x) prediction -- particularly in high-dimensional settings. However, a formal explanation of why the optimal target depends on the specific properties of the data remains elusive. In this work, we provide a theoretical framework based on a generalized prediction formulation that accommodates arbitrary output targets, of which $\varepsilon$-, v-, and x-prediction are special cases. We derive the analytical relationship between data's geometry and the optimal prediction target, offering a rigorous justification for why x-prediction becomes superior when the ambient dimension significantly exceeds the data's intrinsic dimension. Furthermore, while our theory identifies dimensionality as the governing factor for the optimal prediction target, the intrinsic dimension of manifold-bound data is typically intractable to estimate in practice. To bridge this gap, we propose k-Diff, a framework that employs a data-driven approach to learn the optimal prediction parameter k directly from data, bypassing the need for explicit dimension estimation. Extensive experiments in both latent-space and pixel-space image generation demonstrate that k-Diff consistently outperforms fixed-target baselines across varying architectures and data scales, providing a principled and automated approach to enhancing generative performance.

