---
layout: default
title: WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents
---

# WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents
**arXiv**：[2603.05044v1](https://arxiv.org/abs/2603.05044) · [PDF](https://arxiv.org/pdf/2603.05044.pdf)  
**作者**：Sicheng Fan, Qingyun Shi, Shengze Xu, Shengbo Cai, Tieyong Zeng, Li Ling, Yanyi Shang, Dehan Kong  

**一句话要点**：提出WebFactory自动化压缩大语言模型知识为GUI智能体，解决数据依赖与效率问题。

**关键词**：GUI智能体, 知识压缩, 强化学习, 自动化训练, 大语言模型, 泛化性能

## 3 点简述
- 核心问题：当前GUI智能体训练依赖不安全实时交互或昂贵人工数据，忽视知识压缩效率。
- 方法要点：引入全自动闭环强化学习流程，包括环境合成、任务生成、轨迹收集、分解奖励训练和系统评估。
- 实验或效果：在仅10个网站合成数据上训练，性能媲美更多环境人工数据训练的智能体，泛化能力强。

## 摘要（原文）

> Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

