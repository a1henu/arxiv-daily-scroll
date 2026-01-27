---
layout: default
title: Beyond Retention: Orchestrating Structural Safety and Plasticity in Continual Learning for LLMs
---

# Beyond Retention: Orchestrating Structural Safety and Plasticity in Continual Learning for LLMs
**arXiv**：[2601.18255v1](https://arxiv.org/abs/2601.18255) · [PDF](https://arxiv.org/pdf/2601.18255.pdf)  
**作者**：Fei Meng  

**一句话要点**：提出正交子空间唤醒方法以解决大语言模型持续学习中结构安全与可塑性的平衡问题

**关键词**：持续学习, 大语言模型, 经验回放, 正交子空间, 结构安全, 代码生成

## 3 点简述
- 核心问题：经验回放在持续学习中导致代码生成等结构化任务性能下降，牺牲结构完整性
- 方法要点：通过唤醒阶段识别旧任务参数子空间，强制新任务更新正交化以保护知识结构
- 实验或效果：在四任务序列中，OSW成功保留脆弱编码能力，同时保持新任务高可塑性

## 摘要（原文）

> Continual learning in Large Language Models (LLMs) faces the critical challenge of balancing stability (retaining old knowledge) and plasticity (learning new tasks). While Experience Replay (ER) is a standard countermeasure against catastrophic forgetting, its impact across diverse capabilities remains underexplored. In this work, we uncover a critical dichotomy in ER's behavior: while it induces positive backward transfer on robust, unstructured tasks (e.g., boosting performance on previous NLP classification tasks through repeated rehearsal), it causes severe negative transfer on fragile, structured domains like code generation (e.g., a significant relative drop in coding accuracy). This reveals that ER trades structural integrity for broad consolidation. To address this dilemma, we propose \textbf{Orthogonal Subspace Wake-up (OSW)}. OSW identifies essential parameter subspaces of previous tasks via a brief "wake-up" phase and enforces orthogonal updates for new tasks, providing a mathematically grounded "safety guarantee" for established knowledge structures. Empirical results across a diverse four-task sequence demonstrate that OSW uniquely succeeds in preserving fragile coding abilities where Replay fails, while simultaneously maintaining high plasticity for novel tasks. Our findings emphasize the necessity of evaluating structural safety alongside average retention in LLM continual learning.

