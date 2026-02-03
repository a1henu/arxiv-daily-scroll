---
layout: default
title: Grad2Reward: From Sparse Judgment to Dense Rewards for Improving Open-Ended LLM Reasoning
---

# Grad2Reward: From Sparse Judgment to Dense Rewards for Improving Open-Ended LLM Reasoning
**arXiv**：[2602.01791v1](https://arxiv.org/abs/2602.01791) · [PDF](https://arxiv.org/pdf/2602.01791.pdf)  
**作者**：Zheng Zhang, Ao Lu, Yuanhao Zeng, Ziwei Shan, Jinjin Guo, Lufei Li, Yexin Li, Kan Ren  

**一句话要点**：提出Grad2Reward框架，通过梯度归因从Judge模型提取密集奖励，以改进开放领域LLM推理。

**关键词**：强化学习, 大语言模型推理, 梯度归因, 密集奖励, 开放领域任务, 自判断机制

## 3 点简述
- 问题：现有LLM-as-a-Judge方法提供稀疏奖励，缺乏细粒度监督，且忽略Judge的中间反馈信号。
- 方法：利用单次反向传播从Judge推理过程中提取密集过程奖励，实现精确的令牌级信用分配，并引入自判断机制。
- 效果：实验表明，优化后的策略在多种开放任务中表现优异，验证了其有效性和广泛泛化能力。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant breakthroughs in complex LLM reasoning within verifiable domains, such as mathematics and programming. Recent efforts have sought to extend this paradigm to open-ended tasks by employing LLMs-as-a-Judge to provide sequence-level rewards for policy optimization. However, these rewards are inherently sparse, failing to provide the fine-grained supervision necessary for generating complex, long-form trajectories. Furthermore, current work treats the Judge as a black-box oracle, discarding the rich intermediate feedback signals encoded in it. To address these limitations, we introduce Grad2Reward, a novel framework that extracts dense process rewards directly from the Judge's model inference process via a single backward pass. By leveraging gradient-based attribution, Grad2Reward enables precise token-level credit assignment, substantially enhancing training efficiency and reasoning quality. Additionally, Grad2Reward introduces a self-judging mechanism, allowing the policy to improve through its own evaluative signals without training specialized reward models or reliance on superior external Judges. The experiments demonstrate that policies optimized with Grad2Reward achieve outstanding performance across diverse open-ended tasks, affirming its effectiveness and broad generalizability.

