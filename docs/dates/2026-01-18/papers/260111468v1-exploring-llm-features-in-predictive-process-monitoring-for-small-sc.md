---
layout: default
title: Exploring LLM Features in Predictive Process Monitoring for Small-Scale Event-Logs
---

# Exploring LLM Features in Predictive Process Monitoring for Small-Scale Event-Logs
**arXiv**：[2601.11468v1](https://arxiv.org/abs/2601.11468) · [PDF](https://arxiv.org/pdf/2601.11468.pdf)  
**作者**：Alessandro Padella, Massimiliano de Leoni, Marlon Dumas  

**一句话要点**：扩展LLM预测过程监控框架，评估其在数据稀缺场景下的泛化性与推理机制

**关键词**：预测过程监控, 大型语言模型, 数据稀缺, 关键绩效指标, 推理机制, 事件日志

## 3 点简述
- 核心问题：预测过程监控在数据稀缺（如仅100条轨迹）时性能受限，需提升预测准确性和泛化能力。
- 方法要点：扩展基于LLM的框架，通过提示全面评估其语义利用、推理机制及多关键绩效指标预测。
- 实验或效果：在三个事件日志上，LLM在总时间和活动发生预测上超越基准方法，并利用先验知识和训练轨迹内部相关性。

## 摘要（原文）

> Predictive Process Monitoring is a branch of process mining that aims to predict the outcome of an ongoing process. Recently, it leveraged machine-and-deep learning architectures. In this paper, we extend our prior LLM-based Predictive Process Monitoring framework, which was initially focused on total time prediction via prompting. The extension consists of comprehensively evaluating its generality, semantic leverage, and reasoning mechanisms, also across multiple Key Performance Indicators. Empirical evaluations conducted on three distinct event logs and across the Key Performance Indicators of Total Time and Activity Occurrence prediction indicate that, in data-scarce settings with only 100 traces, the LLM surpasses the benchmark methods. Furthermore, the experiments also show that the LLM exploits both its embodied prior knowledge and the internal correlations among training traces. Finally, we examine the reasoning strategies employed by the model, demonstrating that the LLM does not merely replicate existing predictive methods but performs higher-order reasoning to generate the predictions.

