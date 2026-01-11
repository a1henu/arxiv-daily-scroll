---
layout: default
title: Adversarial Yet Cooperative: Multi-Perspective Reasoning in Retrieved-Augmented Language Models
---

# Adversarial Yet Cooperative: Multi-Perspective Reasoning in Retrieved-Augmented Language Models
**arXiv**：[2601.04651v1](https://arxiv.org/abs/2601.04651) · [PDF](https://arxiv.org/pdf/2601.04651.pdf)  
**作者**：Can Xu, Lingyong Yan, Jiayi Wu, Haosen Wang, Shuaiqiang Wang, Yuchen Li, Jizhou Huang, Dawei Yin, Xiang Li  

**一句话要点**：提出对抗推理RAG框架，通过多视角推理与过程感知奖励解决检索增强语言模型中的单视角限制和训练信号不足问题。

**关键词**：检索增强生成, 对抗推理, 过程感知奖励, 多视角推理, 语言模型优化

## 3 点简述
- 核心问题：检索增强语言模型存在单视角推理限制和训练过程依赖结果导向奖励信号不足。
- 方法要点：设计Reasoner-Verifier对抗框架，结合过程感知优势奖励，优化推理保真度和验证严谨性。
- 实验或效果：在多个基准测试中验证了方法的有效性，提升推理深度和自校正能力。

## 摘要（原文）

> Recent advances in synergizing large reasoning models (LRMs) with retrieval-augmented generation (RAG) have shown promising results, yet two critical challenges remain: (1) reasoning models typically operate from a single, unchallenged perspective, limiting their ability to conduct deep, self-correcting reasoning over external documents, and (2) existing training paradigms rely excessively on outcome-oriented rewards, which provide insufficient signal for shaping the complex, multi-step reasoning process. To address these issues, we propose an Reasoner-Verifier framework named Adversarial Reasoning RAG (ARR). The Reasoner and Verifier engage in reasoning on retrieved evidence and critiquing each other's logic while being guided by process-aware advantage that requires no external scoring model. This reward combines explicit observational signals with internal model uncertainty to jointly optimize reasoning fidelity and verification rigor. Experiments on multiple benchmarks demonstrate the effectiveness of our method.

