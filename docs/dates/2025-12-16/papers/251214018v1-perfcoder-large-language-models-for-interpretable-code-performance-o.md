---
layout: default
title: PerfCoder: Large Language Models for Interpretable Code Performance Optimization
---

# PerfCoder: Large Language Models for Interpretable Code Performance Optimization
**arXiv**：[2512.14018v1](https://arxiv.org/abs/2512.14018) · [PDF](https://arxiv.org/pdf/2512.14018.pdf)  
**作者**：Jiuding Yang, Shengyao Lu, Hongxuan Liu, Shayan Shirahmad Gale Bagi, Zahra Fazel, Tomasz Czajkowski, Di Niu  

**一句话要点**：提出PerfCoder以通过可解释优化提升代码性能

**关键词**：代码性能优化, 大语言模型微调, 可解释优化, 强化学习对齐, 代码生成

## 3 点简述
- 核心问题：大语言模型生成高性能代码能力有限，缺乏可解释性能优化监督
- 方法要点：基于真实优化轨迹微调，结合运行时测量进行偏好对齐，实现输入特定优化
- 实验或效果：在PIE基准上超越现有模型，提升32B模型和GPT-5的代码优化性能

## 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance.

