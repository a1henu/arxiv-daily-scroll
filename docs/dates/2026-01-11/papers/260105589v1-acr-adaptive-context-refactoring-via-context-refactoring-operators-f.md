---
layout: default
title: ACR: Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue
---

# ACR: Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue
**arXiv**：[2601.05589v1](https://arxiv.org/abs/2601.05589) · [PDF](https://arxiv.org/pdf/2601.05589.pdf)  
**作者**：Jiawei Shen, Jia Zhu, Hanghui Guo, Weijie Shi, Yue Cui, Qingyu Niu, Guoqing Ma, Yidan Liang, Jingjiang Liu, Yiling Wang, Shimin Di, Jiajie Xu  

**一句话要点**：提出自适应上下文重构框架以解决多轮对话中的上下文惯性与状态漂移问题

**关键词**：多轮对话, 上下文重构, 自适应框架, 教师引导训练, 状态漂移缓解

## 3 点简述
- 核心问题：多轮对话中模型易出现上下文惯性与状态漂移，现有方法如扩展上下文窗口或压缩上下文存在局限
- 方法要点：基于上下文重构算子库和教师引导自进化训练，动态监控并重塑交互历史，解耦上下文管理与推理过程
- 实验或效果：在多轮对话任务上显著超越基线方法，同时减少令牌消耗

## 摘要（原文）

> Large Language Models (LLMs) have shown remarkable performance in multi-turn dialogue. However, in multi-turn dialogue, models still struggle to stay aligned with what has been established earlier, follow dependencies across many turns, and avoid drifting into incorrect facts as the interaction grows longer. Existing approaches primarily focus on extending the context window, introducing external memory, or applying context compression, yet these methods still face limitations such as \textbf{contextual inertia} and \textbf{state drift}. To address these challenges, we propose the \textbf{A}daptive \textbf{C}ontext \textbf{R}efactoring \textbf{(ACR)} Framework, which dynamically monitors and reshapes the interaction history to mitigate contextual inertia and state drift actively. ACR is built on a library of context refactoring operators and a teacher-guided self-evolving training paradigm that learns when to intervene and how to refactor, thereby decoupling context management from the reasoning process. Extensive experiments on multi-turn dialogue demonstrate that our method significantly outperforms existing baselines while reducing token consumption.

