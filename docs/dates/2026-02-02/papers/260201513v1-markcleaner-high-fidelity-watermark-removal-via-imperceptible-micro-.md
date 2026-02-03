---
layout: default
title: MarkCleaner: High-Fidelity Watermark Removal via Imperceptible Micro-Geometric Perturbation
---

# MarkCleaner: High-Fidelity Watermark Removal via Imperceptible Micro-Geometric Perturbation
**arXiv**：[2602.01513v1](https://arxiv.org/abs/2602.01513) · [PDF](https://arxiv.org/pdf/2602.01513.pdf)  
**作者**：Xiaoxi Kong, Jieyu Yuan, Pengdi Chen, Yuanlin Zhang, Chongyi Li, Bin Li  

**一句话要点**：提出MarkCleaner框架，通过微几何扰动实现高保真水印去除，避免语义漂移。

**关键词**：水印去除, 微几何扰动, 语义内容保留, 2D高斯泼溅, 实时推理

## 3 点简述
- 核心问题：语义水印对传统图像攻击具有强鲁棒性，但微几何扰动可破坏相位对齐以去除水印。
- 方法要点：采用微几何扰动监督训练，结合掩码引导编码器和基于2D高斯泼溅的解码器，分离语义内容与空间对齐。
- 实验或效果：在去除效果和视觉保真度上表现优异，支持高效实时推理。

## 摘要（原文）

> Semantic watermarks exhibit strong robustness against conventional image-space attacks. In this work, we show that such robustness does not survive under micro-geometric perturbations: spatial displacements can remove watermarks by breaking the phase alignment. Motivated by this observation, we introduce MarkCleaner, a watermark removal framework that avoids semantic drift caused by regeneration-based watermark removal. Specifically, MarkCleaner is trained with micro-geometry-perturbed supervision, which encourages the model to separate semantic content from strict spatial alignment and enables robust reconstruction under subtle geometric displacements. The framework adopts a mask-guided encoder that learns explicit spatial representations and a 2D Gaussian Splatting-based decoder that explicitly parameterizes geometric perturbations while preserving semantic content. Extensive experiments demonstrate that MarkCleaner achieves superior performance in both watermark removal effectiveness and visual fidelity, while enabling efficient real-time inference. Our code will be made available upon acceptance.

