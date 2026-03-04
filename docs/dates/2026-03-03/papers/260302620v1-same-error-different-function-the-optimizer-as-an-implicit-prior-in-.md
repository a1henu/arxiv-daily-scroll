---
layout: default
title: Same Error, Different Function: The Optimizer as an Implicit Prior in Financial Time Series
---

# Same Error, Different Function: The Optimizer as an Implicit Prior in Financial Time Series
**arXiv**：[2603.02620v1](https://arxiv.org/abs/2603.02620) · [PDF](https://arxiv.org/pdf/2603.02620.pdf)  
**作者**：Federico Vittorio Cortesi, Giuseppe Iannone, Giulia Crippa, Tomaso Poggio, Pierfrancesco Beneventano  

**一句话要点**：揭示优化器作为隐式先验在金融时间序列中的影响，强调模型评估需超越标量损失

**关键词**：金融时间序列, 欠指定问题, 优化器隐式先验, 波动率预测, 模型评估

## 3 点简述
- 核心问题：神经网络在金融时间序列中面临欠指定问题，不同模型训练管道在相同测试损失下学习到不同函数
- 方法要点：通过大规模S&P 500股票波动率预测实验，分析优化器选择如何重塑非线性响应和时间依赖性
- 实验或效果：优化器差异导致投资组合的夏普比率相近时，换手率分散近3倍，影响决策结果

## 摘要（原文）

> Neural networks applied to financial time series operate in a regime of underspecification, where model predictors achieve indistinguishable out-of-sample error. Using large-scale volatility forecasting for S$\&$P 500 stocks, we show that different model-training-pipeline pairs with identical test loss learn qualitatively different functions. Across architectures, predictive accuracy remains unchanged, yet optimizer choice reshapes non-linear response profiles and temporal dependence differently. These divergences have material consequences for decisions: volatility-ranked portfolios trace a near-vertical Sharpe-turnover frontier, with nearly $3\times$ turnover dispersion at comparable Sharpe ratios. We conclude that in underspecified settings, optimization acts as a consequential source of inductive bias, thus model evaluation should extend beyond scalar loss to encompass functional and decision-level implications.

