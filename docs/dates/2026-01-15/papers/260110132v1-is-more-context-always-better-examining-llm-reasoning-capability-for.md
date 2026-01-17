---
layout: default
title: Is More Context Always Better? Examining LLM Reasoning Capability for Time Interval Prediction
---

# Is More Context Always Better? Examining LLM Reasoning Capability for Time Interval Prediction
**arXiv**：[2601.10132v1](https://arxiv.org/abs/2601.10132) · [PDF](https://arxiv.org/pdf/2601.10132.pdf)  
**作者**：Yanan Cao, Farnaz Fallahi, Murali Mohana Krishna Dandu, Lalitesh Morishetti, Kai Zhao, Luyi Ma, Sinduja Subramaniam, Jianpeng Xu, Evren Korpeoglu, Kaushiki Nag, Sushant Kumar, Kannan Achan  

**一句话要点**：研究LLM在时间间隔预测中的推理能力，挑战‘更多上下文总更好’的假设

**关键词**：时间间隔预测, LLM推理能力, 上下文影响, 结构化行为数据, 零样本基准测试

## 3 点简述
- 核心问题：LLM能否从结构化行为数据中推断时间规律，如重复购买间隔
- 方法要点：在零样本设置下，用简单复购场景基准测试LLM，对比统计和机器学习模型
- 实验或效果：LLM超越轻量统计基线但不及专用模型，适度上下文提升准确性，过多细节降低性能

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive capabilities in reasoning and prediction across different domains. Yet, their ability to infer temporal regularities from structured behavioral data remains underexplored. This paper presents a systematic study investigating whether LLMs can predict time intervals between recurring user actions, such as repeated purchases, and how different levels of contextual information shape their predictive behavior. Using a simple but representative repurchase scenario, we benchmark state-of-the-art LLMs in zero-shot settings against both statistical and machine-learning models. Two key findings emerge. First, while LLMs surpass lightweight statistical baselines, they consistently underperform dedicated machine-learning models, showing their limited ability to capture quantitative temporal structure. Second, although moderate context can improve LLM accuracy, adding further user-level detail degrades performance. These results challenge the assumption that "more context leads to better reasoning". Our study highlights fundamental limitations of today's LLMs in structured temporal inference and offers guidance for designing future context-aware hybrid models that integrate statistical precision with linguistic flexibility.

