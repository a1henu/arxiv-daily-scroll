---
layout: default
title: TBC: A Target-Background Contrast Metric for Low-Altitude Infrared and Visible Image Fusion
---

# TBC: A Target-Background Contrast Metric for Low-Altitude Infrared and Visible Image Fusion
**arXiv**：[2512.15211v1](https://arxiv.org/abs/2512.15211) · [PDF](https://arxiv.org/pdf/2512.15211.pdf)  
**作者**：Yufeng Xie  

**一句话要点**：提出目标-背景对比度（TBC）度量以解决低空红外与可见光图像融合中的噪声陷阱问题。

**关键词**：图像融合, 无参考度量, 目标检测, 低空无人机, 红外图像, 可见光图像

## 3 点简述
- 核心问题：传统无参考度量在低光环境下易将传感器噪声误判为有效细节，导致噪声陷阱。
- 方法要点：基于韦伯定律，TBC关注显著目标的相对对比度，惩罚背景噪声并奖励目标可见性。
- 实验或效果：在DroneVehicle数据集上验证，TBC更符合人类感知，为低空场景提供可靠标准。

## 摘要（原文）

> Infrared and visible image fusion is a pivotal technology in low-altitude UAV reconnaissance missions, providing high-quality data support for downstream tasks such as target detection and tracking by integrating thermal saliency with background texture details.However, traditional no-reference metrics fail(Specifically,like Entropy (EN) and Average Gradient (AG)) in complex low-light environments. They often misinterpret high-frequency sensor noise as valid detail. This creates a "Noise Trap," paradoxically assigning higher scores to noisy images and misguiding fusion algorithms.To address this, we propose the Target-Background Contrast (TBC) metric. Inspired by Weber's Law, TBC focuses on the relative contrast of salient targets rather than global statistics. Unlike traditional metrics, TBC penalizes background noise and rewards target visibility. Experiments on the DroneVehicle dataset demonstrate that TBC aligns better with human perception and provides a reliable standard for low-altitude scenarios.

