---
layout: default
title: Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
---

# Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking
**arXiv**：[2602.24009v1](https://arxiv.org/abs/2602.24009) · [PDF](https://arxiv.org/pdf/2602.24009.pdf)  
**作者**：Zhicheng Fang, Jingjie Zheng, Chenxu Fu, Wei Xu  

**一句话要点**：提出JAILBREAK FOUNDRY系统，通过多智能体工作流将越狱论文转化为可执行模块，以解决LLM安全基准滞后问题。

**关键词**：越狱攻击, 基准测试, 多智能体系统, 可重现性, 大语言模型安全, 自动化评估

## 3 点简述
- 核心问题：LLM越狱技术演进快于基准，导致评估过时且难以跨论文比较。
- 方法要点：采用JBF-LIB、JBF-FORGE和JBF-EVAL三组件，自动化翻译论文为模块并标准化评估。
- 实验或效果：在30个攻击中，平均ASR偏差+0.26个百分点，代码重用率达82.5%，实现标准化评估。

## 摘要（原文）

> Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce JAILBREAK FOUNDRY (JBF), a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) JBF-LIB for shared contracts and reusable utilities; (ii) JBF-FORGE for the multi-agent paper-to-module translation; and (iii) JBF-EVAL for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced-reported) attack success rate (ASR) deviation of +0.26 percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

