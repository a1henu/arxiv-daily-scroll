---
layout: default
title: MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation
---

# MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation
**arXiv**：[2603.03680v1](https://arxiv.org/abs/2603.03680) · [PDF](https://arxiv.org/pdf/2603.03680.pdf)  
**作者**：Lu Yang, Zelai Xu, Minyang Xie, Jiaxuan Gao, Zhao Shok, Yu Wang, Yi Wu  

**一句话要点**：提出MAGE元强化学习框架，赋能大语言模型智能体在非平稳多智能体环境中进行战略探索与利用

**关键词**：元强化学习, 大语言模型智能体, 战略探索与利用, 多智能体环境, 群体训练, 优势归一化

## 3 点简述
- 核心问题：现有元强化学习方法主要关注单智能体探索，缺乏多智能体环境所需的战略利用能力
- 方法要点：通过多回合训练整合交互历史与反思，结合群体训练与优势归一化技术
- 实验效果：在探索与利用任务中超越基线，对未见对手展现出强泛化能力

## 摘要（原文）

> Large Language Model (LLM) agents have demonstrated remarkable proficiency in learned tasks, yet they often struggle to adapt to non-stationary environments with feedback. While In-Context Learning and external memory offer some flexibility, they fail to internalize the adaptive ability required for long-term improvement. Meta-Reinforcement Learning (meta-RL) provides an alternative by embedding the learning process directly within the model. However, existing meta-RL approaches for LLMs focus primarily on exploration in single-agent settings, neglecting the strategic exploitation necessary for multi-agent environments. We propose MAGE, a meta-RL framework that empowers LLM agents for strategic exploration and exploitation. MAGE utilizes a multi-episode training regime where interaction histories and reflections are integrated into the context window. By using the final episode reward as the objective, MAGE incentivizes the agent to refine its strategy based on past experiences. We further combine population-based training with an agent-specific advantage normalization technique to enrich agent diversity and ensure stable learning. Experiment results show that MAGE outperforms existing baselines in both exploration and exploitation tasks. Furthermore, MAGE exhibits strong generalization to unseen opponents, suggesting it has internalized the ability for strategic exploration and exploitation. Code is available at https://github.com/Lu-Yang666/MAGE.

