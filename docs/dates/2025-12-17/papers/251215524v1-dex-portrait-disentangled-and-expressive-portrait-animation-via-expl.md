---
layout: default
title: DeX-Portrait: Disentangled and Expressive Portrait Animation via Explicit and Latent Motion Representations
---

# DeX-Portrait: Disentangled and Expressive Portrait Animation via Explicit and Latent Motion Representations
**arXiv**：[2512.15524v1](https://arxiv.org/abs/2512.15524) · [PDF](https://arxiv.org/pdf/2512.15524.pdf)  
**作者**：Yuxiang Shi, Zhe Li, Yanwen Wang, Hao Zhu, Xun Cao, Ligang Liu  

**一句话要点**：提出DeX-Portrait以解决肖像动画中头部姿态与面部表情解耦控制不足的问题。

**关键词**：肖像动画, 解耦控制, 扩散模型, 姿态表达分离, 条件生成, 身份一致性

## 3 点简述
- 核心问题：现有扩散模型难以实现头部姿态与面部表情的高保真解耦控制，限制编辑应用。
- 方法要点：通过显式全局变换表示姿态、隐式潜在码表示表情，结合双分支条件机制和交叉注意力注入。
- 实验或效果：在动画质量和解耦可控性上优于先进基线，支持身份一致性保持。

## 摘要（原文）

> Portrait animation from a single source image and a driving video is a long-standing problem. Recent approaches tend to adopt diffusion-based image/video generation models for realistic and expressive animation. However, none of these diffusion models realizes high-fidelity disentangled control between the head pose and facial expression, hindering applications like expression-only or pose-only editing and animation. To address this, we propose DeX-Portrait, a novel approach capable of generating expressive portrait animation driven by disentangled pose and expression signals. Specifically, we represent the pose as an explicit global transformation and the expression as an implicit latent code. First, we design a powerful motion trainer to learn both pose and expression encoders for extracting precise and decomposed driving signals. Then we propose to inject the pose transformation into the diffusion model through a dual-branch conditioning mechanism, and the expression latent through cross attention. Finally, we design a progressive hybrid classifier-free guidance for more faithful identity consistency. Experiments show that our method outperforms state-of-the-art baselines on both animation quality and disentangled controllability.

