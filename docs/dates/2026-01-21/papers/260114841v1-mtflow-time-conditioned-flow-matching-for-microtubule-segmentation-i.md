---
layout: default
title: MTFlow: Time-Conditioned Flow Matching for Microtubule Segmentation in Noisy Microscopy Images
---

# MTFlow: Time-Conditioned Flow Matching for Microtubule Segmentation in Noisy Microscopy Images
**arXiv**：[2601.14841v1](https://arxiv.org/abs/2601.14841) · [PDF](https://arxiv.org/pdf/2601.14841.pdf)  
**作者**：Sidi Mohamed Sid El Moctar, Achraf Ait Laydi, Yousef El Mourabit, Hélène Bouvrais  

**一句话要点**：提出MTFlow时间条件流匹配模型，用于噪声显微镜图像中的微管分割

**关键词**：微管分割, 流匹配, 时间条件模型, 显微镜图像, 曲线结构分析

## 3 点简述
- 核心问题：微管分割因细丝曲率、密集交叉和图像噪声而具有挑战性
- 方法要点：基于U-Net和时间嵌入，学习向量场迭代优化噪声掩码
- 实验或效果：在合成和真实数据集上达到竞争性精度，并泛化至其他曲线结构

## 摘要（原文）

> Microtubules are cytoskeletal filaments that play essential roles in many cellular processes and are key therapeutic targets in several diseases. Accurate segmentation of microtubule networks is critical for studying their organization and dynamics but remains challenging due to filament curvature, dense crossings, and image noise. We present MTFlow, a novel time-conditioned flow-matching model for microtubule segmentation. Unlike conventional U-Net variants that predict masks in a single pass, MTFlow learns vector fields that iteratively transport noisy masks toward the ground truth, enabling interpretable, trajectory-based refinement. Our architecture combines a U-Net backbone with temporal embeddings, allowing the model to capture the dynamics of uncertainty resolution along filament boundaries. We trained and evaluated MTFlow on synthetic and real microtubule datasets and assessed its generalization capability on public biomedical datasets of curvilinear structures such as retinal blood vessels and nerves. MTFlow achieves competitive segmentation accuracy comparable to state-of-the-art models, offering a powerful and time-efficient tool for filamentous structure analysis with more precise annotations than manual or semi-automatic approaches.

