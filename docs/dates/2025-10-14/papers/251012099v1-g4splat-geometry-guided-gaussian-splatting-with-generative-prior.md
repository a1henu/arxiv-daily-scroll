---
layout: default
title: G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior
---

# G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior
**arXiv**：[2510.12099v1](https://arxiv.org/abs/2510.12099) · [PDF](https://arxiv.org/pdf/2510.12099.pdf)  
**作者**：Junfeng Ni, Yixin Chen, Zhifei Yang, Yu Liu, Ruijie Lu, Song-Chun Zhu, Siyuan Huang  

**一句话要点**：提出几何引导的高斯泼溅方法，利用生成先验增强3D场景重建

**关键词**：3D场景重建, 高斯泼溅, 生成先验, 几何指导, 多视图一致性, 深度估计

## 3 点简述
- 现有方法缺乏可靠几何监督，导致重建质量差和多视图不一致
- 利用平面结构获取精确深度图，并整合几何指导以改进可见性掩码和视图选择
- 在多个数据集上实验，几何和外观重建优于基线，支持单视图和无位姿视频输入

## 摘要（原文）

> Despite recent advances in leveraging generative prior from pre-trained
> diffusion models for 3D scene reconstruction, existing methods still face two
> critical limitations. First, due to the lack of reliable geometric supervision,
> they struggle to produce high-quality reconstructions even in observed regions,
> let alone in unobserved areas. Second, they lack effective mechanisms to
> mitigate multi-view inconsistencies in the generated images, leading to severe
> shape-appearance ambiguities and degraded scene geometry. In this paper, we
> identify accurate geometry as the fundamental prerequisite for effectively
> exploiting generative models to enhance 3D scene reconstruction. We first
> propose to leverage the prevalence of planar structures to derive accurate
> metric-scale depth maps, providing reliable supervision in both observed and
> unobserved regions. Furthermore, we incorporate this geometry guidance
> throughout the generative pipeline to improve visibility mask estimation, guide
> novel view selection, and enhance multi-view consistency when inpainting with
> video diffusion models, resulting in accurate and consistent scene completion.
> Extensive experiments on Replica, ScanNet++, and DeepBlending show that our
> method consistently outperforms existing baselines in both geometry and
> appearance reconstruction, particularly for unobserved regions. Moreover, our
> method naturally supports single-view inputs and unposed videos, with strong
> generalizability in both indoor and outdoor scenarios with practical real-world
> applicability. The project page is available at
> https://dali-jack.github.io/g4splat-web/.

