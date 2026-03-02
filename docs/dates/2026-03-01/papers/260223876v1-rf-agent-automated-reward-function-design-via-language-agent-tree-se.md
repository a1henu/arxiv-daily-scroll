---
layout: default
title: RF-Agent: Automated Reward Function Design via Language Agent Tree Search
---

# RF-Agent: Automated Reward Function Design via Language Agent Tree Search
**arXiv**：[2602.23876v1](https://arxiv.org/abs/2602.23876) · [PDF](https://arxiv.org/pdf/2602.23876.pdf)  
**作者**：Ning Gao, Xiuhui Zhang, Xingyu Jiang, Mukang You, Mohan Zhang, Yue Deng  

**一句话要点**：提出RF-Agent框架，通过语言代理树搜索自动设计低层控制任务的奖励函数

**关键词**：奖励函数设计, 语言代理, 蒙特卡洛树搜索, 低层控制, 序列决策, 自动优化

## 3 点简述
- 核心问题：低层控制任务中奖励函数设计依赖专家经验，现有LLM方法利用历史反馈差、搜索效率低
- 方法要点：将LLM视为语言代理，结合蒙特卡洛树搜索，以序列决策过程优化奖励函数设计
- 实验或效果：在17个多样化低层控制任务中取得优异结果，代码已开源

## 摘要（原文）

> Designing efficient reward functions for low-level control tasks is a challenging problem. Recent research aims to reduce reliance on expert experience by using Large Language Models (LLMs) with task information to generate dense reward functions. These methods typically rely on training results as feedback, iteratively generating new reward functions with greedy or evolutionary algorithms. However, they suffer from poor utilization of historical feedback and inefficient search, resulting in limited improvements in complex control tasks. To address this challenge, we propose RF-Agent, a framework that treats LLMs as language agents and frames reward function design as a sequential decision-making process, enhancing optimization through better contextual reasoning. RF-Agent integrates Monte Carlo Tree Search (MCTS) to manage the reward design and optimization process, leveraging the multi-stage contextual reasoning ability of LLMs. This approach better utilizes historical information and improves search efficiency to identify promising reward functions. Outstanding experimental results in 17 diverse low-level control tasks demonstrate the effectiveness of our method. The source code is available at https://github.com/deng-ai-lab/RF-Agent.

