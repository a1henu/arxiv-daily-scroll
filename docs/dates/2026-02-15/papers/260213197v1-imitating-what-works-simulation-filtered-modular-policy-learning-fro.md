---
layout: default
title: Imitating What Works: Simulation-Filtered Modular Policy Learning from Human Videos
---

# Imitating What Works: Simulation-Filtered Modular Policy Learning from Human Videos
**arXiv**：[2602.13197v1](https://arxiv.org/abs/2602.13197) · [PDF](https://arxiv.org/pdf/2602.13197.pdf)  
**作者**：Albert J. Zhai, Kuo-Hao Zeng, Jiasen Lu, Ali Farhadi, Shenlong Wang, Wei-Chiu Ma  

**一句话要点**：提出Perceive-Simulate-Imitate框架，通过仿真过滤人类视频数据训练模块化抓取策略，以解决机器人抓取任务兼容性问题。

**关键词**：机器人操作学习, 模块化策略, 仿真过滤, 人类视频模仿, 抓取兼容性, 监督学习

## 3 点简述
- 核心问题：人类视频数据对机器人抓取学习效果有限，尤其是非类人手机器人，导致抓取与后续任务不兼容。
- 方法要点：采用模块化策略设计，结合仿真过滤人类视频轨迹数据，生成任务导向的抓取标签进行监督学习。
- 实验或效果：真实世界实验显示，无需机器人数据即可高效学习精确操作技能，性能比直接使用抓取生成器更稳健。

## 摘要（原文）

> The ability to learn manipulation skills by watching videos of humans has the potential to unlock a new source of highly scalable data for robot learning. Here, we tackle prehensile manipulation, in which tasks involve grasping an object before performing various post-grasp motions. Human videos offer strong signals for learning the post-grasp motions, but they are less useful for learning the prerequisite grasping behaviors, especially for robots without human-like hands. A promising way forward is to use a modular policy design, leveraging a dedicated grasp generator to produce stable grasps. However, arbitrary stable grasps are often not task-compatible, hindering the robot's ability to perform the desired downstream motion. To address this challenge, we present Perceive-Simulate-Imitate (PSI), a framework for training a modular manipulation policy using human video motion data processed by paired grasp-trajectory filtering in simulation. This simulation step extends the trajectory data with grasp suitability labels, which allows for supervised learning of task-oriented grasping capabilities. We show through real-world experiments that our framework can be used to learn precise manipulation skills efficiently without any robot data, resulting in significantly more robust performance than using a grasp generator naively.

