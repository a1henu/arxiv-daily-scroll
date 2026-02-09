---
layout: default
title: Time-uniform conformal and PAC prediction
---

# Time-uniform conformal and PAC prediction
**arXiv**：[2602.06297v1](https://arxiv.org/abs/2602.06297) · [PDF](https://arxiv.org/pdf/2602.06297.pdf)  
**作者**：Kayla E. Scharfstein, Arun Kumar Kuchibhotla  

**一句话要点**：提出时间均匀的共形与PAC预测方法，以解决序列数据中不确定性量化问题。

**关键词**：共形预测, PAC预测, 序列数据, 不确定性量化, 任意时间有效性

## 3 点简述
- 核心问题：传统共形预测在序列设置中无法保证覆盖，且不适应动态更新。
- 方法要点：扩展共形和PAC框架至样本数不固定的序列场景，实现任意时间有效的预测集。
- 实验或效果：理论保证覆盖，并在模拟和真实数据集上验证有效性和实用性。

## 摘要（原文）

> Given that machine learning algorithms are increasingly being deployed to aid in high stakes decision-making, uncertainty quantification methods that wrap around these black box models such as conformal prediction have received much attention in recent years. In sequential settings, where data are observed/generated in a streaming fashion, traditional conformal methods do not provide any guarantee without fixing the sample size. More importantly, traditional conformal methods cannot cope with sequentially updated predictions. As such, we develop an extension of the conformal prediction and related probably approximately correct (PAC) prediction frameworks to sequential settings where the number of data points is not fixed in advance. The resulting prediction sets are anytime-valid in that their expected coverage is at the required level at any time chosen by the analyst even if this choice depends on the data. We present theoretical guarantees for our proposed methods and demonstrate their validity and utility on simulated and real datasets.

