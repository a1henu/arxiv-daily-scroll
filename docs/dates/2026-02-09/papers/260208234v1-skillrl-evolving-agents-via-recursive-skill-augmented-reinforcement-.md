---
layout: default
title: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning
---

# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning
**arXiv**：[2602.08234v1](https://arxiv.org/abs/2602.08234) · [PDF](https://arxiv.org/pdf/2602.08234.pdf)  
**作者**：Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, Zeyu Zheng, Cihang Xie, Huaxiu Yao  

**一句话要点**：提出SkillRL框架，通过自动技能发现与递归进化提升LLM智能体在复杂任务中的泛化能力。

**关键词**：强化学习, 技能发现, 递归进化, 经验蒸馏, 智能体泛化, 分层技能库

## 3 点简述
- 核心问题：LLM智能体缺乏从原始经验中提取高级可复用行为模式的能力，导致泛化受限。
- 方法要点：引入基于经验的蒸馏机制构建分层技能库，结合自适应检索与递归进化机制优化策略。
- 实验或效果：在ALFWorld等任务中实现SOTA性能，提升超过15.3%，并保持任务复杂度增加时的鲁棒性。

## 摘要（原文）

> Large Language Model (LLM) agents have shown stunning results in complex tasks, yet they often operate in isolation, failing to learn from past experiences. Existing memory-based methods primarily store raw trajectories, which are often redundant and noise-heavy. This prevents agents from extracting high-level, reusable behavioral patterns that are essential for generalization. In this paper, we propose SkillRL, a framework that bridges the gap between raw experience and policy improvement through automatic skill discovery and recursive evolution. Our approach introduces an experience-based distillation mechanism to build a hierarchical skill library SkillBank, an adaptive retrieval strategy for general and task-specific heuristics, and a recursive evolution mechanism that allows the skill library to co-evolve with the agent's policy during reinforcement learning. These innovations significantly reduce the token footprint while enhancing reasoning utility. Experimental results on ALFWorld, WebShop and seven search-augmented tasks demonstrate that SkillRL achieves state-of-the-art performance, outperforming strong baselines over 15.3% and maintaining robustness as task complexity increases. Code is available at this https://github.com/aiming-lab/SkillRL.

