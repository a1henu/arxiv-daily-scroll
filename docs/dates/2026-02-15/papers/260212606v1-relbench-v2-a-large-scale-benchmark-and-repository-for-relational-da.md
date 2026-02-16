---
layout: default
title: RelBench v2: A Large-Scale Benchmark and Repository for Relational Data
---

# RelBench v2: A Large-Scale Benchmark and Repository for Relational Data
**arXiv**：[2602.12606v1](https://arxiv.org/abs/2602.12606) · [PDF](https://arxiv.org/pdf/2602.12606.pdf)  
**作者**：Justin Gu, Rishabh Ranjan, Charilaos Kanatsoulis, Haiming Tang, Martin Jurkovic, Valter Hudovernik, Mark Znidar, Pranshu Chaturvedi, Parth Shroff, Fengyu Li, Jure Leskovec  

**一句话要点**：提出RelBench v2以扩展关系深度学习基准，支持大规模模型评估与多任务预测。

**关键词**：关系深度学习, 基准测试, 自动补全任务, 多表预测, 数据集扩展

## 3 点简述
- 关系深度学习缺乏大规模、真实场景的基准，阻碍模型系统评估与进展。
- RelBench v2新增四个大规模数据集和自动补全任务，并集成外部基准以统一评估框架。
- 实验显示关系深度学习模型在自动补全、预测和推荐任务中优于单表基线。

## 摘要（原文）

> Relational deep learning (RDL) has emerged as a powerful paradigm for learning directly on relational databases by modeling entities and their relationships across multiple interconnected tables. As this paradigm evolves toward larger models and relational foundation models, scalable and realistic benchmarks are essential for enabling systematic evaluation and progress. In this paper, we introduce RelBench v2, a major expansion of the RelBench benchmark for RDL. RelBench v2 adds four large-scale relational datasets spanning scholarly publications, enterprise resource planning, consumer platforms, and clinical records, increasing the benchmark to 11 datasets comprising over 22 million rows across 29 tables. We further introduce autocomplete tasks, a new class of predictive objectives that require models to infer missing attribute values directly within relational tables while respecting temporal constraints, expanding beyond traditional forecasting tasks constructed via SQL queries. In addition, RelBench v2 expands beyond its native datasets by integrating external benchmarks and evaluation frameworks: we translate event streams from the Temporal Graph Benchmark into relational schemas for unified relational-temporal evaluation, interface with ReDeLEx to provide uniform access to 70+ real-world databases suitable for pretraining, and incorporate 4DBInfer datasets and tasks to broaden multi-table prediction coverage. Experimental results demonstrate that RDL models consistently outperform single-table baselines across autocomplete, forecasting, and recommendation tasks, highlighting the importance of modeling relational structure explicitly.

