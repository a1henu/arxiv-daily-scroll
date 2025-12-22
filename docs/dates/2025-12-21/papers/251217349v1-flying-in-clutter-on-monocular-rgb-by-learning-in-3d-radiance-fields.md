---
layout: default
title: Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation
---

# Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation
**arXiv**：[2512.17349v1](https://arxiv.org/abs/2512.17349) · [PDF](https://arxiv.org/pdf/2512.17349.pdf)  
**作者**：Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  

**一句话要点**：提出基于3D高斯溅射与对抗域适应的框架，实现单目RGB图像在杂乱环境中的零样本飞行导航。

**关键词**：单目视觉导航, 3D高斯溅射, 域适应, 零样本转移, 飞行机器人

## 3 点简述
- 核心问题：单目RGB图像能否支持飞行机器人在杂乱环境中导航，克服仿真到现实的感知差距。
- 方法要点：结合3D高斯溅射的高保真仿真与对抗域适应，训练策略以依赖域不变特征。
- 实验或效果：策略在物理世界中实现零样本转移，在多变光照下实现安全敏捷飞行。

## 摘要（原文）

> Modern autonomous navigation systems predominantly rely on lidar and depth cameras. However, a fundamental question remains: Can flying robots navigate in clutter using solely monocular RGB images? Given the prohibitive costs of real-world data collection, learning policies in simulation offers a promising path. Yet, deploying such policies directly in the physical world is hindered by the significant sim-to-real perception gap. Thus, we propose a framework that couples the photorealism of 3D Gaussian Splatting (3DGS) environments with Adversarial Domain Adaptation. By training in high-fidelity simulation while explicitly minimizing feature discrepancy, our method ensures the policy relies on domain-invariant cues. Experimental results demonstrate that our policy achieves robust zero-shot transfer to the physical world, enabling safe and agile flight in unstructured environments with varying illumination.

