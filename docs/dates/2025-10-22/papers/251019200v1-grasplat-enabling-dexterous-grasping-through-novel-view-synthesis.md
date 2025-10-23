---
layout: default
title: GRASPLAT: Enabling dexterous grasping through novel view synthesis
---

# GRASPLAT: Enabling dexterous grasping through novel view synthesis
**arXiv**：[2510.19200v1](https://arxiv.org/abs/2510.19200) · [PDF](https://arxiv.org/pdf/2510.19200.pdf)  
**作者**：Matteo Bortolon, Nuno Ferreira Duarte, Plinio Moreno, Fabio Poiesi, José Santos-Victor, Alessio Del Bue  

**一句话要点**：提出GRASPLAT框架，通过新视角合成实现灵巧抓取

**关键词**：灵巧抓取, 新视角合成, 3D高斯泼溅, 光度损失, 机器人抓取, RGB图像训练

## 3 点简述
- 核心问题：多指手灵巧抓取依赖完整3D扫描，但真实场景中获取高质量3D数据困难。
- 方法要点：利用3D高斯泼溅合成手-物体交互图像，通过光度损失优化抓取预测。
- 实验或效果：在合成和真实数据集上，抓取成功率比现有图像方法提升高达36.9%。

## 摘要（原文）

> Achieving dexterous robotic grasping with multi-fingered hands remains a
> significant challenge. While existing methods rely on complete 3D scans to
> predict grasp poses, these approaches face limitations due to the difficulty of
> acquiring high-quality 3D data in real-world scenarios. In this paper, we
> introduce GRASPLAT, a novel grasping framework that leverages consistent 3D
> information while being trained solely on RGB images. Our key insight is that
> by synthesizing physically plausible images of a hand grasping an object, we
> can regress the corresponding hand joints for a successful grasp. To achieve
> this, we utilize 3D Gaussian Splatting to generate high-fidelity novel views of
> real hand-object interactions, enabling end-to-end training with RGB data.
> Unlike prior methods, our approach incorporates a photometric loss that refines
> grasp predictions by minimizing discrepancies between rendered and real images.
> We conduct extensive experiments on both synthetic and real-world grasping
> datasets, demonstrating that GRASPLAT improves grasp success rates up to 36.9%
> over existing image-based methods. Project page:
> https://mbortolon97.github.io/grasplat/

