---
layout: default
title: FlowDA: Accurate, Low-Latency Weather Data Assimilation via Flow Matching
---

# FlowDA: Accurate, Low-Latency Weather Data Assimilation via Flow Matching
**arXiv**：[2602.06800v1](https://arxiv.org/abs/2602.06800) · [PDF](https://arxiv.org/pdf/2602.06800.pdf)  
**作者**：Ran Cheng, Lailai Zhu  

**一句话要点**：提出FlowDA基于流匹配实现低延迟、高精度的天气数据同化

**关键词**：数据同化, 流匹配, 天气预报, 生成模型, 低延迟计算, 观测嵌入

## 3 点简述
- 核心问题：传统变分数据同化方法在机器学习天气预报中计算成本高，生成式方法存在采样步骤多和长时域误差累积问题。
- 方法要点：基于流匹配构建生成式框架，通过SetConv嵌入观测条件，微调Aurora基础模型以提高效率和鲁棒性。
- 实验或效果：在观测率低至0.1%时优于基线，对观测噪声鲁棒，长时域循环同化中表现稳定。

## 摘要（原文）

> Data assimilation (DA) is a fundamental component of modern weather prediction, yet it remains a major computational bottleneck in machine learning (ML)-based forecasting pipelines due to reliance on traditional variational methods. Recent generative ML-based DA methods offer a promising alternative but typically require many sampling steps and suffer from error accumulation under long-horizon auto-regressive rollouts with cycling assimilation. We propose FlowDA, a low-latency weather-scale generative DA framework based on flow matching. FlowDA conditions on observations through a SetConv-based embedding and fine-tunes the Aurora foundation model to deliver accurate, efficient, and robust analyses. Experiments across observation rates decreasing from $3.9\%$ to $0.1\%$ demonstrate superior performance of FlowDA over strong baselines with similar tunable-parameter size. FlowDA further shows robustness to observational noise and stable performance in long-horizon auto-regressive cycling DA. Overall, FlowDA points to an efficient and scalable direction for data-driven DA.

