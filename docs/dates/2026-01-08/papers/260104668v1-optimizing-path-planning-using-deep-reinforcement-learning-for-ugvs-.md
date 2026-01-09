---
layout: default
title: Optimizing Path Planning using Deep Reinforcement Learning for UGVs in Precision Agriculture
---

# Optimizing Path Planning using Deep Reinforcement Learning for UGVs in Precision Agriculture
**arXiv**：[2601.04668v1](https://arxiv.org/abs/2601.04668) · [PDF](https://arxiv.org/pdf/2601.04668.pdf)  
**作者**：Laukik Patade, Rohan Rane, Sandeep Pillai  

**一句话要点**：提出基于深度强化学习的连续动作空间路径规划方法，以优化精准农业中无人地面车辆的动态导航

**关键词**：深度强化学习, 路径规划, 无人地面车辆, 精准农业, 连续动作空间, 动态环境

## 3 点简述
- 核心问题：传统网格方法（如A*）在动态农业环境中适应性不足，需自适应学习策略。
- 方法要点：研究从DQN扩展到连续动作空间模型（DDPG和TD3），提升决策能力。
- 实验或效果：在三维仿真中，预训练TD3代理在动态环境中达到95%成功率，确保作物和机器人安全。

## 摘要（原文）

> This study focuses on optimizing path planning for unmanned ground vehicles (UGVs) in precision agriculture using deep reinforcement learning (DRL) techniques in continuous action spaces. The research begins with a review of traditional grid-based methods, such as A* and Dijkstra's algorithms, and discusses their limitations in dynamic agricultural environments, highlighting the need for adaptive learning strategies. The study then explores DRL approaches, including Deep Q-Networks (DQN), which demonstrate improved adaptability and performance in two-dimensional simulations. Enhancements such as Double Q-Networks and Dueling Networks are evaluated to further improve decision-making. Building on these results, the focus shifts to continuous action space models, specifically Deep Deterministic Policy Gradient (DDPG) and Twin Delayed Deep Deterministic Policy Gradient (TD3), which are tested in increasingly complex environments. Experiments conducted in a three-dimensional environment using ROS and Gazebo demonstrate the effectiveness of continuous DRL algorithms in navigating dynamic agricultural scenarios. Notably, the pretrained TD3 agent achieves a 95 percent success rate in dynamic environments, demonstrating the robustness of the proposed approach in handling moving obstacles while ensuring safety for both crops and the robot.

