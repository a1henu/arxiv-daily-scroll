---
layout: default
title: MUGSQA: Novel Multi-Uncertainty-Based Gaussian Splatting Quality Assessment Method, Dataset, and Benchmarks
---

# MUGSQA: Novel Multi-Uncertainty-Based Gaussian Splatting Quality Assessment Method, Dataset, and Benchmarks
**arXiv**：[2511.06830v1](https://arxiv.org/abs/2511.06830) · [PDF](https://arxiv.org/pdf/2511.06830.pdf)  
**作者**：Tianang Chen, Jian Jin, Shilv Cai, Zhuangzi Li, Weisi Lin  

**一句话要点**：提出多不确定性高斯泼溅质量评估方法、数据集和基准以解决3D重建质量评估挑战

**关键词**：高斯泼溅, 3D重建质量评估, 多不确定性, 主观质量评估, 数据集构建, 基准测试

## 3 点简述
- 核心问题：高斯泼溅3D重建方法的质量评估缺乏统一标准，难以比较不同变体。
- 方法要点：设计多距离主观质量评估方法，模拟人类观看行为，收集感知数据。
- 实验或效果：构建MUGSQA数据集和两个基准，评估重建方法鲁棒性和质量指标性能。

## 摘要（原文）

> Gaussian Splatting (GS) has recently emerged as a promising technique for 3D
> object reconstruction, delivering high-quality rendering results with
> significantly improved reconstruction speed. As variants continue to appear,
> assessing the perceptual quality of 3D objects reconstructed with different
> GS-based methods remains an open challenge. To address this issue, we first
> propose a unified multi-distance subjective quality assessment method that
> closely mimics human viewing behavior for objects reconstructed with GS-based
> methods in actual applications, thereby better collecting perceptual
> experiences. Based on it, we also construct a novel GS quality assessment
> dataset named MUGSQA, which is constructed considering multiple uncertainties
> of the input data. These uncertainties include the quantity and resolution of
> input views, the view distance, and the accuracy of the initial point cloud.
> Moreover, we construct two benchmarks: one to evaluate the robustness of
> various GS-based reconstruction methods under multiple uncertainties, and the
> other to evaluate the performance of existing quality assessment metrics. Our
> dataset and benchmark code will be released soon.

