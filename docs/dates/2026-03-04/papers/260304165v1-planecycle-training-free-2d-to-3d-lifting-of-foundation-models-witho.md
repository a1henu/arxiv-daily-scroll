---
layout: default
title: PlaneCycle: Training-Free 2D-to-3D Lifting of Foundation Models Without Adapters
---

# PlaneCycle: Training-Free 2D-to-3D Lifting of Foundation Models Without Adapters
**arXiv**：[2603.04165v1](https://arxiv.org/abs/2603.04165) · [PDF](https://arxiv.org/pdf/2603.04165.pdf)  
**作者**：Yinghong Yu, Guangyuan Li, Jiancheng Yang  

**一句话要点**：提出PlaneCycle训练免费算子，实现基础模型从2D到3D的无适配器提升

**关键词**：2D到3D提升, 训练免费算子, 基础模型扩展, 3D视觉, 无参数方法, 架构无关

## 3 点简述
- 核心问题：2D基础模型扩展至3D通常需重训练或适配器，增加成本与复杂性
- 方法要点：通过循环聚合正交平面，重用预训练2D骨干，实现渐进式3D融合，无额外参数
- 实验或效果：在3D分类与分割基准上，无训练下超越2D基线，接近全训练模型性能

## 摘要（原文）

> Large-scale 2D foundation models exhibit strong transferable representations, yet extending them to 3D volumetric data typically requires retraining, adapters, or architectural redesign. We introduce PlaneCycle, a training-free, adapter-free operator for architecture-agnostic 2D-to-3D lifting of foundation models. PlaneCycle reuses the original pretrained 2D backbone by cyclically distributing spatial aggregation across orthogonal HW, DW, and DH planes throughout network depth, enabling progressive 3D fusion while preserving pretrained inductive biases. The method introduces no additional parameters and is applicable to arbitrary 2D networks. Using pretrained DINOv3 models, we evaluate PlaneCycle on six 3D classification and three 3D segmentation benchmarks. Without any training, the lifted models exhibit intrinsic 3D fusion capability and, under linear probing, outperform slice-wise 2D baselines and strong 3D counterparts, approaching the performance of fully trained models. With full fine-tuning, PlaneCycle matches standard 3D architectures, highlighting its potential as a seamless and practical 2D-to-3D lifting operator. These results demonstrate that 3D capability can be unlocked from pretrained 2D foundation models without structural modification or retraining. Code is available at https://github.com/HINTLab/PlaneCycle.

