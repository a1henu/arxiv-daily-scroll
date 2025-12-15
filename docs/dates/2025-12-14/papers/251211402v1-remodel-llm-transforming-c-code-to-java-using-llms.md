---
layout: default
title: REMODEL-LLM: Transforming C code to Java using LLMs
---

# REMODEL-LLM: Transforming C code to Java using LLMs
**arXiv**：[2512.11402v1](https://arxiv.org/abs/2512.11402) · [PDF](https://arxiv.org/pdf/2512.11402.pdf)  
**作者**：Aryan Gupta, Y. Raghu Reddy  

**一句话要点**：提出基于AST和规则提示的混合管道，评估小量化LLM在C到Java代码翻译中的性能

**关键词**：代码翻译, 量化语言模型, 抽象语法树, 规则提示, C到Java转换, 性能评估

## 3 点简述
- 研究C到Java代码自动翻译的挑战，涉及范式、内存模型和数据类型差异
- 采用AST语义分解和约束规则提示的混合方法，测试19个小量化LLM
- 结果显示仅三个模型通过超50%测试，但复杂概念如函数指针仍失败

## 摘要（原文）

> The automated translation of C code to Java code is a notoriously difficult task, fraught with challenges stemming from fundamental paradigm shifts (procedural vs. Object Oriented), memory models (manual pointers vs. Garbage Collection), and incompatible data types. This paper investigates the efficacy of 19 small, quantized LLMs (under 20 billion parameters) for the C to Java translation task. We use a novel, hybrid pipeline that leverages Abstract Syntax Trees (ASTs) for semantic decomposition and employs a highly constrained, rule based prompting strategy. The results are stark: a clear multi tiered performance divide emerged. The vast majority of models (Tier 3, e.g., llama3.1, gemma3, starcoder2) failed 100\% of the tests, proving incapable of generating even basic, runnable Java boilerplate. A small middle tier (Tier 2, e.g., mistral-nemo and mistral) produced runnable code but was plagued by dangerous semantic failures and wrong translations. Only three models (Tier 1: phi4, deepseek-coder-v2, codeqwen) proved viable, passing over 50\% of the test suite. Even these top models failed on the most complex C concepts, such as function pointers, sizeof, and enum logic, revealing a hard ceiling for the reasoning capabilities of current quantized models.

