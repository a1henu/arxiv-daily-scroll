---
layout: default
title: Building a Correct-by-Design Lakehouse. Data Contracts, Versioning, and Transactional Pipelines for Humans and Agents
---

# Building a Correct-by-Design Lakehouse. Data Contracts, Versioning, and Transactional Pipelines for Humans and Agents
**arXiv**：[2602.02335v1](https://arxiv.org/abs/2602.02335) · [PDF](https://arxiv.org/pdf/2602.02335.pdf)  
**作者**：Weiming Sheng, Jinlang Wang, Manuel Barros, Aldrin Montana, Jacopo Tagliabue, Luca Bigon  

**一句话要点**：提出Bauplan代码优先湖仓，通过类型化表合约、Git式版本化和事务性运行解决并发操作安全问题。

**关键词**：湖仓架构, 数据合约, 数据版本化, 事务性管道, 并发安全, 代码优先设计

## 3 点简述
- 湖仓在并发操作时存在上游下游不匹配和部分效应泄漏等安全问题。
- 采用类型化表合约、Git式数据版本化和事务性运行来确保管道边界可检查、可审查和原子性。
- 基于轻量级形式化事务模型报告早期结果，并讨论未来工作。

## 摘要（原文）

> Lakehouses are the default cloud platform for analytics and AI, but they become unsafe when untrusted actors concurrently operate on production data: upstream-downstream mismatches surface only at runtime, and multi-table pipelines can leak partial effects. Inspired by software engineering, we design Bauplan, a code-first lakehouse that aims to make (most) illegal states unrepresentable using familiar abstractions. Bauplan acts along three axes: typed table contracts to make pipeline boundaries checkable, Git-like data versioning for review and reproducibility, and transactional runs that guarantee pipeline-level atomicity. We report early results from a lightweight formal transaction model and discuss future work motivated by counterexamples.

