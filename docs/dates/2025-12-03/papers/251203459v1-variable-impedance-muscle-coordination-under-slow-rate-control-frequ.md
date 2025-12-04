---
layout: default
title: Variable-Impedance Muscle Coordination under Slow-Rate Control Frequencies and Limited Observation Conditions Evaluated through Legged Locomotion
---

# Variable-Impedance Muscle Coordination under Slow-Rate Control Frequencies and Limited Observation Conditions Evaluated through Legged Locomotion
**arXiv**：[2512.03459v1](https://arxiv.org/abs/2512.03459) · [PDF](https://arxiv.org/pdf/2512.03459.pdf)  
**作者**：Hidaka Asai, Tomoyuki Noda, Jun Morimoto  

**一句话要点**：提出可变阻抗肌肉协调模型，在慢速控制频率和有限观测条件下实现稳定单足运动

**关键词**：可变阻抗控制, 肌肉协调, 分层控制器, 强化学习, 形态计算, 运动控制

## 3 点简述
- 核心问题：人体运动控制如何在感官信息有限时保持敏捷稳健，低层肌肉计算如何减轻高层控制器负担
- 方法要点：采用分层控制器，高层为强化学习训练的神经网络，低层为可变阻抗肌肉协调模型
- 实验或效果：在慢速控制频率和延迟、部分、替代观测条件下，可变阻抗肌肉协调使高层网络学习稳定运动

## 摘要（原文）

> Human motor control remains agile and robust despite limited sensory information for feedback, a property attributed to the body's ability to perform morphological computation through muscle coordination with variable impedance. However, it remains unclear how such low-level mechanical computation reduces the control requirements of the high-level controller. In this study, we implement a hierarchical controller consisting of a high-level neural network trained by reinforcement learning and a low-level variable-impedance muscle coor dination model with mono- and biarticular muscles in monoped locomotion task. We systematically restrict the high-level controller by varying the control frequency and by introducing biologically inspired observation conditions: delayed, partial, and substituted observation. Under these conditions, we evaluate how the low-level variable-impedance muscle coordination contributes to learning process of high-level neural network. The results show that variable-impedance muscle coordination enables stable locomotion even under slow-rate control frequency and limited observation conditions. These findings demonstrate that the morphological computation of muscle coordination effectively offloads high-frequency feedback of the high-level controller and provide a design principle for the controller in motor control.

