---
layout: default
title: Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists
---

# Speeding Up the Learning of 3D Gaussians with Much Shorter Gaussian Lists
**arXiv**：[2603.09277v1](https://arxiv.org/abs/2603.09277) · [PDF](https://arxiv.org/pdf/2603.09277.pdf)  
**作者**：Jiaqi Liu, Zhizhong Han  

**一句话要点**：提出缩短高斯列表的训练策略与损失函数，以加速3D高斯溅射学习

**关键词**：3D高斯溅射, 渲染加速, 训练策略, 熵约束, 分辨率调度

## 3 点简述
- 核心问题：3D高斯溅射学习效率有待提升，高斯列表过长影响渲染速度
- 方法要点：通过重置高斯尺度缩小覆盖范围，引入熵约束锐化权重分布，缩短像素高斯列表
- 实验或效果：在基准测试中，效率显著优于现有方法，且未牺牲渲染质量

## 摘要（原文）

> 3D Gaussian splatting (3DGS) has become a vital tool for learning a radiance field from multiple posed images. Although 3DGS shows great advantages over NeRF in terms of rendering quality and efficiency, it remains a research challenge to further improve the efficiency of learning 3D Gaussians. To overcome this challenge, we propose novel training strategies and losses to shorten each Gaussian list used to render a pixel, which speeds up the splatting by involving fewer Gaussians along a ray. Specifically, we shrink the size of each Gaussian by resetting their scales regularly, encouraging smaller Gaussians to cover fewer nearby pixels, which shortens the Gaussian lists of pixels. Additionally, we introduce an entropy constraint on the alpha blending procedure to sharpen the weight distribution of Gaussians along each ray, which drives dominant weights larger while making minor weights smaller. As a result, each Gaussian becomes more focused on the pixels where it is dominant, which reduces its impact on nearby pixels, leading to even shorter Gaussian lists. Eventually, we integrate our method into a rendering resolution scheduler which further improves efficiency through progressive resolution increase. We evaluate our method by comparing it with state-of-the-art methods on widely used benchmarks. Our results show significant advantages over others in efficiency without sacrificing rendering quality.

