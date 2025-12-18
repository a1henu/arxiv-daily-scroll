---
layout: default
title: IMKD: Intensity-Aware Multi-Level Knowledge Distillation for Camera-Radar Fusion
---

# IMKD: Intensity-Aware Multi-Level Knowledge Distillation for Camera-Radar Fusion
**arXiv**：[2512.15581v1](https://arxiv.org/abs/2512.15581) · [PDF](https://arxiv.org/pdf/2512.15581.pdf)  
**作者**：Shashank Mishra, Karan Patil, Didier Stricker, Jason Rambach  

**一句话要点**：提出IMKD强度感知多级知识蒸馏框架，以增强雷达-相机融合3D目标检测性能

**关键词**：雷达-相机融合, 知识蒸馏, 3D目标检测, 强度感知, 多级蒸馏, 传感器特性保留

## 3 点简述
- 现有蒸馏方法直接转移模态特征，可能扭曲传感器特性并削弱各自优势
- IMKD采用三阶段强度感知蒸馏策略，保留传感器内在特性并放大互补优势
- 在nuScenes基准测试中达到67.0% NDS和61.0% mAP，优于先前蒸馏方法

## 摘要（原文）

> High-performance Radar-Camera 3D object detection can be achieved by leveraging knowledge distillation without using LiDAR at inference time. However, existing distillation methods typically transfer modality-specific features directly to each sensor, which can distort their unique characteristics and degrade their individual strengths. To address this, we introduce IMKD, a radar-camera fusion framework based on multi-level knowledge distillation that preserves each sensor's intrinsic characteristics while amplifying their complementary strengths. IMKD applies a three-stage, intensity-aware distillation strategy to enrich the fused representation across the architecture: (1) LiDAR-to-Radar intensity-aware feature distillation to enhance radar representations with fine-grained structural cues, (2) LiDAR-to-Fused feature intensity-guided distillation to selectively highlight useful geometry and depth information at the fusion level, fostering complementarity between the modalities rather than forcing them to align, and (3) Camera-Radar intensity-guided fusion mechanism that facilitates effective feature alignment and calibration. Extensive experiments on the nuScenes benchmark show that IMKD reaches 67.0% NDS and 61.0% mAP, outperforming all prior distillation-based radar-camera fusion methods. Our code and models are available at https://github.com/dfki-av/IMKD/.

