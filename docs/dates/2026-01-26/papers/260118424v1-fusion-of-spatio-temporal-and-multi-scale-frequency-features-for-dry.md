---
layout: default
title: Fusion of Spatio-Temporal and Multi-Scale Frequency Features for Dry Electrodes MI-EEG Decoding
---

# Fusion of Spatio-Temporal and Multi-Scale Frequency Features for Dry Electrodes MI-EEG Decoding
**arXiv**：[2601.18424v1](https://arxiv.org/abs/2601.18424) · [PDF](https://arxiv.org/pdf/2601.18424.pdf)  
**作者**：Tianyi Gong, Can Han, Junxi Wu, Dahong Qian  

**一句话要点**：提出STGMFM三支框架，融合时空与多尺度频率特征以解决干电极MI-EEG解码中的噪声和分布偏移问题。

**关键词**：干电极脑电解码, 时空图神经网络, 多尺度频率特征, 运动想象, 噪声鲁棒性, 决策融合

## 3 点简述
- 干电极MI-EEG存在信噪比低、相位对齐差和会话间方差大等核心问题，导致数据分布偏移和特征不稳定。
- 方法采用三支框架：双图阶建模时空依赖，多尺度频率混合支捕获稳健包络动态，决策级融合增强噪声容忍。
- 在收集的干电极MI-EEG数据上，STGMFM优于CNN/Transformer/图基线，代码已开源。

## 摘要（原文）

> Dry-electrode Motor Imagery Electroencephalography (MI-EEG) enables fast, comfortable, real-world Brain Computer Interface by eliminating gels and shortening setup for at-home and wearable use.However, dry recordings pose three main issues: lower Signal-to-Noise Ratio with more baseline drift and sudden transients; weaker and noisier data with poor phase alignment across trials; and bigger variances between sessions. These drawbacks lead to larger data distribution shift, making features less stable for MI-EEG tasks.To address these problems, we introduce STGMFM, a tri-branch framework tailored for dry-electrode MI-EEG, which models complementary spatio-temporal dependencies via dual graph orders, and captures robust envelope dynamics with a multi-scale frequency mixing branch, motivated by the observation that amplitude envelopes are less sensitive to contact variability than instantaneous waveforms. Physiologically meaningful connectivity priors guide learning, and decision-level fusion consolidates a noise-tolerant consensus. On our collected dry-electrode MI-EEG, STGMFM consistently surpasses competitive CNN/Transformer/graph baselines. Codes are available at https://github.com/Tianyi-325/STGMFM.

