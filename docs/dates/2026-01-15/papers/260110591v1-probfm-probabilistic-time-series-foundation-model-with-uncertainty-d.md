---
layout: default
title: ProbFM: Probabilistic Time Series Foundation Model with Uncertainty Decomposition
---

# ProbFM: Probabilistic Time Series Foundation Model with Uncertainty Decomposition
**arXiv**：[2601.10591v1](https://arxiv.org/abs/2601.10591) · [PDF](https://arxiv.org/pdf/2601.10591.pdf)  
**作者**：Arundeep Chinta, Lucas Vinh Tran, Jay Katukuri  

**一句话要点**：提出ProbFM概率时间序列基础模型，通过深度证据回归实现金融预测中的不确定性分解

**关键词**：时间序列基础模型, 不确定性量化, 深度证据回归, 金融预测, 概率建模

## 3 点简述
- 现有时间序列基础模型在不确定性量化上存在限制，如分布假设过强或缺乏分解机制
- ProbFM基于Transformer和深度证据回归，单次前向传播即可学习不确定性并分解为认知与偶然成分
- 在加密货币回报预测实验中，DER方法保持预测准确性，同时提供明确的不确定性分解

## 摘要（原文）

> Time Series Foundation Models (TSFMs) have emerged as a promising approach for zero-shot financial forecasting, demonstrating strong transferability and data efficiency gains. However, their adoption in financial applications is hindered by fundamental limitations in uncertainty quantification: current approaches either rely on restrictive distributional assumptions, conflate different sources of uncertainty, or lack principled calibration mechanisms. While recent TSFMs employ sophisticated techniques such as mixture models, Student's t-distributions, or conformal prediction, they fail to address the core challenge of providing theoretically-grounded uncertainty decomposition. For the very first time, we present a novel transformer-based probabilistic framework, ProbFM (probabilistic foundation model), that leverages Deep Evidential Regression (DER) to provide principled uncertainty quantification with explicit epistemic-aleatoric decomposition. Unlike existing approaches that pre-specify distributional forms or require sampling-based inference, ProbFM learns optimal uncertainty representations through higher-order evidence learning while maintaining single-pass computational efficiency. To rigorously evaluate the core DER uncertainty quantification approach independent of architectural complexity, we conduct an extensive controlled comparison study using a consistent LSTM architecture across five probabilistic methods: DER, Gaussian NLL, Student's-t NLL, Quantile Loss, and Conformal Prediction. Evaluation on cryptocurrency return forecasting demonstrates that DER maintains competitive forecasting accuracy while providing explicit epistemic-aleatoric uncertainty decomposition. This work establishes both an extensible framework for principled uncertainty quantification in foundation models and empirical evidence for DER's effectiveness in financial applications.

