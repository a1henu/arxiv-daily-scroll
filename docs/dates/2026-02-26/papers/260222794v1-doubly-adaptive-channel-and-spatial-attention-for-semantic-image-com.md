---
layout: default
title: Doubly Adaptive Channel and Spatial Attention for Semantic Image Communication by IoT Devices
---

# Doubly Adaptive Channel and Spatial Attention for Semantic Image Communication by IoT Devices
**arXiv**：[2602.22794v1](https://arxiv.org/abs/2602.22794) · [PDF](https://arxiv.org/pdf/2602.22794.pdf)  
**作者**：Soroosh Miri, Sepehr Abolhasani, Shahrokh Farahmand, S. Mohammad Razavizadeh  

**一句话要点**：提出双重自适应通道与空间注意力机制，以提升物联网设备在动态信道下的语义图像通信性能。

**关键词**：语义通信, 深度联合源信道编码, 注意力机制, 物联网设备, 自适应编码, 图像传输

## 3 点简述
- 核心问题：物联网网络面临带宽有限、资源受限和信道动态变化等挑战，需低复杂度语义通信方案。
- 方法要点：在自适应深度联合源信道编码基础上，引入双重自适应通道与空间注意力模块，动态调整特征提取。
- 实验或效果：仿真显示，相比现有方法，DA-DJSCC在多项性能指标上显著提升，复杂度增加轻微。

## 摘要（原文）

> Internet of Things (IoT) networks face significant challenges such as limited communication bandwidth, constrained computational and energy resources, and highly dynamic wireless channel conditions. Utilization of deep neural networks (DNNs) combined with semantic communication has emerged as a promising paradigm to address these limitations. Deep joint source-channel coding (DJSCC) has recently been proposed to enable semantic communication of images. Building upon the original DJSCC formulation, low-complexity attention-style architectures has been added to the DNNs for further performance enhancement. As a main hurdle, training these DNNs separately for various signal-to-noise ratios (SNRs) will amount to excessive storage or communication overhead, which can not be maintained by small IoT devices. SNR Adaptive DJSCC (ADJSCC), has been proposed to train the DNNs once but feed the current SNR as part of the data to the channel-wise attention mechanism. We improve upon ADJSCC by a simultaneous utilization of doubly adaptive channel-wise and spatial attention modules at both transmitter and receiver. These modules dynamically adjust to varying channel conditions and spatial feature importance, enabling robust and efficient feature extraction and semantic information recovery. Simulation results corroborate that our proposed doubly adaptive DJSCC (DA-DJSCC) significantly improves upon ADJSCC in several performance criteria, while incurring a mild increase in complexity. These facts render DA-DJSCC a desirable choice for semantic communication in performance demanding but low-complexity IoT networks.

