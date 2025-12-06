---
layout: default
title: Denoise to Track: Harnessing Video Diffusion Priors for Robust Correspondence
---

# Denoise to Track: Harnessing Video Diffusion Priors for Robust Correspondence
**arXiv**：[2512.04619v1](https://arxiv.org/abs/2512.04619) · [PDF](https://arxiv.org/pdf/2512.04619.pdf)  
**作者**：Tianyu Yuan, Yuanbo Yang, Lin-Zhuo Chen, Yao Yao, Zhuzhong Qian  

**一句话要点**：提出HeFT框架，利用视频扩散先验实现零样本点跟踪

**关键词**：零样本跟踪, 视频扩散模型, 特征选择, 注意力机制, 对应估计

## 3 点简述
- 分析VDiT内部表示，发现注意力头与低频成分对匹配至关重要
- 设计头与频率感知特征选择策略，提升跟踪鲁棒性
- 在TAP-Vid基准上达到零样本最优，接近监督方法性能

## 摘要（原文）

> In this work, we introduce HeFT (Head-Frequency Tracker), a zero-shot point tracking framework that leverages the visual priors of pretrained video diffusion models. To better understand how they encode spatiotemporal information, we analyze the internal representations of Video Diffusion Transformer (VDiT). Our analysis reveals that attention heads act as minimal functional units with distinct specializations for matching, semantic understanding, and positional encoding. Additionally, we find that the low-frequency components in VDiT features are crucial for establishing correspondences, whereas the high-frequency components tend to introduce noise. Building on these insights, we propose a head- and frequency-aware feature selection strategy that jointly selects the most informative attention head and low-frequency components to enhance tracking performance. Specifically, our method extracts discriminative features through single-step denoising, applies feature selection, and employs soft-argmax localization with forward-backward consistency checks for correspondence estimation. Extensive experiments on TAP-Vid benchmarks demonstrate that HeFT achieves state-of-the-art zero-shot tracking performance, approaching the accuracy of supervised methods while eliminating the need for annotated training data. Our work further underscores the promise of video diffusion models as powerful foundation models for a wide range of downstream tasks, paving the way toward unified visual foundation models.

