---
layout: default
title: Taming Scylla: Understanding the multi-headed agentic daemon of the coding seas
---

# Taming Scylla: Understanding the multi-headed agentic daemon of the coding seas
**arXiv**：[2602.08765v1](https://arxiv.org/abs/2602.08765) · [PDF](https://arxiv.org/pdf/2602.08765.pdf)  
**作者**：Micah Villmow  

**一句话要点**：提出Scylla评估框架，通过结构化消融研究量化代理编码工具中架构选择对能力与成本的影响。

**关键词**：代理编码评估, 成本通过率, 结构化消融研究, 模型无关框架, 多代理系统, LLM工具基准测试

## 3 点简述
- 核心问题：缺乏严格方法评估LLM代理编码工具中不同架构选择（如提示、技能、多代理设置）对能力与成本的实际影响。
- 方法要点：引入七层测试（T0-T6）逐步增加复杂度，使用成本通过率（CoP）作为关键指标，模型无关且可复现。
- 实验或效果：使用Claude Sonnet 4.5演示，结合多LLM法官评估，表明架构复杂度不一定提升质量，量化了复杂度与效率的权衡。

## 摘要（原文）

> LLM-based tools are automating more software development tasks at a rapid pace, but there is no rigorous way to evaluate how different architectural choices -- prompts, skills, tools, multi-agent setups -- materially affect both capability and cost. This paper introduces Scylla, an evaluation framework for benchmarking agentic coding tools through structured ablation studies that uses seven testing tiers (T0-T6) progressively adding complexity to isolate what directly influences results and how. The key metric is Cost-of-Pass (CoP): the expected dollar cost to get one correct solution, which directly quantifies the trade-off between complexity and efficiency. The framework is model-agnostic, designed to work with any CLI tool; this paper demonstrates it with Claude Sonnet 4.5, using multiple LLM judges (Opus 4.5, Sonnet 4.5, Haiku 4.5) from the same vendor for evaluation consensus, where judges score results using direct tests, human-designed LLM-evaluated rubrics, and qualitative assessment. The result is a reproducible framework that quantifies trade-offs between agent complexity and actual outcomes, suggesting that architectural complexity does not always improve quality.

