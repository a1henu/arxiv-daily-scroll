---
layout: default
title: Anka: A Domain-Specific Language for Reliable LLM Code Generation
---

# Anka: A Domain-Specific Language for Reliable LLM Code Generation
**arXiv**：[2512.23214v1](https://arxiv.org/abs/2512.23214) · [PDF](https://arxiv.org/pdf/2512.23214.pdf)  
**作者**：Saif Khalfan Saif Al Mazrouei  

**一句话要点**：提出Anka领域特定语言以提升LLM在复杂代码生成任务中的可靠性

**关键词**：领域特定语言, 代码生成, LLM可靠性, 数据转换管道, 约束语法, 基准测试

## 3 点简述
- LLM在复杂多步编程任务中因通用语言灵活性导致系统错误
- Anka DSL通过约束语法减少歧义，实现高解析成功率和任务准确率
- 实验显示Anka在多步管道任务中准确率显著优于Python，验证DSL设计优势

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in code generation, yet they exhibit systematic errors on complex, multi-step programming tasks. We hypothesize that these errors stem from the flexibility of general-purpose languages, which permits multiple valid approaches and requires implicit state management. To test this hypothesis, we introduce Anka, a domain-specific language (DSL) for data transformation pipelines designed with explicit, constrained syntax that reduces ambiguity in code generation. Despite having zero prior training exposure to Anka, Claude 3.5 Haiku achieves 99.9% parse success and 95.8% overall task accuracy across 100 benchmark problems. Critically, Anka demonstrates a 40 percentage point accuracy advantage over Python on multi-step pipeline tasks (100% vs. 60%), where Python's flexible syntax leads to frequent errors in operation sequencing and variable management. Cross-model validation with GPT-4o-mini confirms this advantage (+26.7 percentage points on multi-step tasks). Our results demonstrate that: (1) LLMs can learn novel DSLs entirely from in-context prompts, achieving near-native accuracy; (2) constrained syntax significantly reduces errors on complex tasks; and (3) domain-specific languages purposefully designed for LLM generation can outperform general-purpose languages on which the LLM has extensive training. We release the complete language implementation, benchmark suite, and evaluation framework to facilitate further research.

