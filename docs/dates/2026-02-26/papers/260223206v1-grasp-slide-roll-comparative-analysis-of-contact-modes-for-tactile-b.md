---
layout: default
title: Grasp, Slide, Roll: Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction
---

# Grasp, Slide, Roll: Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction
**arXiv**：[2602.23206v1](https://arxiv.org/abs/2602.23206) · [PDF](https://arxiv.org/pdf/2602.23206.pdf)  
**作者**：Chung Hee Kim, Shivani Kamtikar, Tye Brady, Taskin Padir, Joshua Migdal  

**一句话要点**：比较抓取、滑动和滚动三种触觉接触模式，以提升机器人触觉形状重建效率与精度

**关键词**：触觉感知, 形状重建, 接触模式, 信息论探索, 机器人操作

## 3 点简述
- 核心问题：触觉感知中物理交互耗时且需策略性选择接触位置以最大化信息增益
- 方法要点：结合信息论探索框架，比较抓取释放、手指滑动和手掌滚动三种接触模式
- 实验或效果：手指滑动和手掌滚动减少34%交互次数，提高55%重建精度，在UR5e机器人上验证

## 摘要（原文）

> Tactile sensing allows robots to gather detailed geometric information about objects through physical interaction, complementing vision-based approaches. However, efficiently acquiring useful tactile data remains challenging due to the time-consuming nature of physical contact and the need to strategically choose contact locations that maximize information gain while minimizing physical interactions. This paper studies how different contact modes affect object shape reconstruction using a tactile-enabled dexterous gripper. We compare three contact interaction modes: grasp-releasing, sliding induced by finger-grazing, and palm-rolling. These contact modes are combined with an information-theoretic exploration framework that guides subsequent sampling locations using a shape completion model. Our results show that the improved tactile sensing efficiency of finger-grazing and palm-rolling translates into faster convergence in shape reconstruction, requiring 34% fewer physical interactions while improving reconstruction accuracy by 55%. We validate our approach using a UR5e robot arm equipped with an Inspire-Robots Dexterous Hand, showing robust performance across primitive object geometries.

