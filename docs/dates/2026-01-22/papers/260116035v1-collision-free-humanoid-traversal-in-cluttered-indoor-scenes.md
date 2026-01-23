---
layout: default
title: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
---

# Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
**arXiv**：[2601.16035v1](https://arxiv.org/abs/2601.16035) · [PDF](https://arxiv.org/pdf/2601.16035.pdf)  
**作者**：Han Xue, Sikai Liang, Zhikai Zhang, Zicheng Zeng, Yun Liu, Yunrui Lian, Jilong Wang, Qingtao Liu, Xuesong Shi, Li Yi  

**一句话要点**：提出HumanoidPF以解决人形机器人在杂乱室内场景中无碰撞穿越问题

**关键词**：人形机器人导航, 无碰撞穿越, 人形势场, 强化学习, 室内场景生成, sim-to-real迁移

## 3 点简述
- 核心问题：人形机器人需将感知的多样化障碍物映射到穿越技能，但缺乏有效的人形-障碍物关系表示
- 方法要点：提出HumanoidPF编码无碰撞运动方向，结合混合场景生成方法，促进RL技能学习
- 实验或效果：在仿真和真实世界验证有效性，实现单点击远程操作，sim-to-real差距可忽略

## 摘要（原文）

> We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

