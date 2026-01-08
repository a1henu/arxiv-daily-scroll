---
layout: default
title: Beyond Physical Labels: Redefining Domains for Robust WiFi-based Gesture Recognition
---

# Beyond Physical Labels: Redefining Domains for Robust WiFi-based Gesture Recognition
**arXiv**：[2601.03825v1](https://arxiv.org/abs/2601.03825) · [PDF](https://arxiv.org/pdf/2601.03825.pdf)  
**作者**：Xiang Zhang, Huan Yan, Jinyang Huang, Bin Liu, Yuanhao Feng, Jianchun Liu, Meng Li, Fusang Zhang, Zhi Liu  

**一句话要点**：提出GesFi系统，通过WiFi潜在域挖掘提升基于WiFi的手势识别跨域鲁棒性

**关键词**：WiFi手势识别, 潜在域挖掘, 对抗学习, 跨域泛化, 鲁棒性增强

## 3 点简述
- 核心问题：基于WiFi的手势识别面临分布偏移，传统物理标签不足以支持跨域泛化
- 方法要点：使用类对抗学习和无监督聚类挖掘潜在域，并通过对抗学习对齐以增强鲁棒性
- 实验或效果：在单对和多对设置下评估，GesFi在跨域任务中优于现有方法，性能提升最高达78%

## 摘要（原文）

> In this paper, we propose GesFi, a novel WiFi-based gesture recognition system that introduces WiFi latent domain mining to redefine domains directly from the data itself. GesFi first processes raw sensing data collected from WiFi receivers using CSI-ratio denoising, Short-Time Fast Fourier Transform, and visualization techniques to generate standardized input representations. It then employs class-wise adversarial learning to suppress gesture semantic and leverages unsupervised clustering to automatically uncover latent domain factors responsible for distributional shifts. These latent domains are then aligned through adversarial learning to support robust cross-domain generalization. Finally, the system is applied to the target environment for robust gesture inference. We deployed GesFi under both single-pair and multi-pair settings using commodity WiFi transceivers, and evaluated it across multiple public datasets and real-world environments. Compared to state-of-the-art baselines, GesFi achieves up to 78% and 50% performance improvements over existing adversarial methods, and consistently outperforms prior generalization approaches across most cross-domain tasks.

