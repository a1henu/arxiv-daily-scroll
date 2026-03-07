---
layout: default
title: Beyond the Patch: Exploring Vulnerabilities of Visuomotor Policies via Viewpoint-Consistent 3D Adversarial Object
---

# Beyond the Patch: Exploring Vulnerabilities of Visuomotor Policies via Viewpoint-Consistent 3D Adversarial Object
**arXiv**：[2603.04913v1](https://arxiv.org/abs/2603.04913) · [PDF](https://arxiv.org/pdf/2603.04913.pdf)  
**作者**：Chanmi Lee, Minsung Yoon, Woojae Kim, Sebin Lee, Sung-eui Yoon  

**一句话要点**：提出基于可微分渲染的视点一致3D对抗纹理优化方法，以增强移动相机下机器人视觉运动策略的鲁棒性。

**关键词**：视觉运动策略, 3D对抗攻击, 可微分渲染, 视点一致性, 机器人操纵

## 3 点简述
- 核心问题：传统2D对抗补丁在动态视点下因透视失真而失效，需探索3D对象的潜在漏洞。
- 方法要点：采用EOT与C2F课程，结合距离相关频率特性和显著性引导扰动，优化对抗纹理。
- 实验或效果：方法在多种环境条件下有效，并验证了黑盒可迁移性和实际应用性。

## 摘要（原文）

> Neural network-based visuomotor policies enable robots to perform manipulation tasks but remain susceptible to perceptual attacks. For example, conventional 2D adversarial patches are effective under fixed-camera setups, where appearance is relatively consistent; however, their efficacy often diminishes under dynamic viewpoints from moving cameras, such as wrist-mounted setups, due to perspective distortions. To proactively investigate potential vulnerabilities beyond 2D patches, this work proposes a viewpoint-consistent adversarial texture optimization method for 3D objects through differentiable rendering. As optimization strategies, we employ Expectation over Transformation (EOT) with a Coarse-to-Fine (C2F) curriculum, exploiting distance-dependent frequency characteristics to induce textures effective across varying camera-object distances. We further integrate saliency-guided perturbations to redirect policy attention and design a targeted loss that persistently drives robots toward adversarial objects. Our comprehensive experiments show that the proposed method is effective under various environmental conditions, while confirming its black-box transferability and real-world applicability.

