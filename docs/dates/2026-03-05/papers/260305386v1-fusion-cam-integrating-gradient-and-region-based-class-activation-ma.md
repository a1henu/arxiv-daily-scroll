---
layout: default
title: Fusion-CAM: Integrating Gradient and Region-Based Class Activation Maps for Robust Visual Explanations
---

# Fusion-CAM: Integrating Gradient and Region-Based Class Activation Maps for Robust Visual Explanations
**arXiv**：[2603.05386v1](https://arxiv.org/abs/2603.05386) · [PDF](https://arxiv.org/pdf/2603.05386.pdf)  
**作者**：Hajar Dekdegue, Moncef Garouani, Josiane Mothe, Jordan Bernigaud  

**一句话要点**：提出Fusion-CAM以融合梯度和区域类激活图，提供鲁棒视觉解释

**关键词**：类激活图, 可解释AI, 梯度融合, 视觉解释, 深度学习

## 3 点简述
- 核心问题：梯度CAM噪声大且覆盖不全，区域CAM平滑过度且细节不敏感
- 方法要点：先降噪梯度图，再加权融合区域图，最后自适应像素级融合
- 实验或效果：在标准基准上优于现有CAM变体，提供灵活解释工具

## 摘要（原文）

> Interpreting the decision-making process of deep convolutional neural networks remains a central challenge in achieving trustworthy and transparent artificial intelligence. Explainable AI (XAI) techniques, particularly Class Activation Map (CAM) methods, are widely adopted to visualize the input regions influencing model predictions. Gradient-based approaches (e.g. Grad-CAM) provide highly discriminative, fine-grained details by computing gradients of class activations but often yield noisy and incomplete maps that emphasize only the most salient regions rather than the complete objects. Region-based approaches (e.g. Score-CAM) aggregate information over larger areas, capturing broader object coverage at the cost of over-smoothing and reduced sensitivity to subtle features. We introduce Fusion-CAM, a novel framework that bridges this explanatory gap by unifying both paradigms through a dedicated fusion mechanism to produce robust and highly discriminative visual explanations. Our method first denoises gradient-based maps, yielding cleaner and more focused activations. It then combines the refined gradient map with region-based maps using contribution weights to enhance class coverage. Finally, we propose an adaptive similarity-based pixel-level fusion that evaluates the agreement between both paradigms and dynamically adjusts the fusion strength. This adaptive mechanism reinforces consistent activations while softly blending conflicting regions, resulting in richer, context-aware, and input-adaptive visual explanations. Extensive experiments on standard benchmarks show that Fusion-CAM consistently outperforms existing CAM variants in both qualitative visualization and quantitative evaluation, providing a robust and flexible tool for interpreting deep neural networks.

