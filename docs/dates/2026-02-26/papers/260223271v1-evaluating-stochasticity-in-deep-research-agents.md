---
layout: default
title: Evaluating Stochasticity in Deep Research Agents
---

# Evaluating Stochasticity in Deep Research Agents
**arXiv**：[2602.23271v1](https://arxiv.org/abs/2602.23271) · [PDF](https://arxiv.org/pdf/2602.23271.pdf)  
**作者**：Haotian Zhai, Elias Stengel-Eskin, Pratik Patil, Liu Leqi  

**一句话要点**：提出评估框架以量化深度研究代理的随机性，并基于信息获取MDP模型提出缓解策略。

**关键词**：深度研究代理, 随机性评估, 信息获取MDP, 输出方差, 缓解策略, 结构化输出

## 3 点简述
- 核心问题：深度研究代理在相同查询下输出存在显著随机性，阻碍实际部署。
- 方法要点：建模为信息获取MDP，识别信息获取、压缩和推断三个随机性来源。
- 实验或效果：在DeepSearchQA上，缓解方法降低平均随机性22%且保持高质量。

## 摘要（原文）

> Deep Research Agents (DRAs) are promising agentic systems that gather and synthesize information to support research across domains such as financial decision-making, medical analysis, and scientific discovery. Despite recent improvements in research quality (e.g., outcome accuracy when ground truth is available), DRA system design often overlooks a critical barrier to real-world deployment: stochasticity. Under identical queries, repeated executions of DRAs can exhibit substantial variability in terms of research outcome, findings, and citations. In this paper, we formalize the study of stochasticity in DRAs by modeling them as information acquisition Markov Decision Processes. We introduce an evaluation framework that quantifies variance in the system and identify three sources of it: information acquisition, information compression, and inference. Through controlled experiments, we investigate how stochasticity from these modules across different decision steps influences the variance of DRA outputs. Our results show that reducing stochasticity can improve research output quality, with inference and early-stage stochasticity contributing the most to DRA output variance. Based on these findings, we propose strategies for mitigating stochasticity while maintaining output quality via structured output and ensemble-based query generation. Our experiments on DeepSearchQA show that our proposed mitigation methods reduce average stochasticity by 22% while maintaining high research quality.

