---
layout: default
title: From Reactive to Map-Based AI: Tuned Local LLMs for Semantic Zone Inference in Object-Goal Navigation
---

# From Reactive to Map-Based AI: Tuned Local LLMs for Semantic Zone Inference in Object-Goal Navigation
**arXiv**：[2603.08086v1](https://arxiv.org/abs/2603.08086) · [PDF](https://arxiv.org/pdf/2603.08086.pdf)  
**作者**：Yudai Noda, Kanji Tanaka  

**一句话要点**：提出基于地图的AI框架，通过微调LLM进行语义区域推断以提升物体目标导航性能

**关键词**：物体目标导航, 语义区域推断, 大型语言模型微调, 拓扑地图, 旅行商问题优化, AI2-THOR模拟器

## 3 点简述
- 核心问题：传统基于LLM的物体目标导航代理缺乏显式空间记忆，导致探索冗余和短视行为。
- 方法要点：结合微调Llama-2模型与混合拓扑-网格地图系统，推断语义区域类别和目标存在概率。
- 实验或效果：在AI2-THOR模拟器中评估，显著优于前沿探索和反应式LLM基线，提升成功率和路径效率。

## 摘要（原文）

> Object-Goal Navigation (ObjectNav) requires an agent to find and navigate to a target object category in unknown environments. While recent Large Language Model (LLM)-based agents exhibit zero-shot reasoning, they often rely on a "reactive" paradigm that lacks explicit spatial memory, leading to redundant exploration and myopic behaviors. To address these limitations, we propose a transition from reactive AI to "Map-Based AI" by integrating LLM-based semantic inference with a hybrid topological-grid mapping system. Our framework employs a fine-tuned Llama-2 model via Low-Rank Adaptation (LoRA) to infer semantic zone categories and target existence probabilities from verbalized object observations. In this study, a "zone" is defined as a functional area described by the set of observed objects, providing crucial semantic co-occurrence cues for finding the target. This semantic information is integrated into a topological graph, enabling the agent to prioritize high-probability areas and perform systematic exploration via Traveling Salesman Problem (TSP) optimization. Evaluations in the AI2-THOR simulator demonstrate that our approach significantly outperforms traditional frontier exploration and reactive LLM baselines, achieving a superior Success Rate (SR) and Success weighted by Path Length (SPL).

