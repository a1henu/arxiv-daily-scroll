---
layout: default
title: CAMEL: An ECG Language Model for Forecasting Cardiac Events
---

# CAMEL: An ECG Language Model for Forecasting Cardiac Events
**arXiv**：[2602.15677v1](https://arxiv.org/abs/2602.15677) · [PDF](https://arxiv.org/pdf/2602.15677.pdf)  
**作者**：Neelay Velingker, Alaia Solko-Breslin, Mayank Keoliya, Seewon Choi, Jiayi Xin, Anika Marathe, Alireza Oraii, Rajat Deo, Sameed Khatana, Rajeev Alur, Mayur Naik, Eric Wong  

**一句话要点**：提出CAMEL心电图语言模型，通过长信号推理实现心脏事件预测。

**关键词**：心电图语言模型, 心脏事件预测, 长信号推理, 跨模态编码器, 课程学习训练, 零样本性能

## 3 点简述
- 核心问题：现有心电图语言模型无法预测未来心脏事件，限制了早期干预的临床价值。
- 方法要点：设计专用心电图编码器，结合LoRA适应和课程学习训练，支持信号与文本的跨模态理解。
- 实验或效果：在6个任务9个数据集上实现零样本性能，包括新基准ECGForecastBench，超越现有模型和全监督基线。

## 摘要（原文）

> Electrocardiograms (ECG) are electrical recordings of the heart that are critical for diagnosing cardiovascular conditions. ECG language models (ELMs) have recently emerged as a promising framework for ECG classification accompanied by report generation. However, current models cannot forecast future cardiac events despite the immense clinical value for planning earlier intervention. To address this gap, we propose CAMEL, the first ELM that is capable of inference over longer signal durations which enables its forecasting capability. Our key insight is a specialized ECG encoder which enables cross-understanding of ECG signals with text. We train CAMEL using established LLM training procedures, combining LoRA adaptation with a curriculum learning pipeline. Our curriculum includes ECG classification, metrics calculations, and multi-turn conversations to elicit reasoning. CAMEL demonstrates strong zero-shot performance across 6 tasks and 9 datasets, including ECGForecastBench, a new benchmark that we introduce for forecasting arrhythmias. CAMEL is on par with or surpasses ELMs and fully supervised baselines both in- and out-of-distribution, achieving SOTA results on ECGBench (+7.0% absolute average gain) as well as ECGForecastBench (+12.4% over fully supervised models and +21.1% over zero-shot ELMs).

