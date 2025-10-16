---
layout: default
title: No-Reference Rendered Video Quality Assessment: Dataset and Metrics
---

# No-Reference Rendered Video Quality Assessment: Dataset and Metrics
**arXiv**：[2510.13349v1](https://arxiv.org/abs/2510.13349) · [PDF](https://arxiv.org/pdf/2510.13349.pdf)  
**作者**：Sipeng Yang, Jiayu Ji, Qingchuan Zhu, Zhiyao Yang, Xiaogang Jin  

**一句话要点**：提出无参考渲染视频质量评估数据集与指标，以解决渲染视频中时间伪影问题。

**关键词**：无参考视频质量评估, 渲染视频, 时间伪影, 主观质量标注, 实时渲染, 超采样方法

## 3 点简述
- 核心问题：现有无参考视频质量评估方法对相机视频有偏，不适用于渲染视频。
- 方法要点：构建大规模渲染视频数据集，并设计结合图像质量和时间稳定性的评估指标。
- 实验或效果：新指标在渲染视频上优于现有方法，并用于超采样和帧生成策略评估。

## 摘要（原文）

> Quality assessment of videos is crucial for many computer graphics
> applications, including video games, virtual reality, and augmented reality,
> where visual performance has a significant impact on user experience. When test
> videos cannot be perfectly aligned with references or when references are
> unavailable, the significance of no-reference video quality assessment (NR-VQA)
> methods is undeniable. However, existing NR-VQA datasets and metrics are
> primarily focused on camera-captured videos; applying them directly to rendered
> videos would result in biased predictions, as rendered videos are more prone to
> temporal artifacts. To address this, we present a large rendering-oriented
> video dataset with subjective quality annotations, as well as a designed NR-VQA
> metric specific to rendered videos. The proposed dataset includes a wide range
> of 3D scenes and rendering settings, with quality scores annotated for various
> display types to better reflect real-world application scenarios. Building on
> this dataset, we calibrate our NR-VQA metric to assess rendered video quality
> by looking at both image quality and temporal stability. We compare our metric
> to existing NR-VQA metrics, demonstrating its superior performance on rendered
> videos. Finally, we demonstrate that our metric can be used to benchmark
> supersampling methods and assess frame generation strategies in real-time
> rendering.

