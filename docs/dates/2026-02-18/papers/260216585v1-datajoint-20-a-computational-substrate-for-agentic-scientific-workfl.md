---
layout: default
title: DataJoint 2.0: A Computational Substrate for Agentic Scientific Workflows
---

# DataJoint 2.0: A Computational Substrate for Agentic Scientific Workflows
**arXiv**：[2602.16585v1](https://arxiv.org/abs/2602.16585) · [PDF](https://arxiv.org/pdf/2602.16585.pdf)  
**作者**：Dimitri Yatsenko, Thinh T. Nguyen  

**一句话要点**：提出DataJoint 2.0关系型工作流模型以支持科学工作流的代理协作

**关键词**：科学工作流管理, 关系型数据库, 数据溯源, 代理协作, SciOps

## 3 点简述
- 核心问题：科学数据管道缺乏类似DevOps的SciOps，导致溯源分散且无事务保证。
- 方法要点：通过关系型工作流模型，用表表示步骤、行表示工件，外键规定执行顺序。
- 实验或效果：集成对象存储、语义匹配、可扩展类型系统和分布式作业协调，支持代理参与而不破坏数据。

## 摘要（原文）

> Operational rigor determines whether human-agent collaboration succeeds or fails. Scientific data pipelines need the equivalent of DevOps -- SciOps -- yet common approaches fragment provenance across disconnected systems without transactional guarantees. DataJoint 2.0 addresses this gap through the relational workflow model: tables represent workflow steps, rows represent artifacts, foreign keys prescribe execution order. The schema specifies not only what data exists but how it is derived -- a single formal system where data structure, computational dependencies, and integrity constraints are all queryable, enforceable, and machine-readable. Four technical innovations extend this foundation: object-augmented schemas integrating relational metadata with scalable object storage, semantic matching using attribute lineage to prevent erroneous joins, an extensible type system for domain-specific formats, and distributed job coordination designed for composability with external orchestration. By unifying data structure, data, and computational transformations, DataJoint creates a substrate for SciOps where agents can participate in scientific workflows without risking data corruption.

