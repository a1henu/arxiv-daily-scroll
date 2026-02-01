---
layout: default
title: Task-Awareness Improves LLM Generations and Uncertainty
---

# Task-Awareness Improves LLM Generations and Uncertainty
**arXiv**：[2601.21500v1](https://arxiv.org/abs/2601.21500) · [PDF](https://arxiv.org/pdf/2601.21500.pdf)  
**作者**：Tim Tomov, Dominik Fuchsgruber, Stephan Günnemann  

**一句话要点**：提出任务感知潜在结构建模以提升LLM生成与不确定性估计

**关键词**：任务感知解码, 潜在结构建模, 贝叶斯最优响应, 不确定性估计, LLM预测可靠性

## 3 点简述
- 核心问题：现有解码与不确定性方法忽视输出结构，仅操作于语言空间。
- 方法要点：在任务依赖潜在结构中建模LLM输出，结合相异度计算贝叶斯最优响应。
- 实验或效果：贝叶斯最优响应优于标准解码，不确定性估计与输出质量对齐更佳。

## 摘要（原文）

> In many applications of LLMs, natural language responses often have an underlying structure such as representing discrete labels, numerical values, or graphs. Yet, existing decoding and uncertainty estimation methods operate only in language space and largely disregard structural information. We address this by modeling LLM outputs directly in a task-dependent latent structure. By equipping this structure with a dissimilarity measure, we can compute Bayes-optimal responses. These are not selected from sampled generations but are newly synthesized by combining individual responses in the latent space. Across different tasks, Bayes-optimal responses consistently outperform standard decoding methods like beam search. Moreover, quantifying uncertainty via the induced Bayesian risk captures variations in terms of the latent structure and improves alignment with output quality and correctness. Our decision-theoretic framework is applicable to any problem that admits a latent response structure and enables reliable task-aware LLM predictions.

