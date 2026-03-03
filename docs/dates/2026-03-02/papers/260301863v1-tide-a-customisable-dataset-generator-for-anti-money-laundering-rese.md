---
layout: default
title: Tide: A Customisable Dataset Generator for Anti-Money Laundering Research
---

# Tide: A Customisable Dataset Generator for Anti-Money Laundering Research
**arXiv**：[2603.01863v1](https://arxiv.org/abs/2603.01863) · [PDF](https://arxiv.org/pdf/2603.01863.pdf)  
**作者**：Montijn van den Beukel, Jože Martin Rožanec, Ana-Lucia Varbanescu  

**一句话要点**：提出Tide可定制数据集生成器，以解决反洗钱研究中缺乏真实交易数据的问题。

**关键词**：反洗钱研究, 合成数据集生成, 图神经网络, 时间动态建模, 机器学习基准, 金融网络分析

## 3 点简述
- 核心问题：真实金融数据因隐私和法律限制难以获取，现有合成生成器忽略洗钱的时间动态特征。
- 方法要点：Tide生成基于图的金融网络，结合结构和时间特性定义洗钱模式，支持可重复和定制化生成。
- 实验或效果：评估显示模型排名随非法比率变化，LightGBM在低比率下表现最佳，XGBoost在高比率下领先。

## 摘要（原文）

> The lack of accessible transactional data significantly hinders machine learning research for Anti-Money Laundering (AML). Privacy and legal concerns prevent the sharing of real financial data, while existing synthetic generators focus on simplistic structural patterns and neglect the temporal dynamics (timing and frequency) that characterise sophisticated laundering schemes.
>   We present Tide, an open-source synthetic dataset generator that produces graph-based financial networks incorporating money laundering patterns defined by both structural and temporal characteristics. Tide enables reproducible, customisable dataset generation tailored to specific research needs. We release two reference datasets with varying illicit ratios (LI: 0.10\%, HI: 0.19\%), alongside the implementation of state-of-the-art detection models.
>   Evaluation across these datasets reveals condition-dependent model rankings: LightGBM achieves the highest PR-AUC (78.05) in the low illicit ratio condition, while XGBoost performs best (85.12) at higher fraud prevalence. These divergent rankings demonstrate that the reference datasets can meaningfully differentiate model capabilities across operational conditions.
>   Tide provides the research community with a configurable benchmark that exposes meaningful performance variation across model architectures, advancing the development of robust AML detection methods.

