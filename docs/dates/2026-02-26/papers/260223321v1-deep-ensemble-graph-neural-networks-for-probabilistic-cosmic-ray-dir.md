---
layout: default
title: Deep ensemble graph neural networks for probabilistic cosmic-ray direction and energy reconstruction in autonomous radio arrays
---

# Deep ensemble graph neural networks for probabilistic cosmic-ray direction and energy reconstruction in autonomous radio arrays
**arXiv**：[2602.23321v1](https://arxiv.org/abs/2602.23321) · [PDF](https://arxiv.org/pdf/2602.23321.pdf)  
**作者**：Arsène Ferrière, Aurélien Benoit-Lévy, Olivier Martineau-Huynh, Matías Tueros  

**一句话要点**：提出基于图神经网络的深度集成方法，用于自主射电阵列中宇宙射线方向和能量的概率重建。

**关键词**：图神经网络, 宇宙射线重建, 不确定性估计, 自主射电阵列, 物理知识融合

## 3 点简述
- 核心问题：从地面射电探测器阵列的电压迹线中精确重建超高能宇宙射线的到达方向和能量。
- 方法要点：将触发天线表示为图结构，结合物理知识设计图神经网络，并采用不确定性估计方法提升预测可靠性。
- 实验或效果：在模拟数据上实现0.092°的角分辨率和16.4%的能量重建分辨率，并验证模型在域偏移下的稳健性。

## 摘要（原文）

> Using advanced machine learning techniques, we developed a method for reconstructing precisely the arrival direction and energy of ultra-high-energy cosmic rays from the voltage traces they induced on ground-based radio detector arrays.
>   In our approach, triggered antennas are represented as a graph structure, which serves as input for a graph neural network (GNN). By incorporating physical knowledge into both the GNN architecture and the input data, we improve the precision and reduce the required size of the training set with respect to a fully data-driven approach. This method achieves an angular resolution of 0.092° and an electromagnetic energy reconstruction resolution of 16.4% on simulated data with realistic noise conditions.
>   We also employ uncertainty estimation methods to enhance the reliability of our predictions, quantifying the confidence of the GNN's outputs and providing confidence intervals for both direction and energy reconstruction. Finally, we investigate strategies to verify the model's consistency and robustness under real life variations, with the goal of identifying scenarios in which predictions remain reliable despite domain shifts between simulation and reality.

