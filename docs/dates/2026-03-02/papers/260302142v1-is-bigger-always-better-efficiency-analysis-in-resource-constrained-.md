---
layout: default
title: Is Bigger Always Better? Efficiency Analysis in Resource-Constrained Small Object Detection
---

# Is Bigger Always Better? Efficiency Analysis in Resource-Constrained Small Object Detection
**arXiv**：[2603.02142v1](https://arxiv.org/abs/2603.02142) · [PDF](https://arxiv.org/pdf/2603.02142.pdf)  
**作者**：Kwame Mbobda-Kuate, Gabriel Kasmi  

**一句话要点**：在资源受限地球观测中，通过效率分析揭示小模型优于大模型，优化模型尺寸、数据集尺寸和输入分辨率。

**关键词**：小目标检测, 模型效率分析, 资源受限地球观测, 缩放定律验证, YOLO模型

## 3 点简述
- 核心问题：缩放定律在资源受限地球观测中是否适用，大模型是否总是优于小模型。
- 方法要点：系统分析模型尺寸、数据集尺寸和输入分辨率三个维度，以模型效率（mAP$_{50}$每单位模型尺寸）为优化目标。
- 实验或效果：YOLO11N实现最高效率和绝对mAP$_{50}$，分辨率是主要资源分配杠杆，数据增加在低分辨率下回报可忽略。

## 摘要（原文）

> Scaling laws assume larger models trained on more data consistently outperform smaller ones -- an assumption that drives model selection in computer vision but remains untested in resource-constrained Earth observation (EO). We conduct a systematic efficiency analysis across three scaling dimensions: model size, dataset size, and input resolution, on rooftop PV detection in Madagascar. Optimizing for model efficiency (mAP$_{50}$ per unit of model size), we find a consistent efficiency inversion: YOLO11N achieves both the highest efficiency ($24\times$ higher than YOLO11X) and the highest absolute mAP$_{50}$ (0.617). Resolution is the dominant resource allocation lever ($+$120% efficiency gain), while additional data yields negligible returns at low resolution. These findings are robust to the deployment objective: small high-resolution configurations are Pareto-dominant across all 44 setups in the joint accuracy-throughput space, leaving no tradeoff to resolve. In data-scarce EO, bigger is not just unnecessary: it can be worse.

