---
layout: default
title: SCG With Your Phone: Diagnosis of Rhythmic Spectrum Disorders in Field Conditions
---

# SCG With Your Phone: Diagnosis of Rhythmic Spectrum Disorders in Field Conditions
**arXiv**：[2601.13926v1](https://arxiv.org/abs/2601.13926) · [PDF](https://arxiv.org/pdf/2601.13926.pdf)  
**作者**：Peter Golenderov, Yaroslav Matushenko, Anastasia Tushina, Michal Barodkin  

**一句话要点**：提出增强U-Net v3框架，用于智能手机采集的噪声SCG信号分割与节律分析，实现现场条件下的心脏节律监测。

**关键词**：心震图分割, 深度学习架构, 智能手机传感, 心脏节律分析, 现场诊断

## 3 点简述
- 核心问题：智能手机采集的SCG信号受噪声、运动伪影和设备异质性影响，难以可靠检测主动脉瓣开放事件。
- 方法要点：集成多尺度卷积、残差连接和注意力门的U-Net v3架构，结合自适应3D到1D投影处理任意手机朝向。
- 实验或效果：在多种设备类型和无监督数据收集条件下，方法表现出高准确性和鲁棒性，支持低成本自动化心脏监测。

## 摘要（原文）

> Aortic valve opening (AO) events are crucial for detecting frequency and rhythm disorders, especially in real-world settings where seismocardiography (SCG) signals collected via consumer smartphones are subject to noise, motion artifacts, and variability caused by device heterogeneity. In this work, we present a robust deep-learning framework for SCG segmentation and rhythm analysis using accelerometer recordings obtained with consumer smartphones. We develop an enhanced U-Net v3 architecture that integrates multi-scale convolutions, residual connections, and attention gates, enabling reliable segmentation of noisy SCG signals. A dedicated post-processing pipeline converts probability masks into precise AO timestamps, whereas a novel adaptive 3D-to-1D projection method ensures robustness to arbitrary smartphone orientation. Experimental results demonstrate that the proposed method achieves consistently high accuracy and robustness across various device types and unsupervised data-collection conditions. Our approach enables practical, low-cost, and automated cardiac-rhythm monitoring using everyday mobile devices, paving the way for scalable, field-deployable cardiovascular assessment and future multimodal diagnostic systems.

