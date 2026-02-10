---
layout: default
title: TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation
---

# TwinRL-VLA: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation
**arXiv**：[2602.09023v1](https://arxiv.org/abs/2602.09023) · [PDF](https://arxiv.org/pdf/2602.09023.pdf)  
**作者**：Qinwen Xu, Jiaming Liu, Rui Zhou, Shaojun Shi, Nuowei Han, Zhuoyang Liu, Chenyang Gu, Shuo Gu, Yang Yue, Gao Huang, Wenzhao Zheng, Sirui Han, Peng Jia, Shanghang Zhang  

**一句话要点**：提出TwinRL框架，通过数字孪生与真实世界协作强化学习，提升视觉-语言-动作模型在机器人操作中的探索效率与泛化能力。

**关键词**：数字孪生, 强化学习, 视觉-语言-动作模型, 机器人操作, 模拟到真实迁移, 探索效率

## 3 点简述
- 核心问题：VLA模型在真实世界机器人操作中，面临专家演示成本高、在线强化学习探索效率低和探索空间受限的挑战。
- 方法要点：构建高保真数字孪生，采用探索空间扩展策略和模拟到真实引导探索，结合数字孪生并行在线强化学习与人类在环部署。
- 实验或效果：在四个任务中，TwinRL在分布内外区域接近100%成功率，比现有真实世界强化学习方法提速至少30%，平均仅需约20分钟。

## 摘要（原文）

> Despite strong generalization capabilities, Vision-Language-Action (VLA) models remain constrained by the high cost of expert demonstrations and insufficient real-world interaction. While online reinforcement learning (RL) has shown promise in improving general foundation models, applying RL to VLA manipulation in real-world settings is still hindered by low exploration efficiency and a restricted exploration space. Through systematic real-world experiments, we observe that the effective exploration space of online RL is closely tied to the data distribution of supervised fine-tuning (SFT). Motivated by this observation, we propose TwinRL, a digital twin-real-world collaborative RL framework designed to scale and guide exploration for VLA models. First, a high-fidelity digital twin is efficiently reconstructed from smartphone-captured scenes, enabling realistic bidirectional transfer between real and simulated environments. During the SFT warm-up stage, we introduce an exploration space expansion strategy using digital twins to broaden the support of the data trajectory distribution. Building on this enhanced initialization, we propose a sim-to-real guided exploration strategy to further accelerate online RL. Specifically, TwinRL performs efficient and parallel online RL in the digital twin prior to deployment, effectively bridging the gap between offline and online training stages. Subsequently, we exploit efficient digital twin sampling to identify failure-prone yet informative configurations, which are used to guide targeted human-in-the-loop rollouts on the real robot. In our experiments, TwinRL approaches 100% success in both in-distribution regions covered by real-world demonstrations and out-of-distribution regions, delivering at least a 30% speedup over prior real-world RL methods and requiring only about 20 minutes on average across four tasks.

