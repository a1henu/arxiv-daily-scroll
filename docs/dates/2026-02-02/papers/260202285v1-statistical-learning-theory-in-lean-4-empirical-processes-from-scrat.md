---
layout: default
title: Statistical Learning Theory in Lean 4: Empirical Processes from Scratch
---

# Statistical Learning Theory in Lean 4: Empirical Processes from Scratch
**arXiv**：[2602.02285v1](https://arxiv.org/abs/2602.02285) · [PDF](https://arxiv.org/pdf/2602.02285.pdf)  
**作者**：Yuanhe Zhang, Jason D. Lee, Fanghui Liu  

**一句话要点**：在Lean 4中首次完整形式化统计学习理论，基于经验过程理论构建可重用基础。

**关键词**：统计学习理论, Lean 4形式化, 经验过程理论, Dudley熵积分, 最小二乘回归, 人机协作验证

## 3 点简述
- 核心问题：Lean 4 Mathlib库中统计学习理论内容缺失，需形式化经验过程理论。
- 方法要点：开发高斯Lipschitz集中性、Dudley熵积分定理，应用于最小二乘回归。
- 实验或效果：通过人机协作工作流验证，代码开源，为机器学习理论提供形式化工具。

## 摘要（原文）

> We present the first comprehensive Lean 4 formalization of statistical learning theory (SLT) grounded in empirical process theory. Our end-to-end formal infrastructure implement the missing contents in latest Lean 4 Mathlib library, including a complete development of Gaussian Lipschitz concentration, the first formalization of Dudley's entropy integral theorem for sub-Gaussian processes, and an application to least-squares (sparse) regression with a sharp rate. The project was carried out using a human-AI collaborative workflow, in which humans design proof strategies and AI agents execute tactical proof construction, leading to the human-verified Lean 4 toolbox for SLT. Beyond implementation, the formalization process exposes and resolves implicit assumptions and missing details in standard SLT textbooks, enforcing a granular, line-by-line understanding of the theory. This work establishes a reusable formal foundation and opens the door for future developments in machine learning theory. The code is available at https://github.com/YuanheZ/lean-stat-learning-theory

