---
layout: default
title: Multimodal Reinforcement Learning with Agentic Verifier for AI Agents
---

# Multimodal Reinforcement Learning with Agentic Verifier for AI Agents
**arXiv**：[2512.03438v1](https://arxiv.org/abs/2512.03438) · [PDF](https://arxiv.org/pdf/2512.03438.pdf)  
**作者**：Reuben Tan, Baolin Peng, Zhengyuan Yang, Hao Cheng, Oier Mees, Theodore Zhao, Andrea Tupini, Isar Meijier, Qianhui Wu, Yuncong Yang, Lars Liden, Yu Gu, Sheng Zhang, Xiaodong Liu, Lijuan Wang, Marc Pollefeys, Yong Jae Lee, Jianfeng Gao  

**一句话要点**：提出Argos代理奖励系统，以解决多模态强化学习中奖励信号稀疏和噪声问题。

**关键词**：多模态强化学习, 代理奖励系统, 时空定位, 推理过程评估, 奖励黑客减少, 帕累托最优性

## 3 点简述
- 核心问题：多模态强化学习依赖稀疏结果奖励，缺乏细粒度指导，且教师模型奖励可能含噪声。
- 方法要点：Argos从教师模型和规则评分函数池中选择，评估响应准确性、时空定位和推理过程质量。
- 实验或效果：在空间推理、视觉幻觉及机器人任务中实现SOTA，减少奖励黑客行为，理论基于帕累托最优性。

## 摘要（原文）

> Agentic reasoning models trained with multimodal reinforcement learning (MMRL) have become increasingly capable, yet they are almost universally optimized using sparse, outcome-based rewards computed based on the final answers. Richer rewards computed from the reasoning tokens can improve learning significantly by providing more fine-grained guidance. However, it is challenging to compute more informative rewards in MMRL beyond those based on outcomes since different samples may require different scoring functions and teacher models may provide noisy reward signals too. In this paper, we introduce the Argos (Agentic Reward for Grounded & Objective Scoring), a principled reward agent to train multimodal reasoning models for agentic tasks. For each sample, Argos selects from a pool of teacher-model derived and rule-based scoring functions to simultaneously evaluate: (i) final response accuracy, (ii) spatiotemporal localization of referred entities and actions, and (iii) the quality of the reasoning process. We find that by leveraging our agentic verifier across both SFT data curation and RL training, our model achieves state-of-the-art results across multiple agentic tasks such as spatial reasoning, visual hallucination as well as robotics and embodied AI benchmarks. Critically, we demonstrate that just relying on SFT post-training on highly curated reasoning data is insufficient, as agents invariably collapse to ungrounded solutions during RL without our online verification. We also show that our agentic verifier can help to reduce reward-hacking in MMRL. Finally, we also provide a theoretical justification for the effectiveness of Argos through the concept of pareto-optimality.

