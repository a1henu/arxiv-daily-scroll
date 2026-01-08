---
layout: default
title: Defeasible Conditionals using Answer Set Programming
---

# Defeasible Conditionals using Answer Set Programming
**arXiv**：[2601.03840v1](https://arxiv.org/abs/2601.03840) · [PDF](https://arxiv.org/pdf/2601.03840.pdf)  
**作者**：Racquel Dennison, Jesse Heyninck, Thomas Meyer  

**一句话要点**：提出基于答案集编程的可废止条件句计算方法，用于自动构建最小排序模型和检查蕴涵。

**关键词**：可废止推理, 答案集编程, Rational Closure, KLM框架, 蕴涵检查

## 3 点简述
- 核心问题：可废止蕴涵在信息不完整时进行合理推理，KLM框架是基础模型，Rational Closure是主要算法。
- 方法要点：使用答案集编程提供Rational Closure的声明式定义，支持从知识库自动构建最小排序模型。
- 实验或效果：形式化证明ASP编码正确性，与InfOCF求解器比较，显示计算效率提升。

## 摘要（原文）

> Defeasible entailment is concerned with drawing plausible conclusions from incomplete information. A foundational framework for modelling defeasible entailment is the KLM framework. Introduced by Kraus, Lehmann, and Magidor, the KLM framework outlines several key properties for defeasible entailment. One of the most prominent algorithms within this framework is Rational Closure (RC). This paper presents a declarative definition for computing RC using Answer Set Programming (ASP). Our approach enables the automatic construction of the minimal ranked model from a given knowledge base and supports entailment checking for specified queries. We formally prove the correctness of our ASP encoding and conduct empirical evaluations to compare the performance of our implementation with that of existing imperative implementations, specifically the InfOCF solver. The results demonstrate that our ASP-based approach adheres to RC's theoretical foundations and offers improved computational efficiency.

