---
layout: default
title: DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing
---

# DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing
**arXiv**：[2601.09609v1](https://arxiv.org/abs/2601.09609) · [PDF](https://arxiv.org/pdf/2601.09609.pdf)  
**作者**：Qian Cao, Yahui Liu, Wei Bi, Yi Zhao, Ruihua Song, Xiting Wang, Ruiming Tang, Guorui Zhou, Han Li  

**一句话要点**：提出DPWriter框架，通过多样化规划分支增强大语言模型在创意写作中的输出多样性。

**关键词**：强化学习, 大语言模型, 创意写作, 多样化规划, 思维链, 输出多样性

## 3 点简述
- 核心问题：基于强化学习的大语言模型优化常导致输出多样性降低，影响开放任务如创意写作的实用性。
- 方法要点：采用半结构化长思维链分解生成过程，引入基于多样性变化的规划分支和群体感知多样性奖励。
- 实验或效果：在创意写作基准测试中，显著提升输出多样性而不损害生成质量，优于现有基线方法。

## 摘要（原文）

> Reinforcement learning (RL)-based enhancement of large language models (LLMs) often leads to reduced output diversity, undermining their utility in open-ended tasks like creative writing. Current methods lack explicit mechanisms for guiding diverse exploration and instead prioritize optimization efficiency and performance over diversity. This paper proposes an RL framework structured around a semi-structured long Chain-of-Thought (CoT), in which the generation process is decomposed into explicitly planned intermediate steps. We introduce a Diverse Planning Branching method that strategically introduces divergence at the planning phase based on diversity variation, alongside a group-aware diversity reward to encourage distinct trajectories. Experimental results on creative writing benchmarks demonstrate that our approach significantly improves output diversity without compromising generation quality, consistently outperforming existing baselines.

