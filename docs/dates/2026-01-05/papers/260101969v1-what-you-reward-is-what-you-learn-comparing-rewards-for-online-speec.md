---
layout: default
title: What you reward is what you learn: Comparing rewards for online speech policy optimization in public HRI
---

# What you reward is what you learn: Comparing rewards for online speech policy optimization in public HRI
**arXiv**：[2601.01969v1](https://arxiv.org/abs/2601.01969) · [PDF](https://arxiv.org/pdf/2601.01969.pdf)  
**作者**：Sichao Song, Yuki Okafuji, Kaito Ariu, Amy Koike  

**一句话要点**：提出基于多臂老虎机在线优化社交机器人语音策略，比较三种奖励在公共人机交互中的效果。

**关键词**：社交机器人, 在线策略优化, 多臂老虎机, 语音策略, 公共人机交互, 奖励设计

## 3 点简述
- 核心问题：在开放环境中设计高效且可接受的对话服务机器人语音策略，需适应非平稳条件。
- 方法要点：将在线策略优化建模为多臂老虎机问题，使用Thompson采样从六种语音动作中选择，比较三种二进制奖励。
- 实验或效果：通过12天现场部署和离线评估，分析不同奖励诱导的交互行为，提炼实际部署设计经验。

## 摘要（原文）

> Designing policies that are both efficient and acceptable for conversational service robots in open and diverse environments is non-trivial. Unlike fixed, hand-tuned parameters, online learning can adapt to non-stationary conditions. In this paper, we study how to adapt a social robot's speech policy in the wild. During a 12-day in-situ deployment with over 1,400 public encounters, we cast online policy optimization as a multi-armed bandit problem and use Thompson sampling to select among six actions defined by speech rate (slow/normal/fast) and verbosity (concise/detailed). We compare three complementary binary rewards--Ru (user rating), Rc (conversation closure), and Rt (>=2 turns)--and show that each induces distinct arm distributions and interaction behaviors. We complement the online results with offline evaluations that analyze contextual factors (e.g., crowd level, group size) using video-annotated data. Taken together, we distill ready-to-use design lessons for deploying online optimization of speech policies in real public HRI settings.

