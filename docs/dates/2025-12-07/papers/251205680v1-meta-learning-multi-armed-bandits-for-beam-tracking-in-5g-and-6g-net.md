---
layout: default
title: Meta-Learning Multi-armed Bandits for Beam Tracking in 5G and 6G Networks
---

# Meta-Learning Multi-armed Bandits for Beam Tracking in 5G and 6G Networks
**arXiv**：[2512.05680v1](https://arxiv.org/abs/2512.05680) · [PDF](https://arxiv.org/pdf/2512.05680.pdf)  
**作者**：Alexander Mattick, George Yammine, Georgios Kontes, Setareh Maghsudi, Christopher Mutschler  

**一句话要点**：提出基于元学习多臂老虎机的波束跟踪方法，以解决5G/6G网络中移动用户设备的最优波束选择挑战。

**关键词**：波束跟踪, 元学习, 多臂老虎机, 5G/6G网络, 部分可观测马尔可夫决策过程

## 3 点简述
- 核心问题：大规模码本和波束反射/遮挡效应使移动用户设备的最优波束选择困难。
- 方法要点：将波束选择建模为部分可观测马尔可夫决策过程，通过元学习多臂老虎机在线搜索移动最优波束。
- 实验或效果：方法能处理新轨迹和环境变化，性能优于先前工作数个数量级。

## 摘要（原文）

> Beamforming-capable antenna arrays with many elements enable higher data rates in next generation 5G and 6G networks. In current practice, analog beamforming uses a codebook of pre-configured beams with each of them radiating towards a specific direction, and a beam management function continuously selects \textit{optimal} beams for moving user equipments (UEs). However, large codebooks and effects caused by reflections or blockages of beams make an optimal beam selection challenging. In contrast to previous work and standardization efforts that opt for supervised learning to train classifiers to predict the next best beam based on previously selected beams we formulate the problem as a partially observable Markov decision process (POMDP) and model the environment as the codebook itself. At each time step, we select a candidate beam conditioned on the belief state of the unobservable optimal beam and previously probed beams. This frames the beam selection problem as an online search procedure that locates the moving optimal beam. In contrast to previous work, our method handles new or unforeseen trajectories and changes in the physical environment, and outperforms previous work by orders of magnitude.

