---
layout: default
title: Rethinking Metrics and Diffusion Architecture for 3D Point Cloud Generation
---

# Rethinking Metrics and Diffusion Architecture for 3D Point Cloud Generation
**arXiv**：[2511.05308v1](https://arxiv.org/abs/2511.05308) · [PDF](https://arxiv.org/pdf/2511.05308.pdf)  
**作者**：Matteo Bastico, David Ryckelynck, Laurent Corté, Yannick Tillier, Etienne Decencière  

**一句话要点**：提出新指标与扩散变换器架构以改进3D点云生成评估与质量

**关键词**：3D点云生成, 生成模型评估, 扩散模型, 变换器架构, 点云指标

## 3 点简述
- 核心问题：常用指标如Chamfer距离缺乏鲁棒性，无法准确评估几何保真度。
- 方法要点：引入样本对齐、DCD和新指标SNC，结合扩散变换器生成高质量点云。
- 实验或效果：在ShapeNet上实验，模型性能超越先前方法，达到新SOTA。

## 摘要（原文）

> As 3D point clouds become a cornerstone of modern technology, the need for
> sophisticated generative models and reliable evaluation metrics has grown
> exponentially. In this work, we first expose that some commonly used metrics
> for evaluating generated point clouds, particularly those based on Chamfer
> Distance (CD), lack robustness against defects and fail to capture geometric
> fidelity and local shape consistency when used as quality indicators. We
> further show that introducing samples alignment prior to distance calculation
> and replacing CD with Density-Aware Chamfer Distance (DCD) are simple yet
> essential steps to ensure the consistency and robustness of point cloud
> generative model evaluation metrics. While existing metrics primarily focus on
> directly comparing 3D Euclidean coordinates, we present a novel metric, named
> Surface Normal Concordance (SNC), which approximates surface similarity by
> comparing estimated point normals. This new metric, when combined with
> traditional ones, provides a more comprehensive evaluation of the quality of
> generated samples. Finally, leveraging recent advancements in transformer-based
> models for point cloud analysis, such as serialized patch attention , we
> propose a new architecture for generating high-fidelity 3D structures, the
> Diffusion Point Transformer. We perform extensive experiments and comparisons
> on the ShapeNet dataset, showing that our model outperforms previous solutions,
> particularly in terms of quality of generated point clouds, achieving new
> state-of-the-art. Code available at
> https://github.com/matteo-bastico/DiffusionPointTransformer.

