---
layout: default
title: HOMURA: Taming the Sand-Glass for Time-Constrained LLM Translation via Reinforcement Learning
---

# HOMURA: Taming the Sand-Glass for Time-Constrained LLM Translation via Reinforcement Learning
**arXiv**：[2601.10187v1](https://arxiv.org/abs/2601.10187) · [PDF](https://arxiv.org/pdf/2601.10187.pdf)  
**作者**：Ziang Cui, Mengran Yu, Tianjiao Li, Chenyu Shi, Yingxuan Shi, Lusheng Zhang, Hongwei Lin  

**一句话要点**：提出HOMURA强化学习框架以解决时间约束下LLM翻译的跨语言冗长偏差问题

**关键词**：时间约束翻译, 强化学习, 跨语言冗长偏差, 音节级时长控制, 语义保持

## 3 点简述
- 核心问题：LLM翻译存在跨语言冗长偏差，不适用于字幕配音等严格时间约束任务
- 方法要点：通过KL正则化目标和动态音节比奖励，优化语义保持与时间合规的权衡
- 实验或效果：在Sand-Glass基准上显著优于基线，实现精确长度控制且不损害语义

## 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable strides in multilingual translation but are hindered by a systemic cross-lingual verbosity bias, rendering them unsuitable for strict time-constrained tasks like subtitling and dubbing. Current prompt-engineering approaches struggle to resolve this conflict between semantic fidelity and rigid temporal feasibility. To bridge this gap, we first introduce Sand-Glass, a benchmark specifically designed to evaluate translation under syllable-level duration constraints. Furthermore, we propose HOMURA, a reinforcement learning framework that explicitly optimizes the trade-off between semantic preservation and temporal compliance. By employing a KL-regularized objective with a novel dynamic syllable-ratio reward, HOMURA effectively "tames" the output length. Experimental results demonstrate that our method significantly outperforms strong LLM baselines, achieving precise length control that respects linguistic density hierarchies without compromising semantic adequacy.

