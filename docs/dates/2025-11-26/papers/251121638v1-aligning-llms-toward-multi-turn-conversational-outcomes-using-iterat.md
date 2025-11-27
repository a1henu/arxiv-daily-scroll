---
layout: default
title: Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative PPO
---

# Aligning LLMs Toward Multi-Turn Conversational Outcomes Using Iterative PPO
**arXiv**：[2511.21638v1](https://arxiv.org/abs/2511.21638) · [PDF](https://arxiv.org/pdf/2511.21638.pdf)  
**作者**：Daniel R. Jiang, Jalaj Bhandari, Yukai Yang, Rémi Munos, Tyler Lu  

**一句话要点**：提出迭代PPO方法以优化多轮对话LLMs，适用于目标导向场景。

**关键词**：多轮对话优化, 强化学习对齐, 迭代PPO算法, Q函数学习, RLHF应用

## 3 点简述
- 核心问题：多轮对话中奖励稀疏、长视野，响应规划与令牌生成不一致。
- 方法要点：将多轮RL问题简化为单轮RLHF，使用学习Q函数作为奖励模型。
- 实验或效果：迭代PPO结合在线更新与离线训练，提升稳定性和适应性。

## 摘要（原文）

> Optimizing large language models (LLMs) for multi-turn conversational outcomes remains a significant challenge, especially in goal-oriented settings like AI marketing or sales agents who facilitate transactions via messaging platforms. The difficulty stems from sparse, long-horizon rewards and the discrepancy between response-level planning and token-level generation. In this technical note, we propose a formal reduction of the multi-turn RL problem into a sequence of single-turn RLHF-style problems. This is achieved by setting a learned multi-turn Q-function as the reward model for the single-turn problem. We demonstrate and prove a key insight: solving this single-turn RL problem with standard token-level PPO is equivalent to a policy improvement step within the multi-turn problem. This insight naturally leads to Iterative PPO, a batch online policy iteration algorithm that alternates between fitting Q-functions from logged conversation trajectories and improving the policy. A major practical advantage is that Iterative PPO directly leverages stable, off-the-shelf single-turn RLHF tools, making it straightforward to implement. Our method occupies a middle ground between fully online and fully offline approaches, retaining the adaptability of online updates while gaining the stability benefits of offline training.

