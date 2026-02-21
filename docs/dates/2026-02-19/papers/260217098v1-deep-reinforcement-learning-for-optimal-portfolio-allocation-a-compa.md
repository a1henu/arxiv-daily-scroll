---
layout: default
title: Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization
---

# Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization
**arXiv**：[2602.17098v1](https://arxiv.org/abs/2602.17098) · [PDF](https://arxiv.org/pdf/2602.17098.pdf)  
**作者**：Srijan Sood, Kassiani Papasotiriou, Marius Vaiciulis, Tucker Balch  

**一句话要点**：比较深度强化学习与均值方差优化在投资组合分配中的性能

**关键词**：深度强化学习, 投资组合优化, 均值方差优化, 回测分析, 金融科技

## 3 点简述
- 核心问题：投资组合优化需平衡收益与风险，传统方法如均值方差优化在实践中广泛应用。
- 方法要点：使用模型无关深度强化学习代理，基于历史市场数据训练，并与均值方差优化进行对比。
- 实验或效果：回测显示深度强化学习在夏普比率、最大回撤和绝对收益等指标上表现优异。

## 摘要（原文）

> Portfolio Management is the process of overseeing a group of investments, referred to as a portfolio, with the objective of achieving predetermined investment goals. Portfolio optimization is a key component that involves allocating the portfolio assets so as to maximize returns while minimizing risk taken. It is typically carried out by financial professionals who use a combination of quantitative techniques and investment expertise to make decisions about the portfolio allocation.
>   Recent applications of Deep Reinforcement Learning (DRL) have shown promising results when used to optimize portfolio allocation by training model-free agents on historical market data. Many of these methods compare their results against basic benchmarks or other state-of-the-art DRL agents but often fail to compare their performance against traditional methods used by financial professionals in practical settings. One of the most commonly used methods for this task is Mean-Variance Portfolio Optimization (MVO), which uses historical time series information to estimate expected asset returns and covariances, which are then used to optimize for an investment objective.
>   Our work is a thorough comparison between model-free DRL and MVO for optimal portfolio allocation. We detail the specifics of how to make DRL for portfolio optimization work in practice, also noting the adjustments needed for MVO. Backtest results demonstrate strong performance of the DRL agent across many metrics, including Sharpe ratio, maximum drawdowns, and absolute returns.

