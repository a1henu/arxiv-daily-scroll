---
layout: default
title: From Power to Precision: Learning Fine-grained Dexterity for Multi-fingered Robotic Hands
---

# From Power to Precision: Learning Fine-grained Dexterity for Multi-fingered Robotic Hands
**arXiv**：[2511.13710v1](https://arxiv.org/abs/2511.13710) · [PDF](https://arxiv.org/pdf/2511.13710.pdf)  
**作者**：Jianglong Ye, Lai Wei, Guangqi Jiang, Changwei Jing, Xueyan Zou, Xiaolong Wang  

**一句话要点**：提出联合优化控制与硬件设计以增强多指机器人手的精细操作能力

**关键词**：多指机器人手, 精细操作, 联合优化, sim-to-real, 指尖几何设计

## 3 点简述
- 核心问题：多指机器人手难以同时实现强力抓握和精细操作
- 方法要点：通过轻量级指尖几何修改和动态控制切换简化精度控制
- 实验或效果：在sim-to-real精度抓取中达到82.5%零样本成功率

## 摘要（原文）

> Human grasps can be roughly categorized into two types: power grasps and precision grasps. Precision grasping enables tool use and is believed to have influenced human evolution. Today's multi-fingered robotic hands are effective in power grasps, but for tasks requiring precision, parallel grippers are still more widely adopted. This contrast highlights a key limitation in current robotic hand design: the difficulty of achieving both stable power grasps and precise, fine-grained manipulation within a single, versatile system. In this work, we bridge this gap by jointly optimizing the control and hardware design of a multi-fingered dexterous hand, enabling both power and precision manipulation. Rather than redesigning the entire hand, we introduce a lightweight fingertip geometry modification, represent it as a contact plane, and jointly optimize its parameters along with the corresponding control. Our control strategy dynamically switches between power and precision manipulation and simplifies precision control into parallel thumb-index motions, which proves robust for sim-to-real transfer. On the design side, we leverage large-scale simulation to optimize the fingertip geometry using a differentiable neural-physics surrogate model. We validate our approach through extensive experiments in both sim-to-real and real-to-real settings. Our method achieves an 82.5% zero-shot success rate on unseen objects in sim-to-real precision grasping, and a 93.3% success rate in challenging real-world tasks involving bread pinching. These results demonstrate that our co-design framework can significantly enhance the fine-grained manipulation ability of multi-fingered hands without reducing their ability for power grasps. Our project page is at https://jianglongye.com/power-to-precision

