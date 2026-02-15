---
layout: default
title: Leveraging LLMs to support co-evolution between definitions and instances of textual DSLs: A Systematic Evaluation
---

# Leveraging LLMs to support co-evolution between definitions and instances of textual DSLs: A Systematic Evaluation
**arXiv**：[2602.11904v1](https://arxiv.org/abs/2602.11904) · [PDF](https://arxiv.org/pdf/2602.11904.pdf)  
**作者**：Weixing Zhang, Bowen Jiang, Yuhong Fu, Anne Koziolek, Regina Hebig, Daniel Strüber  

**一句话要点**：系统评估LLM支持文本DSL定义与实例协同演化的潜力

**关键词**：文本DSL协同演化, 大语言模型评估, 语法演化, 实例更新, 人文信息保留, 系统实验

## 3 点简述
- 核心问题：文本DSL语法演化导致实例过时，现有模型驱动方法不适用且可能丢失布局和注释等人文信息。
- 方法要点：使用Claude Sonnet 4.5和GPT-5.2，在十个案例语言上评估LLM协同演化语法和实例的正确性和人文信息保留。
- 实验效果：小规模实例（修改行数<20）性能优异（精确率和召回率≥94%），但随规模增大性能下降，响应时间增加，语法演化复杂性和删除粒度影响较大。

## 摘要（原文）

> Software languages evolve over time for reasons such as feature additions. When grammars evolve, textual instances that originally conformed to them may become outdated. While model-driven engineering provides many techniques for co-evolving models with metamodel changes, these approaches are not designed for textual DSLs and may lose human-relevant information such as layout and comments. This study systematically evaluates the potential of large language models (LLMs) for co-evolving grammars and instances of textual DSLs. Using Claude Sonnet 4.5 and GPT-5.2 across ten case languages with ten runs each, we assess both correctness and preservation of human-oriented information. Results show strong performance on small-scale cases ($\geq$94% precision and recall for instances requiring fewer than 20 modified lines), but performance degraded with scale: Claude maintains 85% recall at 40 lines, while GPT fails on the largest instances. Response time increases substantially with instance size, and grammar evolution complexity and deletion granularity affect performance more than change type. These findings clarify when LLM-based co-evolution is effective and where current limitations remain.

