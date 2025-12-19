---
layout: default
title: Olaf: Bringing an Animated Character to Life in the Physical World
---

# Olaf: Bringing an Animated Character to Life in the Physical World
**arXiv**：[2512.16705v1](https://arxiv.org/abs/2512.16705) · [PDF](https://arxiv.org/pdf/2512.16705.pdf)  
**作者**：David Müller, Espen Knoop, Dario Mylonopoulos, Agon Serifi, Michael A. Hopkins, Ruben Grandia, Moritz Bächer  

**一句话要点**：提出基于强化学习的动画参考控制方法，实现物理世界中卡通角色Olaf的逼真运动。

**关键词**：强化学习控制, 机器人动画角色, 机械设计创新, 物理模拟验证, 风格化运动

## 3 点简述
- 核心问题：动画角色运动非物理化，需在机器人平台上实现逼真且风格化的运动控制。
- 方法要点：使用强化学习结合动画参考，设计隐藏式腿部结构和球形/平面连杆以适应角色比例。
- 实验或效果：通过模拟和硬件验证，引入额外奖励减少噪音和过热，提升角色可信度。

## 摘要（原文）

> Animated characters often move in non-physical ways and have proportions that are far from a typical walking robot. This provides an ideal platform for innovation in both mechanical design and stylized motion control. In this paper, we bring Olaf to life in the physical world, relying on reinforcement learning guided by animation references for control. To create the illusion of Olaf's feet moving along his body, we hide two asymmetric legs under a soft foam skirt. To fit actuators inside the character, we use spherical and planar linkages in the arms, mouth, and eyes. Because the walk cycle results in harsh contact sounds, we introduce additional rewards that noticeably reduce impact noise. The large head, driven by small actuators in the character's slim neck, creates a risk of overheating, amplified by the costume. To keep actuators from overheating, we feed temperature values as additional inputs to policies, introducing new rewards to keep them within bounds. We validate the efficacy of our modeling in simulation and on hardware, demonstrating an unmatched level of believability for a costumed robotic character.

