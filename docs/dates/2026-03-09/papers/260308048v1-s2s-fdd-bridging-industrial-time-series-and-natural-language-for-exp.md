---
layout: default
title: S2S-FDD: Bridging Industrial Time Series and Natural Language for Explainable Zero-shot Fault Diagnosis
---

# S2S-FDD: Bridging Industrial Time Series and Natural Language for Explainable Zero-shot Fault Diagnosis
**arXiv**：[2603.08048v1](https://arxiv.org/abs/2603.08048) · [PDF](https://arxiv.org/pdf/2603.08048.pdf)  
**作者**：Baoxue Li, Chunhui Zhao  

**一句话要点**：提出S2S-FDD框架，通过信号转语义和多轮树状诊断实现工业时序数据的可解释零样本故障诊断

**关键词**：故障诊断, 时序信号处理, 自然语言摘要, 零样本学习, 可解释性, 工业系统

## 3 点简述
- 核心问题：传统故障诊断模型输出抽象，无法回答'为什么'或'如何修复'，且大语言模型处理工业信号存在语义鸿沟
- 方法要点：设计信号转语义算子将时序信号转为自然语言摘要，并基于描述采用多轮树状诊断方法参考历史文档动态查询信号
- 实验或效果：在多相流过程实验中验证了方法的可行性和有效性，支持可解释零样本故障诊断

## 摘要（原文）

> Fault diagnosis is critical for the safe operation of industrial systems. Conventional diagnosis models typically produce abstract outputs such as anomaly scores or fault categories, failing to answer critical operational questions like "Why" or "How to repair". While large language models (LLMs) offer strong generalization and reasoning abilities, their training on discrete textual corpora creates a semantic gap when processing high-dimensional, temporal industrial signals. To address this challenge, we propose a Signals-to-Semantics fault diagnosis (S2S-FDD) framework that bridges high-dimensional sensor signals with natural language semantics through two key innovations: We first design a Signal-to-Semantic operator to convert abstract time-series signals into natural language summaries, capturing trends, periodicity, and deviations. Based on the descriptions, we design a multi-turn tree-structured diagnosis method to perform fault diagnosis by referencing historical maintenance documents and dynamically querying additional signals. The framework further supports human-in-the-loop feedback for continuous refinement. Experiments on the multiphase flow process show the feasibility and effectiveness of the proposed method for explainable zero-shot fault diagnosis.

