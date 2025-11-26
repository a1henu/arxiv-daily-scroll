---
layout: default
title: Beyond Relational: Semantic-Aware Multi-Modal Analytics with LLM-Native Query Optimization
---

# Beyond Relational: Semantic-Aware Multi-Modal Analytics with LLM-Native Query Optimization
**arXiv**：[2511.19830v1](https://arxiv.org/abs/2511.19830) · [PDF](https://arxiv.org/pdf/2511.19830.pdf)  
**作者**：Junhao Zhu, Lu Chen, Xiangyu Ke, Ziquan Fang, Tianyi Li, Yunjun Gao, Christian S. Jensen  

**一句话要点**：提出Nirvana框架以优化多模态数据分析中的语义查询处理

**关键词**：多模态数据分析, 语义查询优化, LLM驱动系统, 查询计划搜索, 成本优化, 计算重用

## 3 点简述
- 传统关系查询难以捕捉语义，限制多模态分析应用
- 结合逻辑优化器与物理优化器，提升LLM查询效率
- 实验显示运行时间减少10%-85%，成本平均降低76%

## 摘要（原文）

> Multi-modal analytical processing has the potential to transform applications in e-commerce, healthcare, entertainment, and beyond. However, real-world adoption remains elusive due to the limited ability of traditional relational query operators to capture query semantics. The emergence of foundation models, particularly the large language models (LLMs), opens up new opportunities to develop flexible, semantic-aware data analytics systems that transcend the relational paradigm.
>   We present Nirvana, a multi-modal data analytics framework that incorporates programmable semantic operators while leveraging both logical and physical query optimization strategies, tailored for LLM-driven semantic query processing. Nirvana addresses two key challenges. First, it features an agentic logical optimizer that uses natural language-specified transformation rules and random-walk-based search to explore vast spaces of semantically equivalent query plans -- far beyond the capabilities of conventional optimizers. Second, it introduces a cost-aware physical optimizer that selects the most effective LLM backend for each operator using a novel improvement-score metric. To further enhance efficiency, Nirvana incorporates computation reuse and evaluation pushdown techniques guided by model capability hypotheses. Experimental evaluations on three real-world benchmarks demonstrate that Nirvana is able to reduce end-to-end runtime by 10%--85% and reduces system processing costs by 76% on average, outperforming state-of-the-art systems at both efficiency and scalability.

