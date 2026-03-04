---
layout: default
title: Look Forward to Walk Backward: Efficient Terrain Memory for Backward Locomotion with Forward Vision
---

# Look Forward to Walk Backward: Efficient Terrain Memory for Backward Locomotion with Forward Vision
**arXiv**：[2603.03138v1](https://arxiv.org/abs/2603.03138) · [PDF](https://arxiv.org/pdf/2603.03138.pdf)  
**作者**：Shixin Luo, Songbo Li, Yuan Hao, Yaqi Wang, Jun Zheng, Jun Wu, Qiuguo Zhu  

**一句话要点**：提出LF2WB框架，利用前向视觉与地形记忆实现无后视的足式机器人高效后向运动

**关键词**：足式机器人, 地形记忆, 后向运动, 前向视觉, 硬件高效计算, 无碰撞导航

## 3 点简述
- 核心问题：足式机器人后向运动时前向视野受限，仅依赖本体感知易碰撞障碍物，无法适应复杂地形。
- 方法要点：通过前向运动时写入紧凑关联记忆，后向时检索记忆，采用delta-rule选择性更新和硬件高效训练。
- 实验或效果：仿真和真实场景验证，提升后向敏捷性，在有限感知下实现无碰撞复杂地形运动。

## 摘要（原文）

> Legged robots with egocentric forward-facing depth cameras can couple exteroception and proprioception to achieve robust forward agility on complex terrain. When these robots walk backward, the forward-only field of view provides no preview. Purely proprioceptive controllers can remain stable on moderate ground when moving backward but cannot fully exploit the robot's capabilities on complex terrain and must collide with obstacles. We present Look Forward to Walk Backward (LF2WB), an efficient terrain-memory locomotion framework that uses forward egocentric depth and proprioception to write a compact associative memory during forward motion and to retrieve it for collision-free backward locomotion without rearward vision. The memory backbone employs a delta-rule selective update that softly removes then writes the memory state along the active subspace. Training uses hardware-efficient parallel computation, and deployment runs recurrent, constant-time per-step inference with a constant-size state, making the approach suitable for onboard processors on low-cost robots. Experiments in both simulations and real-world scenarios demonstrate the effectiveness of our method, improving backward agility across complex terrains under limited sensing.

