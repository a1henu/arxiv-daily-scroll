---
layout: default
title: Easy Data Unlearning Bench
---

# Easy Data Unlearning Bench
**arXiv**：[2602.16400v1](https://arxiv.org/abs/2602.16400) · [PDF](https://arxiv.org/pdf/2602.16400.pdf)  
**作者**：Roy Rinberg, Pol Puigdemont, Martin Pawelczyk, Volkan Cevher  

**一句话要点**：提出统一可扩展的基准套件以简化机器遗忘算法的评估

**关键词**：机器遗忘, 基准评估, KLoM指标, 可扩展框架, 可重现研究

## 3 点简述
- 核心问题：现有机器遗忘评估基准设置复杂且工程开销大，阻碍研究进展。
- 方法要点：引入基于KLoM指标的基准套件，提供预计算模型集合和标准化基础设施。
- 实验或效果：通过标准化设置和指标，支持可重现、可扩展和公平的遗忘方法比较。

## 摘要（原文）

> Evaluating machine unlearning methods remains technically challenging, with recent benchmarks requiring complex setups and significant engineering overhead. We introduce a unified and extensible benchmarking suite that simplifies the evaluation of unlearning algorithms using the KLoM (KL divergence of Margins) metric. Our framework provides precomputed model ensembles, oracle outputs, and streamlined infrastructure for running evaluations out of the box. By standardizing setup and metrics, it enables reproducible, scalable, and fair comparison across unlearning methods. We aim for this benchmark to serve as a practical foundation for accelerating research and promoting best practices in machine unlearning. Our code and data are publicly available.

