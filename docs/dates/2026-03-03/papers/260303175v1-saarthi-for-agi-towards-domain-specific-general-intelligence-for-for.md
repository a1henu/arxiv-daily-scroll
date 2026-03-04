---
layout: default
title: Saarthi for AGI: Towards Domain-Specific General Intelligence for Formal Verification
---

# Saarthi for AGI: Towards Domain-Specific General Intelligence for Formal Verification
**arXiv**：[2603.03175v1](https://arxiv.org/abs/2603.03175) · [PDF](https://arxiv.org/pdf/2603.03175.pdf)  
**作者**：Aman Kumar, Deepak Narayan Gadde, Luu Danh Minh, Vaisakh Naduvodi Viswambharan, Keerthan Kopparam Radhakrishna, Sivaram Pothireddypalli  

**一句话要点**：提出结构化规则书与RAG增强，提升Saarthi框架在形式验证中的断言生成准确性与迭代效率。

**关键词**：形式验证, 多智能体协作, 检索增强生成, 结构化规则书, 断言生成

## 3 点简述
- 核心问题：LLM代理在形式验证中易产生幻觉和错误，需提高准确性与可控性。
- 方法要点：引入结构化规则书和GraphRAG技术，优化SVA生成与知识检索。
- 实验或效果：在NVIDIA CVDP基准测试中，断言准确率提升70%，覆盖闭合迭代次数减少50%。

## 摘要（原文）

> Saarthi is an agentic AI framework that uses multi-agent collaboration to perform end-to-end formal verification. Even though the framework provides a complete flow from specification to coverage closure, with around 40% efficacy, there are several challenges that need to be addressed to make it more robust and reliable. Artificial General Intelligence (AGI) is still a distant goal, and current Large Language Model (LLM)-based agents are prone to hallucinations and making mistakes, especially when dealing with complex tasks such as formal verification. However, with the right enhancements and improvements, we believe that Saarthi can be a significant step towards achieving domain-specific general intelligence for formal verification. Especially for problems that require Short Term, Short Context (STSC) capabilities, such as formal verification, Saarthi can be a powerful tool to assist verification engineers in their work. In this paper, we present two key enhancements to the Saarthi framework: (1) a structured rulebook and specification grammar to improve the accuracy and controllability of SystemVerilog Assertion (SVA) generation, and (2) integration of advanced Retrieval Augmented Generation (RAG) techniques, such as GraphRAG, to provide agents with access to technical knowledge and best practices for iterative refinement and improvement of outputs. We also benchmark these enhancements for the overall Saarthi framework using challenging test cases from NVIDIA's CVDP benchmark targeting formal verification. Our benchmark results stand out with a 70% improvement in the accuracy of generated assertions, and a 50% reduction in the number of iterations required to achieve coverage closure.

