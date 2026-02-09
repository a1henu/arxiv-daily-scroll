---
layout: default
title: Autoregressive Models for Knowledge Graph Generation
---

# Autoregressive Models for Knowledge Graph Generation
**arXiv**：[2602.06707v1](https://arxiv.org/abs/2602.06707) · [PDF](https://arxiv.org/pdf/2602.06707.pdf)  
**作者**：Thiviyan Thanapalasingam, Antonis Vozikis, Peter Bloem, Paul Groth  

**一句话要点**：提出自回归模型ARK以解决知识图谱生成中的语义依赖与约束学习问题

**关键词**：知识图谱生成, 自回归模型, 语义约束学习, 变分扩展, 计算效率, 知识库补全

## 3 点简述
- 核心问题：知识图谱生成需学习三元组间复杂语义依赖，同时满足领域有效性约束，不同于独立评分链接预测
- 方法要点：ARK将图谱视为三元组序列，通过自回归建模学习隐式语义约束，无需显式规则监督
- 实验或效果：在IntelliGraphs基准上，模型语义有效性达89.2%至100.0%，能生成训练未见的新图谱

## 摘要（原文）

> Knowledge Graph (KG) generation requires models to learn complex semantic dependencies between triples while maintaining domain validity constraints. Unlike link prediction, which scores triples independently, generative models must capture interdependencies across entire subgraphs to produce semantically coherent structures. We present ARK (Auto-Regressive Knowledge Graph Generation), a family of autoregressive models that generate KGs by treating graphs as sequences of (head, relation, tail) triples. ARK learns implicit semantic constraints directly from data, including type consistency, temporal validity, and relational patterns, without explicit rule supervision. On the IntelliGraphs benchmark, our models achieve 89.2% to 100.0% semantic validity across diverse datasets while generating novel graphs not seen during training. We also introduce SAIL, a variational extension of ARK that enables controlled generation through learned latent representations, supporting both unconditional sampling and conditional completion from partial graphs. Our analysis reveals that model capacity (hidden dimensionality >= 64) is more critical than architectural depth for KG generation, with recurrent architectures achieving comparable validity to transformer-based alternatives while offering substantial computational efficiency. These results demonstrate that autoregressive models provide an effective framework for KG generation, with practical applications in knowledge base completion and query answering.

