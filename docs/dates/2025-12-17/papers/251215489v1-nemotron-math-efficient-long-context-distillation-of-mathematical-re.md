---
layout: default
title: Nemotron-Math: Efficient Long-Context Distillation of Mathematical Reasoning from Multi-Mode Supervision
---

# Nemotron-Math: Efficient Long-Context Distillation of Mathematical Reasoning from Multi-Mode Supervision
**arXiv**：[2512.15489v1](https://arxiv.org/abs/2512.15489) · [PDF](https://arxiv.org/pdf/2512.15489.pdf)  
**作者**：Wei Du, Shubham Toshniwal, Branislav Kisacanin, Sadegh Mahdavi, Ivan Moshkov, George Armstrong, Stephen Ge, Edgar Minasyan, Feng Chen, Igor Gitman  

**一句话要点**：提出Nemotron-Math数据集以高效蒸馏长上下文数学推理，结合多模式监督与工具集成。

**关键词**：数学推理数据集, 长上下文蒸馏, 多模式监督, 工具集成推理, 序列分桶策略

## 3 点简述
- 核心问题：现有数学推理数据集在推理风格多样性和工具集成方面有限，影响模型性能。
- 方法要点：利用gpt-oss-120b生成多模式解决方案，整合AoPS和StackExchange-Math问题，开发序列分桶策略加速长上下文训练。
- 实验或效果：在AoPS问题上超越OpenMathReasoning，提升泛化能力，在AIME基准上实现100%准确率。

## 摘要（原文）

> High-quality mathematical reasoning supervision requires diverse reasoning styles, long-form traces, and effective tool integration, capabilities that existing datasets provide only in limited form. Leveraging the multi-mode generation ability of gpt-oss-120b, we introduce Nemotron-Math, a large-scale mathematical reasoning dataset containing 7.5M solution traces across high, medium, and low reasoning modes, each available both with and without Python tool-integrated reasoning (TIR).
>   The dataset integrates 85K curated AoPS problems with 262K community-sourced StackExchange-Math problems, combining structured competition tasks with diverse real-world mathematical queries. We conduct controlled evaluations to assess the dataset quality.
>   Nemotron-Math consistently outperforms the original OpenMathReasoning on matched AoPS problems. Incorporating StackExchange-Math substantially improves robustness and generalization, especially on HLE-Math, while preserving accuracy on math competition benchmarks.
>   To support efficient long-context training, we develop a sequential bucketed strategy that accelerates 128K context-length fine-tuning by 2--3$\times$ without significant accuracy loss. Overall, Nemotron-Math enables state-of-the-art performance, including 100\% maj@16 accuracy on AIME 2024 and 2025 with Python TIR.

