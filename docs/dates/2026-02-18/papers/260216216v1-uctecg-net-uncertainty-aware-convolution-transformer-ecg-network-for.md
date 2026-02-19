---
layout: default
title: UCTECG-Net: Uncertainty-aware Convolution Transformer ECG Network for Arrhythmia Detection
---

# UCTECG-Net: Uncertainty-aware Convolution Transformer ECG Network for Arrhythmia Detection
**arXiv**：[2602.16216v1](https://arxiv.org/abs/2602.16216) · [PDF](https://arxiv.org/pdf/2602.16216.pdf)  
**作者**：Hamzeh Asgharnezhad, Pegah Tabarisaadi, Abbas Khosravi, Roohallah Alizadehsani, U. Rajendra Acharya  

**一句话要点**：提出UCTECG-Net，结合卷积与Transformer处理心电信号，集成不确定性量化以提升心律失常检测可靠性。

**关键词**：心电图分类, 不确定性量化, 卷积Transformer, 心律失常检测, 深度学习可靠性

## 3 点简述
- 核心问题：深度学习在心电图分类中预测可靠性不足，限制其在安全关键场景的应用。
- 方法要点：设计混合架构，联合处理原始心电信号和频谱图，并集成三种不确定性量化方法。
- 实验或效果：在MIT-BIH和PTB数据集上性能优于基线，不确定性估计更可靠，支持风险感知决策。

## 摘要（原文）

> Deep learning has improved automated electrocardiogram (ECG) classification, but limited insight into prediction reliability hinders its use in safety-critical settings. This paper proposes UCTECG-Net, an uncertainty-aware hybrid architecture that combines one-dimensional convolutions and Transformer encoders to process raw ECG signals and their spectrograms jointly. Evaluated on the MIT-BIH Arrhythmia and PTB Diagnostic datasets, UCTECG-Net outperforms LSTM, CNN1D, and Transformer baselines in terms of accuracy, precision, recall and F1 score, achieving up to 98.58% accuracy on MIT-BIH and 99.14% on PTB. To assess predictive reliability, we integrate three uncertainty quantification methods (Monte Carlo Dropout, Deep Ensembles, and Ensemble Monte Carlo Dropout) into all models and analyze their behavior using an uncertainty-aware confusion matrix and derived metrics. The results show that UCTECG-Net, particularly with Ensemble or EMCD, provides more reliable and better-aligned uncertainty estimates than competing architectures, offering a stronger basis for risk-aware ECG decision support.

