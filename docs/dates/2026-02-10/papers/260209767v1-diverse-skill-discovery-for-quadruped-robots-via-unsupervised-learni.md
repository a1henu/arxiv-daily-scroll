---
layout: default
title: Diverse Skill Discovery for Quadruped Robots via Unsupervised Learning
---

# Diverse Skill Discovery for Quadruped Robots via Unsupervised Learning
**arXiv**：[2602.09767v1](https://arxiv.org/abs/2602.09767) · [PDF](https://arxiv.org/pdf/2602.09767.pdf)  
**作者**：Ruopeng Cui, Yifei Bi, Haojie Luo, Wei Li  

**一句话要点**：提出正交专家混合架构与多判别器框架，以提升四足机器人无监督技能发现的多样性与效率。

**关键词**：无监督学习, 技能发现, 四足机器人, 强化学习, 表示学习

## 3 点简述
- 现有无监督技能发现方法存在学习效率低和奖励欺骗问题，导致技能多样性不足。
- 采用正交专家混合架构防止行为表示重叠，结合多判别器框架缓解奖励欺骗。
- 在Unitree A1机器人上验证，训练效率提升，状态空间覆盖扩展18.3%。

## 摘要（原文）

> Reinforcement learning necessitates meticulous reward shaping by specialists to elicit target behaviors, while imitation learning relies on costly task-specific data. In contrast, unsupervised skill discovery can potentially reduce these burdens by learning a diverse repertoire of useful skills driven by intrinsic motivation. However, existing methods exhibit two key limitations: they typically rely on a single policy to master a versatile repertoire of behaviors without modeling the shared structure or distinctions among them, which results in low learning efficiency; moreover, they are susceptible to reward hacking, where the reward signal increases and converges rapidly while the learned skills display insufficient actual diversity. In this work, we introduce an Orthogonal Mixture-of-Experts (OMoE) architecture that prevents diverse behaviors from collapsing into overlapping representations, enabling a single policy to master a wide spectrum of locomotion skills. In addition, we design a multi-discriminator framework in which different discriminators operate on distinct observation spaces, effectively mitigating reward hacking. We evaluated our method on the 12-DOF Unitree A1 quadruped robot, demonstrating a diverse set of locomotion skills. Our experiments demonstrate that the proposed framework boosts training efficiency and yields an 18.3\% expansion in state-space coverage compared to the baseline.

