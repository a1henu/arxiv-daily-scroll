---
layout: default
title: Sim2Real Deep Transfer for Per-Device CFO Calibration
---

# Sim2Real Deep Transfer for Per-Device CFO Calibration
**arXiv**：[2601.10264v1](https://arxiv.org/abs/2601.10264) · [PDF](https://arxiv.org/pdf/2601.10264.pdf)  
**作者**：Jingze Zheng, Zhiguo Shi, Shibo He, Chaojie Gu  

**一句话要点**：提出Sim2Real迁移学习框架，通过仿真预训练与轻量适配实现异构SDR平台的单设备CFO校准。

**关键词**：载波频率偏移校准, Sim2Real迁移学习, 软件定义无线电, 正交频分复用, 设备级适配, 轻量微调

## 3 点简述
- 核心问题：异构软件定义无线电平台因硬件损伤未校准，导致OFDM系统载波频率偏移估计性能下降。
- 方法要点：结合参数化硬件失真仿真预训练骨干DNN，仅用少量真实数据微调回归层，实现设备级适配。
- 实验或效果：在三种SDR设备上，相比传统方法，室内多径条件下误码率降低30倍。

## 摘要（原文）

> Carrier Frequency Offset (CFO) estimation in Orthogonal Frequency Division Multiplexing (OFDM) systems faces significant performance degradation across heterogeneous software-defined radio (SDR) platforms due to uncalibrated hardware impairments. Existing deep neural network (DNN)-based approaches lack device-level adaptation, limiting their practical deployment. This paper proposes a Sim2Real transfer learning framework for per-device CFO calibration, combining simulation-driven pretraining with lightweight receiver adaptation. A backbone DNN is pre-trained on synthetic OFDM signals incorporating parametric hardware distortions (e.g., phase noise, IQ imbalance), enabling generalized feature learning without costly cross-device data collection. Subsequently, only the regression layers are fine-tuned using $1,000$ real frames per target device, preserving hardware-agnostic knowledge while adapting to device-specific impairments. Experiments across three SDR families (USRP B210, USRP N210, HackRF One) achieve $30\times$ BER reduction compared to conventional CP-based methods under indoor multipath conditions. The framework bridges the simulation-to-reality gap for robust CFO estimation, enabling cost-effective deployment in heterogeneous wireless systems.

