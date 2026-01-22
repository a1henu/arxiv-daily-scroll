---
layout: default
title: The Plausibility Trap: Using Probabilistic Engines for Deterministic Tasks
---

# The Plausibility Trap: Using Probabilistic Engines for Deterministic Tasks
**arXiv**：[2601.15130v1](https://arxiv.org/abs/2601.15130) · [PDF](https://arxiv.org/pdf/2601.15130.pdf)  
**作者**：Ivan Carrera, Daniel Maldonado-Ruiz  

**一句话要点**：提出工具选择工程与决策矩阵，以解决在确定性任务中滥用概率引擎导致的资源浪费问题。

**关键词**：合理性陷阱, 工具选择工程, 确定性-概率决策矩阵, 资源效率, 生成式AI滥用, OCR基准测试

## 3 点简述
- 核心问题：定义'合理性陷阱'，即用户为简单确定性任务（如OCR）滥用昂贵概率引擎，造成资源浪费。
- 方法要点：引入工具选择工程和确定性-概率决策矩阵，指导开发者何时使用或避免生成式AI。
- 实验或效果：通过OCR和事实核查的微基准测试，量化约6.5倍延迟惩罚和算法奉承风险。

## 摘要（原文）

> The ubiquity of Large Language Models (LLMs) is driving a paradigm shift where user convenience supersedes computational efficiency. This article defines the "Plausibility Trap": a phenomenon where individuals with access to Artificial Intelligence (AI) models deploy expensive probabilistic engines for simple deterministic tasks-such as Optical Character Recognition (OCR) or basic verification-resulting in significant resource waste. Through micro-benchmarks and case studies on OCR and fact-checking, we quantify the "efficiency tax"-demonstrating a ~6.5x latency penalty-and the risks of algorithmic sycophancy. To counter this, we introduce Tool Selection Engineering and the Deterministic-Probabilistic Decision Matrix, a framework to help developers determine when to use Generative AI and, crucially, when to avoid it. We argue for a curriculum shift, emphasizing that true digital literacy relies not only in knowing how to use Generative AI, but also on knowing when not to use it.

