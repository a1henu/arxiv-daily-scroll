---
layout: default
title: SOPRAG: Multi-view Graph Experts Retrieval for Industrial Standard Operating Procedures
---

# SOPRAG: Multi-view Graph Experts Retrieval for Industrial Standard Operating Procedures
**arXiv**：[2602.01858v1](https://arxiv.org/abs/2602.01858) · [PDF](https://arxiv.org/pdf/2602.01858.pdf)  
**作者**：Liangtao Lin, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen  

**一句话要点**：提出SOPRAG框架以解决工业标准操作程序检索中的结构复杂性和意图对齐问题

**关键词**：工业标准操作程序检索, 专家混合范式, 多视图图专家, LLM引导门控, 自动化基准构建, 检索增强生成

## 3 点简述
- 核心问题：工业SOP检索面临专有结构、条件相关性和可执行性挑战，传统RAG方法难以处理
- 方法要点：采用专家混合范式，引入实体、因果和流程图专家，结合程序卡和LLM引导门控机制优化检索
- 实验或效果：在四个工业领域实验中，SOPRAG在检索准确性和响应实用性上显著优于基线，并在关键任务中实现完美执行分数

## 摘要（原文）

> Standard Operating Procedures (SOPs) are essential for ensuring operational safety and consistency in industrial environments. However, retrieving and following these procedures presents unique challenges, such as rigid proprietary structures, condition-dependent relevance, and actionable execution requirement, which standard semantic-driven Retrieval-Augmented Generation (RAG) paradigms fail to address. Inspired by the Mixture-of-Experts (MoE) paradigm, we propose SOPRAG, a novel framework specifically designed to address the above pain points in SOP retrieval. SOPRAG replaces flat chunking with specialized Entity, Causal, and Flow graph experts to resolve industrial structural and logical complexities. To optimize and coordinate these experts, we propose a Procedure Card layer that prunes the search space to eliminate computational noise, and an LLM-Guided gating mechanism that dynamically weights these experts to align retrieval with operator intent. To address the scarcity of domain-specific data, we also introduce an automated, multi-agent workflow for benchmark construction. Extensive experiments across four industrial domains demonstrate that SOPRAG significantly outperforms strong lexical, dense, and graph-based RAG baselines in both retrieval accuracy and response utility, achieving perfect execution scores in real-world critical tasks.

