---
layout: default
title: Principled Confidence Estimation for Deep Computed Tomography
---

# Principled Confidence Estimation for Deep Computed Tomography
**arXiv**：[2602.05812v1](https://arxiv.org/abs/2602.05812) · [PDF](https://arxiv.org/pdf/2602.05812.pdf)  
**作者**：Matteo Gätzner, Johannes Kirschner  

**一句话要点**：提出基于序列似然混合框架的置信度估计方法，用于深度学习CT重建的可靠不确定性量化。

**关键词**：CT重建, 置信度估计, 深度学习不确定性, 序列似然混合, 医学成像, 泊松噪声模型

## 3 点简述
- 核心问题：在CT重建中，为深度学习模型提供理论覆盖保证的置信度估计，以检测幻觉并增强医学成像可靠性。
- 方法要点：基于序列似然混合框架，结合Beer-Lambert定律和泊松噪声的前向模型，适用于U-Net、扩散模型等深度方法。
- 实验或效果：深度重建方法相比经典方法产生更紧的置信区域，保持理论覆盖，支持不确定性感知的可视化。

## 摘要（原文）

> We present a principled framework for confidence estimation in computed tomography (CT) reconstruction. Based on the sequential likelihood mixing framework (Kirschner et al., 2025), we establish confidence regions with theoretical coverage guarantees for deep-learning-based CT reconstructions. We consider a realistic forward model following the Beer-Lambert law, i.e., a log-linear forward model with Poisson noise, closely reflecting clinical and scientific imaging conditions. The framework is general and applies to both classical algorithms and deep learning reconstruction methods, including U-Nets, U-Net ensembles, and generative Diffusion models. Empirically, we demonstrate that deep reconstruction methods yield substantially tighter confidence regions than classical reconstructions, without sacrificing theoretical coverage guarantees. Our approach allows the detection of hallucinations in reconstructed images and provides interpretable visualizations of confidence regions. This establishes deep models not only as powerful estimators, but also as reliable tools for uncertainty-aware medical imaging.

