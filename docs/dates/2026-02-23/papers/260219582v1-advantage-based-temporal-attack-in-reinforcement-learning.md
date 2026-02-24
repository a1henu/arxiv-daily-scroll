---
layout: default
title: Advantage-based Temporal Attack in Reinforcement Learning
---

# Advantage-based Temporal Attack in Reinforcement Learning
**arXiv**：[2602.19582v1](https://arxiv.org/abs/2602.19582) · [PDF](https://arxiv.org/pdf/2602.19582.pdf)  
**作者**：Shenghong He  

**一句话要点**：提出基于优势的对抗变换器以增强强化学习中的时序攻击性能

**关键词**：强化学习, 对抗攻击, 时序相关性, 自注意力机制, 优势函数

## 3 点简述
- 强化学习中现有奖励攻击方法缺乏时序依赖，导致扰动间相关性弱
- AAT采用多尺度因果自注意力机制动态捕获历史信息与当前状态的依赖
- 实验表明AAT在Atari等任务上匹配或超越主流对抗攻击基线

## 摘要（原文）

> Extensive research demonstrates that Deep Reinforcement Learning (DRL) models are susceptible to adversarially constructed inputs (i.e., adversarial examples), which can mislead the agent to take suboptimal or unsafe actions. Recent methods improve attack effectiveness by leveraging future rewards to guide adversarial perturbation generation over sequential time steps (i.e., reward-based attacks). However, these methods are unable to capture dependencies between different time steps in the perturbation generation process, resulting in a weak temporal correlation between the current perturbation and previous perturbations.In this paper, we propose a novel method called Advantage-based Adversarial Transformer (AAT), which can generate adversarial examples with stronger temporal correlations (i.e., time-correlated adversarial examples) to improve the attack performance. AAT employs a multi-scale causal self-attention (MSCSA) mechanism to dynamically capture dependencies between historical information from different time periods and the current state, thus enhancing the correlation between the current perturbation and the previous perturbation. Moreover, AAT introduces a weighted advantage mechanism, which quantifies the effectiveness of a perturbation in a given state and guides the generation process toward high-performance adversarial examples by sampling high-advantage regions. Extensive experiments demonstrate that the performance of AAT matches or surpasses mainstream adversarial attack baselines on Atari, DeepMind Control Suite and Google football tasks.

