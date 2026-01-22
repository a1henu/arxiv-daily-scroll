---
layout: default
title: HELIOS: Hierarchical Graph Abstraction for Structure-Aware LLM Decompilation
---

# HELIOS: Hierarchical Graph Abstraction for Structure-Aware LLM Decompilation
**arXiv**：[2601.14598v1](https://arxiv.org/abs/2601.14598) · [PDF](https://arxiv.org/pdf/2601.14598.pdf)  
**作者**：Yonatan Gizachew Achamyeleh, Harsh Thomare, Mohammad Abdullah Al Faruque  

**一句话要点**：提出HELIOS框架，通过层次化图抽象提升LLM反编译的结构感知能力。

**关键词**：LLM反编译, 控制流图抽象, 编译器反馈, 结构感知推理, 跨架构兼容性

## 3 点简述
- 核心问题：现有LLM反编译忽略程序控制流图，导致输出语法脆弱且逻辑不一致。
- 方法要点：将二进制控制流和函数调用总结为层次化文本表示，结合原始反编译器输出和可选编译器反馈。
- 实验或效果：在HumanEval-Decompile上显著提升编译率和功能正确性，跨架构保持高语法正确性。

## 摘要（原文）

> Large language models (LLMs) have recently been applied to binary decompilation, yet they still treat code as plain text and ignore the graphs that govern program control flow. This limitation often yields syntactically fragile and logically inconsistent output, especially for optimized binaries. This paper presents \textsc{HELIOS}, a framework that reframes LLM-based decompilation as a structured reasoning task. \textsc{HELIOS} summarizes a binary's control flow and function calls into a hierarchical text representation that spells out basic blocks, their successors, and high-level patterns such as loops and conditionals. This representation is supplied to a general-purpose LLM, along with raw decompiler output, optionally combined with a compiler-in-the-loop that returns error messages when the generated code fails to build.
>   On HumanEval-Decompile for \texttt{x86\_64}, \textsc{HELIOS} raises average object file compilability from 45.0\% to 85.2\% for Gemini~2.0 and from 71.4\% to 89.6\% for GPT-4.1~Mini. With compiler feedback, compilability exceeds 94\% and functional correctness improves by up to 5.6 percentage points over text-only prompting. Across six architectures drawn from x86, ARM, and MIPS, \textsc{HELIOS} reduces the spread in functional correctness while keeping syntactic correctness consistently high, all without fine-tuning. These properties make \textsc{HELIOS} a practical building block for reverse engineering workflows in security settings where analysts need recompilable, semantically faithful code across diverse hardware targets.

