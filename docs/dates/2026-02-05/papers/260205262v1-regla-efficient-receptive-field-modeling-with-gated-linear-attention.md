---
layout: default
title: ReGLA: Efficient Receptive-Field Modeling with Gated Linear Attention Network
---

# ReGLA: Efficient Receptive-Field Modeling with Gated Linear Attention Network
**arXiv**：[2602.05262v1](https://arxiv.org/abs/2602.05262) · [PDF](https://arxiv.org/pdf/2602.05262.pdf)  
**作者**：Junzhou Li, Manqi Zhao, Yilin Gao, Zhiheng Yu, Yin Li, Dongsheng Jiang, Li Xiao  

**一句话要点**：提出ReGLA轻量级混合网络，以平衡高分辨率图像上的精度与延迟。

**关键词**：轻量级网络, 门控线性注意力, 高分辨率视觉, 多教师蒸馏, 混合架构

## 3 点简述
- 核心问题：轻量模型在高分辨率图像上平衡精度与延迟的挑战，Transformer架构常有过高延迟。
- 方法要点：结合高效卷积进行局部特征提取和基于ReLU的门控线性注意力进行全局建模，包括ELRF、RGMA模块和多教师蒸馏策略。
- 实验或效果：在ImageNet-1K上达到80.85% Top-1精度，延迟仅4.98 ms，下游任务如COCO和ADE20K上性能优于类似规模模型。

## 摘要（原文）

> Balancing accuracy and latency on high-resolution images is a critical challenge for lightweight models, particularly for Transformer-based architectures that often suffer from excessive latency. To address this issue, we introduce \textbf{ReGLA}, a series of lightweight hybrid networks, which integrates efficient convolutions for local feature extraction with ReLU-based gated linear attention for global modeling. The design incorporates three key innovations: the Efficient Large Receptive Field (ELRF) module for enhancing convolutional efficiency while preserving a large receptive field; the ReLU Gated Modulated Attention (RGMA) module for maintaining linear complexity while enhancing local feature representation; and a multi-teacher distillation strategy to boost performance on downstream tasks. Extensive experiments validate the superiority of ReGLA; particularly the ReGLA-M achieves \textbf{80.85\%} Top-1 accuracy on ImageNet-1K at $224px$, with only \textbf{4.98 ms} latency at $512px$. Furthermore, ReGLA outperforms similarly scaled iFormer models in downstream tasks, achieving gains of \textbf{3.1\%} AP on COCO object detection and \textbf{3.6\%} mIoU on ADE20K semantic segmentation, establishing it as a state-of-the-art solution for high-resolution visual applications.

