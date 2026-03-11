---
layout: default
title: MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data
---

# MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data
**arXiv**：[2603.09206v1](https://arxiv.org/abs/2603.09206) · [PDF](https://arxiv.org/pdf/2603.09206.pdf)  
**作者**：Zongxia Li, Hongyang Du, Chengsong Huang, Xiyang Wu, Lantao Yu, Yicheng He, Jing Xie, Xiaomin Wu, Zhichao Liu, Jiarui Zhang, Fuxiao Liu  

**一句话要点**：提出MM-Zero框架，实现零数据自演化的多模态视觉语言模型推理

**关键词**：视觉语言模型, 自演化, 零数据学习, 强化学习, 多模态推理, GRPO优化

## 3 点简述
- 核心问题：视觉语言模型自演化通常需要种子数据，难以从零数据启动
- 方法要点：引入多角色自演化框架，包括提议者、编码器和求解器，使用GRPO训练
- 实验或效果：在多种多模态基准测试中提升推理性能，扩展自演化范式

## 摘要（原文）

> Self-evolving has emerged as a key paradigm for improving foundational models such as Large Language Models (LLMs) and Vision Language Models (VLMs) with minimal human intervention. While recent approaches have demonstrated that LLM agents can self-evolve from scratch with little to no data, VLMs introduce an additional visual modality that typically requires at least some seed data, such as images, to bootstrap the self-evolution process. In this work, we present Multi-model Multimodal Zero (MM-Zero), the first RL-based framework to achieve zero-data self-evolution for VLM reasoning. Moving beyond prior dual-role (Proposer and Solver) setups, MM-Zero introduces a multi-role self-evolving training framework comprising three specialized roles: a Proposer that generates abstract visual concepts and formulates questions; a Coder that translates these concepts into executable code (e.g., Python, SVG) to render visual images; and a Solver that performs multimodal reasoning over the generated visual content. All three roles are initialized from the same base model and trained using Group Relative Policy Optimization (GRPO), with carefully designed reward mechanisms that integrate execution feedback, visual verification, and difficulty balancing. Our experiments show that MM-Zero improves VLM reasoning performance across a wide range of multimodal benchmarks. MM-Zero establishes a scalable path toward self-evolving multi-model systems for multimodal models, extending the frontier of self-improvement beyond the conventional two-model paradigm.

