---
layout: default
title: Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic
---

# Learning Decentralized LLM Collaboration with Multi-Agent Actor Critic
**arXiv**：[2601.21972v1](https://arxiv.org/abs/2601.21972) · [PDF](https://arxiv.org/pdf/2601.21972.pdf)  
**作者**：Shuo Liu, Tianle Chen, Ryan Amiri, Christopher Amato  

**一句话要点**：提出多智能体演员-评论家方法以优化去中心化大语言模型协作

**关键词**：多智能体强化学习, 去中心化协作, 演员-评论家方法, 大语言模型优化, 稀疏奖励任务

## 3 点简述
- 核心问题：现有方法依赖集中式协议或蒙特卡洛方法，导致部署不灵活或训练样本需求高
- 方法要点：开发CoLLM-CC和CoLLM-DC两种MAAC方法，分别使用集中式和去中心化评论家
- 实验或效果：在长视野或稀疏奖励任务中，CoLLM-CC优于蒙特卡洛方法和CoLLM-DC，后者收敛困难

## 摘要（原文）

> Recent work has explored optimizing LLM collaboration through Multi-Agent Reinforcement Learning (MARL). However, most MARL fine-tuning approaches rely on predefined execution protocols, which often require centralized execution. Decentralized LLM collaboration is more appealing in practice, as agents can run inference in parallel with flexible deployments. Also, current approaches use Monte Carlo methods for fine-tuning, which suffer from high variance and thus require more samples to train effectively. Actor-critic methods are prevalent in MARL for dealing with these issues, so we developed Multi-Agent Actor-Critic (MAAC) methods to optimize decentralized LLM collaboration. In this paper, we analyze when and why these MAAC methods are beneficial. We propose 2 MAAC approaches, \textbf{CoLLM-CC} with a \textbf{C}entralized \textbf{C}ritic and \textbf{CoLLM-DC} with \textbf{D}ecentralized \textbf{C}ritics. Our experiments across writing, coding, and game-playing domains show that Monte Carlo methods and CoLLM-DC can achieve performance comparable to CoLLM-CC in short-horizon and dense-reward settings. However, they both underperform CoLLM-CC on long-horizon or sparse-reward tasks, where Monte Carlo methods require substantially more samples and CoLLM-DC struggles to converge. Our code is available at https://github.com/OpenMLRL/CoMLRL/releases/tag/v1.3.2.

