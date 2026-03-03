---
layout: default
title: Learning from Synthetic Data Improves Multi-hop Reasoning
---

# Learning from Synthetic Data Improves Multi-hop Reasoning
**arXiv**：[2603.02091v1](https://arxiv.org/abs/2603.02091) · [PDF](https://arxiv.org/pdf/2603.02091.pdf)  
**作者**：Anmol Kabra, Yilun Yin, Albert Gong, Kamilė Stankevičiūtė, Dongyoung Go, Johann Lee, Katie Z. Luo, Carla P. Gomes, Kilian Q. Weinberger  

**一句话要点**：提出基于规则生成合成数据进行强化学习微调，以提升大语言模型的多跳推理能力

**关键词**：多跳推理, 强化学习微调, 合成数据生成, 大语言模型, 知识组合, 问答基准测试

## 3 点简述
- 核心问题：强化学习微调依赖高质量可验证数据，但现有数据源（人工标注、大模型生成、大模型验证器）存在成本高、幻觉多、不准确等限制
- 方法要点：使用规则生成的合成数据进行强化学习微调，合成数据仅包含虚构知识，但能训练模型组合知识
- 实验或效果：在真实世界问答基准测试中，微调后模型性能显著提升，尤其在困难问题上，表明合成数据能教授可泛化的推理技能

## 摘要（原文）

> Reinforcement Learning (RL) has been shown to significantly boost reasoning capabilities of large language models (LLMs) in math, coding, and multi-hop reasoning tasks. However, RL fine-tuning requires abundant high-quality verifiable data, often sourced from human annotations, generated from frontier LLMs, or scored by LLM-based verifiers. All three have considerable limitations: human-annotated datasets are small and expensive to curate, LLM-generated data is hallucination-prone and costly, and LLM-based verifiers are inaccurate and slow. In this work, we investigate a cheaper alternative: RL fine-tuning on rule-generated synthetic data for multi-hop reasoning tasks. We discover that LLMs fine-tuned on synthetic data perform significantly better on popular real-world question-answering benchmarks, despite the synthetic data containing only fictional knowledge. On stratifying performance by question difficulty, we find that synthetic data teaches LLMs to compose knowledge -- a fundamental and generalizable reasoning skill. Our work highlights rule-generated synthetic reasoning data as a free and scalable resource to improve LLM reasoning capabilities.

