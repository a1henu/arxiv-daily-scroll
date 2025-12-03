---
layout: default
title: ALDI-ray: Adapting the ALDI Framework for Security X-ray Object Detection
---

# ALDI-ray: Adapting the ALDI Framework for Security X-ray Object Detection
**arXiv**：[2512.02696v1](https://arxiv.org/abs/2512.02696) · [PDF](https://arxiv.org/pdf/2512.02696.pdf)  
**作者**：Omid Reza Heidari, Yang Wang, Xinxin Zuo  

**一句话要点**：提出ALDI++框架以解决安全X射线图像中的领域自适应目标检测问题

**关键词**：领域自适应, 目标检测, 安全X射线成像, 自蒸馏, 特征对齐, ViTDet

## 3 点简述
- 核心问题：安全X射线成像中扫描设备和环境变化导致领域偏移，降低目标检测性能。
- 方法要点：应用ALDI++框架，集成自蒸馏、特征对齐和增强训练策略，有效缓解领域偏移。
- 实验或效果：在EDS数据集上超越SOTA方法，ViTDet骨干网络实现最高mAP，类别分析显示检测精度一致提升。

## 摘要（原文）

> Domain adaptation in object detection is critical for real-world applications where distribution shifts degrade model performance. Security X-ray imaging presents a unique challenge due to variations in scanning devices and environmental conditions, leading to significant domain discrepancies. To address this, we apply ALDI++, a domain adaptation framework that integrates self-distillation, feature alignment, and enhanced training strategies to mitigate domain shift effectively in this area. We conduct extensive experiments on the EDS dataset, demonstrating that ALDI++ surpasses the state-of-the-art (SOTA) domain adaptation methods across multiple adaptation scenarios. In particular, ALDI++ with a Vision Transformer for Detection (ViTDet) backbone achieves the highest mean average precision (mAP), confirming the effectiveness of transformer-based architectures for cross-domain object detection. Additionally, our category-wise analysis highlights consistent improvements in detection accuracy, reinforcing the robustness of the model across diverse object classes. Our findings establish ALDI++ as an efficient solution for domain-adaptive object detection, setting a new benchmark for performance stability and cross-domain generalization in security X-ray imagery.

