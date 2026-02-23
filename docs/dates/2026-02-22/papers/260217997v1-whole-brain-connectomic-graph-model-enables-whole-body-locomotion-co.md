---
layout: default
title: Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly
---

# Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly
**arXiv**：[2602.17997v1](https://arxiv.org/abs/2602.17997) · [PDF](https://arxiv.org/pdf/2602.17997.pdf)  
**作者**：Zehao Jin, Yaoye Zhu, Chen Zhang, Yanan Sui  

**一句话要点**：提出基于果蝇全脑连接组的图模型，实现全身运动控制

**关键词**：全脑连接组, 具身强化学习, 图神经网络, 运动控制, 果蝇模型

## 3 点简述
- 问题：全脑连接组在具身强化学习中作为神经网络控制器的应用尚未探索
- 方法：构建FlyGM图模型，结构等同于果蝇全脑连接组，用于信息传递控制
- 效果：在多种运动任务中实现稳定控制，样本效率和性能优于对比模型

## 摘要（原文）

> Whole-brain biological neural networks naturally support the learning and control of whole-body movements. However, the use of brain connectomes as neural network controllers in embodied reinforcement learning remains unexplored. We investigate using the exact neural architecture of an adult fruit fly's brain for the control of its body movement. We develop Fly-connectomic Graph Model (FlyGM), whose static structure is identical to the complete connectome of an adult Drosophila for whole-body locomotion control. To perform dynamical control, FlyGM represents the static connectome as a directed message-passing graph to impose a biologically grounded information flow from sensory inputs to motor outputs. Integrated with a biomechanical fruit fly model, our method achieves stable control across diverse locomotion tasks without task-specific architectural tuning. To verify the structural advantages of the connectome-based model, we compare it against a degree-preserving rewired graph, a random graph, and multilayer perceptrons, showing that FlyGM yields higher sample efficiency and superior performance. This work demonstrates that static brain connectomes can be transformed to instantiate effective neural policy for embodied learning of movement control.

