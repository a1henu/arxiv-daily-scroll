---
layout: default
title: FreqLens: Interpretable Frequency Attribution for Time Series Forecasting
---

# FreqLens: Interpretable Frequency Attribution for Time Series Forecasting
**arXiv**：[2602.08768v1](https://arxiv.org/abs/2602.08768) · [PDF](https://arxiv.org/pdf/2602.08768.pdf)  
**作者**：Chi-Sheng Chen, Xinyu Zhang, En-Jui Kuo, Guan-Ying Chen, Qiuzhe Xie, Fan Zhang  

**一句话要点**：提出FreqLens框架，通过可学习频率发现和公理化频率归因，增强时间序列预测的可解释性。

**关键词**：时间序列预测, 可解释性, 频率分析, 归因方法, 深度学习

## 3 点简述
- 核心问题：时间序列预测模型缺乏可解释性，限制了在需要可解释预测领域的应用。
- 方法要点：引入可学习频率发现和公理化频率归因，自动发现主导周期模式并提供理论保证。
- 实验或效果：在交通和天气数据集上实现竞争性或更优性能，发现物理意义频率如24小时周期。

## 摘要（原文）

> Time series forecasting models often lack interpretability, limiting their adoption in domains requiring explainable predictions. We propose \textsc{FreqLens}, an interpretable forecasting framework that discovers and attributes predictions to learnable frequency components. \textsc{FreqLens} introduces two key innovations: (1) \emph{learnable frequency discovery} -- frequency bases are parameterized via sigmoid mapping and learned from data with diversity regularization, enabling automatic discovery of dominant periodic patterns without domain knowledge; and (2) \emph{axiomatic frequency attribution} -- a theoretically grounded framework that provably satisfies Completeness, Faithfulness, Null-Frequency, and Symmetry axioms, with per-frequency attributions equivalent to Shapley values. On Traffic and Weather datasets, \textsc{FreqLens} achieves competitive or superior performance while discovering physically meaningful frequencies: all 5 independent runs discover the 24-hour daily cycle ($24.6 \pm 0.1$h, 2.5\% error) and 12-hour half-daily cycle ($11.8 \pm 0.1$h, 1.6\% error) on Traffic, and weekly cycles ($10\times$ longer than the input window) on Weather. These results demonstrate genuine frequency-level knowledge discovery with formal theoretical guarantees on attribution quality.

