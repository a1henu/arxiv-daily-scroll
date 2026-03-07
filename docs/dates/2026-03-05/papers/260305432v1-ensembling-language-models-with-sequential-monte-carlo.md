---
layout: default
title: Ensembling Language Models with Sequential Monte Carlo
---

# Ensembling Language Models with Sequential Monte Carlo
**arXiv**：[2603.05432v1](https://arxiv.org/abs/2603.05432) · [PDF](https://arxiv.org/pdf/2603.05432.pdf)  
**作者**：Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, Clemente Pasti, Jacob Hoover Vigly, Timothy J. O'Donnell, Ryan Cotterell, Tim Vieira  

**一句话要点**：提出基于顺序蒙特卡洛的f-集成框架，以解决语言模型集成中的采样偏差问题。

**关键词**：语言模型集成, 顺序蒙特卡洛, 采样偏差, 结构化文本生成, f-集成分布

## 3 点简述
- 核心问题：语言模型集成时，简单聚合概率会导致采样偏差，难以处理模型词汇不匹配。
- 方法要点：引入f-集成分布框架，使用字节级顺序蒙特卡洛算法实现一致采样。
- 实验或效果：评估多种f-集成策略，显示优于传统概率平均，提升结构化文本生成性能。

## 摘要（原文）

> Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token probabilities yields samples from a locally normalized, biased approximation of the generally intractable ensemble distribution over strings. In this work, we introduce a unified framework for composing $K$ language models into $f$-ensemble distributions for a wide range of functions $f\colon\mathbb{R}_{\geq 0}^{K}\to\mathbb{R}_{\geq 0}$. To sample from these distributions, we propose a byte-level sequential Monte Carlo (SMC) algorithm that operates in a shared character space, enabling ensembles of models with mismatching vocabularies and consistent sampling in the limit. We evaluate a family of $f$-ensembles across prompt and model combinations for various structured text generation tasks, highlighting the benefits of alternative aggregation strategies over traditional probability averaging, and showing that better posterior approximations can yield better ensemble performance.

