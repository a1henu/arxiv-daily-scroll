---
layout: default
title: Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids
---

# Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids
**arXiv**：[2603.02856v1](https://arxiv.org/abs/2603.02856) · [PDF](https://arxiv.org/pdf/2603.02856.pdf)  
**作者**：Hongjin Chen, Wei Zhang, Pengfei Li, Shihao Ma, Ke Ma, Yujie Jin, Zijun Xu, Xiaohui Wang, Yupeng Zheng, Zining Wang, Jieru Zhao, Yilun Chen, Wenchao Ding  

**一句话要点**：提出Rhythm框架以实现双人形机器人交互式全身控制，解决运动学不匹配和接触动力学挑战。

**关键词**：双人形机器人控制, 交互式全身控制, 强化学习, 运动重定向, 现实部署

## 3 点简述
- 核心问题：双人形机器人交互中运动学不匹配和复杂接触动力学阻碍物理耦合交互。
- 方法要点：集成交互感知运动重定向、交互引导强化学习和现实部署系统，生成可行交互参考并掌握耦合动态。
- 实验或效果：在Unitree G1机器人上验证，成功将拥抱和舞蹈等行为从仿真迁移到现实，实现鲁棒交互控制。

## 摘要（原文）

> Realizing interactive whole-body control for multi-humanoid systems is critical for unlocking complex collaborative capabilities in shared environments. Although recent advancements have significantly enhanced the agility of individual robots, bridging the gap to physically coupled multi-humanoid interaction remains challenging, primarily due to severe kinematic mismatches and complex contact dynamics. To address this, we introduce Rhythm, the first unified framework enabling real-world deployment of dual-humanoid systems for complex, physically plausible interactions. Our framework integrates three core components: (1) an Interaction-Aware Motion Retargeting (IAMR) module that generates feasible humanoid interaction references from human data; (2) an Interaction-Guided Reinforcement Learning (IGRL) policy that masters coupled dynamics via graph-based rewards; and (3) a real-world deployment system that enables robust transfer of dual-humanoid interaction. Extensive experiments on physical Unitree G1 robots demonstrate that our framework achieves robust interactive whole-body control, successfully transferring diverse behaviors such as hugging and dancing from simulation to reality.

