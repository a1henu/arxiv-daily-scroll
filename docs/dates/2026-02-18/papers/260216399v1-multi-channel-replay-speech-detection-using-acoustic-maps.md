---
layout: default
title: Multi-Channel Replay Speech Detection using Acoustic Maps
---

# Multi-Channel Replay Speech Detection using Acoustic Maps
**arXiv**：[2602.16399v1](https://arxiv.org/abs/2602.16399) · [PDF](https://arxiv.org/pdf/2602.16399.pdf)  
**作者**：Michael Neri, Tuomas Virtanen  

**一句话要点**：提出声学地图作为多通道重放语音检测的空间特征表示，以增强自动说话人验证系统的安全性。

**关键词**：重放语音检测, 声学地图, 多通道录音, 自动说话人验证, 卷积神经网络, 空间特征表示

## 3 点简述
- 核心问题：重放攻击是自动说话人验证系统在实时语音助手应用中的关键漏洞。
- 方法要点：基于离散方位和仰角网格的经典波束形成，声学地图编码方向性能量分布，反映人声辐射与扬声器重放的物理差异。
- 实验或效果：在ReMASC数据集上，轻量级卷积神经网络以约6k可训练参数实现竞争性能，声学地图提供紧凑且物理可解释的特征空间。

## 摘要（原文）

> Replay attacks remain a critical vulnerability for automatic speaker verification systems, particularly in real-time voice assistant applications. In this work, we propose acoustic maps as a novel spatial feature representation for replay speech detection from multi-channel recordings. Derived from classical beamforming over discrete azimuth and elevation grids, acoustic maps encode directional energy distributions that reflect physical differences between human speech radiation and loudspeaker-based replay. A lightweight convolutional neural network is designed to operate on this representation, achieving competitive performance on the ReMASC dataset with approximately 6k trainable parameters. Experimental results show that acoustic maps provide a compact and physically interpretable feature space for replay attack detection across different devices and acoustic environments.

