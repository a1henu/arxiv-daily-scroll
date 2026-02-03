---
layout: default
title: TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour
---

# TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour
**arXiv**：[2602.02331v1](https://arxiv.org/abs/2602.02331) · [PDF](https://arxiv.org/pdf/2602.02331.pdf)  
**作者**：Shaoting Zhu, Baijun Ye, Jiaxuan Wang, Jiakang Chen, Ziwen Zhuang, Linzhan Mou, Runhan Huang, Hang Zhao  

**一句话要点**：提出快速测试时训练框架以增强人形机器人在未知复杂地形上的动态跑酷能力

**关键词**：测试时训练, 人形机器人跑酷, 几何重建, 仿真到真实迁移, 动态运动控制

## 3 点简述
- 核心问题：通用运动策略在任意高难度地形上表现不佳，难以实现动态跑酷。
- 方法要点：采用真实-仿真-真实框架，通过快速测试时训练在重建的高保真地形网格上微调预训练策略。
- 实验或效果：测试时训练后策略展现鲁棒的零样本仿真到真实迁移能力，整个流程在多数地形上少于10分钟。

## 摘要（原文）

> Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics. Although general locomotion policies demonstrate capabilities across broad terrain distributions, they often struggle with arbitrary and highly challenging environments. To overcome this limitation, we propose a real-to-sim-to-real framework that leverages rapid test-time training (TTT) on novel terrains, significantly enhancing the robot's capability to traverse extremely difficult geometries. We adopt a two-stage end-to-end learning paradigm: a policy is first pre-trained on diverse procedurally generated terrains, followed by rapid fine-tuning on high-fidelity meshes reconstructed from real-world captures. Specifically, we develop a feed-forward, efficient, and high-fidelity geometry reconstruction pipeline using RGB-D inputs, ensuring both speed and quality during test-time training. We demonstrate that TTT-Parkour empowers humanoid robots to master complex obstacles, including wedges, stakes, boxes, trapezoids, and narrow beams. The whole pipeline of capturing, reconstructing, and test-time training requires less than 10 minutes on most tested terrains. Extensive experiments show that the policy after test-time training exhibits robust zero-shot sim-to-real transfer capability.

