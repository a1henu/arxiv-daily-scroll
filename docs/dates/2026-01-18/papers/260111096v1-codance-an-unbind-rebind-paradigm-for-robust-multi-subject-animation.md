---
layout: default
title: CoDance: An Unbind-Rebind Paradigm for Robust Multi-Subject Animation
---

# CoDance: An Unbind-Rebind Paradigm for Robust Multi-Subject Animation
**arXiv**：[2601.11096v1](https://arxiv.org/abs/2601.11096) · [PDF](https://arxiv.org/pdf/2601.11096.pdf)  
**作者**：Shuai Tan, Biao Gong, Ke Ma, Yutong Feng, Qiyuan Zhang, Yan Wang, Yujun Shen, Hengshuang Zhao  

**一句话要点**：提出CoDance框架以解决多主体动画中空间绑定过强和运动重绑定不精确的问题

**关键词**：多主体动画, 解绑-重绑范式, 位置无关表示, 语义引导, 空间错位处理, CoDanceBench

## 3 点简述
- 现有方法因空间绑定过强，难以处理任意主体数量、类型和空间错位
- CoDance采用解绑-重绑范式，通过扰动学习位置无关运动表示，并利用语义和空间引导重绑定
- 在CoDanceBench和现有数据集上实现SOTA性能，展现跨主体和布局的泛化能力

## 摘要（原文）

> Character image animation is gaining significant importance across various domains, driven by the demand for robust and flexible multi-subject rendering. While existing methods excel in single-person animation, they struggle to handle arbitrary subject counts, diverse character types, and spatial misalignment between the reference image and the driving poses. We attribute these limitations to an overly rigid spatial binding that forces strict pixel-wise alignment between the pose and reference, and an inability to consistently rebind motion to intended subjects. To address these challenges, we propose CoDance, a novel Unbind-Rebind framework that enables the animation of arbitrary subject counts, types, and spatial configurations conditioned on a single, potentially misaligned pose sequence. Specifically, the Unbind module employs a novel pose shift encoder to break the rigid spatial binding between the pose and the reference by introducing stochastic perturbations to both poses and their latent features, thereby compelling the model to learn a location-agnostic motion representation. To ensure precise control and subject association, we then devise a Rebind module, leveraging semantic guidance from text prompts and spatial guidance from subject masks to direct the learned motion to intended characters. Furthermore, to facilitate comprehensive evaluation, we introduce a new multi-subject CoDanceBench. Extensive experiments on CoDanceBench and existing datasets show that CoDance achieves SOTA performance, exhibiting remarkable generalization across diverse subjects and spatial layouts. The code and weights will be open-sourced.

