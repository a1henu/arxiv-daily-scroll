---
layout: default
title: Breaking Self-Attention Failure: Rethinking Query Initialization for Infrared Small Target Detection
---

# Breaking Self-Attention Failure: Rethinking Query Initialization for Infrared Small Target Detection
**arXiv**：[2601.02837v1](https://arxiv.org/abs/2601.02837) · [PDF](https://arxiv.org/pdf/2601.02837.pdf)  
**作者**：Yuteng Liu, Duanni Meng, Maoxun Yuan, Xingxing Wei  

**一句话要点**：提出SEF-DETR框架以解决红外小目标检测中自注意力失效问题

**关键词**：红外小目标检测, 自注意力机制, 查询初始化, 频率分析, 目标检测框架, 深度学习

## 3 点简述
- 核心问题：红外小目标检测中自注意力机制导致目标特征被背景淹没，查询初始化不可靠。
- 方法要点：通过频率引导补丁筛选、动态嵌入增强和可靠性一致性融合模块优化查询初始化。
- 实验或效果：在三个公开数据集上优于现有方法，提供鲁棒高效的红外小目标检测方案。

## 摘要（原文）

> Infrared small target detection (IRSTD) faces significant challenges due to the low signal-to-noise ratio (SNR), small target size, and complex cluttered backgrounds. Although recent DETR-based detectors benefit from global context modeling, they exhibit notable performance degradation on IRSTD. We revisit this phenomenon and reveal that the target-relevant embeddings of IRST are inevitably overwhelmed by dominant background features due to the self-attention mechanism, leading to unreliable query initialization and inaccurate target localization. To address this issue, we propose SEF-DETR, a novel framework that refines query initialization for IRSTD. Specifically, SEF-DETR consists of three components: Frequency-guided Patch Screening (FPS), Dynamic Embedding Enhancement (DEE), and Reliability-Consistency-aware Fusion (RCF). The FPS module leverages the Fourier spectrum of local patches to construct a target-relevant density map, suppressing background-dominated features. DEE strengthens multi-scale representations in a target-aware manner, while RCF further refines object queries by enforcing spatial-frequency consistency and reliability. Extensive experiments on three public IRSTD datasets demonstrate that SEF-DETR achieves superior detection performance compared to state-of-the-art methods, delivering a robust and efficient solution for infrared small target detection task.

