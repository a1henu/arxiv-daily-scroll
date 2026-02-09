---
layout: default
title: MicroBi-ConvLSTM: An Ultra-Lightweight Efficient Model for Human Activity Recognition on Resource Constrained Devices
---

# MicroBi-ConvLSTM: An Ultra-Lightweight Efficient Model for Human Activity Recognition on Resource Constrained Devices
**arXiv**：[2602.06523v1](https://arxiv.org/abs/2602.06523) · [PDF](https://arxiv.org/pdf/2602.06523.pdf)  
**作者**：Mridankan Mandal  

**一句话要点**：提出MicroBi-ConvLSTM超轻量模型，用于资源受限设备上的人类活动识别。

**关键词**：人类活动识别, 轻量模型, 卷积循环网络, 边缘计算, 量化部署

## 3 点简述
- 问题：资源受限可穿戴设备上的人类活动识别需平衡准确性与严格内存计算预算。
- 方法：采用两阶段卷积特征提取、4倍时间池化和单层双向LSTM，实现平均11.4K参数。
- 效果：在八个基准测试中保持竞争力，INT8量化后部署足迹平均23.0KB。

## 摘要（原文）

> Human Activity Recognition (HAR) on resource constrained wearables requires models that balance accuracy against strict memory and computational budgets. State of the art lightweight architectures such as TinierHAR (34K parameters) and TinyHAR (55K parameters) achieve strong accuracy, but exceed memory budgets of microcontrollers with limited SRAM once operating system overhead is considered. We present MicroBi-ConvLSTM, an ultra-lightweight convolutional-recurrent architecture achieving 11.4K parameters on average through two stage convolutional feature extraction with 4x temporal pooling and a single bidirectional LSTM layer. This represents 2.9x parameter reduction versus TinierHAR and 11.9x versus DeepConvLSTM while preserving linear O(N) complexity. Evaluation across eight diverse HAR benchmarks shows that MicroBi-ConvLSTM maintains competitive performance within the ultra-lightweight regime: 93.41% macro F1 on UCI-HAR, 94.46% on SKODA assembly gestures, and 88.98% on Daphnet gait freeze detection. Systematic ablation reveals task dependent component contributions where bidirectionality benefits episodic event detection, but provides marginal gains on periodic locomotion. INT8 post training quantization incurs only 0.21% average F1-score degradation, yielding a 23.0 KB average deployment footprint suitable for memory constrained edge devices.

