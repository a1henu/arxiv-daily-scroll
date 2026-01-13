---
layout: default
title: Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids
---

# Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids
**arXiv**：[2601.07718v1](https://arxiv.org/abs/2601.07718) · [PDF](https://arxiv.org/pdf/2601.07718.pdf)  
**作者**：Shaoting Zhu, Ziwen Zhuang, Mengjie Zhao, Kun-Ying Lee, Hang Zhao  

**一句话要点**：提出可扩展感知跑酷框架，实现人形机器人在复杂野外环境中的稳健徒步

**关键词**：人形机器人控制, 强化学习, 感知导航, 野外徒步, 端到端框架

## 3 点简述
- 核心问题：整合外感知面临状态估计漂移和训练可扩展性挑战，如LiDAR方法处理躯干抖动不佳。
- 方法要点：引入立足点安全机制和平面补丁采样策略，通过单阶段强化学习直接映射深度输入到关节动作。
- 实验或效果：全尺寸人形机器人实验显示，策略能在复杂地形中以高达2.5 m/s速度稳健穿越，代码开源。

## 摘要（原文）

> Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

