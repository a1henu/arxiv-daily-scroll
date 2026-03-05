---
layout: default
title: CONCUR: Benchmarking LLMs for Concurrent Code Generation
---

# CONCUR: Benchmarking LLMs for Concurrent Code Generation
**arXiv**：[2603.03683v1](https://arxiv.org/abs/2603.03683) · [PDF](https://arxiv.org/pdf/2603.03683.pdf)  
**作者**：Jue Huang, Tarek Mahmud, Corina Pasareanu, Guowei Yang  

**一句话要点**：提出CONCUR基准以评估大语言模型在并发代码生成中的能力

**关键词**：并发代码生成, 大语言模型评估, 软件工程基准, 死锁检测, 竞态条件

## 3 点简述
- 现有基准主要关注顺序代码，缺乏评估并发代码生成的有效方法
- CONCUR包含43个基础并发问题和72个变异体，共115个问题
- 评估显示当前模型在并发代码生成方面存在局限性

## 摘要（原文）

> Leveraging Large Language Models (LLMs) for code generation has increasingly emerged as a common practice in the domain of software engineering. Relevant benchmarks have been established to evaluate the code generation capabilities of LLMs. However, existing benchmarks focus primarily on sequential code, lacking the ability to effectively evaluate LLMs on concurrent code generation. Compared to sequential code, concurrent code exhibits greater complexity and possesses unique types of bugs, such as deadlocks and race conditions, that do not occur in sequential code. Therefore, a benchmark for evaluating sequential code generation cannot be useful for evaluating concurrent code generation with LLMs. To address this gap, we designed a benchmark CONCUR specifically aimed at evaluating the capability of LLMs to generate concurrent code. CONCUR consists of a base set of 43 concurrency problems derived from a standard concurrency textbook, together with 72 validated mutant variants, resulting in 115 total problems. The base problems serve as the semantic core of the benchmark, while the mutants expand linguistic and structural diversity. We conducted an evaluation of a range of LLMs on CONCUR, highlighting limitations of current models. Overall, our work provides a novel direction for evaluating the capability of LLMs to generate code with focus on concurrency.

