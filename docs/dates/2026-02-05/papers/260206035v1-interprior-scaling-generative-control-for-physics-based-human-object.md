---
layout: default
title: InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions
---

# InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions
**arXiv**：[2602.06035v1](https://arxiv.org/abs/2602.06035) · [PDF](https://arxiv.org/pdf/2602.06035.pdf)  
**作者**：Sirui Xu, Samuel Schulter, Morteza Ziyadi, Xialin He, Xiaohan Fei, Yu-Xiong Wang, Liangyan Gui  

**一句话要点**：提出InterPrior框架，通过大规模模仿预训练和强化学习微调，实现物理人机交互的生成控制扩展。

**关键词**：人机交互生成控制, 模仿学习, 强化学习微调, 物理运动先验, 变分策略蒸馏

## 3 点简述
- 核心问题：人机交互中，基于物理的全身协调控制难以泛化到多样场景和未见对象。
- 方法要点：先通过变分策略蒸馏模仿专家，再结合数据增强和强化学习微调，提升泛化能力。
- 实验或效果：框架能生成未见交互行为，支持用户交互控制，并展示机器人部署潜力。

## 摘要（原文）

> Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

