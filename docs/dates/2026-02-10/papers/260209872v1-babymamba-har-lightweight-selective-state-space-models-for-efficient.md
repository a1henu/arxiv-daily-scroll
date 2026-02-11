---
layout: default
title: BabyMamba-HAR: Lightweight Selective State Space Models for Efficient Human Activity Recognition on Resource Constrained Devices
---

# BabyMamba-HAR: Lightweight Selective State Space Models for Efficient Human Activity Recognition on Resource Constrained Devices
**arXiv**：[2602.09872v1](https://arxiv.org/abs/2602.09872) · [PDF](https://arxiv.org/pdf/2602.09872.pdf)  
**作者**：Mridankan Mandal  

**一句话要点**：提出BabyMamba-HAR框架，通过轻量级选择性状态空间模型在资源受限设备上高效实现人类活动识别。

**关键词**：人类活动识别, 选择性状态空间模型, 轻量级架构, 资源受限设备, TinyML, 传感器数据处理

## 3 点简述
- 核心问题：资源受限设备上人类活动识别需平衡内存、计算与准确性，且需适应异构传感器配置。
- 方法要点：设计两种轻量级Mamba架构，结合权重绑定的双向扫描和轻量时间注意力池化，优化计算复杂度。
- 实验或效果：在八个基准测试中，Crossover-BiDir-BabyMamba-HAR平均宏F1分数达86.52%，参数约27K，MACs约2.21M，性能匹配TinyHAR但计算量显著减少。

## 摘要（原文）

> Human activity recognition (HAR) on wearable and mobile devices is constrained by memory footprint and computational budget, yet competitive accuracy must be maintained across heterogeneous sensor configurations. Selective state space models (SSMs) offer linear time sequence processing with input dependent gating, presenting a compelling alternative to quadratic complexity attention mechanisms. However, the design space for deploying SSMs in the TinyML regime remains largely unexplored. In this paper, BabyMamba-HAR is introduced, a framework comprising two novel lightweight Mamba inspired architectures optimized for resource constrained HAR: (1) CI-BabyMamba-HAR, using a channel independent stem that processes each sensor channel through shared weight, but instance independent transformations to prevent cross channel noise propagation, and (2) Crossover-BiDir-BabyMamba-HAR, using an early fusion stem that achieves channel count independent computational complexity. Both variants incorporate weight tied bidirectional scanning and lightweight temporal attention pooling. Through evaluation across eight diverse benchmarks, it is demonstrated that Crossover-BiDir-BabyMamba-HAR achieves 86.52% average macro F1-score with approximately 27K parameters and 2.21M MACs, matching TinyHAR (86.16%) while requiring 11x fewer MACs on high channel datasets. Systematic ablation studies reveal that bidirectional scanning contributes up to 8.42% F1-score improvement, and gated temporal attention provides up to 8.94% F1-score gain over mean pooling. These findings establish practical design principles for deploying selective state space models as efficient TinyML backbones for HAR.

