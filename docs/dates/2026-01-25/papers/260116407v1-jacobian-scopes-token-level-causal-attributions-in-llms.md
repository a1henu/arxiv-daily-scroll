---
layout: default
title: Jacobian Scopes: token-level causal attributions in LLMs
---

# Jacobian Scopes: token-level causal attributions in LLMs
**arXiv**：[2601.16407v1](https://arxiv.org/abs/2601.16407) · [PDF](https://arxiv.org/pdf/2601.16407.pdf)  
**作者**：Toni J. B. Liu, Baran Zadeoğlu, Nicolas Boullé, Raphaël Sarfati, Christopher J. Earls  

**一句话要点**：提出Jacobian Scopes方法，基于梯度分析大语言模型预测的token级因果归因。

**关键词**：大语言模型, 因果归因, 梯度分析, token级解释, 上下文学习, 模型可解释性

## 3 点简述
- 核心问题：大语言模型预测中，难以确定哪些先验token对特定预测有强影响。
- 方法要点：通过线性化最终隐藏状态与输入的关系，量化输入token的影响，引入三种变体。
- 实验或效果：在指令理解、翻译和上下文学习等案例中，揭示如隐含政治偏见等发现。

## 摘要（原文）

> Large language models (LLMs) make next-token predictions based on clues present in their context, such as semantic descriptions and in-context examples. Yet, elucidating which prior tokens most strongly influence a given prediction remains challenging due to the proliferation of layers and attention heads in modern architectures. We propose Jacobian Scopes, a suite of gradient-based, token-level causal attribution methods for interpreting LLM predictions. By analyzing the linearized relations of final hidden state with respect to inputs, Jacobian Scopes quantify how input tokens influence a model's prediction. We introduce three variants - Semantic, Fisher, and Temperature Scopes - which respectively target sensitivity of specific logits, the full predictive distribution, and model confidence (inverse temperature). Through case studies spanning instruction understanding, translation and in-context learning (ICL), we uncover interesting findings, such as when Jacobian Scopes point to implicit political biases. We believe that our proposed methods also shed light on recently debated mechanisms underlying in-context time-series forecasting. Our code and interactive demonstrations are publicly available at https://github.com/AntonioLiu97/JacobianScopes.

