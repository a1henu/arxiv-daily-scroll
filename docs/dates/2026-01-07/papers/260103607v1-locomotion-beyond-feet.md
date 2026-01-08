---
layout: default
title: Locomotion Beyond Feet
---

# Locomotion Beyond Feet
**arXiv**：[2601.03607v1](https://arxiv.org/abs/2601.03607) · [PDF](https://arxiv.org/pdf/2601.03607.pdf)  
**作者**：Tae Hoon Yang, Haochen Shi, Jiacheng Hu, Zhicong Zhang, Daniel Jiang, Weizhuo Wang, Yao He, Zhen Wu, Yuming Chen, Yifan Hou, Monroe Kennedy, Shuran Song, C. Karen Liu  

**一句话要点**：提出全身人形机器人运动系统，结合关键帧动画与强化学习，应对复杂地形挑战。

**关键词**：人形机器人运动, 全身运动规划, 关键帧动画, 强化学习, 复杂地形导航, 分层控制框架

## 3 点简述
- 核心问题：传统人形机器人运动依赖腿部，难以在低间隙、高墙等复杂地形实现稳定全身运动。
- 方法要点：结合物理基础关键帧动画编码人类运动技能，通过强化学习转化为鲁棒动作，采用分层框架包括地形特定策略和视觉技能规划。
- 实验或效果：真实世界实验验证系统在障碍物尺寸、实例和地形序列上具有泛化能力，实现鲁棒全身运动。

## 摘要（原文）

> Most locomotion methods for humanoid robots focus on leg-based gaits, yet natural bipeds frequently rely on hands, knees, and elbows to establish additional contacts for stability and support in complex environments. This paper introduces Locomotion Beyond Feet, a comprehensive system for whole-body humanoid locomotion across extremely challenging terrains, including low-clearance spaces under chairs, knee-high walls, knee-high platforms, and steep ascending and descending stairs. Our approach addresses two key challenges: contact-rich motion planning and generalization across diverse terrains. To this end, we combine physics-grounded keyframe animation with reinforcement learning. Keyframes encode human knowledge of motor skills, are embodiment-specific, and can be readily validated in simulation or on hardware, while reinforcement learning transforms these references into robust, physically accurate motions. We further employ a hierarchical framework consisting of terrain-specific motion-tracking policies, failure recovery mechanisms, and a vision-based skill planner. Real-world experiments demonstrate that Locomotion Beyond Feet achieves robust whole-body locomotion and generalizes across obstacle sizes, obstacle instances, and terrain sequences.

