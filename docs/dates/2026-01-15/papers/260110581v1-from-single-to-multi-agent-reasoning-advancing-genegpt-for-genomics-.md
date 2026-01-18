---
layout: default
title: From Single to Multi-Agent Reasoning: Advancing GeneGPT for Genomics QA
---

# From Single to Multi-Agent Reasoning: Advancing GeneGPT for Genomics QA
**arXiv**：[2601.10581v1](https://arxiv.org/abs/2601.10581) · [PDF](https://arxiv.org/pdf/2601.10581.pdf)  
**作者**：Kimia Abedini, Farzad Shami, Gianmaria Silvello  

**一句话要点**：提出GenomAgent多智能体框架以提升基因组问答性能

**关键词**：基因组问答, 多智能体系统, 大语言模型, 生物信息学, 知识提取

## 3 点简述
- 核心问题：基因组问答中LLMs受限于领域数据库访问，现有方法依赖刚性API。
- 方法要点：构建多智能体框架，协调专家智能体处理复杂查询，增强适应性。
- 实验或效果：在GeneTuring基准上平均性能优于GeneGPT 12%，框架可扩展至其他科学领域。

## 摘要（原文）

> Comprehending genomic information is essential for biomedical research, yet extracting data from complex distributed databases remains challenging. Large language models (LLMs) offer potential for genomic Question Answering (QA) but face limitations due to restricted access to domain-specific databases. GeneGPT is the current state-of-the-art system that enhances LLMs by utilizing specialized API calls, though it is constrained by rigid API dependencies and limited adaptability. We replicate GeneGPT and propose GenomAgent, a multi-agent framework that efficiently coordinates specialized agents for complex genomics queries. Evaluated on nine tasks from the GeneTuring benchmark, GenomAgent outperforms GeneGPT by 12% on average, and its flexible architecture extends beyond genomics to various scientific domains needing expert knowledge extraction.

