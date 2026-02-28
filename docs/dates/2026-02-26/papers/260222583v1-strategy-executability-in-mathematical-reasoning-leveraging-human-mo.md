---
layout: default
title: Strategy Executability in Mathematical Reasoning: Leveraging Human-Model Differences for Effective Guidance
---

# Strategy Executability in Mathematical Reasoning: Leveraging Human-Model Differences for Effective Guidance
**arXiv**：[2602.22583v1](https://arxiv.org/abs/2602.22583) · [PDF](https://arxiv.org/pdf/2602.22583.pdf)  
**作者**：Weida Liang, Yiyou Sun, Shuyuan Nan, Chuang Li, Dawn Song, Kenji Kawaguchi  

**一句话要点**：提出选择性策略检索框架，通过建模策略可执行性提升数学推理的引导效果。

**关键词**：数学推理, 策略可执行性, 引导学习, 选择性检索, 人机差异

## 3 点简述
- 核心问题：基于示例的引导在数学推理中效果不稳定，源于策略使用与可执行性之间的差距。
- 方法要点：分析人机策略差异，设计选择性策略检索框架，利用多源信号建模可执行性。
- 实验或效果：在多个数学推理基准上实现稳定提升，准确率最高增加13个百分点。

## 摘要（原文）

> Example-based guidance is widely used to improve mathematical reasoning at inference time, yet its effectiveness is highly unstable across problems and models-even when the guidance is correct and problem-relevant. We show that this instability arises from a previously underexplored gap between strategy usage-whether a reasoning strategy appears in successful solutions-and strategy executability-whether the strategy remains effective when instantiated as guidance for a target model. Through a controlled analysis of paired human-written and model-generated solutions, we identify a systematic dissociation between usage and executability: human- and model-derived strategies differ in structured, domain-dependent ways, leading to complementary strengths and consistent source-dependent reversals under guidance. Building on this diagnosis, we propose Selective Strategy Retrieval (SSR), a test-time framework that explicitly models executability by selectively retrieving and combining strategies using empirical, multi-route, source-aware signals. Across multiple mathematical reasoning benchmarks, SSR yields reliable and consistent improvements over direct solving, in-context learning, and single-source guidance, improving accuracy by up to $+13$ points on AIME25 and $+5$ points on Apex for compact reasoning models. Code and benchmark are publicly available at: https://github.com/lwd17/strategy-execute-pipeline.

