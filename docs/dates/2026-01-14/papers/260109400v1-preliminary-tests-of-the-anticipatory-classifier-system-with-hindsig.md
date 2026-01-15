---
layout: default
title: Preliminary Tests of the Anticipatory Classifier System with Hindsight Experience Replay
---

# Preliminary Tests of the Anticipatory Classifier System with Hindsight Experience Replay
**arXiv**：[2601.09400v1](https://arxiv.org/abs/2601.09400) · [PDF](https://arxiv.org/pdf/2601.09400.pdf)  
**作者**：Olgierd Unold, Stanisław Franczyk  

**一句话要点**：提出ACS2HER以解决稀疏奖励环境中学习停滞问题

**关键词**：学习分类器系统, 稀疏奖励学习, 后见经验回放, 认知地图构建, 计算开销分析

## 3 点简述
- 核心问题：ACS2在稀疏奖励环境中性能停滞，学习信号不足
- 方法要点：集成HER机制，失败时重标状态为虚拟目标以稠密化学习信号
- 实验或效果：在Maze 6和FrozenLake基准上加速知识获取，但计算开销和分类器数量增加

## 摘要（原文）

> This paper introduces ACS2HER, a novel integration of the Anticipatory Classifier System (ACS2) with the Hindsight Experience Replay (HER) mechanism. While ACS2 is highly effective at building cognitive maps through latent learning, its performance often stagnates in environments characterized by sparse rewards. We propose a specific architectural variant that triggers hindsight learning when the agent fails to reach its primary goal, re-labeling visited states as virtual goals to densify the learning signal. The proposed model was evaluated on two benchmarks: the deterministic \texttt{Maze 6} and the stochastic \texttt{FrozenLake}. The results demonstrate that ACS2HER significantly accelerates knowledge acquisition and environmental mastery compared to the standard ACS2. However, this efficiency gain is accompanied by increased computational overhead and a substantial expansion in classifier numerosity. This work provides the first analysis of combining anticipatory mechanisms with retrospective goal-relabeling in Learning Classifier Systems.

