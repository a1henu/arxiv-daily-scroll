---
layout: default
title: IoUCert: Robustness Verification for Anchor-based Object Detectors
---

# IoUCert: Robustness Verification for Anchor-based Object Detectors
**arXiv**：[2603.03043v1](https://arxiv.org/abs/2603.03043) · [PDF](https://arxiv.org/pdf/2603.03043.pdf)  
**作者**：Benedikt Brückner, Alejandro Mercado, Yanghao Zhang, Panagiotis Kouvaros, Alessio Lomuscio  

**一句话要点**：提出IoUCert框架以解决锚框目标检测器在输入扰动下的鲁棒性验证难题

**关键词**：目标检测, 鲁棒性验证, 锚框检测器, IoU度量, 形式化方法

## 3 点简述
- 核心问题：目标检测因非线性坐标变换和IoU度量导致形式化鲁棒性验证困难
- 方法要点：通过坐标变换避免非线性松弛，基于锚框偏移优化IoU边界传播
- 实验或效果：首次实现对SSD、YOLOv2和YOLOv3等实际模型的鲁棒性验证

## 摘要（原文）

> While formal robustness verification has seen significant success in image classification, scaling these guarantees to object detection remains notoriously difficult due to complex non-linear coordinate transformations and Intersection-over-Union (IoU) metrics. We introduce {\sc \sf IoUCert}, a novel formal verification framework designed specifically to overcome these bottlenecks in foundational anchor-based object detection architectures. Focusing on the object localisation component in single-object settings, we propose a coordinate transformation that enables our algorithm to circumvent precision-degrading relaxations of non-linear box prediction functions. This allows us to optimise bounds directly with respect to the anchor box offsets which enables a novel Interval Bound Propagation method that derives optimal IoU bounds. We demonstrate that our method enables, for the first time, the robustness verification of realistic, anchor-based models including SSD, YOLOv2, and YOLOv3 variants against various input perturbations.

