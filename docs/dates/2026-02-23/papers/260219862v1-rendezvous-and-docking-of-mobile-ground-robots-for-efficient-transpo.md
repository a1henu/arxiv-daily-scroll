---
layout: default
title: Rendezvous and Docking of Mobile Ground Robots for Efficient Transportation Systems
---

# Rendezvous and Docking of Mobile Ground Robots for Efficient Transportation Systems
**arXiv**：[2602.19862v1](https://arxiv.org/abs/2602.19862) · [PDF](https://arxiv.org/pdf/2602.19862.pdf)  
**作者**：Lars Fischer, Daniel Flögel, Sören Hohmann  

**一句话要点**：提出中央MPC方法以实现移动地面机器人的动态物理耦合，提升物流效率

**关键词**：移动机器人, 动态物理耦合, 模型预测控制, 物流效率, 对接接口建模

## 3 点简述
- 核心问题：现有方法忽略对接接口建模和接近策略，导致动态物理耦合不可靠或低效
- 方法要点：中央MPC方法显式建模机器人动力学和状态，结合对接接口约束，实施接近策略
- 实验或效果：在物流场景中，动态传输比非耦合方法时间效率高19.75%，能量效率高21.04%

## 摘要（原文）

> In-Motion physical coupling of multiple mobile ground robots has the potential to enable new applications like in-motion transfer that improves efficiency in handling and transferring goods, which tackles current challenges in logistics. A key challenge lies in achieving reliable autonomous in-motion physical coupling of two mobile ground robots starting at any initial position. Existing approaches neglect the modeling of the docking interface and the strategy for approaching it, resulting in uncontrolled collisions that make in-motion physical coupling either impossible or inefficient. To address this challenge, we propose a central mpc approach that explicitly models the dynamics and states of two omnidirectional wheeled robots, incorporates constraints related to their docking interface, and implements an approaching strategy for rendezvous and docking. This novel approach enables omnidirectional wheeled robots with a docking interface to physically couple in motion regardless of their initial position. In addition, it makes in-motion transfer possible, which is 19.75% more time- and 21.04% energy-efficient compared to a non-coupling approach in a logistic scenario.

