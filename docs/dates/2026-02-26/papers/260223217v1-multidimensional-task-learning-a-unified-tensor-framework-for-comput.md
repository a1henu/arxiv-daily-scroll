---
layout: default
title: Multidimensional Task Learning: A Unified Tensor Framework for Computer Vision Tasks
---

# Multidimensional Task Learning: A Unified Tensor Framework for Computer Vision Tasks
**arXiv**：[2602.23217v1](https://arxiv.org/abs/2602.23217) · [PDF](https://arxiv.org/pdf/2602.23217.pdf)  
**作者**：Alaa El Ichi, Khalide Jbilou  

**一句话要点**：提出多维任务学习统一张量框架，以解决计算机视觉任务中矩阵约束导致的表达限制问题。

**关键词**：多维任务学习, 张量框架, 广义爱因斯坦MLPs, 计算机视觉任务统一, 维度控制, 任务空间扩展

## 3 点简述
- 核心问题：当前计算机视觉任务受矩阵思维约束，需结构扁平化，限制自然可表达任务空间。
- 方法要点：基于广义爱因斯坦MLPs，使用张量参数直接操作，控制维度保留或收缩，避免信息损失。
- 实验或效果：证明分类、分割和检测是MTL特例，任务空间大于矩阵方法，支持时空或跨模态预测。

## 摘要（原文）

> This paper introduces Multidimensional Task Learning (MTL), a unified mathematical framework based on Generalized Einstein MLPs (GE-MLPs) that operate directly on tensors via the Einstein product. We argue that current computer vision task formulations are inherently constrained by matrix-based thinking: standard architectures rely on matrix-valued weights and vectorvalued biases, requiring structural flattening that restricts the space of naturally expressible tasks. GE-MLPs lift this constraint by operating with tensor-valued parameters, enabling explicit control over which dimensions are preserved or contracted without information loss. Through rigorous mathematical derivations, we demonstrate that classification, segmentation, and detection are special cases of MTL, differing only in their dimensional configuration within a formally defined task space. We further prove that this task space is strictly larger than what matrix-based formulations can natively express, enabling principled task configurations such as spatiotemporal or cross modal predictions that require destructive flattening under conventional approaches. This work provides a mathematical foundation for understanding, comparing, and designing computer vision tasks through the lens of tensor algebra.

