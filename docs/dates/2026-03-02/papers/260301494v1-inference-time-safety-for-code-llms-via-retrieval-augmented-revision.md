---
layout: default
title: Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision
---

# Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision
**arXiv**：[2603.01494v1](https://arxiv.org/abs/2603.01494) · [PDF](https://arxiv.org/pdf/2603.01494.pdf)  
**作者**：Manisha Mukherjee, Vincent J. Hellendoorn  

**一句话要点**：提出基于检索增强修订的推理时安全机制，以提升代码生成大模型的安全性。

**关键词**：代码生成安全, 检索增强生成, 推理时干预, 社区知识利用, 大模型可信部署

## 3 点简述
- 核心问题：代码生成大模型在安全推理上透明度低，对动态漏洞模式脆弱，易生成不安全代码。
- 方法要点：利用检索增强生成，从Stack Overflow知识库检索相关安全讨论，指导大模型在推理时修订代码。
- 实验或效果：在真实和基准数据集上，相比仅提示，该方法提升代码安全性，且静态分析未引入新漏洞。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed for code generation in high-stakes software development, yet their limited transparency in security reasoning and brittleness to evolving vulnerability patterns raise critical trustworthiness concerns. Models trained on static datasets cannot readily adapt to newly discovered vulnerabilities or changing security standards without retraining, leading to the repeated generation of unsafe code.
>   We present a principled approach to trustworthy code generation by design that operates as an inference-time safety mechanism. Our approach employs retrieval-augmented generation to surface relevant security risks in generated code and retrieve related security discussions from a curated Stack Overflow knowledge base, which are then used to guide an LLM during code revision. This design emphasizes three aspects relevant to trustworthiness: (1) interpretability, through transparent safety interventions grounded in expert community explanations; (2) robustness, by allowing adaptation to evolving security practices without model retraining; and (3) safety alignment, through real-time intervention before unsafe code reaches deployment.
>   Across real-world and benchmark datasets, our approach improves the security of LLM-generated code compared to prompting alone, while introducing no new vulnerabilities as measured by static analysis. These results suggest that principled, retrieval-augmented inference-time interventions can serve as a complementary mechanism for improving the safety of LLM-based code generation, and highlight the ongoing value of community knowledge in supporting trustworthy AI deployment.

