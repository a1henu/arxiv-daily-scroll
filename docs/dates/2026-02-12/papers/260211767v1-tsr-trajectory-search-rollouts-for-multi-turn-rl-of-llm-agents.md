---
layout: default
title: TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents
---

# TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents
**arXiv**：[2602.11767v1](https://arxiv.org/abs/2602.11767) · [PDF](https://arxiv.org/pdf/2602.11767.pdf)  
**作者**：Aladin Djuhera, Swanand Ravindra Kadhe, Farhan Ahmed, Holger Boche  

**一句话要点**：提出TSR方法，通过训练时轨迹搜索提升多轮强化学习中智能体的性能与稳定性。

**关键词**：多轮强化学习, 轨迹搜索, 大语言模型智能体, 训练时优化, 树状搜索, 性能提升

## 3 点简述
- 多轮强化学习面临奖励稀疏或延迟、环境随机性挑战，导致轨迹采样效率低。
- TSR在训练时执行轻量级树状搜索，基于任务反馈选择高得分动作构建高质量轨迹。
- 结合PPO和GRPO优化器，在Sokoban等任务上实现最高15%性能提升，学习更稳定。

## 摘要（原文）

> Advances in large language models (LLMs) are driving a shift toward using reinforcement learning (RL) to train agents from iterative, multi-turn interactions across tasks. However, multi-turn RL remains challenging as rewards are often sparse or delayed, and environments can be stochastic. In this regime, naive trajectory sampling can hinder exploitation and induce mode collapse. We propose TSR (Trajectory-Search Rollouts), a training-time approach that repurposes test-time scaling ideas for improved per-turn rollout generation. TSR performs lightweight tree-style search to construct high-quality trajectories by selecting high-scoring actions at each turn using task-specific feedback. This improves rollout quality and stabilizes learning while leaving the underlying optimization objective unchanged, making TSR optimizer-agnostic. We instantiate TSR with best-of-N, beam, and shallow lookahead search, and pair it with PPO and GRPO, achieving up to 15% performance gains and more stable learning on Sokoban, FrozenLake, and WebShop tasks at a one-time increase in training compute. By moving search from inference time to the rollout stage of training, TSR provides a simple and general mechanism for stronger multi-turn agent learning, complementary to existing frameworks and rejection-sampling-style selection methods.

