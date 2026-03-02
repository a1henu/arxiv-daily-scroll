---
layout: default
title: ULW-SleepNet: An Ultra-Lightweight Network for Multimodal Sleep Stage Scoring
---

# ULW-SleepNet: An Ultra-Lightweight Network for Multimodal Sleep Stage Scoring
**arXiv**：[2602.23852v1](https://arxiv.org/abs/2602.23852) · [PDF](https://arxiv.org/pdf/2602.23852.pdf)  
**作者**：Zhaowen Wang, Dongdong Zhou, Qi Xu, Fengyu Cong, Mohammad Al-Sa'd, Jenni Raitoharju  

**一句话要点**：提出ULW-SleepNet以解决多模态睡眠分期中计算复杂度高的问题，适用于可穿戴设备实时监测。

**关键词**：睡眠分期, 多模态学习, 轻量化网络, 可穿戴设备, 实时监测

## 3 点简述
- 核心问题：现有深度学习模型计算量大，且多针对单通道EEG，难以处理多模态PSG数据。
- 方法要点：采用双流可分离卷积块、深度可分离卷积、通道参数共享和全局平均池化，大幅降低参数和计算量。
- 实验或效果：在Sleep-EDF数据集上达到86.9%和81.4%准确率，仅13.3K参数和7.89M FLOPs，参数减少高达98.6%。

## 摘要（原文）

> Automatic sleep stage scoring is crucial for the diagnosis and treatment of sleep disorders. Although deep learning models have advanced the field, many existing models are computationally demanding and designed for single-channel electroencephalography (EEG), limiting their practicality for multimodal polysomnography (PSG) data. To overcome this, we propose ULW-SleepNet, an ultra-lightweight multimodal sleep stage scoring framework that efficiently integrates information from multiple physiological signals. ULW-SleepNet incorporates a novel Dual-Stream Separable Convolution (DSSC) Block, depthwise separable convolutions, channel-wise parameter sharing, and global average pooling to reduce computational overhead while maintaining competitive accuracy. Evaluated on the Sleep-EDF-20 and Sleep-EDF-78 datasets, ULW-SleepNet achieves accuracies of 86.9% and 81.4%, respectively, with only 13.3K parameters and 7.89M FLOPs. Compared to state-of-the-art methods, our model reduces parameters by up to 98.6% with only marginal performance loss, demonstrating its strong potential for real-time sleep monitoring on wearable and IoT devices. The source code for this study is publicly available at https://github.com/wzw999/ULW-SLEEPNET.

