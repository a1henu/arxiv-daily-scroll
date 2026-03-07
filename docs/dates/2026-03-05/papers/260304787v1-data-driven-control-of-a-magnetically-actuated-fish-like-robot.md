---
layout: default
title: Data-Driven Control of a Magnetically Actuated Fish-Like Robot
---

# Data-Driven Control of a Magnetically Actuated Fish-Like Robot
**arXiv**：[2603.04787v1](https://arxiv.org/abs/2603.04787) · [PDF](https://arxiv.org/pdf/2603.04787.pdf)  
**作者**：Akiyuki Koyama, Hiroaki Kawashima  

**一句话要点**：提出数据驱动控制框架以解决磁驱动鱼形机器人精确导航的挑战

**关键词**：数据驱动控制, 磁驱动机器人, 模型预测控制, 模仿学习, 水下导航

## 3 点简述
- 核心问题：非线性流体动力学、柔性鳍迟滞和变时长控制步长导致精确控制困难
- 方法要点：基于神经网络前向动力学模型，结合梯度模型预测控制和模仿学习优化实时控制
- 实验或效果：仿真验证显示框架实现路径收敛，模仿学习控制器有效复制性能

## 摘要（原文）

> Magnetically actuated fish-like robots offer promising solutions for underwater exploration due to their miniaturization and agility; however, precise control remains a significant challenge because of nonlinear fluid dynamics, flexible fin hysteresis, and the variable-duration control steps inherent to the actuation mechanism. This paper proposes a comprehensive data-driven control framework to address these complexities without relying on analytical modeling. Our methodology comprises three core components: 1) developing a forward dynamics model (FDM) using a neural network trained on real-world experimental data to capture state transitions under varying time steps; 2) integrating this FDM into a gradient-based model predictive control (G-MPC) architecture to optimize control inputs for path following; and 3) applying imitation learning to approximate the G-MPC policy, thereby reducing the computational cost for real-time implementation. We validate the approach through simulations utilizing the identified dynamics model. The results demonstrate that the G-MPC framework achieves accurate path convergence with minimal root mean square error (RMSE), and the imitation learning controller (ILC) effectively replicates this performance. This study highlights the potential of data-driven control strategies for the precise navigation of miniature, fish-like soft robots.

