---
layout: default
title: MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning
---

# MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning
**arXiv**：[2512.13636v1](https://arxiv.org/abs/2512.13636) · [PDF](https://arxiv.org/pdf/2512.13636.pdf)  
**作者**：Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Hongwei Xie, Bing Wang, Guang Chen, Dingkang Liang, Xiang Bai  

**一句话要点**：提出MindDrive框架，通过在线强化学习解决自动驾驶中VLA模型的探索效率问题

**关键词**：自动驾驶, 视觉-语言-动作模型, 在线强化学习, 大语言模型, 轨迹规划, 探索效率

## 3 点简述
- 当前自动驾驶VLA模型依赖模仿学习，存在分布偏移和因果混淆问题
- MindDrive采用双LoRA参数LLM，将连续动作空间映射为离散语言决策以优化探索
- 在Bench2Drive基准上实现驾驶分数78.04%和成功率55.09%的闭环性能

## 摘要（原文）

> Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. MindDrive achieves strong closed-loop performance on the challenging Bench2Drive benchmark, with a Driving Score (DS) of 78.04 and a Success Rate (SR) of 55.09%. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

