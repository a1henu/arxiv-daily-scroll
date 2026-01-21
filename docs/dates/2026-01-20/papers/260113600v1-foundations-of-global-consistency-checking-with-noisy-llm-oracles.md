---
layout: default
title: Foundations of Global Consistency Checking with Noisy LLM Oracles
---

# Foundations of Global Consistency Checking with Noisy LLM Oracles
**arXiv**：[2601.13600v1](https://arxiv.org/abs/2601.13600) · [PDF](https://arxiv.org/pdf/2601.13600.pdf)  
**作者**：Paul He, Elke Kirschbaum, Shiva Kasiviswanathan  

**一句话要点**：提出自适应分治算法以解决基于噪声LLM的全局一致性验证问题

**关键词**：全局一致性验证, 噪声LLM预言机, 自适应分治算法, 最小不一致子集, 命中集修复, 语言一致性框架

## 3 点简述
- 核心问题：验证自然语言事实集合的全局一致性，但LLM判断有噪声且成对检查不足。
- 方法要点：设计自适应分治算法，识别最小不一致子集，可选通过命中集计算最小修复。
- 实验或效果：在合成和真实LLM上实验，方法高效检测和定位不一致，提供可扩展框架。

## 摘要（原文）

> Ensuring that collections of natural-language facts are globally consistent is essential for tasks such as fact-checking, summarization, and knowledge base construction. While Large Language Models (LLMs) can assess the consistency of small subsets of facts, their judgments are noisy, and pairwise checks are insufficient to guarantee global coherence. We formalize this problem and show that verifying global consistency requires exponentially many oracle queries in the worst case. To make the task practical, we propose an adaptive divide-and-conquer algorithm that identifies minimal inconsistent subsets (MUSes) of facts and optionally computes minimal repairs through hitting-sets. Our approach has low-degree polynomial query complexity. Experiments with both synthetic and real LLM oracles show that our method efficiently detects and localizes inconsistencies, offering a scalable framework for linguistic consistency verification with LLM-based evaluators.

