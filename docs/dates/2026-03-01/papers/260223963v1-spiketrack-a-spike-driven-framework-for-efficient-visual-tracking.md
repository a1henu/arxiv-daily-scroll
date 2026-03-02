---
layout: default
title: SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking
---

# SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking
**arXiv**：[2602.23963v1](https://arxiv.org/abs/2602.23963) · [PDF](https://arxiv.org/pdf/2602.23963.pdf)  
**作者**：Qiuyang Zhang, Jiujun Cheng, Qichao Mao, Cong Liu, Yu Fang, Yuhong Li, Mengying Ge, Shangce Gao  

**一句话要点**：提出SpikeTrack框架，通过非对称设计和记忆检索模块实现高效RGB视觉跟踪

**关键词**：脉冲神经网络, 视觉跟踪, 能效优化, 时空动态, 非对称设计, 记忆检索

## 3 点简述
- 核心问题：现有SNN跟踪框架在效率与准确性间存在权衡，未充分利用神经元时空动态
- 方法要点：采用非对称时间步扩展和单向信息流，结合记忆检索模块增强目标感知
- 实验或效果：在LaSOT数据集上超越TransT，能耗仅为1/26，达到SNN跟踪器SOTA

## 摘要（原文）

> Spiking Neural Networks (SNNs) promise energy-efficient vision, but applying them to RGB visual tracking remains difficult: Existing SNN tracking frameworks either do not fully align with spike-driven computation or do not fully leverage neurons' spatiotemporal dynamics, leading to a trade-off between efficiency and accuracy. To address this, we introduce SpikeTrack, a spike-driven framework for energy-efficient RGB object tracking. SpikeTrack employs a novel asymmetric design that uses asymmetric timestep expansion and unidirectional information flow, harnessing spatiotemporal dynamics while cutting computation. To ensure effective unidirectional information transfer between branches, we design a memory-retrieval module inspired by neural inference mechanisms. This module recurrently queries a compact memory initialized by the template to retrieve target cues and sharpen target perception over time. Extensive experiments demonstrate that SpikeTrack achieves the state-of-the-art among SNN-based trackers and remains competitive with advanced ANN trackers. Notably, it surpasses TransT on LaSOT dataset while consuming only 1/26 of its energy. To our knowledge, SpikeTrack is the first spike-driven framework to make RGB tracking both accurate and energy efficient. The code and models are available at https://github.com/faicaiwawa/SpikeTrack.

