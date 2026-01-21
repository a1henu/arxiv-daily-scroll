---
layout: default
title: Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models
---

# Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models
**arXiv**：[2601.14152v1](https://arxiv.org/abs/2601.14152) · [PDF](https://arxiv.org/pdf/2601.14152.pdf)  
**作者**：Hyunjong Ok, Jaeho Lee  

**一句话要点**：揭示因果注意力在语言模型中导致提示顺序敏感性的机制，聚焦多项选择题场景

**关键词**：因果注意力, 提示顺序敏感性, 多项选择题回答, 语言模型架构分析, 信息瓶颈

## 3 点简述
- 核心问题：语言模型对提示结构敏感，但机制未知，如CQO顺序优于QOC
- 方法要点：通过系统架构分析，识别因果注意力是核心机制，QOC中因果掩码限制选项关注上下文
- 实验或效果：在广泛模型和数据集上，CQO比QOC性能提升超过14%p，验证信息瓶颈效应

## 摘要（原文）

> Large language models exhibit surprising sensitivity to the structure of the prompt, but the mechanisms underlying this sensitivity remain poorly understood. In this work, we conduct an in-depth investigation on a striking case: in multiple-choice question answering, placing context before the questions and options (CQO) outperforms the reverse order (QOC) by over 14%p, consistently over a wide range of models and datasets. Through systematic architectural analysis, we identify causal attention as the core mechanism: in QOC prompts, the causal mask prevents option tokens from attending to context, creating an information bottleneck where context becomes invisible to options.

