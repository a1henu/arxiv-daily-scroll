---
layout: default
title: Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics
---

# Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics
**arXiv**：[2601.02200v1](https://arxiv.org/abs/2601.02200) · [PDF](https://arxiv.org/pdf/2601.02200.pdf)  
**作者**：Markus Borg, Nadim Hagatulah, Adam Tornhill, Emma Söderberg  

**一句话要点**：提出CodeHealth指标以评估AI友好性，指导混合开发中AI干预风险

**关键词**：AI友好代码, 代码健康指标, LLM重构, 语义保留, 混合开发, Python代码分析

## 3 点简述
- 核心问题：混合开发时代，需确保代码对AI工具可靠，而传统优化仅针对人类理解。
- 方法要点：基于LLM重构5000个Python文件，研究AI友好代码概念与CodeHealth指标的关联。
- 实验或效果：发现CodeHealth与AI重构后语义保留相关，人类友好代码更兼容AI工具。

## 摘要（原文）

> We are entering a hybrid era in which human developers and AI coding agents work in the same codebases. While industry practice has long optimized code for human comprehension, it is increasingly important to ensure that LLMs with different capabilities can edit code reliably. In this study, we investigate the concept of ``AI-friendly code'' via LLM-based refactoring on a dataset of 5,000 Python files from competitive programming. We find a meaningful association between CodeHealth, a quality metric calibrated for human comprehension, and semantic preservation after AI refactoring. Our findings confirm that human-friendly code is also more compatible with AI tooling. These results suggest that organizations can use CodeHealth to guide where AI interventions are lower risk and where additional human oversight is warranted. Investing in maintainability not only helps humans; it also prepares for large-scale AI adoption.

