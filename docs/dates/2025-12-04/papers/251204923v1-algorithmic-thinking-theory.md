---
layout: default
title: Algorithmic Thinking Theory
---

# Algorithmic Thinking Theory
**arXiv**：[2512.04923v1](https://arxiv.org/abs/2512.04923) · [PDF](https://arxiv.org/pdf/2512.04923.pdf)  
**作者**：MohammadHossein Bateni, Vincent Cohen-Addad, Yuzhou Gu, Silvio Lattanzi, Simon Meierhans, Christopher Mohri  

**一句话要点**：提出理论框架分析大语言模型迭代推理算法，基于实验证据而非架构细节。

**关键词**：大语言模型, 推理算法, 理论框架, 迭代改进, 答案聚合, 概率预言机

## 3 点简述
- 核心问题：如何形式化分析大语言模型迭代改进和答案聚合的推理算法。
- 方法要点：引入基于概率预言机的理论框架，抽象推理计划为算法设计。
- 实验或效果：框架基于实验证据，提供通用视角，适用于当前和未来推理预言机。

## 摘要（原文）

> Large language models (LLMs) have proven to be highly effective for solving complex reasoning tasks. Surprisingly, their capabilities can often be improved by iterating on previously generated solutions. In this context, a reasoning plan for generating and combining a set of solutions can be thought of as an algorithm for reasoning using a probabilistic oracle.
>   We introduce a theoretical framework for analyzing such reasoning algorithms. This framework formalizes the principles underlying popular techniques for iterative improvement and answer aggregation, providing a foundation for designing a new generation of more powerful reasoning methods. Unlike approaches for understanding models that rely on architectural specifics, our model is grounded in experimental evidence. As a result, it offers a general perspective that may extend to a wide range of current and future reasoning oracles.

