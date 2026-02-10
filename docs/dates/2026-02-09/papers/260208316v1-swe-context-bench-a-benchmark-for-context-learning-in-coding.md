---
layout: default
title: SWE Context Bench: A Benchmark for Context Learning in Coding
---

# SWE Context Bench: A Benchmark for Context Learning in Coding
**arXiv**：[2602.08316v1](https://arxiv.org/abs/2602.08316) · [PDF](https://arxiv.org/pdf/2602.08316.pdf)  
**作者**：Jared Zhu, Minhao Hu, Junde Wu  

**一句话要点**：提出SWE-ContextBench以评估编程代理在代码库任务中的经验复用能力

**关键词**：编程代理基准, 经验复用评估, 代码库任务, 软件工程基准, 经验检索

## 3 点简述
- 核心问题：现有基准未评估编程代理跨相关任务的经验复用能力，导致效率与准确性难以衡量
- 方法要点：基于SWE-Bench Lite构建，通过真实依赖关系扩展任务序列，评估准确性、时间效率和成本效率
- 实验或效果：正确选择摘要化经验可提升准确性并显著降低运行时和令牌成本，而错误选择则效果有限或负面

## 摘要（原文）

> Large language models are increasingly used as programming agents for repository level software engineering tasks. While recent benchmarks evaluate correctness in realistic codebases, they largely treat tasks as independent and do not assess whether agents can reuse experience across related problems. As a result, the ability of agents to accumulate, retrieve, and apply prior experience, as well as the efficiency gains from such reuse, remains difficult to measure. We introduce SWE-ContextBench, a benchmark designed to explicitly evaluate experience reuse in programming agents. Built on SWE-Bench Lite, SWE-ContextBench augments 300 base tasks with 99 related tasks derived from real dependency and reference relationships among GitHub issues and pull requests, forming task sequences with shared context. The benchmark evaluates agents along three complementary dimensions: prediction accuracy, time efficiency, and cost efficiency. Using SWE-ContextBench, we study multiple experience reuse settings, including oracle guided and autonomous retrieval, as well as full execution trajectories and compact summaries. Our results show that correctly selected summarized experience improves resolution accuracy and substantially reduces runtime and token cost, particularly on harder tasks. In contrast, unfiltered or incorrectly selected experience provides limited or negative benefits. These findings highlight the importance of experience representation and retrieval quality, and position SWE-ContextBench as a principled benchmark for studying experience reuse in programming agents.

