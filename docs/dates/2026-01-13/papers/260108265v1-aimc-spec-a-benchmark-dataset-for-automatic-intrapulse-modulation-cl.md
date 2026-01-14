---
layout: default
title: AIMC-Spec: A Benchmark Dataset for Automatic Intrapulse Modulation Classification under Variable Noise Conditions
---

# AIMC-Spec: A Benchmark Dataset for Automatic Intrapulse Modulation Classification under Variable Noise Conditions
**arXiv**：[2601.08265v1](https://arxiv.org/abs/2601.08265) · [PDF](https://arxiv.org/pdf/2601.08265.pdf)  
**作者**：Sebastian L. Cocks, Salvador Dreo, Feras Dayoub  

**一句话要点**：提出AIMC-Spec基准数据集，以解决雷达信号自动脉内调制分类在可变噪声条件下缺乏标准化数据的问题。

**关键词**：自动脉内调制分类, 雷达信号分析, 基准数据集, 频谱图分类, 深度学习评估

## 3 点简述
- 核心问题：自动脉内调制分类领域因缺乏标准化数据集而进展受阻，尤其在噪声或退化条件下。
- 方法要点：创建包含33种调制类型和13个信噪比水平的合成数据集，用于基于频谱图的图像分类。
- 实验或效果：评估五种深度学习算法，显示性能差异显著，频率调制信号在低信噪比下分类更可靠。

## 摘要（原文）

> A lack of standardized datasets has long hindered progress in automatic intrapulse modulation classification (AIMC) - a critical task in radar signal analysis for electronic support systems, particularly under noisy or degraded conditions. AIMC seeks to identify the modulation type embedded within a single radar pulse from its complex in-phase and quadrature (I/Q) representation, enabling automated interpretation of intrapulse structure. This paper introduces AIMC-Spec, a comprehensive synthetic dataset for spectrogram-based image classification, encompassing 33 modulation types across 13 signal-to-noise ratio (SNR) levels. To benchmark AIMC-Spec, five representative deep learning algorithms - ranging from lightweight CNNs and denoising architectures to transformer-based networks - were re-implemented and evaluated under a unified input format. The results reveal significant performance variation, with frequency-modulated (FM) signals classified more reliably than phase or hybrid types, particularly at low SNRs. A focused FM-only test further highlights how modulation type and network architecture influence classifier robustness. AIMC-Spec establishes a reproducible baseline and provides a foundation for future research and standardization in the AIMC domain.

