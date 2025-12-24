---
layout: default
title: SegEarth-R2: Towards Comprehensive Language-guided Segmentation for Remote Sensing Images
---

# SegEarth-R2: Towards Comprehensive Language-guided Segmentation for Remote Sensing Images
**arXiv**：[2512.20013v1](https://arxiv.org/abs/2512.20013) · [PDF](https://arxiv.org/pdf/2512.20013.pdf)  
**作者**：Zepeng Xin, Kaiyu Li, Luodi Chen, Wanchen Li, Yuchen Xiao, Hui Qiao, Weizhan Zhang, Deyu Meng, Xiangyong Cao  

**一句话要点**：提出SegEarth-R2模型与LaSeRS数据集，以解决遥感图像中复杂语言引导分割的挑战

**关键词**：遥感图像分割, 语言引导分割, 多目标分割, 空间注意力监督, 分割查询机制, 地理空间推理

## 3 点简述
- 核心问题：现有模型难以处理遥感图像中的复杂语言指令，如多目标、层次粒度、推理需求和语言变异性。
- 方法要点：引入空间注意力监督机制处理小目标定位，设计灵活分割查询机制支持单目标和多目标场景。
- 实验或效果：SegEarth-R2在LaSeRS等基准上表现优异，为地理空间分割建立强大基线。

## 摘要（原文）

> Effectively grounding complex language to pixels in remote sensing (RS) images is a critical challenge for applications like disaster response and environmental monitoring. Current models can parse simple, single-target commands but fail when presented with complex geospatial scenarios, e.g., segmenting objects at various granularities, executing multi-target instructions, and interpreting implicit user intent. To drive progress against these failures, we present LaSeRS, the first large-scale dataset built for comprehensive training and evaluation across four critical dimensions of language-guided segmentation: hierarchical granularity, target multiplicity, reasoning requirements, and linguistic variability. By capturing these dimensions, LaSeRS moves beyond simple commands, providing a benchmark for complex geospatial reasoning. This addresses a critical gap: existing datasets oversimplify, leading to sensitivity-prone real-world models. We also propose SegEarth-R2, an MLLM architecture designed for comprehensive language-guided segmentation in RS, which directly confronts these challenges. The model's effectiveness stems from two key improvements: (1) a spatial attention supervision mechanism specifically handles the localization of small objects and their components, and (2) a flexible and efficient segmentation query mechanism that handles both single-target and multi-target scenarios. Experimental results demonstrate that our SegEarth-R2 achieves outstanding performance on LaSeRS and other benchmarks, establishing a powerful baseline for the next generation of geospatial segmentation. All data and code will be released at https://github.com/earth-insights/SegEarth-R2.

