---
layout: default
title: Comparison of neural network training strategies for the simulation of dynamical systems
---

# Comparison of neural network training strategies for the simulation of dynamical systems
**arXiv**：[2512.03851v1](https://arxiv.org/abs/2512.03851) · [PDF](https://arxiv.org/pdf/2512.03851.pdf)  
**作者**：Paul Strasser, Andreas Pfeffer, Jakob Weber, Markus Gurtner, Andreas Körner  

**一句话要点**：比较并行与串行-并行训练策略，提升神经网络模拟动态系统的长期预测精度

**关键词**：动态系统模拟, 神经网络训练策略, 长期预测精度, 系统辨识, 并行训练, 串行-并行训练

## 3 点简述
- 核心问题：神经网络模拟动态系统时，训练策略选择对长期预测精度的影响不明确
- 方法要点：对比并行和串行-并行训练策略，澄清术语并关联系统辨识概念
- 实验或效果：在气动阀测试台和工业机器人基准上，并行训练在长期预测中表现更优

## 摘要（原文）

> Neural networks have become a widely adopted tool for modeling nonlinear dynamical systems from data. However, the choice of training strategy remains a key design decision, particularly for simulation tasks. This paper compares two predominant strategies: parallel and series-parallel training. The conducted empirical analysis spans five neural network architectures and two examples: a pneumatic valve test bench and an industrial robot benchmark. The study reveals that, even though series-parallel training dominates current practice, parallel training consistently yields better long-term prediction accuracy. Additionally, this work clarifies the often inconsistent terminology in the literature and relate both strategies to concepts from system identification. The findings suggest that parallel training should be considered the default training strategy for neural network-based simulation of dynamical systems.

