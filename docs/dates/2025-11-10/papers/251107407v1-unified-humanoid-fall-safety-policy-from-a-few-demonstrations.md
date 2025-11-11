---
layout: default
title: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
---

# Unified Humanoid Fall-Safety Policy from a Few Demonstrations
**arXiv**：[2511.07407v1](https://arxiv.org/abs/2511.07407) · [PDF](https://arxiv.org/pdf/2511.07407.pdf)  
**作者**：Zhengjie Xu, Ye Li, Kwan-yee Lin, Stella X. Yu  

**一句话要点**：提出统一人形机器人跌倒安全策略，通过少量演示融合强化学习解决跌倒预防、冲击缓解和快速恢复问题。

**关键词**：人形机器人控制, 跌倒安全策略, 强化学习, 稀疏演示, 模拟到现实迁移, 自适应行为学习

## 3 点简述
- 核心问题：人形机器人跌倒风险高，现有方法无法全面应对跌倒预防、冲击缓解和恢复。
- 方法要点：融合稀疏人类演示与强化学习，使用自适应扩散记忆学习统一安全行为策略。
- 实验或效果：仿真和Unitree G1实验显示稳健的模拟到现实迁移、低冲击力和快速恢复。

## 摘要（原文）

> Falling is an inherent risk of humanoid mobility. Maintaining stability is
> thus a primary safety focus in robot control and learning, yet no existing
> approach fully averts loss of balance. When instability does occur, prior work
> addresses only isolated aspects of falling: avoiding falls, choreographing a
> controlled descent, or standing up afterward. Consequently, humanoid robots
> lack integrated strategies for impact mitigation and prompt recovery when real
> falls defy these scripts. We aim to go beyond keeping balance to make the
> entire fall-and-recovery process safe and autonomous: prevent falls when
> possible, reduce impact when unavoidable, and stand up when fallen. By fusing
> sparse human demonstrations with reinforcement learning and an adaptive
> diffusion-based memory of safe reactions, we learn adaptive whole-body
> behaviors that unify fall prevention, impact mitigation, and rapid recovery in
> one policy. Experiments in simulation and on a Unitree G1 demonstrate robust
> sim-to-real transfer, lower impact forces, and consistently fast recovery
> across diverse disturbances, pointing towards safer, more resilient humanoids
> in real environments. Videos are available at https://firm2025.github.io/.

