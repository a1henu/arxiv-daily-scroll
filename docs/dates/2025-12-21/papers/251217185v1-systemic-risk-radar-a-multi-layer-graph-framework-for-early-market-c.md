---
layout: default
title: Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Warning
---

# Systemic Risk Radar: A Multi-Layer Graph Framework for Early Market Crash Warning
**arXiv**：[2512.17185v1](https://arxiv.org/abs/2512.17185) · [PDF](https://arxiv.org/pdf/2512.17185.pdf)  
**作者**：Sandeep Neela  

**一句话要点**：提出多图层框架SRR以早期预警市场崩溃，通过建模金融市场交互结构。

**关键词**：系统性风险预警, 多图层图模型, 金融市场结构分析, 图神经网络, 早期预警系统, 危机预测

## 3 点简述
- 核心问题：金融危机的预测挑战在于系统性脆弱性源于市场参与者间的动态交互，而非孤立价格变动。
- 方法要点：SRR将金融市场建模为多图层图，捕捉结构变化以检测崩溃前兆。
- 实验或效果：在三次重大危机中评估，显示图结构特征比基于特征的模型提供更早预警信号。

## 摘要（原文）

> Financial crises emerge when structural vulnerabilities accumulate across sectors, markets, and investor behavior. Predicting these systemic transitions is challenging because they arise from evolving interactions between market participants, not isolated price movements alone. We present Systemic Risk Radar (SRR), a framework that models financial markets as multi-layer graphs to detect early signs of systemic fragility and crash-regime transitions.
>   We evaluate SRR across three major crises: the Dot-com crash, the Global Financial Crisis, and the COVID-19 shock. Our experiments compare snapshot GNNs, a simplified temporal GNN prototype, and standard baselines (logistic regression and Random Forest). Results show that structural network information provides useful early-warning signals compared to feature-based models alone.
>   This correlation-based instantiation of SRR demonstrates that graph-derived features capture meaningful changes in market structure during stress events. The findings motivate extending SRR with additional graph layers (sector/factor exposure, sentiment) and more expressive temporal architectures (LSTM/GRU or Transformer encoders) to better handle diverse crisis types.

