---
layout: default
title: Fast Multi-Stack Slice-to-Volume Reconstruction via Multi-Scale Unrolled Optimization
---

# Fast Multi-Stack Slice-to-Volume Reconstruction via Multi-Scale Unrolled Optimization
**arXiv**：[2601.07519v1](https://arxiv.org/abs/2601.07519) · [PDF](https://arxiv.org/pdf/2601.07519.pdf)  
**作者**：Margherita Firenze, Sean I. Young, Clinton J. Wang, Hyuk Jin Yun, Elfar Adalsteinsson, Kiho Im, P. Ellen Grant, Polina Golland  

**一句话要点**：提出快速卷积框架，通过多尺度展开优化融合多正交2D切片堆栈以重建3D解剖结构并精调对齐。

**关键词**：切片到体积重建, 多尺度展开优化, 非刚性位移场, 胎儿脑MRI, 快速卷积框架

## 3 点简述
- 核心问题：切片到体积重建（SVR）中，从错位2D采集联合估计3D解剖和切片姿态的潜力未充分探索。
- 方法要点：结合全卷积网络学习多尺度表示，使用非刚性位移场表示变换，通过轻量级模型优化精调对齐。
- 实验或效果：应用于胎儿脑MRI，在10秒内重建高质量3D体积，对齐精度与最先进迭代SVR相当，速度快。

## 摘要（原文）

> Fully convolutional networks have become the backbone of modern medical imaging due to their ability to learn multi-scale representations and perform end-to-end inference. Yet their potential for slice-to-volume reconstruction (SVR), the task of jointly estimating 3D anatomy and slice poses from misaligned 2D acquisitions, remains underexplored. We introduce a fast convolutional framework that fuses multiple orthogonal 2D slice stacks to recover coherent 3D structure and refines slice alignment through lightweight model-based optimization. Applied to fetal brain MRI, our approach reconstructs high-quality 3D volumes in under 10s, with 1s slice registration and accuracy on par with state-of-the-art iterative SVR pipelines, offering more than speedup. The framework uses non-rigid displacement fields to represent transformations, generalizing to other SVR problems like fetal body and placental MRI. Additionally, the fast inference time paves the way for real-time, scanner-side volumetric feedback during MRI acquisition.

