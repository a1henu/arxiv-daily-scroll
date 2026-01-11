---
layout: default
title: ResMAS: Resilience Optimization in LLM-based Multi-agent Systems
---

# ResMAS: Resilience Optimization in LLM-based Multi-agent Systems
**arXiv**：[2601.04694v1](https://arxiv.org/abs/2601.04694) · [PDF](https://arxiv.org/pdf/2601.04694.pdf)  
**作者**：Zhilun Zhou, Zihan Liu, Jiahe Liu, Qingyu Shao, Yihan Wang, Kun Shao, Depeng Jin, Fengli Xu  

**一句话要点**：提出ResMAS框架，通过优化通信拓扑和提示设计增强LLM多智能体系统的抗扰动能力。

**关键词**：多智能体系统, 大语言模型, 抗扰动优化, 通信拓扑, 提示工程, 强化学习

## 3 点简述
- 核心问题：LLM多智能体系统在分布式环境中易受智能体故障等扰动影响，现有方法多为被动防御。
- 方法要点：两阶段框架，先训练奖励模型和拓扑生成器优化通信拓扑，再基于拓扑优化智能体提示。
- 实验或效果：多任务实验显示ResMAS显著提升系统抗扰动性，并展现出对新任务和模型的强泛化能力。

## 摘要（原文）

> Large Language Model-based Multi-Agent Systems (LLM-based MAS), where multiple LLM agents collaborate to solve complex tasks, have shown impressive performance in many areas. However, MAS are typically distributed across different devices or environments, making them vulnerable to perturbations such as agent failures. While existing works have studied the adversarial attacks and corresponding defense strategies, they mainly focus on reactively detecting and mitigating attacks after they occur rather than proactively designing inherently resilient systems. In this work, we study the resilience of LLM-based MAS under perturbations and find that both the communication topology and prompt design significantly influence system resilience. Motivated by these findings, we propose ResMAS: a two-stage framework for enhancing MAS resilience. First, we train a reward model to predict the MAS's resilience, based on which we train a topology generator to automatically design resilient topology for specific tasks through reinforcement learning. Second, we introduce a topology-aware prompt optimization method that refines each agent's prompt based on its connections and interactions with other agents. Extensive experiments across a range of tasks show that our approach substantially improves MAS resilience under various constraints. Moreover, our framework demonstrates strong generalization ability to new tasks and models, highlighting its potential for building resilient MASs.

