---
layout: default
title: Quantum vs. Classical Machine Learning: A Benchmark Study for Financial Prediction
---

# Quantum vs. Classical Machine Learning: A Benchmark Study for Financial Prediction
**arXiv**：[2601.03802v1](https://arxiv.org/abs/2601.03802) · [PDF](https://arxiv.org/pdf/2601.03802.pdf)  
**作者**：Rehan Ahmad, Muhammad Kashif, Nouhaila Innan, Muhammad Shafique  

**一句话要点**：提出可复现基准框架，系统比较量子与经典机器学习在金融预测中的性能

**关键词**：量子机器学习, 金融预测, 基准测试, 量子神经网络, 风险调整回报, 可复现框架

## 3 点简述
- 核心问题：量子机器学习在金融预测中是否优于经典方法，需公平评估
- 方法要点：标准化数据、特征和评估指标，比较架构匹配的量子与经典模型
- 实验或效果：量子模型在特定任务中表现更优，如方向分类和风险调整回报

## 摘要（原文）

> In this paper, we present a reproducible benchmarking framework that systematically compares QML models with architecture-matched classical counterparts across three financial tasks: (i) directional return prediction on U.S. and Turkish equities, (ii) live-trading simulation with Quantum LSTMs versus classical LSTMs on the S\&P 500, and (iii) realized volatility forecasting using Quantum Support Vector Regression. By standardizing data splits, features, and evaluation metrics, our study provides a fair assessment of when current-generation QML models can match or exceed classical methods. Our results reveal that quantum approaches show performance gains when data structure and circuit design are well aligned. In directional classification, hybrid quantum neural networks surpass the parameter-matched ANN by \textbf{+3.8 AUC} and \textbf{+3.4 accuracy points} on \texttt{AAPL} stock and by \textbf{+4.9 AUC} and \textbf{+3.6 accuracy points} on Turkish stock \texttt{KCHOL}. In live trading, the QLSTM achieves higher risk-adjusted returns in \textbf{two of four} S\&P~500 regimes. For volatility forecasting, an angle-encoded QSVR attains the \textbf{lowest QLIKE} on \texttt{KCHOL} and remains within $\sim$0.02-0.04 QLIKE of the best classical kernels on \texttt{S\&P~500} and \texttt{AAPL}. Our benchmarking framework clearly identifies the scenarios where current QML architectures offer tangible improvements and where established classical methods continue to dominate.

