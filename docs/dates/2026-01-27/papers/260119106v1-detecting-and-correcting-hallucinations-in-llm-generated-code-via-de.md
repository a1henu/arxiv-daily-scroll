---
layout: default
title: Detecting and Correcting Hallucinations in LLM-Generated Code via Deterministic AST Analysis
---

# Detecting and Correcting Hallucinations in LLM-Generated Code via Deterministic AST Analysis
**arXiv**：[2601.19106v1](https://arxiv.org/abs/2601.19106) · [PDF](https://arxiv.org/pdf/2601.19106.pdf)  
**作者**：Dipin Khati, Daniel Rodriguez-Cardenas, Paul Pantzer, Denys Poshyvanyk  

**一句话要点**：提出基于确定性AST分析的框架以检测和纠正LLM生成代码中的知识冲突幻觉

**关键词**：代码生成, 静态分析, 抽象语法树, 知识冲突幻觉, 自动纠正, 确定性修复

## 3 点简述
- 核心问题：LLM生成代码常含知识冲突幻觉，如不存在的API参数，导致运行时错误且难以检测
- 方法要点：通过解析代码为AST，结合动态生成的知识库进行确定性静态分析，实现检测与自动纠正
- 实验或效果：在200个Python代码片段上，检测精度100%，召回率87.6%，自动纠正77.0%的幻觉

## 摘要（原文）

> Large Language Models (LLMs) for code generation boost productivity but frequently introduce Knowledge Conflicting Hallucinations (KCHs), subtle, semantic errors, such as non-existent API parameters, that evade linters and cause runtime failures. Existing mitigations like constrained decoding or non-deterministic LLM-in-the-loop repair are often unreliable for these errors. This paper investigates whether a deterministic, static-analysis framework can reliably detect \textit{and} auto-correct KCHs. We propose a post-processing framework that parses generated code into an Abstract Syntax Tree (AST) and validates it against a dynamically-generated Knowledge Base (KB) built via library introspection. This non-executing approach uses deterministic rules to find and fix both API and identifier-level conflicts. On a manually-curated dataset of 200 Python snippets, our framework detected KCHs with 100\% precision and 87.6\% recall (0.934 F1-score), and successfully auto-corrected 77.0\% of all identified hallucinations. Our findings demonstrate that this deterministic post-processing approach is a viable and reliable alternative to probabilistic repair, offering a clear path toward trustworthy code generation.

