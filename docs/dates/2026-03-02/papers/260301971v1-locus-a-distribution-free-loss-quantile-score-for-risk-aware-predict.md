---
layout: default
title: LOCUS: A Distribution-Free Loss-Quantile Score for Risk-Aware Predictions
---

# LOCUS: A Distribution-Free Loss-Quantile Score for Risk-Aware Predictions
**arXiv**：[2603.01971v1](https://arxiv.org/abs/2603.01971) · [PDF](https://arxiv.org/pdf/2603.01971.pdf)  
**作者**：Matheus Barreto, Mário de Castro, Thiago R. Ramos, Denis Valle, Rafael Izbicki  

**一句话要点**：提出Locus分布无关损失分位数评分，用于风险感知预测以减少大损失事件

**关键词**：风险感知预测, 损失分位数评分, 分布无关方法, 回归基准测试, 大损失控制

## 3 点简述
- 核心问题：机器学习模型平均准确但大损失事件可能主导部署成本，需风险感知评估
- 方法要点：Locus作为分布无关包装器，基于预测函数损失生成可解释评分，通过分位数校准实现跨输入可比
- 实验或效果：在13个回归基准测试中，Locus有效提升风险排序并降低大损失频率，优于标准启发式方法

## 摘要（原文）

> Modern machine learning models can be accurate on average yet still make mistakes that dominate deployment cost. We introduce Locus, a distribution-free wrapper that produces a per-input loss-scale reliability score for a fixed prediction function. Rather than quantifying uncertainty about the label, Locus models the realized loss of the prediction function using any engine that outputs a predictive distribution for the loss given an input. A simple split-calibration step turns this function into a distribution-free interpretable score that is comparable across inputs and can be read as an upper loss level. The score is useful on its own for ranking, and it can optionally be thresholded to obtain a transparent flagging rule with distribution-free control of large-loss events. Experiments across 13 regression benchmarks show that Locus yields effective risk ranking and reduces large-loss frequency compared to standard heuristics.

