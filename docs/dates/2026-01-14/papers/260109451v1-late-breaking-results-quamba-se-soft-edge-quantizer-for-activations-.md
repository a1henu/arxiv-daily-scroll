---
layout: default
title: Late Breaking Results: Quamba-SE: Soft-edge Quantizer for Activations in State Space Models
---

# Late Breaking Results: Quamba-SE: Soft-edge Quantizer for Activations in State Space Models
**arXiv**：[2601.09451v1](https://arxiv.org/abs/2601.09451) · [PDF](https://arxiv.org/pdf/2601.09451.pdf)  
**作者**：Yizhi Chen, Ahmed Hemani  

**一句话要点**：提出Quamba-SE软边量化器，用于状态空间模型激活量化，通过自适应尺度保留异常值信息。

**关键词**：状态空间模型, 激活量化, 软边量化, 自适应尺度, 异常值处理, 零样本基准测试

## 3 点简述
- 核心问题：现有INT8量化方法硬裁剪异常值，导致状态空间模型激活信息丢失。
- 方法要点：使用三个自适应尺度：高精度处理小值、标准尺度处理正常值、低精度处理异常值。
- 实验或效果：在Mamba-130M模型上评估，6个零样本基准测试中平均准确率提升达0.83%。

## 摘要（原文）

> We propose Quamba-SE, a soft-edge quantizer for State Space Model (SSM) activation quantization. Unlike existing methods, using standard INT8 operation, Quamba-SE employs three adaptive scales: high-precision for small values, standard scale for normal values, and low-precision for outliers. This preserves outlier information instead of hard clipping, while maintaining precision for other values. We evaluate on Mamba- 130M across 6 zero-shot benchmarks. Results show that Quamba- SE consistently outperforms Quamba, achieving up to +2.68% on individual benchmarks and up to +0.83% improvement in the average accuracy of 6 datasets.

