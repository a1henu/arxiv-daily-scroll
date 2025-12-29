---
layout: default
title: A Lightweight Multi-Scale Attention Framework for Real-Time Spinal Endoscopic Instance Segmentation
---

# A Lightweight Multi-Scale Attention Framework for Real-Time Spinal Endoscopic Instance Segmentation
**arXiv**：[2512.21984v1](https://arxiv.org/abs/2512.21984) · [PDF](https://arxiv.org/pdf/2512.21984.pdf)  
**作者**：Qi Lai, JunYan Li, Qiang Cai, Lei Wang, Tao Yan, XiaoKun Liang  

**一句话要点**：提出LMSF-A轻量多尺度注意力框架，用于实时脊柱内窥镜实例分割，平衡精度与速度。

**关键词**：实时实例分割, 轻量模型, 多尺度注意力, 脊柱内窥镜, 医学图像分割, 小批量训练

## 3 点简述
- 核心问题：脊柱内窥镜实例分割面临视野窄、高光、烟雾/出血、边界不清和大尺度变化等挑战，且需在有限硬件上实现实时部署。
- 方法要点：设计轻量多尺度注意力框架，包括C2f-Pro主干、SSFF和TFE颈部、LMSH头部，支持多分支训练和单路径推理，减少参数。
- 实验或效果：在PELD数据集上表现优异，仅需1.8M参数和8.8 GFLOPs，泛化至公开牙齿基准，代码和数据集已开源。

## 摘要（原文）

> Real-time instance segmentation for spinal endoscopy is important for identifying and protecting critical anatomy during surgery, but it is difficult because of the narrow field of view, specular highlights, smoke/bleeding, unclear boundaries, and large scale changes. Deployment is also constrained by limited surgical hardware, so the model must balance accuracy and speed and remain stable under small-batch (even batch-1) training. We propose LMSF-A, a lightweight multi-scale attention framework co-designed across backbone, neck, and head. The backbone uses a C2f-Pro module that combines RepViT-style re-parameterized convolution (RVB) with efficient multi-scale attention (EMA), enabling multi-branch training while collapsing into a single fast path for inference. The neck improves cross-scale consistency and boundary detail using Scale-Sequence Feature Fusion (SSFF) and Triple Feature Encoding (TFE), which strengthens high-resolution features. The head adopts a Lightweight Multi-task Shared Head (LMSH) with shared convolutions and GroupNorm to reduce parameters and support batch-1 stability. We also release the clinically reviewed PELD dataset (61 patients, 610 images) with instance masks for adipose tissue, bone, ligamentum flavum, and nerve. Experiments show that LMSF-A is highly competitive (or even better than) in all evaluation metrics and much lighter than most instance segmentation methods requiring only 1.8M parameters and 8.8 GFLOPs, and it generalizes well to a public teeth benchmark. Code and dataset: https://github.com/hhwmortal/PELD-Instance-segmentation.

