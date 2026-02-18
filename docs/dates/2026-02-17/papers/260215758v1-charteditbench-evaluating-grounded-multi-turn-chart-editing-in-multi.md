---
layout: default
title: ChartEditBench: Evaluating Grounded Multi-Turn Chart Editing in Multimodal Language Models
---

# ChartEditBench: Evaluating Grounded Multi-Turn Chart Editing in Multimodal Language Models
**arXiv**：[2602.15758v1](https://arxiv.org/abs/2602.15758) · [PDF](https://arxiv.org/pdf/2602.15758.pdf)  
**作者**：Manav Nitin Kapadnis, Lawanya Baghel, Atharva Naik, Carolyn Rosé  

**一句话要点**：提出ChartEditBench基准以评估多模态大语言模型在多轮图表编辑中的持续交互能力

**关键词**：多模态大语言模型, 图表编辑基准, 多轮交互评估, 执行保真度检查, 视觉相似性验证, 意图感知编程

## 3 点简述
- 核心问题：现有MLLMs在单轮图表生成表现强，但多轮迭代编辑中因错误累积和共享上下文断裂导致性能下降
- 方法要点：构建包含5000条难度控制修改链的基准，集成基于执行的保真度检查、像素级视觉相似性和逻辑代码验证的评估框架
- 实验或效果：实验显示MLLMs在风格编辑表现强，但在数据转换中频繁执行失败，基准为意图感知多模态编程提供挑战性测试

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) perform strongly on single-turn chart generation, their ability to support real-world exploratory data analysis remains underexplored. In practice, users iteratively refine visualizations through multi-turn interactions that require maintaining common ground, tracking prior edits, and adapting to evolving preferences. We introduce ChartEditBench, a benchmark for incremental, visually grounded chart editing via code, comprising 5,000 difficulty-controlled modification chains and a rigorously human-verified subset. Unlike prior one-shot benchmarks, ChartEditBench evaluates sustained, context-aware editing. We further propose a robust evaluation framework that mitigates limitations of LLM-as-a-Judge metrics by integrating execution-based fidelity checks, pixel-level visual similarity, and logical code verification. Experiments with state-of-the-art MLLMs reveal substantial degradation in multi-turn settings due to error accumulation and breakdowns in shared context, with strong performance on stylistic edits but frequent execution failures on data-centric transformations. ChartEditBench, establishes a challenging testbed for grounded, intent-aware multimodal programming.

