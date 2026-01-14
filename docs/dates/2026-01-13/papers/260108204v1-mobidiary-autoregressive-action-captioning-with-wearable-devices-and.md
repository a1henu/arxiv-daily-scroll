---
layout: default
title: MobiDiary: Autoregressive Action Captioning with Wearable Devices and Wireless Signals
---

# MobiDiary: Autoregressive Action Captioning with Wearable Devices and Wireless Signals
**arXiv**：[2601.08204v1](https://arxiv.org/abs/2601.08204) · [PDF](https://arxiv.org/pdf/2601.08204.pdf)  
**作者**：Fei Deng, Yinghui He, Chuntong Chu, Ge Wang, Han Ding, Jinsong Han, Fei Wang  

**一句话要点**：提出MobiDiary框架，利用可穿戴设备和Wi-Fi信号生成日常活动的自然语言描述

**关键词**：人类活动识别, 多模态融合, 自回归生成, 传感器信号处理, 自然语言描述

## 3 点简述
- 核心问题：传统视觉活动识别存在隐私和环境限制，需从物理信号生成自然语言描述
- 方法要点：设计统一传感器编码器，利用运动信号共享偏置，结合Transformer解码器自回归生成
- 实验效果：在多个公开基准测试中，在描述指标上达到最先进性能，优于专用基线

## 摘要（原文）

> Human Activity Recognition (HAR) in smart homes is critical for health monitoring and assistive living. While vision-based systems are common, they face privacy concerns and environmental limitations (e.g., occlusion). In this work, we present MobiDiary, a framework that generates natural language descriptions of daily activities directly from heterogeneous physical signals (specifically IMU and Wi-Fi). Unlike conventional approaches that restrict outputs to pre-defined labels, MobiDiary produces expressive, human-readable summaries. To bridge the semantic gap between continuous, noisy physical signals and discrete linguistic descriptions, we propose a unified sensor encoder. Instead of relying on modality-specific engineering, we exploit the shared inductive biases of motion-induced signals--where both inertial and wireless data reflect underlying kinematic dynamics. Specifically, our encoder utilizes a patch-based mechanism to capture local temporal correlations and integrates heterogeneous placement embedding to unify spatial contexts across different sensors. These unified signal tokens are then fed into a Transformer-based decoder, which employs an autoregressive mechanism to generate coherent action descriptions word-by-word. We comprehensively evaluate our approach on multiple public benchmarks (XRF V2, UWash, and WiFiTAD). Experimental results demonstrate that MobiDiary effectively generalizes across modalities, achieving state-of-the-art performance on captioning metrics (e.g., BLEU@4, CIDEr, RMC) and outperforming specialized baselines in continuous action understanding.

