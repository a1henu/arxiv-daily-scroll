---
layout: default
title: Principled Confidence Estimation for Deep Computed Tomography
---

# Principled Confidence Estimation for Deep Computed Tomography
**arXiv**：[2602.05812v1](https://arxiv.org/abs/2602.05812) · [PDF](https://arxiv.org/pdf/2602.05812.pdf)  
**作者**：Matteo Gätzner, Johannes Kirschner  

**一句话要点**：提出基于序列似然混合框架的置信度估计方法，用于深度学习CT重建的可靠不确定性量化。

**关键词**：置信度估计, CT重建, 深度学习, 不确定性量化, 医学成像, 序列似然混合

## 3 点简述
- 核心问题：深度学习CT重建缺乏理论保证的置信度估计，难以检测幻觉和提供不确定性可视化。
- 方法要点：基于序列似然混合框架，建立具有理论覆盖保证的置信区域，适用于经典算法和深度学习模型。
- 实验或效果：实证显示深度学习重建方法在保持理论覆盖的同时，产生比经典方法更紧的置信区域。

## 摘要（原文）

> We present a principled framework for confidence estimation in computed tomography (CT) reconstruction. Based on the sequential likelihood mixing framework (Kirschner et al., 2025), we establish confidence regions with theoretical coverage guarantees for deep-learning-based CT reconstructions. We consider a realistic forward model following the Beer-Lambert law, i.e., a log-linear forward model with Poisson noise, closely reflecting clinical and scientific imaging conditions. The framework is general and applies to both classical algorithms and deep learning reconstruction methods, including U-Nets, U-Net ensembles, and generative Diffusion models. Empirically, we demonstrate that deep reconstruction methods yield substantially tighter confidence regions than classical reconstructions, without sacrificing theoretical coverage guarantees. Our approach allows the detection of hallucinations in reconstructed images and provides interpretable visualizations of confidence regions. This establishes deep models not only as powerful estimators, but also as reliable tools for uncertainty-aware medical imaging.

