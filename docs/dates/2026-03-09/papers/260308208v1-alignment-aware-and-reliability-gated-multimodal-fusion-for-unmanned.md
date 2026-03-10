---
layout: default
title: Alignment-Aware and Reliability-Gated Multimodal Fusion for Unmanned Aerial Vehicle Detection Across Heterogeneous Thermal-Visual Sensors
---

# Alignment-Aware and Reliability-Gated Multimodal Fusion for Unmanned Aerial Vehicle Detection Across Heterogeneous Thermal-Visual Sensors
**arXiv**：[2603.08208v1](https://arxiv.org/abs/2603.08208) · [PDF](https://arxiv.org/pdf/2603.08208.pdf)  
**作者**：Ishrat Jahan, Molla E Majid, M Murugappan, Muhammad E. H. Chowdhury, N. B. Prakash, Saad Bin Abul Kashem, Balamurugan Balusamy, Amith Khandakar  

**一句话要点**：提出RGIF和RGMAF融合策略以解决异构热-视觉传感器无人机检测中的空间对齐与可靠性问题。

**关键词**：无人机检测, 多模态融合, 传感器配准, 可靠性加权, 热-视觉传感器, YOLOv10x

## 3 点简述
- 核心问题：异构传感器融合中空间对应性差和标注不一致性限制无人机检测鲁棒性。
- 方法要点：RGIF基于ECC仿射配准和引导滤波保持热显著性；RGMAF结合仿射与光流配准及可靠性加权注意力机制。
- 实验或效果：在MMFW-UAV数据集上，RGIF提升mAP@50至97.65%，RGMAF达到最高召回率98.64%。

## 摘要（原文）

> Reliable unmanned aerial vehicle (UAV) detection is critical for autonomous airspace monitoring but remains challenging when integrating sensor streams that differ substantially in resolution, perspective, and field of view. Conventional fusion methods-such as wavelet-, Laplacian-, and decision-level approaches-often fail to preserve spatial correspondence across modalities and suffer from annotation of inconsistencies, limiting their robustness in real-world settings. This study introduces two fusion strategies, Registration-aware Guided Image Fusion (RGIF) and Reliability-Gated Modality-Attention Fusion (RGMAF), designed to overcome these limitations. RGIF employs Enhanced Correlation Coefficient (ECC)-based affine registration combined with guided filtering to maintain thermal saliency while enhancing structural detail. RGMAF integrates affine and optical-flow registration with a reliability-weighted attention mechanism that adaptively balances thermal contrast and visual sharpness. Experiments were conducted on the Multi-Sensor and Multi-View Fixed-Wing (MMFW)-UAV dataset comprising 147,417 annotated air-to-air frames collected from infrared, wide-angle, and zoom sensors. Among single-modality detectors, YOLOv10x demonstrated the most stable cross-domain performance and was selected as the detection backbone for evaluating fused imagery. RGIF improved the visual baseline by 2.13% mAP@50 (achieving 97.65%), while RGMAF attained the highest recall of 98.64%. These findings show that registration-aware and reliability-adaptive fusion provides a robust framework for integrating heterogeneous modalities, substantially enhancing UAV detection performance in multimodal environments.

