---
layout: default
title: VLM-Guided Experience Replay
---

# VLM-Guided Experience Replay
**arXiv**：[2602.01915v1](https://arxiv.org/abs/2602.01915) · [PDF](https://arxiv.org/pdf/2602.01915.pdf)  
**作者**：Elad Sharony, Tom Jurgenson, Orr Krupnik, Dotan Di Castro, Shie Mannor  

**一句话要点**：提出基于视觉语言模型引导的经验回放优先排序方法，以提升强化学习样本效率与成功率。

**关键词**：强化学习, 经验回放, 视觉语言模型, 样本效率, 优先排序, 机器人控制

## 3 点简述
- 核心问题：强化学习中回放缓冲区的经验优先排序未被探索，影响样本效率与性能。
- 方法要点：使用预训练视觉语言模型自动评估并优先排序经验子轨迹，无需微调。
- 实验或效果：在游戏与机器人场景中，平均成功率提升11-52%，样本效率提高19-45%。

## 摘要（原文）

> Recent advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) have enabled powerful semantic and multimodal reasoning capabilities, creating new opportunities to enhance sample efficiency, high-level planning, and interpretability in reinforcement learning (RL). While prior work has integrated LLMs and VLMs into various components of RL, the replay buffer, a core component for storing and reusing experiences, remains unexplored. We propose addressing this gap by leveraging VLMs to guide the prioritization of experiences in the replay buffer. Our key idea is to use a frozen, pre-trained VLM (requiring no fine-tuning) as an automated evaluator to identify and prioritize promising sub-trajectories from the agent's experiences. Across scenarios, including game-playing and robotics, spanning both discrete and continuous domains, agents trained with our proposed prioritization method achieve 11-52% higher average success rates and improve sample efficiency by 19-45% compared to previous approaches. https://esharony.me/projects/vlm-rb/

