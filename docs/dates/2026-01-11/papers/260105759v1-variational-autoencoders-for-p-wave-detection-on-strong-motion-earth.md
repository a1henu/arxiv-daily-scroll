---
layout: default
title: Variational Autoencoders for P-wave Detection on Strong Motion Earthquake Spectrograms
---

# Variational Autoencoders for P-wave Detection on Strong Motion Earthquake Spectrograms
**arXiv**：[2601.05759v1](https://arxiv.org/abs/2601.05759) · [PDF](https://arxiv.org/pdf/2601.05759.pdf)  
**作者**：Turkan Simge Ispak, Salih Tileylioglu, Erdem Akagunduz  

**一句话要点**：提出基于注意力机制的变分自编码器，用于强震动地震谱图的P波检测，以提升地震早期预警性能。

**关键词**：变分自编码器, P波检测, 地震早期预警, 自监督学习, 异常检测, 注意力机制

## 3 点简述
- 核心问题：强震动记录中P波检测面临高噪声、标记数据少和波形复杂等挑战。
- 方法要点：将P波到达检测重构为自监督异常检测任务，通过网格搜索评估不同架构在重建保真度与异常判别间的权衡。
- 实验或效果：注意力机制模型在近源范围（0-40公里）达到0.91的AUC，优于跳跃连接模型，适合即时预警应用。

## 摘要（原文）

> Accurate P-wave detection is critical for earthquake early warning, yet strong-motion records pose challenges due to high noise levels, limited labeled data, and complex waveform characteristics. This study reframes P-wave arrival detection as a self-supervised anomaly detection task to evaluate how architectural variations regulate the trade-off between reconstruction fidelity and anomaly discrimination. Through a comprehensive grid search of 492 Variational Autoencoder configurations, we show that while skip connections minimize reconstruction error (Mean Absolute Error approximately 0.0012), they induce "overgeneralization", allowing the model to reconstruct noise and masking the detection signal. In contrast, attention mechanisms prioritize global context over local detail and yield the highest detection performance with an area-under-the-curve of 0.875. The attention-based Variational Autoencoder achieves an area-under-the-curve of 0.91 in the 0 to 40-kilometer near-source range, demonstrating high suitability for immediate early warning applications. These findings establish that architectural constraints favoring global context over pixel-perfect reconstruction are essential for robust, self-supervised P-wave detection.

