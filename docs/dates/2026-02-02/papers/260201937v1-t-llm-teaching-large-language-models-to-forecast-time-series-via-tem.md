---
layout: default
title: T-LLM: Teaching Large Language Models to Forecast Time Series via Temporal Distillation
---

# T-LLM: Teaching Large Language Models to Forecast Time Series via Temporal Distillation
**arXiv**：[2602.01937v1](https://arxiv.org/abs/2602.01937) · [PDF](https://arxiv.org/pdf/2602.01937.pdf)  
**作者**：Suhan Guo, Bingxu Wang, Shaodan Zhang, Furao Shen  

**一句话要点**：提出T-LLM框架，通过时间蒸馏教授大语言模型时间序列预测能力。

**关键词**：时间序列预测, 大语言模型, 蒸馏训练, 趋势建模, 频域分析

## 3 点简述
- 核心问题：时间序列数据受时间约束，限制大语言模型通过规模预训练获取预测能力。
- 方法要点：使用轻量级时间教师模型结合趋势建模和频域分析，在训练中蒸馏预测行为到LLM。
- 实验或效果：在基准数据集和传染病预测任务中，T-LLM在全样本、少样本和零样本设置下优于现有方法。

## 摘要（原文）

> Time series forecasting plays a critical role in decision-making across many real-world applications. Unlike data in vision and language domains, time series data is inherently tied to the evolution of underlying processes and can only accumulate as real-world time progresses, limiting the effectiveness of scale-driven pretraining alone. This time-bound constraint poses a challenge for enabling large language models (LLMs) to acquire forecasting capability, as existing approaches primarily rely on representation-level alignment or inference-time temporal modules rather than explicitly teaching forecasting behavior to the LLM. We propose T-LLM, a temporal distillation framework that equips general-purpose LLMs with time series forecasting capability by transferring predictive behavior from a lightweight temporal teacher during training. The teacher combines trend modeling and frequency-domain analysis to provide structured temporal supervision, and is removed entirely at inference, leaving the LLM as the sole forecasting model. Experiments on benchmark datasets and infectious disease forecasting tasks demonstrate that T-LLM consistently outperforms existing LLM-based forecasting methods under full-shot, few-shot, and zero-shot settings, while enabling a simple and efficient deployment pipeline.

