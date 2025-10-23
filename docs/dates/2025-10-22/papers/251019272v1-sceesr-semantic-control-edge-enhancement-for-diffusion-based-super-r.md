---
layout: default
title: SCEESR: Semantic-Control Edge Enhancement for Diffusion-Based Super-Resolution
---

# SCEESR: Semantic-Control Edge Enhancement for Diffusion-Based Super-Resolution
**arXiv**：[2510.19272v1](https://arxiv.org/abs/2510.19272) · [PDF](https://arxiv.org/pdf/2510.19272.pdf)  
**作者**：Yun Kai Zhuang  

**一句话要点**：提出语义控制边缘增强框架以提升一步扩散超分辨率的几何精度与效率

**关键词**：图像超分辨率, 一步扩散模型, ControlNet, 边缘增强, 混合损失函数, 结构控制

## 3 点简述
- 真实图像超分辨率需处理复杂退化与重建模糊，生成模型在感知质量与计算成本间存在权衡
- 使用ControlNet机制集成边缘信息，在单步推理中提供动态结构控制，结合混合损失优化
- 实验表明方法有效提升结构完整性和真实感，保持一步生成效率，平衡输出质量与速度

## 摘要（原文）

> Real-world image super-resolution (Real-ISR) must handle complex degradations
> and inherent reconstruction ambiguities. While generative models have improved
> perceptual quality, a key trade-off remains with computational cost. One-step
> diffusion models offer speed but often produce structural inaccuracies due to
> distillation artifacts. To address this, we propose a novel SR framework that
> enhances a one-step diffusion model using a ControlNet mechanism for semantic
> edge guidance. This integrates edge information to provide dynamic structural
> control during single-pass inference. We also introduce a hybrid loss combining
> L2, LPIPS, and an edge-aware AME loss to optimize for pixel accuracy,
> perceptual quality, and geometric precision. Experiments show our method
> effectively improves structural integrity and realism while maintaining the
> efficiency of one-step generation, achieving a superior balance between output
> quality and inference speed. The results of test datasets will be published at
> https://drive.google.com/drive/folders/1amddXQ5orIyjbxHgGpzqFHZ6KTolinJF?usp=drive_link
> and the related code will be published at
> https://github.com/ARBEZ-ZEBRA/SCEESR.

