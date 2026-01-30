---
layout: default
title: Training slow silicon neurons to control extremely fast robots with spiking reinforcement learning
---

# Training slow silicon neurons to control extremely fast robots with spiking reinforcement learning
**arXiv**：[2601.21548v1](https://arxiv.org/abs/2601.21548) · [PDF](https://arxiv.org/pdf/2601.21548.pdf)  
**作者**：Irene Ambrosini, Ingo Blakowski, Dmitrii Zendrikov, Cristiano Capone, Luna Gava, Giacomo Indiveri, Chiara De Luca, Chiara Bartolozzi  

**一句话要点**：提出混合信号神经形态处理器上的脉冲神经网络，通过强化学习实现高速机器人实时控制

**关键词**：脉冲神经网络, 神经形态计算, 强化学习, 机器人控制, 事件驱动学习, 硬件算法协同设计

## 3 点简述
- 核心问题：空气曲棍球等高速交互任务需毫秒级决策，传统方法难以实时处理
- 方法要点：采用硬件算法协同设计，利用固定随机连接和局部e-prop学习规则进行事件驱动学习
- 实验或效果：在少量试验中实现成功交互，展示实时学习能力，支持智能机器持续学习

## 摘要（原文）

> Air hockey demands split-second decisions at high puck velocities, a challenge we address with a compact network of spiking neurons running on a mixed-signal analog/digital neuromorphic processor. By co-designing hardware and learning algorithms, we train the system to achieve successful puck interactions through reinforcement learning in a remarkably small number of trials. The network leverages fixed random connectivity to capture the task's temporal structure and adopts a local e-prop learning rule in the readout layer to exploit event-driven activity for fast and efficient learning. The result is real-time learning with a setup comprising a computer and the neuromorphic chip in-the-loop, enabling practical training of spiking neural networks for robotic autonomous systems. This work bridges neuroscience-inspired hardware with real-world robotic control, showing that brain-inspired approaches can tackle fast-paced interaction tasks while supporting always-on learning in intelligent machines.

