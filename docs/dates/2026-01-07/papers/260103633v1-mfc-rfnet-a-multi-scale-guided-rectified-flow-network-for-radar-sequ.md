---
layout: default
title: MFC-RFNet: A Multi-scale Guided Rectified Flow Network for Radar Sequence Prediction
---

# MFC-RFNet: A Multi-scale Guided Rectified Flow Network for Radar Sequence Prediction
**arXiv**：[2601.03633v1](https://arxiv.org/abs/2601.03633) · [PDF](https://arxiv.org/pdf/2601.03633.pdf)  
**作者**：Wenjie Luo, Chuanhu Deng, Chaorong Li, Rongyao Deng, Qiang Yang  

**一句话要点**：提出MFC-RFNet，通过多尺度引导整流流网络解决雷达序列预测中的复杂演化与特征对齐问题。

**关键词**：雷达序列预测, 多尺度融合, 整流流训练, 时空对齐, 生成模型, 降水临近预报

## 3 点简述
- 核心问题：雷达回波序列预测需建模多尺度演化、校正帧间特征错位，并高效捕获长程时空上下文。
- 方法要点：集成多尺度通信与引导特征融合，包括小波引导跳跃连接、特征通信模块和条件引导空间变换融合。
- 实验或效果：在四个公开数据集上优于基线，在更高雨率阈值和更长预测时间保持清晰回波形态和稳定技能。

## 摘要（原文）

> Accurate and high-resolution precipitation nowcasting from radar echo sequences is crucial for disaster mitigation and economic planning, yet it remains a significant challenge. Key difficulties include modeling complex multi-scale evolution, correcting inter-frame feature misalignment caused by displacement, and efficiently capturing long-range spatiotemporal context without sacrificing spatial fidelity. To address these issues, we present the Multi-scale Feature Communication Rectified Flow (RF) Network (MFC-RFNet), a generative framework that integrates multi-scale communication with guided feature fusion. To enhance multi-scale fusion while retaining fine detail, a Wavelet-Guided Skip Connection (WGSC) preserves high-frequency components, and a Feature Communication Module (FCM) promotes bidirectional cross-scale interaction. To correct inter-frame displacement, a Condition-Guided Spatial Transform Fusion (CGSTF) learns spatial transforms from conditioning echoes to align shallow features. The backbone adopts rectified flow training to learn near-linear probability-flow trajectories, enabling few-step sampling with stable fidelity. Additionally, lightweight Vision-RWKV (RWKV) blocks are placed at the encoder tail, the bottleneck, and the first decoder layer to capture long-range spatiotemporal dependencies at low spatial resolutions with moderate compute. Evaluations on four public datasets (SEVIR, MeteoNet, Shanghai, and CIKM) demonstrate consistent improvements over strong baselines, yielding clearer echo morphology at higher rain-rate thresholds and sustained skill at longer lead times. These results suggest that the proposed synergy of RF training with scale-aware communication, spatial alignment, and frequency-aware fusion presents an effective and robust approach for radar-based nowcasting.

