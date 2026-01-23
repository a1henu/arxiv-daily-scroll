---
layout: default
title: Benchmarking Text-to-Python against Text-to-SQL: The Impact of Explicit Logic and Ambiguity
---

# Benchmarking Text-to-Python against Text-to-SQL: The Impact of Explicit Logic and Ambiguity
**arXiv**：[2601.15728v1](https://arxiv.org/abs/2601.15728) · [PDF](https://arxiv.org/pdf/2601.15728.pdf)  
**作者**：Hangle Hu, Chenyu Hou, Bin Cao, Ruizhe Li  

**一句话要点**：提出BIRD-Python基准与逻辑补全框架，解决文本到Python代码生成中的歧义问题

**关键词**：文本到代码生成, Python代码生成, SQL代码生成, 基准评估, 歧义解析, 逻辑补全

## 3 点简述
- 核心问题：文本到Python在数据检索中的可靠性未充分探索，相比成熟的SQL存在歧义敏感性问题
- 方法要点：建立BIRD-Python基准进行跨范式评估，提出逻辑补全框架通过领域知识解决歧义
- 实验效果：当补充领域知识后，文本到Python能达到与文本到SQL相当的性能水平

## 摘要（原文）

> While Text-to-SQL remains the dominant approach for database interaction, real-world analytics increasingly require the flexibility of general-purpose programming languages such as Python or Pandas to manage file-based data and complex analytical workflows. Despite this growing need, the reliability of Text-to-Python in core data retrieval remains underexplored relative to the mature SQL ecosystem. To address this gap, we introduce BIRD-Python, a benchmark designed for cross-paradigm evaluation. We systematically refined the original dataset to reduce annotation noise and align execution semantics, thereby establishing a consistent and standardized baseline for comparison. Our analysis reveals a fundamental paradigmatic divergence: whereas SQL leverages implicit DBMS behaviors through its declarative structure, Python requires explicit procedural logic, making it highly sensitive to underspecified user intent. To mitigate this challenge, we propose the Logic Completion Framework (LCF), which resolves ambiguity by incorporating latent domain knowledge into the generation process. Experimental results show that (1) performance differences primarily stem from missing domain context rather than inherent limitations in code generation, and (2) when these gaps are addressed, Text-to-Python achieves performance parity with Text-to-SQL. These findings establish Python as a viable foundation for analytical agents-provided that systems effectively ground ambiguous natural language inputs in executable logical specifications. Resources are available at https://anonymous.4open.science/r/Bird-Python-43B7/.

