---
layout: default
title: Task Complexity Matters: An Empirical Study of Reasoning in LLMs for Sentiment Analysis
---

# Task Complexity Matters: An Empirical Study of Reasoning in LLMs for Sentiment Analysis
**arXiv**：[2602.24060v1](https://arxiv.org/abs/2602.24060) · [PDF](https://arxiv.org/pdf/2602.24060.pdf)  
**作者**：Donghao Huang, Zhaoxia Wang  

**一句话要点**：实证研究揭示LLM推理能力在情感分析中的任务复杂性依赖效应

**关键词**：大语言模型推理, 情感分析, 任务复杂性, 实证评估, 帕累托前沿分析, 错误分析

## 3 点简述
- 核心问题：验证推理是否普遍提升语言任务性能，挑战推理万能假设
- 方法要点：评估504种配置，涵盖七种模型家族和不同粒度情感数据集
- 实验效果：推理效果随任务复杂度变化，简单任务性能下降，复杂任务显著提升

## 摘要（原文）

> Large language models (LLMs) with reasoning capabilities have fueled a compelling narrative that reasoning universally improves performance across language tasks. We test this claim through a comprehensive evaluation of 504 configurations across seven model families--including adaptive, conditional, and reinforcement learning-based reasoning architectures--on sentiment analysis datasets of varying granularity (binary, five-class, and 27-class emotion). Our findings reveal that reasoning effectiveness is strongly task-dependent, challenging prevailing assumptions: (1) Reasoning shows task-complexity dependence--binary classification degrades up to -19.9 F1 percentage points (pp), while 27-class emotion recognition gains up to +16.0pp; (2) Distilled reasoning variants underperform base models by 3-18 pp on simpler tasks, though few-shot prompting enables partial recovery; (3) Few-shot learning improves over zero-shot in most cases regardless of model type, with gains varying by architecture and task complexity; (4) Pareto frontier analysis shows base models dominate efficiency-performance trade-offs, with reasoning justified only for complex emotion recognition despite 2.1x-54x computational overhead. We complement these quantitative findings with qualitative error analysis revealing that reasoning degrades simpler tasks through systematic over-deliberation, offering mechanistic insight beyond the high-level overthinking hypothesis.

