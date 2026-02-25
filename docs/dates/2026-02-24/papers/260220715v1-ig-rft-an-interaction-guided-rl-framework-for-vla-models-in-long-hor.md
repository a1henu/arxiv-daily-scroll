---
layout: default
title: IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation
---

# IG-RFT: An Interaction-Guided RL Framework for VLA Models in Long-Horizon Robotic Manipulation
**arXiv**：[2602.20715v1](https://arxiv.org/abs/2602.20715) · [PDF](https://arxiv.org/pdf/2602.20715.pdf)  
**作者**：Zhian Su, Weijie Kong, Haonan Dong, Huixu Dong  

**一句话要点**：提出IG-RFT系统以解决VLA模型在长视野机器人操作中的强化学习微调挑战

**关键词**：视觉语言动作模型, 强化学习微调, 机器人操作, 长视野任务, 交互引导, 混合奖励函数

## 3 点简述
- 核心问题：VLA模型在长视野复杂任务中泛化困难，强化学习微调面临探索效率低和样本成本高的问题
- 方法要点：引入IG-AWR算法动态调节探索强度，设计混合密集奖励函数结合轨迹和子任务奖励
- 实验或效果：在四个真实世界任务中平均成功率85.0%，显著优于基线方法

## 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated significant potential for generalist robotic policies; however, they struggle to generalize to long-horizon complex tasks in novel real-world domains due to distribution shifts and the scarcity of high-quality demonstrations. Although reinforcement learning (RL) offers a promising avenue for policy improvement, applying it to real-world VLA fine-tuning faces challenges regarding exploration efficiency, training stability, and sample cost. To address these issues, we propose IG-RFT, a novel Interaction-Guided Reinforced Fine-Tuning system designed for flow-based VLA models. Firstly, to facilitate effective policy optimization, we introduce Interaction-Guided Advantage Weighted Regression (IG-AWR), an RL algorithm that dynamically modulates exploration intensity based on the robot's interaction status. Furthermore, to address the limitations of sparse or task-specific rewards, we design a novel hybrid dense reward function that integrates the trajectory-level reward and the subtask-level reward. Finally, we construct a three-stage RL system comprising SFT, Offline RL, and Human-in-the-Loop RL for fine-tuning VLA models. Extensive real-world experiments on four challenging long-horizon tasks demonstrate that IG-RFT achieves an average success rate of 85.0%, significantly outperforming SFT (18.8%) and standard Offline RL baselines (40.0%). Ablation studies confirm the critical contributions of IG-AWR and hybrid reward shaping. In summary, our work establishes and validates a novel reinforced fine-tuning system for VLA models in real-world robotic manipulation.

