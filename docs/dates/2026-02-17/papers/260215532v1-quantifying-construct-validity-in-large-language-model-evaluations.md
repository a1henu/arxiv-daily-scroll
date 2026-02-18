---
layout: default
title: Quantifying construct validity in large language model evaluations
---

# Quantifying construct validity in large language model evaluations
**arXiv**：[2602.15532v1](https://arxiv.org/abs/2602.15532) · [PDF](https://arxiv.org/pdf/2602.15532.pdf)  
**作者**：Ryan Othniel Kearns  

**一句话要点**：提出结构化能力模型以量化大语言模型评估中的构念效度

**关键词**：构念效度, 基准测试, 结构化能力模型, 潜在因子模型, 缩放定律, 模型评估

## 3 点简述
- 核心问题：现有基准测试结果常被误认为等同于模型能力，但存在测试集污染和标注错误等问题，影响构念效度。
- 方法要点：结合潜在因子模型和缩放定律，结构化能力模型从基准结果中提取可解释且可泛化的能力，分离模型规模与能力。
- 实验或效果：在OpenLLM排行榜数据上，该模型在拟合指标和分布外预测上优于现有方法，提升了解释和预测能力。

## 摘要（原文）

> The LLM community often reports benchmark results as if they are synonymous with general model capabilities. However, benchmarks can have problems that distort performance, like test set contamination and annotator error. How can we know that a benchmark is a reliable indicator of some capability that we want to measure? This question concerns the construct validity of LLM benchmarks, and it requires separating benchmark results from capabilities when we model and predict LLM performance.
>   Both social scientists and computer scientists propose formal models - latent factor models and scaling laws - for identifying the capabilities underlying benchmark scores. However, neither technique is satisfactory for construct validity. Latent factor models ignore scaling laws, and as a result, the capabilities they extract often proxy model size. Scaling laws ignore measurement error, and as a result, the capabilities they extract are both uninterpretable and overfit to the observed benchmarks.
>   This thesis presents the structured capabilities model, the first model to extract interpretable and generalisable capabilities from a large collection of LLM benchmark results. I fit this model and its two alternatives on a large sample of results from the OpenLLM Leaderboard. Structured capabilities outperform latent factor models on parsimonious fit indices, and exhibit better out-of-distribution benchmark prediction than scaling laws. These improvements are possible because neither existing approach separates model scale from capabilities in the appropriate way. Model scale should inform capabilities, as in scaling laws, and these capabilities should inform observed results up to measurement error, as in latent factor models. In combining these two insights, structured capabilities demonstrate better explanatory and predictive power for quantifying construct validity in LLM evaluations.

