---
layout: default
title: Bayesian Transformer for Probabilistic Load Forecasting in Smart Grids
---

# Bayesian Transformer for Probabilistic Load Forecasting in Smart Grids
**arXiv**：[2603.07899v1](https://arxiv.org/abs/2603.07899) · [PDF](https://arxiv.org/pdf/2603.07899.pdf)  
**作者**：Sajib Debnath, Md. Uzzal Mia  

**一句话要点**：提出贝叶斯Transformer框架，用于智能电网中概率负荷预测，以解决极端天气下预测不确定性校准不足的问题。

**关键词**：概率负荷预测, 贝叶斯Transformer, 不确定性校准, 智能电网, 极端天气预测, 蒙特卡洛Dropout

## 3 点简述
- 核心问题：现有深度学习模型在极端天气分布偏移下产生过度自信的点预测，缺乏可靠的不确定性估计。
- 方法要点：集成蒙特卡洛Dropout、变分前馈层和随机注意力三种不确定性机制于PatchTST骨干网络，结合多分位数损失和校准后处理。
- 实验或效果：在五个电网数据集上评估，显示在24小时基准上CRPS为0.0289，优于深度集成和确定性LSTM，并在热浪和寒潮事件中保持高预测区间覆盖率。

## 摘要（原文）

> The reliable operation of modern power grids requires probabilistic load forecasts with well-calibrated uncertainty estimates. However, existing deep learning models produce overconfident point predictions that fail catastrophically under extreme weather distributional shifts. This study proposes a Bayesian Transformer (BT) framework that integrates three complementary uncertainty mechanisms into a PatchTST backbone: Monte Carlo Dropout for epistemic parameter uncertainty, variational feed-forward layers with log-uniform weight priors, and stochastic attention with learnable Gaussian noise perturbations on pre-softmax logits, representing, to the best of our knowledge, the first application of Bayesian attention to probabilistic load forecasting. A seven-level multi-quantile pinball-loss prediction head and post-training isotonic regression calibration produce sharp, near-nominally covered prediction intervals. Evaluation of five grid datasets (PJM, ERCOT, ENTSO-E Germany, France, and Great Britain) augmented with NOAA covariates across 24, 48, and 168-hour horizons demonstrates state-of-the-art performance. On the primary benchmark (PJM, H=24h), BT achieves a CRPS of 0.0289, improving 7.4% over Deep Ensembles and 29.9% over the deterministic LSTM, with 90.4% PICP at the 90% nominal level and the narrowest prediction intervals (4,960 MW) among all probabilistic baselines. During heat-wave and cold snap events, BT maintained 89.6% and 90.1% PICP respectively, versus 64.7% and 67.2% for the deterministic LSTM, confirming that Bayesian epistemic uncertainty naturally widens intervals for out-of-distribution inputs. Calibration remained stable across all horizons (89.8-90.4% PICP), while ablation confirmed that each component contributed a distinct value. The calibrated outputs directly support risk-based reserve sizing, stochastic unit commitment, and demand response activation.

