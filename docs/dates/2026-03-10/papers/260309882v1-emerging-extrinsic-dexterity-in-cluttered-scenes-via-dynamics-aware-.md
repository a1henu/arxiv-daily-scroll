---
layout: default
title: Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning
---

# Emerging Extrinsic Dexterity in Cluttered Scenes via Dynamics-aware Policy Learning
**arXiv**：[2603.09882v1](https://arxiv.org/abs/2603.09882) · [PDF](https://arxiv.org/pdf/2603.09882.pdf)  
**作者**：Yixin Zheng, Jiangran Lyu, Yifan Zhang, Jiayi Chen, Mi Yan, Yuntian Deng, Xuesong Shi, Xiaoguang Zhao, Yizhou Wang, Zhizheng Zhang, He Wang  

**一句话要点**：提出DAPL框架以解决杂乱场景中外在灵巧性挑战

**关键词**：外在灵巧性, 杂乱场景操作, 动态感知策略学习, 强化学习, 世界建模, 模拟到真实迁移

## 3 点简述
- 核心问题：杂乱场景中多物体接触动态耦合，现有方法缺乏显式建模。
- 方法要点：通过显式世界建模学习接触动态表示，并用于条件强化学习。
- 实验或效果：模拟成功率提升超25%，真实世界成功率约50%，展示稳健迁移。

## 摘要（原文）

> Extrinsic dexterity leverages environmental contact to overcome the limitations of prehensile manipulation. However, achieving such dexterity in cluttered scenes remains challenging and underexplored, as it requires selectively exploiting contact among multiple interacting objects with inherently coupled dynamics. Existing approaches lack explicit modeling of such complex dynamics and therefore fall short in non-prehensile manipulation in cluttered environments, which in turn limits their practical applicability in real-world environments. In this paper, we introduce a Dynamics-Aware Policy Learning (DAPL) framework that can facilitate policy learning with a learned representation of contact-induced object dynamics in cluttered environments. This representation is learned through explicit world modeling and used to condition reinforcement learning, enabling extrinsic dexterity to emerge without hand-crafted contact heuristics or complex reward shaping. We evaluate our approach in both simulation and the real world. Our method outperforms prehensile manipulation, human teleoperation, and prior representation-based policies by over 25% in success rate on unseen simulated cluttered scenes with varying densities. The real-world success rate reaches around 50% across 10 cluttered scenes, while a practical grocery deployment further demonstrates robust sim-to-real transfer and applicability.

