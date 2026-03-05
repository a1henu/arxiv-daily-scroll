---
layout: default
title: Activation Outliers in Transformer Quantization: Reproduction, Statistical Analysis, and Deployment Tradeoffs
---

# Activation Outliers in Transformer Quantization: Reproduction, Statistical Analysis, and Deployment Tradeoffs
**arXiv**：[2603.04308v1](https://arxiv.org/abs/2603.04308) · [PDF](https://arxiv.org/pdf/2603.04308.pdf)  
**作者**：Pranav Kumar Kaliaperumal  

**一句话要点**：复现与分析Transformer量化中的激活异常值，评估缓解策略与部署权衡

**关键词**：Transformer量化, 激活异常值, 后训练量化, 混合精度, 部署权衡, 统计建模

## 3 点简述
- 核心问题：Transformer后训练量化因结构化激活异常值导致严重精度下降，如BERT-base在QNLI上W8A8量化精度下降35.33点。
- 方法要点：通过统计分析和系统评估，比较混合精度量化、分组量化等方法，强调通道感知精度分配的重要性。
- 实验或效果：混合精度量化恢复精度接近FP32基线，分组量化对分组结构敏感，部署分析显示延迟和内存使用差异小。

## 摘要（原文）

> Post-training quantization (PTQ) of transformers is known to suffer from severe accuracy degradation due to structured activation outliers, as originally analyzed by Bondarenko et al. (EMNLP 2021) in work associated with Qualcomm AI Research. This paper provides a reproducible empirical reproduction and systems-level extension of that phenomenon in BERT-base fine-tuned on QNLI. When global W8A8 quantization is applied, validation accuracy drops sharply from 89.66% (FP32) to 54.33%, a decrease of 35.33 points. Statistical analysis of FP32 activations shows strongly heavy-tailed behavior that intensifies with model depth: kurtosis reaches 271 in the final layers and approximately 55% of activation energy is concentrated in the top 1% of channels. We evaluate several mitigation strategies. Mixed precision PTQ restores accuracy close to the FP32 baseline (89.42%). Per-embedding-group (PEG) quantization shows strong sensitivity to grouping structure, improving accuracy from 66.12% with three groups to 86.18% with four groups. In contrast, percentile-based calibration, even at thresholds between 99.0 and 99.99, fails to recover accuracy (about 50.54%), indicating that large activation channels encode structured signal rather than rare noise. Deployment profiling on an RTX 3050 GPU shows minimal differences in latency and memory usage across methods (median latency about 58-59 ms; VRAM usage about 484-486 MB), highlighting the importance of hardware-aware evaluation. Overall, the results show that PTQ failure in transformers is primarily driven by structured channel dominance amplified through residual connections. Effective mitigation therefore requires channel-aware precision allocation rather than scalar clipping alone.

