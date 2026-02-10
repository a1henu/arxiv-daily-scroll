---
layout: default
title: AnomSeer: Reinforcing Multimodal LLMs to Reason for Time-Series Anomaly Detection
---

# AnomSeer: Reinforcing Multimodal LLMs to Reason for Time-Series Anomaly Detection
**arXiv**：[2602.08868v1](https://arxiv.org/abs/2602.08868) · [PDF](https://arxiv.org/pdf/2602.08868.pdf)  
**作者**：Junru Zhang, Lang Feng, Haoran Shi, Xu Guo, Han Yu, Yabo Dong, Duanqing Xu  

**一句话要点**：提出AnomSeer以强化多模态大语言模型在时间序列异常检测中的细粒度推理能力

**关键词**：时间序列异常检测, 多模态大语言模型, 细粒度推理, 专家思维链, TimerPO优化, 最优传输

## 3 点简述
- 核心问题：多模态大语言模型依赖粗粒度启发式方法，难以进行多维度细粒度推理，影响复杂时间序列数据的理解。
- 方法要点：通过专家思维链提供可验证的细粒度推理，并引入基于最优传输的时间序列接地优势与正交投影的TimerPO优化策略。
- 实验或效果：在多种异常场景下，AnomSeer在分类和定位准确率上超越大型商业基线，尤其在点和频率驱动异常中表现突出。

## 摘要（原文）

> Time-series anomaly detection (TSAD) with multimodal large language models (MLLMs) is an emerging area, yet a persistent challenge remains: MLLMs rely on coarse time-series heuristics but struggle with multi-dimensional, detailed reasoning, which is vital for understanding complex time-series data. We present AnomSeer to address this by reinforcing the model to ground its reasoning in precise, structural details of time series, unifying anomaly classification, localization, and explanation. At its core, an expert chain-of-thought trace is generated to provide a verifiable, fine-grained reasoning from classical analyses (e.g., statistical measures, frequency transforms). Building on this, we propose a novel time-series grounded policy optimization (TimerPO) that incorporates two additional components beyond standard reinforcement learning: a time-series grounded advantage based on optimal transport and an orthogonal projection to ensure this auxiliary granular signal does not interfere with the primary detection objective. Across diverse anomaly scenarios, AnomSeer, with Qwen2.5-VL-3B/7B-Instruct, outperforms larger commercial baselines (e.g., GPT-4o) in classification and localization accuracy, particularly on point- and frequency-driven exceptions. Moreover, it produces plausible time-series reasoning traces that support its conclusions.

