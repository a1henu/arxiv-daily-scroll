---
layout: default
title: Integrated Prediction and Multi-period Portfolio Optimization
---

# Integrated Prediction and Multi-period Portfolio Optimization
**arXiv**：[2512.11273v1](https://arxiv.org/abs/2512.11273) · [PDF](https://arxiv.org/pdf/2512.11273.pdf)  
**作者**：Qi Deng, Yuxuan Linghu, Zhiyuan Liu  

**一句话要点**：提出IPMO模型以解决多期投资组合优化中预测与决策脱节问题

**关键词**：多期投资组合优化, 端到端学习, 可微优化, 交易成本, 风险调整收益, 时间序列预测

## 3 点简述
- 核心问题：传统两阶段方法预测与决策脱节，忽略交易成本影响
- 方法要点：集成预测与优化，采用可微凸优化层和MDFP微分方案提升可扩展性
- 实验或效果：在真实市场数据上，IPMO在风险调整后净收益和分配路径上优于基准

## 摘要（原文）

> Multi-period portfolio optimization is important for real portfolio management, as it accounts for transaction costs, path-dependent risks, and the intertemporal structure of trading decisions that single-period models cannot capture. Classical methods usually follow a two-stage framework: machine learning algorithms are employed to produce forecasts that closely fit the realized returns, and the predicted values are then used in a downstream portfolio optimization problem to determine the asset weights. This separation leads to a fundamental misalignment between predictions and decision outcomes, while also ignoring the impact of transaction costs. To bridge this gap, recent studies have proposed the idea of end-to-end learning, integrating the two stages into a single pipeline. This paper introduces IPMO (Integrated Prediction and Multi-period Portfolio Optimization), a model for multi-period mean-variance portfolio optimization with turnover penalties. The predictor generates multi-period return forecasts that parameterize a differentiable convex optimization layer, which in turn drives learning via portfolio performance. For scalability, we introduce a mirror-descent fixed-point (MDFP) differentiation scheme that avoids factorizing the Karush-Kuhn-Tucker (KKT) systems, which thus yields stable implicit gradients and nearly scale-insensitive runtime as the decision horizon grows. In experiments with real market data and two representative time-series prediction models, the IPMO method consistently outperforms the two-stage benchmarks in risk-adjusted performance net of transaction costs and achieves more coherent allocation paths. Our results show that integrating machine learning prediction with optimization in the multi-period setting improves financial outcomes and remains computationally tractable.

