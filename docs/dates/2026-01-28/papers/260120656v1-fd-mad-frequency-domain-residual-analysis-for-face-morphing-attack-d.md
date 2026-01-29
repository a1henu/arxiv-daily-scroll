---
layout: default
title: FD-MAD: Frequency-Domain Residual Analysis for Face Morphing Attack Detection
---

# FD-MAD: Frequency-Domain Residual Analysis for Face Morphing Attack Detection
**arXiv**：[2601.20656v1](https://arxiv.org/abs/2601.20656) · [PDF](https://arxiv.org/pdf/2601.20656.pdf)  
**作者**：Diogo J. Paulo, Hugo Proença, João C. Neves  

**一句话要点**：提出基于频域残差分析与区域融合的轻量级人脸伪造检测方法，以提升跨数据集检测性能。

**关键词**：人脸伪造检测, 频域分析, 跨数据集评估, 轻量级方法, 马尔可夫随机场, 单图像检测

## 3 点简述
- 核心问题：单图像人脸伪造检测在跨数据集场景中性能不足，缺乏可信参考。
- 方法要点：利用频域残差分离信号频率与自然谱衰减，结合马尔可夫随机场融合面部区域证据。
- 实验或效果：在FRLL-Morph和MAD22数据集上平均EER分别为1.85%和6.12%，仅用频谱特征实现低错误率。

## 摘要（原文）

> Face morphing attacks present a significant threat to face recognition systems used in electronic identity enrolment and border control, particularly in single-image morphing attack detection (S-MAD) scenarios where no trusted reference is available. In spite of the vast amount of research on this problem, morph detection systems struggle in cross-dataset scenarios. To address this problem, we introduce a region-aware frequency-based morph detection strategy that drastically improves over strong baseline methods in challenging cross-dataset and cross-morph settings using a lightweight approach. Having observed the separability of bona fide and morph samples in the frequency domain of different facial parts, our approach 1) introduces the concept of residual frequency domain, where the frequency of the signal is decoupled from the natural spectral decay to easily discriminate between morph and bona fide data; 2) additionally, we reason in a global and local manner by combining the evidence from different facial regions in a Markov Random Field, which infers a globally consistent decision. The proposed method, trained exclusively on the synthetic morphing attack detection development dataset (SMDD), is evaluated in challenging cross-dataset and cross-morph settings on FRLL-Morph and MAD22 sets. Our approach achieves an average equal error rate (EER) of 1.85\% on FRLL-Morph and ranks second on MAD22 with an average EER of 6.12\%, while also obtaining a good bona fide presentation classification error rate (BPCER) at a low attack presentation classification error rate (APCER) using only spectral features. These findings indicate that Fourier-domain residual modeling with structured regional fusion offers a competitive alternative to deep S-MAD architectures.

