---
layout: default
title: Make Some Noise: Unsupervised Remote Sensing Change Detection Using Latent Space Perturbations
---

# Make Some Noise: Unsupervised Remote Sensing Change Detection Using Latent Space Perturbations
**arXiv**：[2602.19881v1](https://arxiv.org/abs/2602.19881) · [PDF](https://arxiv.org/pdf/2602.19881.pdf)  
**作者**：Blaž Rolih, Matic Fučka, Filip Wolf, Luka Čehovin Zajc  

**一句话要点**：提出MaSoN框架，通过潜在空间扰动实现无监督遥感变化检测，提升泛化能力。

**关键词**：无监督变化检测, 遥感图像分析, 潜在空间扰动, 特征统计驱动, 多模态扩展

## 3 点简述
- 核心问题：现有方法依赖预定义假设，泛化能力有限，难以处理复杂变化类型。
- 方法要点：在训练中直接在潜在特征空间合成多样化变化，基于目标数据统计动态估计。
- 实验或效果：在五个基准测试中达到最先进性能，平均F1分数提升14.1个百分点。

## 摘要（原文）

> Unsupervised change detection (UCD) in remote sensing aims to localise semantic changes between two images of the same region without relying on labelled data during training. Most recent approaches rely either on frozen foundation models in a training-free manner or on training with synthetic changes generated in pixel space. Both strategies inherently rely on predefined assumptions about change types, typically introduced through handcrafted rules, external datasets, or auxiliary generative models. Due to these assumptions, such methods fail to generalise beyond a few change types, limiting their real-world usage, especially in rare or complex scenarios. To address this, we propose MaSoN (Make Some Noise), an end-to-end UCD framework that synthesises diverse changes directly in the latent feature space during training. It generates changes that are dynamically estimated using feature statistics of target data, enabling diverse yet data-driven variation aligned with the target domain. It also easily extends to new modalities, such as SAR. MaSoN generalises strongly across diverse change types and achieves state-of-the-art performance on five benchmarks, improving the average F1 score by 14.1 percentage points. Project page: https://blaz-r.github.io/mason_ucd

