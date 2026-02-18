---
layout: default
title: Training-Free Zero-Shot Anomaly Detection in 3D Brain MRI with 2D Foundation Models
---

# Training-Free Zero-Shot Anomaly Detection in 3D Brain MRI with 2D Foundation Models
**arXiv**：[2602.15315v1](https://arxiv.org/abs/2602.15315) · [PDF](https://arxiv.org/pdf/2602.15315.pdf)  
**作者**：Tai Le-Gia, Jaehyun Ahn  

**一句话要点**：提出基于2D基础模型的无训练零样本异常检测框架，用于3D脑MRI体积异常检测。

**关键词**：零样本异常检测, 3D脑MRI, 无训练框架, 体积令牌, 2D基础模型, 医学图像分析

## 3 点简述
- 核心问题：现有零样本异常检测方法难以扩展到3D医学图像，缺乏体积结构捕捉。
- 方法要点：通过聚合多轴切片构建局部体积令牌，恢复立方空间上下文，无需训练或监督。
- 实验或效果：框架在标准GPU上计算紧凑3D表示，实现简单鲁棒的体积异常检测。

## 摘要（原文）

> Zero-shot anomaly detection (ZSAD) has gained increasing attention in medical imaging as a way to identify abnormalities without task-specific supervision, but most advances remain limited to 2D datasets. Extending ZSAD to 3D medical images has proven challenging, with existing methods relying on slice-wise features and vision-language models, which fail to capture volumetric structure. In this paper, we introduce a fully training-free framework for ZSAD in 3D brain MRI that constructs localized volumetric tokens by aggregating multi-axis slices processed by 2D foundation models. These 3D patch tokens restore cubic spatial context and integrate directly with distance-based, batch-level anomaly detection pipelines. The framework provides compact 3D representations that are practical to compute on standard GPUs and require no fine-tuning, prompts, or supervision. Our results show that training-free, batch-based ZSAD can be effectively extended from 2D encoders to full 3D MRI volumes, offering a simple and robust approach for volumetric anomaly detection.

