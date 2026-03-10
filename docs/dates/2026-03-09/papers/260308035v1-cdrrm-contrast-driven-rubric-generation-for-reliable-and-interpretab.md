---
layout: default
title: CDRRM: Contrast-Driven Rubric Generation for Reliable and Interpretable Reward Modeling
---

# CDRRM: Contrast-Driven Rubric Generation for Reliable and Interpretable Reward Modeling
**arXiv**：[2603.08035v1](https://arxiv.org/abs/2603.08035) · [PDF](https://arxiv.org/pdf/2603.08035.pdf)  
**作者**：Dengcan Liu, Fengkai Yang, Xiaohan Wang, Shurui Yan, Jiajun Chai, Jiahao Li, Yikun Ban, Zhendong Mao, Wei Lin, Guojun Yin  

**一句话要点**：提出CDRRM框架，通过对比-合成范式生成高质量评分标准，以解决奖励模型可解释性差和依赖专家标注的问题。

**关键词**：奖励建模, 可解释性, 评分标准生成, 对比学习, 数据效率, 大语言模型对齐

## 3 点简述
- 核心问题：传统奖励模型可解释性差、依赖昂贵专家标注，基于评分标准的方法缺乏质量控制，存在噪声和偏见。
- 方法要点：采用对比-合成范式，先通过多维对比分析识别因果判别因素，再合成紧凑、上下文感知的评分标准指导偏好判断。
- 实验或效果：在三个基准测试中实现最优性能，有效缓解评估偏见，仅需3k高质量样本训练即可超越全微调基线，数据效率高。

## 摘要（原文）

> Reward modeling is essential for aligning Large Language Models(LLMs) with human preferences, yet conventional reward models suffer from poor interpretability and heavy reliance on costly expert annotations. While recent rubric-based approaches enhance evaluation transparency, they lack systematic quality control, yielding noisy and redundant criteria, failing to mitigate persistent biases (e.g., verbosity, position) in LLM evaluators, and creating a scalability-reliability trade-off. To address these limitations, we propose CDRRM (Contrast-Driven Rubric Reward Model), a framework built on a novel Contrast-then-Synthesis paradigm for high-quality rubric generation and guided preference judgment. CDRRM first conducts multi-dimensional contrastive profiling on preference pairs to identify causal discriminative factors, then synthesizes these insights into compact, context-aware rubrics to guide preference judg- ments. Extensive experiments on three authoritative benchmarks (RewardBench, RMBench, RMB) demonstrate that CDRRM achieves state-of-the-art performance across diverse domains and effectively mitigates aforementioned evaluation biases. Notably, our approach delivers exceptional data efficiency: training the rubric generator on only 3k high-quality samples empowers a frozen pre-trained judge model to outperform fully fine-tuned baselines. This work offers a scalable, interpretable, and data-efficient path for reward modeling.

