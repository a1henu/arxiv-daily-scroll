---
layout: default
title: ToTMNet: FFT-Accelerated Toeplitz Temporal Mixing Network for Lightweight Remote Photoplethysmography
---

# ToTMNet: FFT-Accelerated Toeplitz Temporal Mixing Network for Lightweight Remote Photoplethysmography
**arXiv**：[2601.04159v1](https://arxiv.org/abs/2601.04159) · [PDF](https://arxiv.org/pdf/2601.04159.pdf)  
**作者**：Vladimir Frants, Sos Agaian, Karen Panetta  

**一句话要点**：提出ToTMNet，使用FFT加速的Toeplitz时序混合层替代注意力机制，实现轻量级远程光电容积描记术。

**关键词**：远程光电容积描记术, Toeplitz算子, FFT加速, 轻量级模型, 时序建模, 心率估计

## 3 点简述
- 远程光电容积描记术（rPPG）从面部视频估计血容量脉冲波形，但现有深度模型计算成本高，注意力机制导致时间复杂度二次增长。
- ToTMNet采用FFT加速的Toeplitz时序混合层，通过循环嵌入和FFT卷积实现近线性时间操作，结合门控机制和局部深度时序卷积，参数仅63k。
- 在UBFC-rPPG和SCAMPS数据集上验证，ToTMNet在心率估计中达到高精度，如UBFC-rPPG上MAE为1.055 bpm，Pearson相关0.996，门控机制对域适应有效。

## 摘要（原文）

> Remote photoplethysmography (rPPG) estimates a blood volume pulse (BVP) waveform from facial videos captured by commodity cameras. Although recent deep models improve robustness compared to classical signal-processing approaches, many methods increase computational cost and parameter count, and attention-based temporal modeling introduces quadratic scaling with respect to the temporal length. This paper proposes ToTMNet, a lightweight rPPG architecture that replaces temporal attention with an FFT-accelerated Toeplitz temporal mixing layer. The Toeplitz operator provides full-sequence temporal receptive field using a linear number of parameters in the clip length and can be applied in near-linear time using circulant embedding and FFT-based convolution. ToTMNet integrates the global Toeplitz temporal operator into a compact gated temporal mixer that combines a local depthwise temporal convolution branch with gated global Toeplitz mixing, enabling efficient long-range temporal filtering while only having 63k parameters. Experiments on two datasets, UBFC-rPPG (real videos) and SCAMPS (synthetic videos), show that ToTMNet achieves strong heart-rate estimation accuracy with a compact design. On UBFC-rPPG intra-dataset evaluation, ToTMNet reaches 1.055 bpm MAE with Pearson correlation 0.996. In a synthetic-to-real setting (SCAMPS to UBFC-rPPG), ToTMNet reaches 1.582 bpm MAE with Pearson correlation 0.994. Ablation results confirm that the gating mechanism is important for effectively using global Toeplitz mixing, especially under domain shift. The main limitation of this preprint study is the use of only two datasets; nevertheless, the results indicate that Toeplitz-structured temporal mixing is a practical and efficient alternative to attention for rPPG.

