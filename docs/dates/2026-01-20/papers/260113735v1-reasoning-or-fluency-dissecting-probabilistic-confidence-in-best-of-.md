---
layout: default
title: Reasoning or Fluency? Dissecting Probabilistic Confidence in Best-of-N Selection
---

# Reasoning or Fluency? Dissecting Probabilistic Confidence in Best-of-N Selection
**arXiv**：[2601.13735v1](https://arxiv.org/abs/2601.13735) · [PDF](https://arxiv.org/pdf/2601.13735.pdf)  
**作者**：Hojin Kim, Jaehyung Kim  

**一句话要点**：提出对比因果度量以改进最佳N选择，揭示概率置信度主要捕捉表面流畅性而非推理逻辑

**关键词**：最佳N选择, 概率置信度, 因果依赖, 推理质量评估, 语言模型评估

## 3 点简述
- 核心问题：概率置信度作为推理质量代理的假设可能不成立，因其可能无法捕捉步骤间因果依赖
- 方法要点：引入三类步骤间因果扰动，并设计对比因果度量来显式隔离因果依赖
- 实验或效果：扰动下选择准确率仅轻微下降，新度量比基于概率的方法产生更忠实输出选择

## 摘要（原文）

> Probabilistic confidence metrics are increasingly adopted as proxies for reasoning quality in Best-of-N selection, under the assumption that higher confidence reflects higher reasoning fidelity. In this work, we challenge this assumption by investigating whether these metrics truly capture inter-step causal dependencies necessary for valid reasoning. We introduce three classes of inter-step causality perturbations that systematically disrupt dependencies between reasoning steps while preserving local fluency. Surprisingly, across diverse model families and reasoning benchmarks, we find that selection accuracy degrades only marginally under these disruptions. Even severe interventions, such as applying hard attention masks that directly prevent the model from attending to prior reasoning steps, do not substantially reduce selection performance. These findings provide strong evidence that current probabilistic metrics are largely insensitive to logical structure, and primarily capture surface-level fluency or in-distribution priors instead. Motivated by this gap, we propose a contrastive causality metric that explicitly isolates inter-step causal dependencies, and demonstrate that it yields more faithful output selection than existing probability-based approaches.

