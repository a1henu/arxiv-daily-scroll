---
layout: default
title: Semantics and Content Matter: Towards Multi-Prior Hierarchical Mamba for Image Deraining
---

# Semantics and Content Matter: Towards Multi-Prior Hierarchical Mamba for Image Deraining
**arXiv**：[2511.13113v1](https://arxiv.org/abs/2511.13113) · [PDF](https://arxiv.org/pdf/2511.13113.pdf)  
**作者**：Zhaocheng Yu, Kui Jiang, Junjun Jiang, Xianming Liu, Guanglu Sun, Yi Xiao  

**一句话要点**：提出多先验分层Mamba网络以解决图像去雨中的语义和空间细节保真问题

**关键词**：图像去雨, 多先验融合, 分层Mamba网络, 语义引导, 结构先验, 渐进融合注入

## 3 点简述
- 核心问题：现有去雨方法在语义和空间细节保真方面表现不足，影响自动驾驶等应用性能。
- 方法要点：融合CLIP语义先验和DINOv2结构先验，通过渐进融合注入和分层Mamba模块增强特征表示。
- 实验或效果：在Rain200H数据集上PSNR提升0.57 dB，并在真实雨天场景中表现出优越泛化能力。

## 摘要（原文）

> Rain significantly degrades the performance of computer vision systems, particularly in applications like autonomous driving and video surveillance. While existing deraining methods have made considerable progress, they often struggle with fidelity of semantic and spatial details. To address these limitations, we propose the Multi-Prior Hierarchical Mamba (MPHM) network for image deraining. This novel architecture synergistically integrates macro-semantic textual priors (CLIP) for task-level semantic guidance and micro-structural visual priors (DINOv2) for scene-aware structural information. To alleviate potential conflicts between heterogeneous priors, we devise a progressive Priors Fusion Injection (PFI) that strategically injects complementary cues at different decoder levels. Meanwhile, we equip the backbone network with an elaborate Hierarchical Mamba Module (HMM) to facilitate robust feature representation, featuring a Fourier-enhanced dual-path design that concurrently addresses global context modeling and local detail recovery. Comprehensive experiments demonstrate MPHM's state-of-the-art performance, achieving a 0.57 dB PSNR gain on the Rain200H dataset while delivering superior generalization on real-world rainy scenarios.

