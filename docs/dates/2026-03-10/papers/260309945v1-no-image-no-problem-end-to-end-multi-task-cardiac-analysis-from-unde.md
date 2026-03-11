---
layout: default
title: No Image, No Problem: End-to-End Multi-Task Cardiac Analysis from Undersampled k-Space
---

# No Image, No Problem: End-to-End Multi-Task Cardiac Analysis from Undersampled k-Space
**arXiv**：[2603.09945v1](https://arxiv.org/abs/2603.09945) · [PDF](https://arxiv.org/pdf/2603.09945.pdf)  
**作者**：Yundi Zhang, Sevgi Gokce Kafali, Niklas Bubeck, Daniel Rueckert, Jiazhen Pan  

**一句话要点**：提出k-MTR框架，直接从欠采样k空间进行多任务心脏分析，避免传统重建-分析流程的瓶颈。

**关键词**：心脏MRI, k空间表示学习, 多任务学习, 欠采样重建, 潜在空间对齐, 医学图像分析

## 3 点简述
- 核心问题：传统心脏MRI流程依赖图像重建，导致欠采样引入伪影和信息瓶颈，影响诊断效率。
- 方法要点：k-MTR通过潜在空间对齐欠采样k空间与全采样图像，直接学习语义表示，绕过显式逆问题。
- 实验或效果：在大规模模拟数据上验证，k-MTR在回归、分类和分割任务中达到与图像域基线竞争的性能。

## 摘要（原文）

> Conventional clinical CMR pipelines rely on a sequential "reconstruct-then-analyze" paradigm, forcing an ill-posed intermediate step that introduces avoidable artifacts and information bottlenecks. This creates a fundamental mathematical paradox: it attempts to recover high-dimensional pixel arrays (i.e., images) from undersampled k-space, rather than directly extracting the low-dimensional physiological labels actually required for diagnosis. To unlock the direct diagnostic potential of k-space, we propose k-MTR (k-space Multi-Task Representation), a k-space representation learning framework that aligns undersampled k-space data and fully-sampled images into a shared semantic manifold. Leveraging a large-scale controlled simulation of 42,000 subjects, k-MTR forces the k-space encoder to restore anatomical information lost to undersampling directly within the latent space, bypassing the explicit inverse problem for downstream analysis. We demonstrate that this latent alignment enables the dense latent space embedded with high-level physiological semantics directly from undersampled frequencies. Across continuous phenotype regression, disease classification, and anatomical segmentation, k-MTR achieves highly competitive performance against state-of-the-art image-domain baselines. By showcasing that precise spatial geometries and multi-task features can be successfully recovered directly from the k-space representations, k-MTR provides a robust architectural blueprint for task-aware cardiac MRI workflows.

