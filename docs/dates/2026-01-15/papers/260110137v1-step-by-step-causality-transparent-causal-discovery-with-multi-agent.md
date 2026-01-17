---
layout: default
title: Step-by-Step Causality: Transparent Causal Discovery with Multi-Agent Tree-Query and Adversarial Confidence Estimation
---

# Step-by-Step Causality: Transparent Causal Discovery with Multi-Agent Tree-Query and Adversarial Confidence Estimation
**arXiv**：[2601.10137v1](https://arxiv.org/abs/2601.10137) · [PDF](https://arxiv.org/pdf/2601.10137.pdf)  
**作者**：Ziyi Ding, Chenfei Ye-Hao, Zheyuan Wang, Xiao-Ping Zhang  

**一句话要点**：提出Tree-Query框架，通过多专家LLM树状查询解决数据无关因果发现中的透明性与置信度问题。

**关键词**：因果发现, 大语言模型, 树状查询, 置信度估计, 数据无关先验, 透明推理

## 3 点简述
- 核心问题：传统因果发现方法存在误差传播，LLM因果预言机缺乏透明性与置信度评估。
- 方法要点：采用树结构多专家LLM框架，将成对因果发现分解为关于后门路径、独立性、潜在混杂和因果方向的查询序列。
- 实验或效果：在数据无关基准测试中提升结构指标，案例研究展示混杂因素筛选与高置信度因果结论。

## 摘要（原文）

> Causal discovery aims to recover ``what causes what'', but classical constraint-based methods (e.g., PC, FCI) suffer from error propagation, and recent LLM-based causal oracles often behave as opaque, confidence-free black boxes. This paper introduces Tree-Query, a tree-structured, multi-expert LLM framework that reduces pairwise causal discovery to a short sequence of queries about backdoor paths, (in)dependence, latent confounding, and causal direction, yielding interpretable judgments with robustness-aware confidence scores. Theoretical guarantees are provided for asymptotic identifiability of four pairwise relations. On data-free benchmarks derived from Mooij et al. and UCI causal graphs, Tree-Query improves structural metrics over direct LLM baselines, and a diet--weight case study illustrates confounder screening and stable, high-confidence causal conclusions. Tree-Query thus offers a principled way to obtain data-free causal priors from LLMs that can complement downstream data-driven causal discovery. Code is available at https://anonymous.4open.science/r/Repo-9B3E-4F96.

