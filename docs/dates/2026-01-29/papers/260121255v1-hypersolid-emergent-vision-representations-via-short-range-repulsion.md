---
layout: default
title: Hypersolid: Emergent Vision Representations via Short-Range Repulsion
---

# Hypersolid: Emergent Vision Representations via Short-Range Repulsion
**arXiv**：[2601.21255v1](https://arxiv.org/abs/2601.21255) · [PDF](https://arxiv.org/pdf/2601.21255.pdf)  
**作者**：Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo  

**一句话要点**：提出Hypersolid方法，通过短程硬球排斥防止表示崩溃，提升细粒度和低分辨率分类任务性能。

**关键词**：自监督学习, 表示崩溃, 短程排斥, 离散填充, 细粒度分类, 低分辨率分类

## 3 点简述
- 核心问题：自监督学习中防止表示崩溃的挑战，现有方法依赖全局正则化。
- 方法要点：将表示学习重新解释为离散填充问题，使用短程硬球排斥避免局部碰撞。
- 实验或效果：在高分离几何机制下保持增强多样性，在细粒度和低分辨率分类任务中表现优异。

## 摘要（原文）

> A recurring challenge in self-supervised learning is preventing representation collapse. Existing solutions typically rely on global regularization, such as maximizing distances, decorrelating dimensions or enforcing certain distributions. We instead reinterpret representation learning as a discrete packing problem, where preserving information simplifies to maintaining injectivity. We operationalize this in Hypersolid, a method using short-range hard-ball repulsion to prevent local collisions. This constraint results in a high-separation geometric regime that preserves augmentation diversity, excelling on fine-grained and low-resolution classification tasks.

