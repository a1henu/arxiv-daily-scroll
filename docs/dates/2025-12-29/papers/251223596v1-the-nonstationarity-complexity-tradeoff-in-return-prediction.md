---
layout: default
title: The Nonstationarity-Complexity Tradeoff in Return Prediction
---

# The Nonstationarity-Complexity Tradeoff in Return Prediction
**arXiv**：[2512.23596v1](https://arxiv.org/abs/2512.23596) · [PDF](https://arxiv.org/pdf/2512.23596.pdf)  
**作者**：Agostino Capponi, Chengpiao Huang, J. Antonio Sidaoui, Kaizheng Wang, Jiacheng Zou  

**一句话要点**：提出基于锦标赛的模型选择方法，以解决股票收益预测中非平稳性与模型复杂度间的权衡问题。

**关键词**：股票收益预测, 非平稳环境, 模型选择, 锦标赛方法, 机器学习, 金融时间序列

## 3 点简述
- 研究股票收益预测中非平稳环境下的机器学习模型，揭示非平稳性与模型复杂度间的根本权衡。
- 开发新颖模型选择方法，联合优化模型类别和训练窗口大小，通过锦标赛程序在非平稳验证数据上自适应评估候选模型。
- 应用于17个行业组合收益，平均提升样本外R² 14-23%，在经济衰退期表现显著优于基准，交易策略累计收益提高31%。

## 摘要（原文）

> We investigate machine learning models for stock return prediction in non-stationary environments, revealing a fundamental nonstationarity-complexity tradeoff: complex models reduce misspecification error but require longer training windows that introduce stronger non- stationarity. We resolve this tension with a novel model selection method that jointly optimizes model class and training window size using a tournament procedure that adaptively evaluates candidates on non-stationary validation data. Our theoretical analysis demonstrates that this approach balances misspecification error, estimation variance, and non-stationarity, performing close to the best model in hindsight. Applying our method to 17 industry portfolio returns, we consistently outperform standard rolling-window benchmarks, improving out-of-sample $R^2$ by 14-23% on average. During NBER- designated recessions, improvements are substantial: our method achieves positive $R^2$ during the Gulf War recession while benchmarks are negative, and improves $R^2$ in absolute terms by at least 80bps during the 2001 recession as well as superior performance during the 2008 Financial Crisis. Economically, a trading strategy based on our selected model generates 31% higher cumulative returns averaged across the industries.

