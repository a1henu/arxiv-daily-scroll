---
layout: default
title: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
---

# Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
**arXiv**：[2512.04601v1](https://arxiv.org/abs/2512.04601) · [PDF](https://arxiv.org/pdf/2512.04601.pdf)  
**作者**：Joey Hong, Kang Liu, Zhan Ling, Jiecao Chen, Sergey Levine  

**一句话要点**：提出自然语言演员-评论家算法，以提升大语言模型代理在稀疏奖励长时任务中的训练效率与稳定性。

**关键词**：大语言模型代理, 演员-评论家算法, 自然语言动作空间, 离策略学习, 稀疏奖励任务, 训练稳定性

## 3 点简述
- 核心问题：长时任务中稀疏奖励导致策略梯度方法训练不稳定、样本复杂度高，且自然语言动作空间探索困难。
- 方法要点：使用生成式大语言模型评论家输出自然语言而非标量值，提供更丰富的训练信号，支持离策略训练。
- 实验或效果：在推理、网页浏览和工具使用等任务中，NLAC展现出优于现有方法的潜力，提供更可扩展和稳定的训练范式。

## 摘要（原文）

> Large language model (LLM) agents -- LLMs that dynamically interact with an environment over long horizons -- have become an increasingly important area of research, enabling automation in complex tasks involving tool-use, web browsing, and dialogue with people. In the absence of expert demonstrations, training LLM agents has relied on policy gradient methods that optimize LLM policies with respect to an (often sparse) reward function. However, in long-horizon tasks with sparse rewards, learning from trajectory-level rewards can be noisy, leading to training that is unstable and has high sample complexity. Furthermore, policy improvement hinges on discovering better actions through exploration, which can be difficult when actions lie in natural language space. In this paper, we propose Natural Language Actor-Critic (NLAC), a novel actor-critic algorithm that trains LLM policies using a generative LLM critic that produces natural language rather than scalar values. This approach leverages the inherent strengths of LLMs to provide a richer and more actionable training signal; particularly, in tasks with large, open-ended action spaces, natural language explanations for why an action is suboptimal can be immensely useful for LLM policies to reason how to improve their actions, without relying on random exploration. Furthermore, our approach can be trained off-policy without policy gradients, offering a more data-efficient and stable alternative to existing on-policy methods. We present results on a mixture of reasoning, web browsing, and tool-use with dialogue tasks, demonstrating that NLAC shows promise in outperforming existing training approaches and offers a more scalable and stable training paradigm for LLM agents.

