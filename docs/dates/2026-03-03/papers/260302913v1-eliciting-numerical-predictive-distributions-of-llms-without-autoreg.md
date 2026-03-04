---
layout: default
title: Eliciting Numerical Predictive Distributions of LLMs Without Autoregression
---

# Eliciting Numerical Predictive Distributions of LLMs Without Autoregression
**arXiv**：[2603.02913v1](https://arxiv.org/abs/2603.02913) · [PDF](https://arxiv.org/pdf/2603.02913.pdf)  
**作者**：Julianna Piskorz, Katarzyna Kobalczyk, Mihaela van der Schaar  

**一句话要点**：提出回归探针方法以直接预测LLM数值输出的统计函数，避免自回归采样

**关键词**：大语言模型, 回归任务, 预测分布, 不确定性量化, 内部表示分析, 轻量级推理

## 3 点简述
- 核心问题：LLM自回归解码在连续值输出任务中计算成本高，难以高效获取预测分布
- 方法要点：训练回归探针从LLM内部表示直接预测均值、中位数、分位数等统计函数
- 实验或效果：LLM嵌入携带预测分布摘要统计信息，包括数值不确定性，支持轻量级替代方案

## 摘要（原文）

> Large Language Models (LLMs) have recently been successfully applied to regression tasks -- such as time series forecasting and tabular prediction -- by leveraging their in-context learning abilities. However, their autoregressive decoding process may be ill-suited to continuous-valued outputs, where obtaining predictive distributions over numerical targets requires repeated sampling, leading to high computational cost and inference time. In this work, we investigate whether distributional properties of LLM predictions can be recovered without explicit autoregressive generation. To this end, we study a set of regression probes trained to predict statistical functionals (e.g., mean, median, quantiles) of the LLM's numerical output distribution directly from its internal representations. Our results suggest that LLM embeddings carry informative signals about summary statistics of their predictive distributions, including the numerical uncertainty. This investigation opens up new questions about how LLMs internally encode uncertainty in numerical tasks, and about the feasibility of lightweight alternatives to sampling-based approaches for uncertainty-aware numerical predictions.

