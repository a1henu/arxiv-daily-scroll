---
layout: default
title: FinSight-Net:A Physics-Aware Decoupled Network with Frequency-Domain Compensation for Underwater Fish Detection in Smart Aquaculture
---

# FinSight-Net:A Physics-Aware Decoupled Network with Frequency-Domain Compensation for Underwater Fish Detection in Smart Aquaculture
**arXiv**：[2602.19437v1](https://arxiv.org/abs/2602.19437) · [PDF](https://arxiv.org/pdf/2602.19437.pdf)  
**作者**：Jinsong Yang, Zeyuan Hu, Yichen Li, Hong Yu  

**一句话要点**：提出FinSight-Net，一种物理感知解耦网络，通过频域补偿解决智能水产养殖中水下鱼类检测的物理限制问题。

**关键词**：水下鱼类检测, 物理感知网络, 频域补偿, 智能水产养殖, 轻量级检测

## 3 点简述
- 核心问题：水下波长吸收和浑浊散射导致对比度下降、结构模糊和背散射噪声，影响检测可靠性。
- 方法要点：采用多尺度解耦双流处理瓶颈补偿频域信息损失，设计高效路径聚合FPN恢复高频空间细节。
- 实验或效果：在多个数据集上达到先进性能，在UW-BlurredFish上mAP为92.8%，参数减少29.0%。

## 摘要（原文）

> Underwater fish detection (UFD) is a core capability for smart aquaculture and marine ecological monitoring. While recent detectors improve accuracy by stacking feature extractors or introducing heavy attention modules, they often incur substantial computational overhead and, more importantly, neglect the physics that fundamentally limits UFD: wavelength-dependent absorption and turbidity-induced scattering significantly degrade contrast, blur fine structures, and introduce backscattering noise, leading to unreliable localization and recognition. To address these challenges, we propose FinSight-Net, an efficient and physics-aware detection framework tailored for complex aquaculture environments. FinSight-Net introduces a Multi-Scale Decoupled Dual-Stream Processing (MS-DDSP) bottleneck that explicitly targets frequency-specific information loss via heterogeneous convolutional branches, suppressing backscattering artifacts while compensating distorted biological cues through scale-aware and channel-weighted pathways. We further design an Efficient Path Aggregation FPN (EPA-FPN) as a detail-filling mechanism: it restores high-frequency spatial information typically attenuated in deep layers by establishing long-range skip connections and pruning redundant fusion routes, enabling robust detection of non-rigid fish targets under severe blur and turbidity. Extensive experiments on DeepFish, AquaFishSet, and our challenging UW-BlurredFish benchmark demonstrate that FinSight-Net achieves state-of-the-art performance. In particular, on UW-BlurredFish, FinSight-Net reaches 92.8% mAP, outperforming YOLOv11s by 4.8% while reducing parameters by 29.0%, providing a strong and lightweight solution for real-time automated monitoring in smart aquaculture.

