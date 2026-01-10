---
layout: default
title: AdaptEval: A Benchmark for Evaluating Large Language Models on Code Snippet Adaptation
---

# AdaptEval: A Benchmark for Evaluating Large Language Models on Code Snippet Adaptation
**arXiv**：[2601.04540v1](https://arxiv.org/abs/2601.04540) · [PDF](https://arxiv.org/pdf/2601.04540.pdf)  
**作者**：Tanghaoran Zhang, Xinjun Mao, Shangwen Wang, Yuxin Zhao, Yao Lu, Jin Zhang, Zhang Zhang, Kang Yang, Yue Yu  

**一句话要点**：提出AdaptEval基准以评估大语言模型在代码片段适应任务中的性能

**关键词**：代码适应评估, 大语言模型基准, 软件工程任务, 多粒度标注, 细粒度测试

## 3 点简述
- 核心问题：缺乏评估大语言模型在代码适应任务中的基准，其实用性未知
- 方法要点：基于开发者实践构建任务，包含多粒度标注和细粒度评估框架
- 实验或效果：评估六个指令调优模型，揭示模型在遵循显式指令方面的局限性

## 摘要（原文）

> Recent advancements in large language models (LLMs) have automated various software engineering tasks, with benchmarks emerging to evaluate their capabilities. However, for adaptation, a critical activity during code reuse, there is no benchmark to assess LLMs' performance, leaving their practical utility in this area unclear. To fill this gap, we propose AdaptEval, a benchmark designed to evaluate LLMs on code snippet adaptation. Unlike existing benchmarks, AdaptEval incorporates the following three distinctive features: First, Practical Context. Tasks in AdaptEval are derived from developers' practices, preserving rich contextual information from Stack Overflow and GitHub communities. Second, Multi-granularity Annotation. Each task is annotated with requirements at both task and adaptation levels, supporting the evaluation of LLMs across diverse adaptation scenarios. Third, Fine-grained Evaluation. AdaptEval includes a two-tier testing framework combining adaptation-level and function-level tests, which enables evaluating LLMs' performance across various individual adaptations. Based on AdaptEval, we conduct the first empirical study to evaluate six instruction-tuned LLMs and especially three reasoning LLMs on code snippet adaptation. Experimental results demonstrate that AdaptEval enables the assessment of LLMs' adaptation capabilities from various perspectives. It also provides critical insights into their current limitations, particularly their struggle to follow explicit instructions. We hope AdaptEval can facilitate further investigation and enhancement of LLMs' capabilities in code snippet adaptation, supporting their real-world applications.

