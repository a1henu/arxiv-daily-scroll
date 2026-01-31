---
layout: default
title: Task-Awareness Improves LLM Generations and Uncertainty
---

# Task-Awareness Improves LLM Generations and Uncertainty
**arXiv**：[2601.21500v1](https://arxiv.org/abs/2601.21500) · [PDF](https://arxiv.org/pdf/2601.21500.pdf)  
**作者**：Tim Tomov, Dominik Fuchsgruber, Stephan Günnemann  

**一句话要点**：提出基于任务感知的贝叶斯最优解码框架，以提升LLM在结构化输出任务中的生成质量和不确定性估计。

**关键词**：任务感知解码, 贝叶斯最优响应, 不确定性估计, 潜在结构建模, LLM生成优化

## 3 点简述
- 核心问题：现有解码方法忽视LLM输出中的潜在结构信息，影响生成质量和不确定性估计。
- 方法要点：在任务依赖的潜在空间中建模输出，结合相异性度量计算贝叶斯最优响应。
- 实验或效果：贝叶斯最优响应在多种任务中优于标准解码方法，不确定性估计与输出质量更对齐。

## 摘要（原文）

> In many applications of LLMs, natural language responses often have an underlying structure such as representing discrete labels, numerical values, or graphs. Yet, existing decoding and uncertainty estimation methods operate only in language space and largely disregard structural information. We address this by modeling LLM outputs directly in a task-dependent latent structure. By equipping this structure with a dissimilarity measure, we can compute Bayes-optimal responses. These are not selected from sampled generations but are newly synthesized by combining individual responses in the latent space. Across different tasks, Bayes-optimal responses consistently outperform standard decoding methods like beam search. Moreover, quantifying uncertainty via the induced Bayesian risk captures variations in terms of the latent structure and improves alignment with output quality and correctness. Our decision-theoretic framework is applicable to any problem that admits a latent response structure and enables reliable task-aware LLM predictions.

