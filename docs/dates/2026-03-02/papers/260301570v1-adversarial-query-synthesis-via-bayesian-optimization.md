---
layout: default
title: Adversarial Query Synthesis via Bayesian Optimization
---

# Adversarial Query Synthesis via Bayesian Optimization
**arXiv**：[2603.01570v1](https://arxiv.org/abs/2603.01570) · [PDF](https://arxiv.org/pdf/2603.01570.pdf)  
**作者**：Jeffrey Tao, Yimeng Zeng, Haydn Thomas Jones, Natalie Maus, Osbert Bastani, Jacob R. Gardner, Ryan Marcus  

**一句话要点**：提出贝叶斯优化技术以自动搜索困难基准查询，减少数据库基准构建的手动工作量。

**关键词**：数据库基准, 贝叶斯优化, 查询生成, 机器学习集成, 性能评估

## 3 点简述
- 核心问题：数据库基准构建需大量手动工作，难以生成困难查询以评估系统性能。
- 方法要点：采用贝叶斯优化自动搜索查询空间，高效识别导致高优化开销的查询。
- 实验或效果：初步实验显示，生成查询的优化空间比现有基准增加一倍以上。

## 摘要（原文）

> Benchmark workloads are extremely important to the database management research community, especially as more machine learning components are integrated into database systems. Here, we propose a Bayesian optimization technique to automatically search for difficult benchmark queries, significantly reducing the amount of manual effort usually required. In preliminary experiments, we show that our approach can generate queries with more than double the optimization headroom compared to existing benchmarks.

