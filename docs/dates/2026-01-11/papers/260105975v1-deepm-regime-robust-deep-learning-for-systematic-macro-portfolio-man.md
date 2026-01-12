---
layout: default
title: DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management
---

# DeePM: Regime-Robust Deep Learning for Systematic Macro Portfolio Management
**arXiv**：[2601.05975v1](https://arxiv.org/abs/2601.05975) · [PDF](https://arxiv.org/pdf/2601.05975.pdf)  
**作者**：Kieran Wood, Stephen J. Roberts, Stefan Zohren  

**一句话要点**：提出DeePM以解决宏观投资组合管理中的异步数据、低信噪比和分布稳健性问题。

**关键词**：宏观投资组合管理, 深度学习, 因果延迟机制, 宏观经济图先验, 分布稳健优化, 风险调整收益

## 3 点简述
- 核心问题：处理异步宏观数据、低信噪比和风险调整收益的稳健优化。
- 方法要点：采用因果延迟机制、宏观经济图先验和分布稳健目标函数。
- 实验或效果：在2010-2025年回测中，风险调整收益约为传统策略的两倍。

## 摘要（原文）

> We propose DeePM (Deep Portfolio Manager), a structured deep-learning macro portfolio manager trained end-to-end to maximize a robust, risk-adjusted utility. DeePM addresses three fundamental challenges in financial learning: (1) it resolves the asynchronous "ragged filtration" problem via a Directed Delay (Causal Sieve) mechanism that prioritizes causal impulse-response learning over information freshness; (2) it combats low signal-to-noise ratios via a Macroeconomic Graph Prior, regularizing cross-asset dependence according to economic first principles; and (3) it optimizes a distributionally robust objective where a smooth worst-window penalty serves as a differentiable proxy for Entropic Value-at-Risk (EVaR) - a window-robust utility encouraging strong performance in the most adverse historical subperiods. In large-scale backtests from 2010-2025 on 50 diversified futures with highly realistic transaction costs, DeePM attains net risk-adjusted returns that are roughly twice those of classical trend-following strategies and passive benchmarks, solely using daily closing prices. Furthermore, DeePM improves upon the state-of-the-art Momentum Transformer architecture by roughly fifty percent. The model demonstrates structural resilience across the 2010s "CTA (Commodity Trading Advisor) Winter" and the post-2020 volatility regime shift, maintaining consistent performance through the pandemic, inflation shocks, and the subsequent higher-for-longer environment. Ablation studies confirm that strictly lagged cross-sectional attention, graph prior, principled treatment of transaction costs, and robust minimax optimization are the primary drivers of this generalization capability.

