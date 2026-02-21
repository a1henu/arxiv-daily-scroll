---
layout: default
title: ALPS: A Diagnostic Challenge Set for Arabic Linguistic & Pragmatic Reasoning
---

# ALPS: A Diagnostic Challenge Set for Arabic Linguistic & Pragmatic Reasoning
**arXiv**：[2602.17054v1](https://arxiv.org/abs/2602.17054) · [PDF](https://arxiv.org/pdf/2602.17054.pdf)  
**作者**：Hussein S. Al-Olimat, Ahmad Alshareef  

**一句话要点**：提出ALPS诊断挑战集以评估阿拉伯语深度语义与语用推理能力

**关键词**：阿拉伯语NLP, 诊断挑战集, 语义推理, 语用推理, 模型评估, 形态句法分析

## 3 点简述
- 核心问题：现有阿拉伯语NLP基准依赖合成或翻译数据，缺乏深度语言验证。
- 方法要点：构建531个专家策划的阿拉伯语原生问题，覆盖15个任务和47个子任务。
- 实验或效果：评估23个模型，揭示模型在形态句法依赖上错误率高，商业模型优于阿拉伯语原生模型。

## 摘要（原文）

> While recent Arabic NLP benchmarks focus on scale, they often rely on synthetic or translated data which may benefit from deeper linguistic verification. We introduce ALPS (Arabic Linguistic & Pragmatic Suite), a native, expert-curated diagnostic challenge set probing Deep Semantics and Pragmatics, capabilities that complement specialized large-scale benchmarks. While broad-coverage benchmarks prioritize scale and multi-task coverage, ALPS targets the depth of linguistic understanding through 531 rigorously crafted questions across 15 tasks and 47 subtasks. We developed the dataset with deep expertise in Arabic linguistics, guaranteeing cultural authenticity and eliminating translation artifacts. Evaluating 23 diverse models (commercial, open-source, and Arabic-native) against a single-pass human performance (avg. 84.6% accuracy) and an expert-adjudicated oracle (99.2%), we reveal a critical dissociation: models achieve high fluency but fail on fundamental morpho-syntactic dependencies, with elevated error rates on morpho-syntactic dependencies (36.5% across diacritics-reliant tasks) compared to compositional semantics. While top commercial models (Gemini-3-flash at 94.2%) surpass the average single human, a substantial gap persists between commercial giants and Arabic-native models, with the best Arabic-specific model (Jais-2-70B at 83.6%) approaching but not matching human performance.

