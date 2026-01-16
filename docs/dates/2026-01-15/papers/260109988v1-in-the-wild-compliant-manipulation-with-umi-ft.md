---
layout: default
title: In-the-Wild Compliant Manipulation with UMI-FT
---

# In-the-Wild Compliant Manipulation with UMI-FT
**arXiv**：[2601.09988v1](https://arxiv.org/abs/2601.09988) · [PDF](https://arxiv.org/pdf/2601.09988.pdf)  
**作者**：Hojung Choi, Yifan Hou, Chuer Pan, Seongheon Hong, Austin Patel, Xiaomeng Xu, Mark R. Cutkosky, Shuran Song  

**一句话要点**：提出UMI-FT手持平台以解决野外环境下合规操作的学习难题

**关键词**：合规操作, 力/力矩传感器, 多模态数据, 自适应策略, 野外演示学习

## 3 点简述
- 问题：商用力/力矩传感器成本高、体积大且易碎，限制了大规模力感知策略学习。
- 方法：UMI-FT平台在每根手指上安装紧凑六轴力/力矩传感器，收集多模态数据训练自适应合规策略。
- 效果：在擦拭白板、串西葫芦和插入灯泡等任务中，优于缺乏合规性或力感应的基线方法。

## 摘要（原文）

> Many manipulation tasks require careful force modulation. With insufficient force the task may fail, while excessive force could cause damage. The high cost, bulky size and fragility of commercial force/torque (F/T) sensors have limited large-scale, force-aware policy learning. We introduce UMI-FT, a handheld data-collection platform that mounts compact, six-axis force/torque sensors on each finger, enabling finger-level wrench measurements alongside RGB, depth, and pose. Using the multimodal data collected from this device, we train an adaptive compliance policy that predicts position targets, grasp force, and stiffness for execution on standard compliance controllers. In evaluations on three contact-rich, force-sensitive tasks (whiteboard wiping, skewering zucchini, and lightbulb insertion), UMI-FT enables policies that reliably regulate external contact forces and internal grasp forces, outperforming baselines that lack compliance or force sensing. UMI-FT offers a scalable path to learning compliant manipulation from in-the-wild demonstrations. We open-source the hardware and software to facilitate broader adoption at:https://umi-ft.github.io/.

