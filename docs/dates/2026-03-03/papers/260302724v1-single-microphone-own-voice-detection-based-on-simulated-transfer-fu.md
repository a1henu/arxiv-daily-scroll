---
layout: default
title: Single Microphone Own Voice Detection based on Simulated Transfer Functions for Hearing Aids
---

# Single Microphone Own Voice Detection based on Simulated Transfer Functions for Hearing Aids
**arXiv**：[2603.02724v1](https://arxiv.org/abs/2603.02724) · [PDF](https://arxiv.org/pdf/2603.02724.pdf)  
**作者**：Mathuranathan Mayuravaani, W. Bastiaan Kleijn, Andrew Lensen, Charlotte Sørensen  

**一句话要点**：提出基于模拟声学传递函数的单麦克风自语音检测方法，用于助听器场景。

**关键词**：自语音检测, 声学传递函数模拟, Transformer分类器, 数据增强, 助听器应用, 单麦克风系统

## 3 点简述
- 核心问题：助听器自语音检测常需多麦克风或传感器，增加设备复杂性与成本。
- 方法要点：使用模拟声学传递函数进行数据增强，训练基于Transformer的分类器，从刚性球体模型逐步微调至头躯模型。
- 实验或效果：在模拟头躯测试数据上达到95.52%准确率，真实录音上未微调达到80%准确率，显示泛化能力。

## 摘要（原文）

> This paper presents a simulation-based approach to own voice detection (OVD) in hearing aids using a single microphone. While OVD can significantly improve user comfort and speech intelligibility, existing solutions often rely on multiple microphones or additional sensors, increasing device complexity and cost. To enable ML-based OVD without requiring costly transfer-function measurements, we propose a data augmentation strategy based on simulated acoustic transfer functions (ATFs) that expose the model to a wide range of spatial propagation conditions. A transformer-based classifier is first trained on analytically generated ATFs and then progressively fine-tuned using numerically simulated ATFs, transitioning from a rigid-sphere model to a detailed head-and-torso representation. This hierarchical adaptation enabled the model to refine its spatial understanding while maintaining generalization. Experimental results show 95.52% accuracy on simulated head-and-torso test data. Under short-duration conditions, the model maintained 90.02% accuracy with one-second utterances. On real hearing aid recordings, the model achieved 80% accuracy without fine-tuning, aided by lightweight test-time feature compensation. This highlights the model's ability to generalize from simulated to real-world conditions, demonstrating practical viability and pointing toward a promising direction for future hearing aid design.

