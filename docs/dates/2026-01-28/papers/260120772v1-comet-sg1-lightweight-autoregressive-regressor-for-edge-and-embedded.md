---
layout: default
title: COMET-SG1: Lightweight Autoregressive Regressor for Edge and Embedded AI
---

# COMET-SG1: Lightweight Autoregressive Regressor for Edge and Embedded AI
**arXiv**：[2601.20772v1](https://arxiv.org/abs/2601.20772) · [PDF](https://arxiv.org/pdf/2601.20772.pdf)  
**作者**：Shakhyar Gogoi  

**一句话要点**：提出COMET-SG1轻量自回归回归模型，用于边缘和嵌入式AI中的稳定时间序列预测。

**关键词**：时间序列预测, 边缘AI, 自回归模型, 轻量模型, 稳定性优化

## 3 点简述
- 核心问题：边缘AI系统需在自回归推理下实现有界长期行为，避免预测误差累积。
- 方法要点：采用线性行为空间编码、记忆锚定转移估计和确定性状态更新，优先稳定性。
- 实验效果：在非平稳合成数据上，短期精度竞争，长期漂移显著低于MLP、LSTM和k近邻基线。

## 摘要（原文）

> COMET-SG1 is a lightweight, stability-oriented autoregressive regression model designed for time-series prediction on edge and embedded AI systems. Unlike recurrent neural networks or transformer-based sequence models, COMET-SG1 operates through linear behavior-space encoding, memory-anchored transition estimation, and deterministic state updates. This structure prioritizes bounded long-horizon behavior under fully autoregressive inference, a critical requirement for edge deployment where prediction errors accumulate over time. Experiments on non-stationary synthetic time-series data demonstrate that COMET-SG1 achieves competitive short-horizon accuracy while exhibiting significantly reduced long-horizon drift compared to MLP, LSTM, and k-nearest neighbor baselines. With a compact parameter footprint and operations compatible with fixed-point arithmetic, COMET-SG1 provides a practical and interpretable approach for stable autoregressive prediction in edge and embedded AI applications.

