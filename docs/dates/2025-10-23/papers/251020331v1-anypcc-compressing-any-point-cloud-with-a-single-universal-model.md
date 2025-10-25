---
layout: default
title: AnyPcc: Compressing Any Point Cloud with a Single Universal Model
---

# AnyPcc: Compressing Any Point Cloud with a Single Universal Model
**arXiv**：[2510.20331v1](https://arxiv.org/abs/2510.20331) · [PDF](https://arxiv.org/pdf/2510.20331.pdf)  
**作者**：Kangli Wang, Qianxi Yi, Yuqi Ye, Shihao Li, Wei Gao  

**一句话要点**：提出AnyPcc通用模型以解决点云压缩中的泛化与OOD数据处理问题

**关键词**：点云压缩, 通用上下文模型, 实例自适应微调, OOD数据处理, 几何压缩

## 3 点简述
- 核心问题：点云压缩中泛化能力不足，源于上下文模型不鲁棒和OOD数据低效处理
- 方法要点：使用通用上下文模型捕获空间和通道依赖，结合实例自适应微调策略
- 实验或效果：在15个数据集上验证，实现点云压缩新最优性能，代码将开源

## 摘要（原文）

> Generalization remains a critical challenge for deep learning-based point
> cloud geometry compression. We argue this stems from two key limitations: the
> lack of robust context models and the inefficient handling of
> out-of-distribution (OOD) data. To address both, we introduce AnyPcc, a
> universal point cloud compression framework. AnyPcc first employs a Universal
> Context Model that leverages priors from both spatial and channel-wise grouping
> to capture robust contextual dependencies. Second, our novel Instance-Adaptive
> Fine-Tuning (IAFT) strategy tackles OOD data by synergizing explicit and
> implicit compression paradigms. It fine-tunes a small subset of network weights
> for each instance and incorporates them into the bitstream, where the marginal
> bit cost of the weights is dwarfed by the resulting savings in geometry
> compression. Extensive experiments on a benchmark of 15 diverse datasets
> confirm that AnyPcc sets a new state-of-the-art in point cloud compression. Our
> code and datasets will be released to encourage reproducible research.

