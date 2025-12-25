---
layout: default
title: LLM Swiss Round: Aggregating Multi-Benchmark Performance via Competitive Swiss-System Dynamics
---

# LLM Swiss Round: Aggregating Multi-Benchmark Performance via Competitive Swiss-System Dynamics
**arXiv**：[2512.21010v1](https://arxiv.org/abs/2512.21010) · [PDF](https://arxiv.org/pdf/2512.21010.pdf)  
**作者**：Jiashuo Liu, Jiayun Wu, Chunjie Wu, Jingkai Liu, Zaiyuan Wang, Huan Zhou, Wenhao Huang, Hongseok Namkoong  

**一句话要点**：提出竞争瑞士系统动态框架以聚合多基准性能，实现风险感知的大语言模型评估

**关键词**：大语言模型评估, 竞争瑞士系统, 蒙特卡洛模拟, 失败敏感性分析, 多基准聚合, 动态排名

## 3 点简述
- 当前大语言模型评估方法依赖静态评分，难以平衡多基准权重和捕捉动态竞争适应性。
- 引入竞争瑞士系统动态框架，通过多轮顺序竞赛模拟动态配对，结合蒙特卡洛模拟计算期望胜分。
- 实施失败敏感性分析，参数化每轮淘汰量以区分稳健通用模型和激进专业模型，提供更细致排名。

## 摘要（原文）

> The rapid proliferation of Large Language Models (LLMs) and diverse specialized benchmarks necessitates a shift from fragmented, task-specific metrics to a holistic, competitive ranking system that effectively aggregates performance across multiple ability dimensions. Primarily using static scoring, current evaluation methods are fundamentally limited. They struggle to determine the proper mix ratio across diverse benchmarks, and critically, they fail to capture a model's dynamic competitive fitness or its vulnerability when confronted with sequential, high-stakes tasks. To address this, we introduce the novel Competitive Swiss-System Dynamics (CSD) framework. CSD simulates a multi-round, sequential contest where models are dynamically paired across a curated sequence of benchmarks based on their accumulated win-loss record. And Monte Carlo Simulation ($N=100,000$ iterations) is used to approximate the statistically robust Expected Win Score ($E[S_m]$), which eliminates the noise of random pairing and early-round luck. Furthermore, we implement a Failure Sensitivity Analysis by parameterizing the per-round elimination quantity ($T_k$), which allows us to profile models based on their risk appetite--distinguishing between robust generalists and aggressive specialists. We demonstrate that CSD provides a more nuanced and context-aware ranking than traditional aggregate scoring and static pairwise models, representing a vital step towards risk-informed, next-generation LLM evaluation.

