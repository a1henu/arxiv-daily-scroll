---
layout: default
title: Decoding as Optimisation on the Probability Simplex: From Top-K to Top-P (Nucleus) to Best-of-K Samplers
---

# Decoding as Optimisation on the Probability Simplex: From Top-K to Top-P (Nucleus) to Best-of-K Samplers
**arXiv**：[2602.18292v1](https://arxiv.org/abs/2602.18292) · [PDF](https://arxiv.org/pdf/2602.18292.pdf)  
**作者**：Xiaotong Ji, Rasul Tutunov, Matthieu Zimmer, Haitham Bou-Ammar  

**一句话要点**：提出解码作为概率单纯形上的优化框架，统一现有采样方法并设计Best-of-K以提升多样本性能。

**关键词**：解码优化, 概率单纯形, 采样方法, Best-of-K, 语言模型, 多样本管道

## 3 点简述
- 解码被视为启发式调参，本文将其形式化为概率单纯形上的正则化优化问题。
- 框架统一贪婪解码、Softmax采样、Top-K、Top-P等，通过最优性条件解释其共性。
- 设计Best-of-K解码器，基于KL锚定覆盖目标，在固定K样本预算下提升模型准确率，如Qwen2.5-Math-7B在MATH500上提升18.6%。

## 摘要（原文）

> Decoding sits between a language model and everything we do with it, yet it is still treated as a heuristic knob-tuning exercise. We argue decoding should be understood as a principled optimisation layer: at each token, we solve a regularised problem over the probability simplex that trades off model score against structural preferences and constraints. This single template recovers greedy decoding, Softmax sampling, Top-K, Top-P, and Sparsemax-style sparsity as special cases, and explains their common structure through optimality conditions. More importantly, the framework makes it easy to invent new decoders without folklore. We demonstrate this by designing Best-of-K (BoK), a KL-anchored coverage objective aimed at multi-sample pipelines (self-consistency, reranking, verifier selection). BoK targets the probability of covering good alternatives within a fixed K-sample budget and improves empirical performance. We show that such samples can improve accuracy by, for example, +18.6% for Qwen2.5-Math-7B on MATH500 at high sampling temperatures.

