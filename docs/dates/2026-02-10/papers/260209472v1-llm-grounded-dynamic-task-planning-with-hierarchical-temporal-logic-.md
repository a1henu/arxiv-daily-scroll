---
layout: default
title: LLM-Grounded Dynamic Task Planning with Hierarchical Temporal Logic for Human-Aware Multi-Robot Collaboration
---

# LLM-Grounded Dynamic Task Planning with Hierarchical Temporal Logic for Human-Aware Multi-Robot Collaboration
**arXiv**：[2602.09472v1](https://arxiv.org/abs/2602.09472) · [PDF](https://arxiv.org/pdf/2602.09472.pdf)  
**作者**：Shuyuan Hu, Tao Lin, Kai Ye, Yang Yang, Tianwei Zhang  

**一句话要点**：提出基于LLM与分层时序逻辑的神经符号框架，以解决多机器人协作中的动态任务规划问题。

**关键词**：多机器人协作, 动态任务规划, 神经符号框架, 分层时序逻辑, 滚动时域规划

## 3 点简述
- 核心问题：LLM生成的多机器人任务规划缺乏运动学可行性和效率，尤其在长时域场景中。
- 方法要点：将LLM推理落地为分层LTL规范，通过滚动时域规划实时处理环境变化。
- 实验或效果：真实世界实验显示，该方法在成功率和交互流畅度上显著优于基线，并最小化规划延迟。

## 摘要（原文）

> While Large Language Models (LLM) enable non-experts to specify open-world multi-robot tasks, the generated plans often lack kinematic feasibility and are not efficient, especially in long-horizon scenarios. Formal methods like Linear Temporal Logic (LTL) offer correctness and optimal guarantees, but are typically confined to static, offline settings and struggle with computational scalability. To bridge this gap, we propose a neuro-symbolic framework that grounds LLM reasoning into hierarchical LTL specifications and solves the corresponding Simultaneous Task Allocation and Planning (STAP) problem. Unlike static approaches, our system resolves stochastic environmental changes, such as moving users or updated instructions via a receding horizon planning (RHP) loop with real-time perception, which dynamically refines plans through a hierarchical state space. Extensive real-world experiments demonstrate that our approach significantly outperforms baseline methods in success rate and interaction fluency while minimizing planning latency.

