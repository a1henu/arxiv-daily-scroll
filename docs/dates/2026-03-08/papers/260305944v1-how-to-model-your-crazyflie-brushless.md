---
layout: default
title: How to Model Your Crazyflie Brushless
---

# How to Model Your Crazyflie Brushless
**arXiv**：[2603.05944v1](https://arxiv.org/abs/2603.05944) · [PDF](https://arxiv.org/pdf/2603.05944.pdf)  
**作者**：Alexander Gräfe, Christoph Scherer, Wolfgang Hönig, Sebastian Trimpe  

**一句话要点**：提出Crazyflie Brushless动力学模型以支持敏捷控制研究

**关键词**：无人机动力学建模, 仿真到实物转移, 强化学习控制, Crazyflie平台, 敏捷控制

## 3 点简述
- 核心问题：为新型无刷电机Crazyflie平台建立精确动力学模型，以促进仿真到实物的控制器学习。
- 方法要点：通过仿真和硬件分析识别关键参数，并开源项目供快速测试控制器。
- 实验或效果：训练端到端神经网络位置控制器和两圈后空翻控制器，验证模型在仿真到实物转移中的有效性。

## 摘要（原文）

> The Crazyflie quadcopter is widely recognized as a leading platform for nano-quadcopter research. In early 2025, the Crazyflie Brushless was introduced, featuring brushless motors that provide around 50% more thrust compared to the brushed motors of its predecessor, the Crazyflie 2.1. This advancement has opened new opportunities for research in agile nano-quadcopter control. To support researchers utilizing this new platform, this work presents a dynamics model of the Crazyflie Brushless and identifies its key parameters. Through simulations and hardware analyses, we assess the accuracy of our model. We furthermore demonstrate its suitability for reinforcement learning applications by training an end-to-end neural network position controller and learning a backflip controller capable of executing two complete rotations with a vertical movement of just 1.8 meters. This showcases the model's ability to facilitate the learning of controllers and acrobatic maneuvers that successfully transfer from simulation to hardware. Utilizing this application, we investigate the impact of domain randomization on control performance, offering valuable insights into bridging the sim-to-real gap with the presented model. We have open-sourced the entire project, enabling users of the Crazyflie Brushless to swiftly implement and test their own controllers on an accurate simulation platform.

