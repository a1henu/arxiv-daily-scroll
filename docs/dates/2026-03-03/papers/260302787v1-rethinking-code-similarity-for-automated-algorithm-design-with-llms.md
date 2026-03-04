---
layout: default
title: Rethinking Code Similarity for Automated Algorithm Design with LLMs
---

# Rethinking Code Similarity for Automated Algorithm Design with LLMs
**arXiv**：[2603.02787v1](https://arxiv.org/abs/2603.02787) · [PDF](https://arxiv.org/pdf/2603.02787.pdf)  
**作者**：Rui Zhang, Zhichao Lu  

**一句话要点**：提出BehaveSim方法，通过问题解决轨迹衡量算法相似性，以增强LLM自动算法设计

**关键词**：算法相似性度量, 问题解决轨迹, 动态时间规整, LLM自动算法设计, 行为多样性

## 3 点简述
- 核心问题：现有代码相似性度量无法区分算法逻辑，导致LLM-AAD中难以评估算法创新
- 方法要点：基于动态时间规整量化执行过程中的中间解序列（问题解决轨迹）
- 实验或效果：集成BehaveSim提升LLM-AAD性能，并支持算法行为聚类分析

## 摘要（原文）

> The rise of Large Language Model-based Automated Algorithm Design (LLM-AAD) has transformed algorithm development by autonomously generating code implementations of expert-level algorithms. Unlike traditional expert-driven algorithm development, in the LLM-AAD paradigm, the main design principle behind an algorithm is often implicitly embedded in the generated code. Therefore, assessing algorithmic similarity directly from code, distinguishing genuine algorithmic innovation from mere syntactic variation, becomes essential. While various code similarity metrics exist, they fail to capture algorithmic similarity, as they focus on surface-level syntax or output equivalence rather than the underlying algorithmic logic.
>   We propose BehaveSim, a novel method to measure algorithmic similarity through the lens of problem-solving behavior as a sequence of intermediate solutions produced during execution, dubbed as problem-solving trajectories (PSTrajs). By quantifying the alignment between PSTrajs using dynamic time warping (DTW), BehaveSim distinguishes algorithms with divergent logic despite syntactic or output-level similarities. We demonstrate its utility in two key applications: (i) Enhancing LLM-AAD: Integrating BehaveSim into existing LLM-AAD frameworks (e.g., FunSearch, EoH) promotes behavioral diversity, significantly improving performance on three AAD tasks. (ii) Algorithm analysis: BehaveSim clusters generated algorithms by behavior, enabling systematic analysis of problem-solving strategies--a crucial tool for the growing ecosystem of AI-generated algorithms. Data and code of this work are open-sourced at https://github.com/RayZhhh/behavesim.

