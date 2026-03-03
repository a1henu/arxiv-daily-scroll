---
layout: default
title: Downstream Task Inspired Underwater Image Enhancement: A Perception-Aware Study from Dataset Construction to Network Design
---

# Downstream Task Inspired Underwater Image Enhancement: A Perception-Aware Study from Dataset Construction to Network Design
**arXiv**：[2603.01767v1](https://arxiv.org/abs/2603.01767) · [PDF](https://arxiv.org/pdf/2603.01767.pdf)  
**作者**：Bosen Lin, Feng Gao, Yanwei Yu, Junyu Dong, Qian Du  

**一句话要点**：提出下游任务启发的感知感知水下图像增强框架，以提升水下图像识别性能。

**关键词**：水下图像增强, 下游任务感知, 注意力机制, 多阶段训练, 感知损失, 数据集构建

## 3 点简述
- 核心问题：现有水下图像增强方法侧重人眼视觉，忽视对下游任务关键的高频细节重建。
- 方法要点：设计双分支网络与任务感知注意力模块，结合多阶段训练和任务驱动感知损失。
- 实验或效果：构建任务启发数据集，实验显示显著提升语义分割、目标检测等下游任务性能。

## 摘要（原文）

> In real underwater environments, downstream image recognition tasks such as semantic segmentation and object detection often face challenges posed by problems like blurring and color inconsistencies. Underwater image enhancement (UIE) has emerged as a promising preprocessing approach, aiming to improve the recognizability of targets in underwater images. However, most existing UIE methods mainly focus on enhancing images for human visual perception, frequently failing to reconstruct high-frequency details that are critical for task-specific recognition. To address this issue, we propose a Downstream Task-Inspired Underwater Image Enhancement (DTI-UIE) framework, which leverages human visual perception model to enhance images effectively for underwater vision tasks. Specifically, we design an efficient two-branch network with task-aware attention module for feature mixing. The network benefits from a multi-stage training framework and a task-driven perceptual loss. Additionally, inspired by human perception, we automatically construct a Task-Inspired UIE Dataset (TI-UIED) using various task-specific networks. Experimental results demonstrate that DTI-UIE significantly improves task performance by generating preprocessed images that are beneficial for downstream tasks such as semantic segmentation, object detection, and instance segmentation. The codes are publicly available at https://github.com/oucailab/DTIUIE.

