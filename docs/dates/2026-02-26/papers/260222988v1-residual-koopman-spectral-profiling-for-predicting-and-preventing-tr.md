---
layout: default
title: Residual Koopman Spectral Profiling for Predicting and Preventing Transformer Training Instability
---

# Residual Koopman Spectral Profiling for Predicting and Preventing Transformer Training Instability
**arXiv**：[2602.22988v1](https://arxiv.org/abs/2602.22988) · [PDF](https://arxiv.org/pdf/2602.22988.pdf)  
**作者**：Bum Jun Kim, Shohei Taniguchi, Makoto Kawano, Yusuke Iwasawa, Yutaka Matsuo  

**一句话要点**：提出残差库普曼谱分析以预测和防止Transformer训练不稳定性

**关键词**：Transformer训练稳定性, 库普曼谱分析, 动态模式分解, 训练发散预测, 谱整形, 语言建模

## 3 点简述
- 核心问题：Transformer训练发散浪费计算资源，需在训练前评估失败概率。
- 方法要点：通过初始化时单次前向传递，提取残差快照的库普曼谱特征，用近单位谱质量量化不稳定性风险。
- 实验或效果：在广泛配置中AUROC达0.995，库普曼谱整形可将发散率从66.7%降至12.5%，并提高学习率。

## 摘要（原文）

> Training divergence in transformers wastes compute, yet practitioners discover instability only after expensive runs begin. They therefore need an expected probability of failure for a transformer before training starts. Our study of Residual Koopman Spectral Profiling (RKSP) provides such an estimate. From a single forward pass at initialization, RKSP extracts Koopman spectral features by applying whitened dynamic mode decomposition to layer-wise residual snapshots. Our central diagnostic, the near-unit spectral mass, quantifies the fraction of modes concentrated near the unit circle, which captures instability risk. For predicting divergence across extensive configurations, this estimator achieves an AUROC of 0.995, outperforming the best gradient baseline. We further make this diagnostic actionable through Koopman Spectral Shaping (KSS), which reshapes spectra during training. We empirically validate that our method works in practice: RKSP predicts divergence at initialization, and when RKSP flags high risk, turning on KSS successfully prevents divergence. In the challenging high learning rate regime without normalization layers, KSS reduces the divergence rate from 66.7% to 12.5% and enables learning rates that are 50% to 150% higher. These findings generalize to WikiText-103 language modeling, vision transformers on CIFAR-10, and pretrained language models, including GPT-2 and LLaMA-2 up to 7B, as well as emerging architectures such as MoE, Mamba-style SSMs, and KAN.

