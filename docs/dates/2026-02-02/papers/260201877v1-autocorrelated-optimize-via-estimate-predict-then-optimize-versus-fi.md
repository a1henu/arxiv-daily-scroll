---
layout: default
title: Autocorrelated Optimize-via-Estimate: Predict-then-Optimize versus Finite-sample Optimal
---

# Autocorrelated Optimize-via-Estimate: Predict-then-Optimize versus Finite-sample Optimal
**arXiv**：[2602.01877v1](https://arxiv.org/abs/2602.01877) · [PDF](https://arxiv.org/pdf/2602.01877.pdf)  
**作者**：Zichun Wang, Gar Goei Loke, Ruiting Zuo  

**一句话要点**：提出自相关优化-通过-估计模型，在有限样本下优化样本外性能，应用于自相关不确定性场景。

**关键词**：数据驱动优化, 自相关不确定性, 组合优化, 有限样本性能, VARMA过程, 优化-通过-估计

## 3 点简述
- 核心问题：比较传统估计-然后-优化与直接优化样本外性能模型在自相关不确定性下的表现。
- 方法要点：提出A-OVE模型，基于充分统计量计算样本外最优解，并给出递归形式。
- 实验或效果：在带交易成本的组合优化问题中，A-OVE实现低遗憾，优于预测-然后-优化基准。

## 摘要（原文）

> Models that directly optimize for out-of-sample performance in the finite-sample regime have emerged as a promising alternative to traditional estimate-then-optimize approaches in data-driven optimization. In this work, we compare their performance in the context of autocorrelated uncertainties, specifically, under a Vector Autoregressive Moving Average VARMA(p,q) process. We propose an autocorrelated Optimize-via-Estimate (A-OVE) model that obtains an out-of-sample optimal solution as a function of sufficient statistics, and propose a recursive form for computing its sufficient statistics. We evaluate these models on a portfolio optimization problem with trading costs. A-OVE achieves low regret relative to a perfect information oracle, outperforming predict-then-optimize machine learning benchmarks. Notably, machine learning models with higher accuracy can have poorer decision quality, echoing the growing literature in data-driven optimization. Performance is retained under small mis-specification.

