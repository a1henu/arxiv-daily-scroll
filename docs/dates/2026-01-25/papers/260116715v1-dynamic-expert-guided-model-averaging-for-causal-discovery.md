---
layout: default
title: Dynamic Expert-Guided Model Averaging for Causal Discovery
---

# Dynamic Expert-Guided Model Averaging for Causal Discovery
**arXiv**：[2601.16715v1](https://arxiv.org/abs/2601.16715) · [PDF](https://arxiv.org/pdf/2601.16715.pdf)  
**作者**：Adrick Tench, Thomas Demeester  

**一句话要点**：提出动态专家引导的模型平均方法，以集成因果发现算法并处理现实数据挑战。

**关键词**：因果发现, 模型平均, 专家知识, 大语言模型, 临床数据分析

## 3 点简述
- 核心问题：因果发现算法众多且假设常被现实数据违反，需依赖专家知识。
- 方法要点：利用动态请求的专家知识（如LLMs）灵活集成多种算法，提升模型鲁棒性。
- 实验或效果：在干净和噪声数据上验证方法有效性，分析专家正确度影响及LLMs在临床因果发现中的能力。

## 摘要（原文）

> Understanding causal relationships is critical for healthcare. Accurate causal models provide a means to enhance the interpretability of predictive models, and furthermore a basis for counterfactual and interventional reasoning and the estimation of treatment effects. However, would-be practitioners of causal discovery face a dizzying array of algorithms without a clear best choice. This abundance of competitive algorithms makes ensembling a natural choice for practical applications. At the same time, real-world use cases frequently face challenges that violate the assumptions of common causal discovery algorithms, forcing heavy reliance on expert knowledge. Inspired by recent work on dynamically requested expert knowledge and LLMs as experts, we present a flexible model averaging method leveraging dynamically requested expert knowledge to ensemble a diverse array of causal discovery algorithms. Experiments demonstrate the efficacy of our method with imperfect experts such as LLMs on both clean and noisy data. We also analyze the impact of different degrees of expert correctness and assess the capabilities of LLMs for clinical causal discovery, providing valuable insights for practitioners.

