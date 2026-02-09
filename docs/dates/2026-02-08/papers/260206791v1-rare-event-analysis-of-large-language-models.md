---
layout: default
title: Rare Event Analysis of Large Language Models
---

# Rare Event Analysis of Large Language Models
**arXiv**：[2602.06791v1](https://arxiv.org/abs/2602.06791) · [PDF](https://arxiv.org/pdf/2602.06791.pdf)  
**作者**：Jake McAllister Dorman, Edward Gillman, Dominic C. Rose, Jamie F. Mair, Juan P. Garrahan  

**一句话要点**：提出大语言模型罕见事件分析框架，涵盖理论、生成策略与概率估计

**关键词**：大语言模型, 罕见事件分析, 概率估计, 生成策略, 模型部署

## 3 点简述
- 核心问题：大语言模型推理中罕见事件难以观察，但部署中可能显著影响性能
- 方法要点：提供端到端分析框架，包括高效生成策略和概率估计方法
- 实验或效果：通过具体示例展示框架应用，并概述扩展到其他模型的潜力

## 摘要（原文）

> Being probabilistic models, during inference large language models (LLMs) display rare events: behaviour that is far from typical but highly significant. By definition all rare events are hard to see, but the enormous scale of LLM usage means that events completely unobserved during development are likely to become prominent in deployment. Here we present an end-to-end framework for the systematic analysis of rare events in LLMs. We provide a practical implementation spanning theory, efficient generation strategies, probability estimation and error analysis, which we illustrate with concrete examples. We outline extensions and applications to other models and contexts, highlighting the generality of the concepts and techniques presented here.

