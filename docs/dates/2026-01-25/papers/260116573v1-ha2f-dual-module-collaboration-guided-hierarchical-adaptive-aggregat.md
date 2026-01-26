---
layout: default
title: HA2F: Dual-module Collaboration-Guided Hierarchical Adaptive Aggregation Framework for Remote Sensing Change Detection
---

# HA2F: Dual-module Collaboration-Guided Hierarchical Adaptive Aggregation Framework for Remote Sensing Change Detection
**arXiv**：[2601.16573v1](https://arxiv.org/abs/2601.16573) · [PDF](https://arxiv.org/pdf/2601.16573.pdf)  
**作者**：Shuying Li, Yuchen Wang, San Zhang, Chuang Yang  

**一句话要点**：提出HA2F框架以解决遥感变化检测中的特征对齐偏差和噪声干扰问题

**关键词**：遥感变化检测, 特征对齐, 噪声抑制, 层次特征聚合, 双模块协作, 自适应框架

## 3 点简述
- 核心问题：现有方法在局部特征提取和整体图像处理间存在跨时相特征匹配偏差，对辐射和几何噪声敏感。
- 方法要点：HA2F包含动态层次特征校准模块和噪声自适应特征细化模块，通过双模块协作实现特征对齐和噪声抑制。
- 实验或效果：在多个数据集上达到最先进性能，精度和计算效率均优于现有方法，消融实验验证模块有效性。

## 摘要（原文）

> Remote sensing change detection (RSCD) aims to identify the spatio-temporal changes of land cover, providing critical support for multi-disciplinary applications (e.g., environmental monitoring, disaster assessment, and climate change studies). Existing methods focus either on extracting features from localized patches, or pursue processing entire images holistically, which leads to the cross temporal feature matching deviation and exhibiting sensitivity to radiometric and geometric noise. Following the above issues, we propose a dual-module collaboration guided hierarchical adaptive aggregation framework, namely HA2F, which consists of dynamic hierarchical feature calibration module (DHFCM) and noise-adaptive feature refinement module (NAFRM). The former dynamically fuses adjacent-level features through perceptual feature selection, suppressing irrelevant discrepancies to address multi-temporal feature alignment deviations. The NAFRM utilizes the dual feature selection mechanism to highlight the change sensitive regions and generate spatial masks, suppressing the interference of irrelevant regions or shadows. Extensive experiments verify the effectiveness of the proposed HA2F, which achieves state-of-the-art performance on LEVIR-CD, WHU-CD, and SYSU-CD datasets, surpassing existing comparative methods in terms of both precision metrics and computational efficiency. In addition, ablation experiments show that DHFCM and NAFRM are effective. \href{https://huggingface.co/InPeerReview/RemoteSensingChangeDetection-RSCD.HA2F}{HA2F Official Code is Available Here!}

