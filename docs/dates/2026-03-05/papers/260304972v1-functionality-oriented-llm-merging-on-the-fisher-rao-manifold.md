---
layout: default
title: Functionality-Oriented LLM Merging on the Fisher--Rao Manifold
---

# Functionality-Oriented LLM Merging on the Fisher--Rao Manifold
**arXiv**：[2603.04972v1](https://arxiv.org/abs/2603.04972) · [PDF](https://arxiv.org/pdf/2603.04972.pdf)  
**作者**：Jiayu Wang, Zuojun Ye, Wenpeng Yin  

**一句话要点**：提出基于Fisher-Rao流形的功能导向LLM合并方法，以解决参数空间启发式合并的局限性。

**关键词**：LLM合并, Fisher-Rao流形, Karcher平均, 表示崩溃, 功能导向, 多专家合并

## 3 点简述
- 现有LLM合并方法多为参数空间启发式，导致功能合并不理想和表示崩溃问题。
- 将模型合并建模为Fisher-Rao流形上的加权Karcher平均，最小化预测分布间的KL距离。
- 实验显示该方法在模型数量和异质性增加时保持稳定，性能优于基线。

## 摘要（原文）

> Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective.
>   We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

