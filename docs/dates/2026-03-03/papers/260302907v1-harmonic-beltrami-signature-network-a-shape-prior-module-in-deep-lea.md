---
layout: default
title: Harmonic Beltrami Signature Network: a Shape Prior Module in Deep Learning Framework
---

# Harmonic Beltrami Signature Network: a Shape Prior Module in Deep Learning Framework
**arXiv**：[2603.02907v1](https://arxiv.org/abs/2603.02907) · [PDF](https://arxiv.org/pdf/2603.02907.pdf)  
**作者**：Chenran Lin, Lok Ming Lui  

**一句话要点**：提出Harmonic Beltrami Signature Network以嵌入形状先验信息于深度学习分割模型

**关键词**：形状表示, 深度学习架构, 图像分割, 几何形状嵌入, Harmonic Beltrami Signature

## 3 点简述
- 核心问题：如何高效提取并利用形状先验信息以提升计算机视觉任务性能
- 方法要点：结合预/后空间变换网络与UNet架构，计算具有平移、缩放和旋转不变性的Harmonic Beltrami Signature
- 实验或效果：HBSN能准确计算复杂形状的表示，并作为通用模块提升现有分割模型性能

## 摘要（原文）

> This paper presents the Harmonic Beltrami Signature Network (HBSN), a novel deep learning architecture for computing the Harmonic Beltrami Signature (HBS) from binary-like images. HBS is a shape representation that provides a one-to-one correspondence with 2D simply connected shapes, with invariance to translation, scaling, and rotation. By exploiting the function approximation capacity of neural networks, HBSN enables efficient extraction and utilization of shape prior information. The proposed network architecture incorporates a pre-Spatial Transformer Network (pre-STN) for shape normalization, a UNet-based backbone for HBS prediction, and a post-STN for angle regularization. Experiments show that HBSN accurately computes HBS representations, even for complex shapes. Furthermore, we demonstrate how HBSN can be directly incorporated into existing deep learning segmentation models, improving their performance through the use of shape priors. The results confirm the utility of HBSN as a general-purpose module for embedding geometric shape information into computer vision pipelines.

