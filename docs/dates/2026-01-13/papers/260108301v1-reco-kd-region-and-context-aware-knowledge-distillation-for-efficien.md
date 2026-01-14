---
layout: default
title: ReCo-KD: Region- and Context-Aware Knowledge Distillation for Efficient 3D Medical Image Segmentation
---

# ReCo-KD: Region- and Context-Aware Knowledge Distillation for Efficient 3D Medical Image Segmentation
**arXiv**：[2601.08301v1](https://arxiv.org/abs/2601.08301) · [PDF](https://arxiv.org/pdf/2601.08301.pdf)  
**作者**：Qizhen Lan, Yu-Chun Hsu, Nida Saddaf Khan, Xiaoqian Jiang  

**一句话要点**：提出ReCo-KD框架，通过区域和上下文感知知识蒸馏，提升轻量模型在3D医学图像分割中的准确性。

**关键词**：3D医学图像分割, 知识蒸馏, 轻量模型, 区域感知, 上下文对齐, 临床部署

## 3 点简述
- 核心问题：高性能3D医学图像分割模型计算量大，轻量模型精度损失显著，限制临床部署。
- 方法要点：结合多尺度结构感知区域蒸馏和多尺度上下文对齐，从教师网络转移细粒度解剖细节和长程上下文信息。
- 实验或效果：在多个数据集上，蒸馏后轻量模型精度接近教师模型，显著减少参数和推理延迟，适合临床应用。

## 摘要（原文）

> Accurate 3D medical image segmentation is vital for diagnosis and treatment planning, but state-of-the-art models are often too large for clinics with limited computing resources. Lightweight architectures typically suffer significant performance loss. To address these deployment and speed constraints, we propose Region- and Context-aware Knowledge Distillation (ReCo-KD), a training-only framework that transfers both fine-grained anatomical detail and long-range contextual information from a high-capacity teacher to a compact student network. The framework integrates Multi-Scale Structure-Aware Region Distillation (MS-SARD), which applies class-aware masks and scale-normalized weighting to emphasize small but clinically important regions, and Multi-Scale Context Alignment (MS-CA), which aligns teacher-student affinity patterns across feature levels. Implemented on nnU-Net in a backbone-agnostic manner, ReCo-KD requires no custom student design and is easily adapted to other architectures. Experiments on multiple public 3D medical segmentation datasets and a challenging aggregated dataset show that the distilled lightweight model attains accuracy close to the teacher while markedly reducing parameters and inference latency, underscoring its practicality for clinical deployment.

