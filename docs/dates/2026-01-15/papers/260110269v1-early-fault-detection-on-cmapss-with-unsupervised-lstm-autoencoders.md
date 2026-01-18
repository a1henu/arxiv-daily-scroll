---
layout: default
title: Early Fault Detection on CMAPSS with Unsupervised LSTM Autoencoders
---

# Early Fault Detection on CMAPSS with Unsupervised LSTM Autoencoders
**arXiv**：[2601.10269v1](https://arxiv.org/abs/2601.10269) · [PDF](https://arxiv.org/pdf/2601.10269.pdf)  
**作者**：P. Sánchez, K. Reyes, B. Radu, E. Fernández  

**一句话要点**：提出基于无监督LSTM自编码器的涡扇发动机早期故障检测框架，无需失效标签。

**关键词**：故障检测, 无监督学习, LSTM自编码器, 涡扇发动机, 健康监测, 自适应阈值

## 3 点简述
- 核心问题：涡扇发动机健康监测需早期故障检测，但缺乏失效标签数据。
- 方法要点：使用回归归一化去除工况影响，LSTM自编码器仅训练健康数据，自适应阈值触发警报。
- 实验或效果：在NASA CMAPSS基准上实现高召回率和低误报率，适用于多种工况。

## 摘要（原文）

> This paper introduces an unsupervised health-monitoring framework for turbofan engines that does not require run-to-failure labels. First, operating-condition effects in NASA CMAPSS sensor streams are removed via regression-based normalisation; then a Long Short-Term Memory (LSTM) autoencoder is trained only on the healthy portion of each trajectory. Persistent reconstruction error, estimated using an adaptive data-driven threshold, triggers real-time alerts without hand-tuned rules. Benchmark results show high recall and low false-alarm rates across multiple operating regimes, demonstrating that the method can be deployed quickly, scale to diverse fleets, and serve as a complementary early-warning layer to Remaining Useful Life models.

