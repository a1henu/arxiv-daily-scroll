---
layout: default
title: SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection
---

# SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection
**arXiv**：[2511.21325v1](https://arxiv.org/abs/2511.21325) · [PDF](https://arxiv.org/pdf/2511.21325.pdf)  
**作者**：Ido Nitzan HIdekel, Gal lifshitz, Khen Cohen, Dan Raviv  

**一句话要点**：提出SONAR框架以解决深度伪造音频检测的泛化性问题

**关键词**：深度伪造检测, 音频信号处理, 频谱对比学习, 高频残差, 泛化性提升

## 3 点简述
- 核心问题：神经网络频谱偏差导致高频伪影未被充分利用，影响检测器泛化
- 方法要点：通过频率引导框架分离音频信号，结合对比学习优化决策边界
- 实验或效果：在ASVspoof 2021等基准上达到SOTA，收敛速度提升四倍

## 摘要（原文）

> Deepfake (DF) audio detectors still struggle to generalize to out of distribution inputs. A central reason is spectral bias, the tendency of neural networks to learn low-frequency structure before high-frequency (HF) details, which both causes DF generators to leave HF artifacts and leaves those same artifacts under-exploited by common detectors. To address this gap, we propose Spectral-cONtrastive Audio Residuals (SONAR), a frequency-guided framework that explicitly disentangles an audio signal into complementary representations. An XLSR encoder captures the dominant low-frequency content, while the same cloned path, preceded by learnable SRM, value-constrained high-pass filters, distills faint HF residuals. Frequency cross-attention reunites the two views for long- and short-range frequency dependencies, and a frequency-aware Jensen-Shannon contrastive loss pulls real content-noise pairs together while pushing fake embeddings apart, accelerating optimization and sharpening decision boundaries. Evaluated on the ASVspoof 2021 and in-the-wild benchmarks, SONAR attains state-of-the-art performance and converges four times faster than strong baselines. By elevating faint high-frequency residuals to first-class learning signals, SONAR unveils a fully data-driven, frequency-guided contrastive framework that splits the latent space into two disjoint manifolds: natural-HF for genuine audio and distorted-HF for synthetic audio, thereby sharpening decision boundaries. Because the scheme operates purely at the representation level, it is architecture-agnostic and, in future work, can be seamlessly integrated into any model or modality where subtle high-frequency cues are decisive.

