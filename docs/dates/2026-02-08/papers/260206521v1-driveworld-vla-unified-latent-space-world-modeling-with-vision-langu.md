---
layout: default
title: DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving
---

# DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving
**arXiv**：[2602.06521v1](https://arxiv.org/abs/2602.06521) · [PDF](https://arxiv.org/pdf/2602.06521.pdf)  
**作者**：Feiyang jia, Lin Liu, Ziying Song, Caiyan Jia, Hangjun Ye, Xiaoshuai Hao, Long Chen  

**一句话要点**：提出DriveWorld-VLA，通过统一潜在空间世界建模与视觉-语言-动作，以增强自动驾驶决策与前瞻想象。

**关键词**：自动驾驶, 世界建模, 视觉-语言-动作, 潜在空间, 端到端学习, 决策规划

## 3 点简述
- 现有端到端自动驾驶方法因潜在状态共享不足，难以统一未来场景演化与动作规划。
- DriveWorld-VLA在表示层面紧密集成视觉-语言-动作与世界模型，支持特征级可控想象。
- 在NAVSIM和nuScenes数据集上实现先进性能，如91.3 PDMS和0.16平均碰撞率。

## 摘要（原文）

> End-to-end (E2E) autonomous driving has recently attracted increasing interest in unifying Vision-Language-Action (VLA) with World Models to enhance decision-making and forward-looking imagination. However, existing methods fail to effectively unify future scene evolution and action planning within a single architecture due to inadequate sharing of latent states, limiting the impact of visual imagination on action decisions. To address this limitation, we propose DriveWorld-VLA, a novel framework that unifies world modeling and planning within a latent space by tightly integrating VLA and world models at the representation level, which enables the VLA planner to benefit directly from holistic scene-evolution modeling and reducing reliance on dense annotated supervision. Additionally, DriveWorld-VLA incorporates the latent states of the world model as core decision-making states for the VLA planner, facilitating the planner to assess how candidate actions impact future scene evolution. By conducting world modeling entirely in the latent space, DriveWorld-VLA supports controllable, action-conditioned imagination at the feature level, avoiding expensive pixel-level rollouts. Extensive open-loop and closed-loop evaluations demonstrate the effectiveness of DriveWorld-VLA, which achieves state-of-the-art performance with 91.3 PDMS on NAVSIMv1, 86.8 EPDMS on NAVSIMv2, and 0.16 3-second average collision rate on nuScenes. Code and models will be released in https://github.com/liulin815/DriveWorld-VLA.git.

