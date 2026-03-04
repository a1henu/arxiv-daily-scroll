---
layout: default
title: Type-Aware Retrieval-Augmented Generation with Dependency Closure for Solver-Executable Industrial Optimization Modeling
---

# Type-Aware Retrieval-Augmented Generation with Dependency Closure for Solver-Executable Industrial Optimization Modeling
**arXiv**：[2603.03180v1](https://arxiv.org/abs/2603.03180) · [PDF](https://arxiv.org/pdf/2603.03180.pdf)  
**作者**：Y. Zhong, R. Huang, M. Wang, Z. Guo, YC. Li, M. Yu, Z. Jin  

**一句话要点**：提出类型感知检索增强生成方法，结合依赖闭包，解决工业优化建模中自然语言到可执行代码的转换问题。

**关键词**：检索增强生成, 工业优化建模, 类型感知, 依赖闭包, 知识图谱, 可执行代码生成

## 3 点简述
- 核心问题：大语言模型在工业优化建模中常因类型不一致和依赖缺失生成不可编译代码。
- 方法要点：构建类型化知识库，通过图依赖传播计算最小依赖闭包，确保代码可执行性。
- 实验或效果：在需求响应优化和柔性作业车间调度案例中，方法生成可执行模型，优于传统检索增强生成基线。

## 摘要（原文）

> Automated industrial optimization modeling requires reliable translation of natural-language requirements into solver-executable code. However, large language models often generate non-compilable models due to missing declarations, type inconsistencies, and incomplete dependency contexts. We propose a type-aware retrieval-augmented generation (RAG) method that enforces modeling entity types and minimal dependency closure to ensure executability. Unlike existing RAG approaches that index unstructured text, our method constructs a domain-specific typed knowledge base by parsing heterogeneous sources, such as academic papers and solver code, into typed units and encoding their mathematical dependencies in a knowledge graph. Given a natural-language instruction, it performs hybrid retrieval and computes a minimal dependency-closed context, the smallest set of typed symbols required for solver-executable code, via dependency propagation over the graph. We validate the method on two constraint-intensive industrial cases: demand response optimization in battery production and flexible job shop scheduling. In the first case, our method generates an executable model incorporating demand-response incentives and load-reduction constraints, achieving peak shaving while preserving profitability; conventional RAG baselines fail. In the second case, it consistently produces compilable models that reach known optimal solutions, demonstrating robust cross-domain generalization; baselines fail entirely. Ablation studies confirm that enforcing type-aware dependency closure is essential for avoiding structural hallucinations and ensuring executability, addressing a critical barrier to deploying large language models in complex engineering optimization tasks.

