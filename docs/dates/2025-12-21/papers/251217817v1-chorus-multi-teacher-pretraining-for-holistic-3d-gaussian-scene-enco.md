---
layout: default
title: Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding
---

# Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding
**arXiv**：[2512.17817v1](https://arxiv.org/abs/2512.17817) · [PDF](https://arxiv.org/pdf/2512.17817.pdf)  
**作者**：Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  

**一句话要点**：提出Chorus多教师预训练框架，以从2D基础模型蒸馏互补信号，学习整体3D高斯场景编码器。

**关键词**：3D高斯场景编码, 多教师预训练, 知识蒸馏, 开放词汇分割, 点云迁移学习, 渲染蒸馏适应

## 3 点简述
- 核心问题：3D高斯场景表示缺乏从基元直接编码丰富通用特征的方法。
- 方法要点：使用共享3D编码器和教师特定投影器，从语言对齐、通用和对象感知教师蒸馏信号。
- 实验或效果：在开放词汇语义分割等任务中评估，并展示在点云基准上的强迁移能力。

## 摘要（原文）

> While 3DGS has emerged as a high-fidelity scene representation, encoding rich, general-purpose features directly from its primitives remains under-explored. We address this gap by introducing Chorus, a multi-teacher pretraining framework that learns a holistic feed-forward 3D Gaussian Splatting (3DGS) scene encoder by distilling complementary signals from 2D foundation models. Chorus employs a shared 3D encoder and teacher-specific projectors to learn from language-aligned, generalist, and object-aware teachers, encouraging a shared embedding space that captures signals from high-level semantics to fine-grained structure.
>   We evaluate Chorus on a wide range of tasks: open-vocabulary semantic and instance segmentation, linear and decoder probing, as well as data-efficient supervision. Besides 3DGS, we also test Chorus on several benchmarks that only support point clouds by pretraining a variant using only Gaussians' centers, colors, estimated normals as inputs. Interestingly, this encoder shows strong transfer and outperforms the point clouds baseline while using 39.9 times fewer training scenes. Finally, we propose a render-and-distill adaptation that facilitates out-of-domain finetuning. Our code and model will be released upon publication.

