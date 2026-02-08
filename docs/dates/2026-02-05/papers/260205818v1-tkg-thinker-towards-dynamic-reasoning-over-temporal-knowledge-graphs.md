---
layout: default
title: TKG-Thinker: Towards Dynamic Reasoning over Temporal Knowledge Graphs via Agentic Reinforcement Learning
---

# TKG-Thinker: Towards Dynamic Reasoning over Temporal Knowledge Graphs via Agentic Reinforcement Learning
**arXiv**：[2602.05818v1](https://arxiv.org/abs/2602.05818) · [PDF](https://arxiv.org/pdf/2602.05818.pdf)  
**作者**：Zihao Jiang, Miao Peng, Zhenyan Shan, Wenjie Xu, Ben Liu, Gong Chen, Ziqi Gao, Min Peng  

**一句话要点**：提出TKG-Thinker，通过智能体强化学习解决时序知识图谱问答中的推理幻觉与泛化限制。

**关键词**：时序知识图谱问答, 智能体强化学习, 动态推理, 监督微调, 多轮交互, 泛化能力

## 3 点简述
- 核心问题：现有提示策略在复杂时序约束下易产生推理幻觉，且静态提示限制模型自主性与泛化能力。
- 方法要点：采用监督微调与强化学习双阶段训练，结合自主规划和自适应检索，实现动态多轮交互推理。
- 实验或效果：在基准数据集上达到最先进性能，并在复杂TKGQA设置中展现出强泛化能力。

## 摘要（原文）

> Temporal knowledge graph question answering (TKGQA) aims to answer time-sensitive questions by leveraging temporal knowledge bases. While Large Language Models (LLMs) demonstrate significant potential in TKGQA, current prompting strategies constrain their efficacy in two primary ways. First, they are prone to reasoning hallucinations under complex temporal constraints. Second, static prompting limits model autonomy and generalization, as it lack optimization through dynamic interaction with temporal knowledge graphs (TKGs) environments. To address these limitations, we propose \textbf{TKG-Thinker}, a novel agent equipped with autonomous planning and adaptive retrieval capabilities for reasoning over TKGs. Specifically, TKG-Thinker performs in-depth temporal reasoning through dynamic multi-turn interactions with TKGs via a dual-training strategy. We first apply Supervised Fine-Tuning (SFT) with chain-of thought data to instill core planning capabilities, followed by a Reinforcement Learning (RL) stage that leverages multi-dimensional rewards to refine reasoning policies under intricate temporal constraints. Experimental results on benchmark datasets with three open-source LLMs show that TKG-Thinker achieves state-of-the-art performance and exhibits strong generalization across complex TKGQA settings.

