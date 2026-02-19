---
layout: default
title: Synthesis and Verification of Transformer Programs
---

# Synthesis and Verification of Transformer Programs
**arXiv**：[2602.16473v1](https://arxiv.org/abs/2602.16473) · [PDF](https://arxiv.org/pdf/2602.16473.pdf)  
**作者**：Hongjian Jiang, Matthew Hague, Philipp Rümmer, Anthony Widjaja Lin  

**一句话要点**：提出C-RASP程序验证与学习方法，应用于Transformer程序优化和约束学习。

**关键词**：程序验证, Transformer程序, 模型检查, 局部搜索学习, C-RASP语言, SMT求解器

## 3 点简述
- 核心问题：自动验证和学习C-RASP程序，以捕获Transformer表达的概念。
- 方法要点：利用Lustre同步数据流程序验证技术，结合SMT求解器进行模型检查；开发基于局部搜索的算法从示例中学习C-RASP。
- 实验或效果：在文献基准测试中验证了方法的有效性，支持Transformer程序优化和基于部分规范的约束学习。

## 摘要（原文）

> C-RASP is a simple programming language that was recently shown to capture concepts expressible by transformers. In this paper, we develop new algorithmic techniques for automatically verifying C-RASPs. To this end, we establish a connection to the verification of synchronous dataflow programs in Lustre, which enables us to exploit state-of-the-art model checkers utilizing highly optimized SMT-solvers. Our second contribution addresses learning a C-RASP program in the first place. To this end, we provide a new algorithm for learning a C-RASP from examples using local search. We demonstrate efficacy of our implementation for benchmarks of C-RASPs in the literature, in particular in connection to the following applications: (1) transformer program optimization, and (2) constrained learning of transformer programs (based on a partial specification).

