---
layout: default
title: Quantifying the Necessity of Chain of Thought through Opaque Serial Depth
---

# Quantifying the Necessity of Chain of Thought through Opaque Serial Depth
**arXiv**：[2603.09786v1](https://arxiv.org/abs/2603.09786) · [PDF](https://arxiv.org/pdf/2603.09786.pdf)  
**作者**：Jonah Brown-Cohen, David Lindner, Rohin Shah  

**一句话要点**：提出不透明串行深度以量化思维链的必要性，用于评估模型未外化推理的潜力。

**关键词**：思维链, 不透明串行深度, 推理监控, Transformer架构, 混合专家模型, 自动化计算

## 3 点简述
- 核心问题：大型语言模型推理过程是否必须通过思维链外化，以监控其内部计算。
- 方法要点：定义不透明串行深度，作为无需思维链的最长计算长度，并开发自动化方法计算上界。
- 实验或效果：计算Gemma 3模型上界，分析混合专家模型深度低于密集模型，支持深度作为评估工具。

## 摘要（原文）

> Large language models (LLMs) tend to externalize their reasoning in their chain of thought, making the chain of thought a good target for monitoring. This is partially an inherent feature of the Transformer architecture: sufficiently long serial cognition must pass through the chain of thought (Korbak et al., 2025). We formalize this argument through the notion of opaque serial depth, given by the length of the longest computation that can be done without the use of interpretable intermediate steps like chain of thought. Given this formalization, we compute numeric upper bounds on the opaque serial depth of Gemma 3 models, as well as asymptotic results for additional architectures beyond standard LLMs. We also open-source an automated method that can calculate upper bounds on the opaque serial depth of arbitrary neural networks, and use it to demonstrate that Mixture-of-Experts models likely have lower depth than dense models. Overall, our results suggest that opaque serial depth is a useful tool for understanding the potential for models to do significant reasoning that is not externalized.

