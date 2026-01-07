---
layout: default
title: Optimizing Control-Friendly Trajectories with Self-Supervised Residual Learning
---

# Optimizing Control-Friendly Trajectories with Self-Supervised Residual Learning
**arXiv**：[2601.02738v1](https://arxiv.org/abs/2601.02738) · [PDF](https://arxiv.org/pdf/2601.02738.pdf)  
**作者**：Kexin Guo, Zihan Yang, Yuhang Liu, Jindou Jia, Xiang Yu  

**一句话要点**：提出自监督残差学习与轨迹优化框架，以解决复杂机器人系统因残余物理效应导致的轨迹跟踪挑战。

**关键词**：自监督学习, 残差学习, 轨迹优化, 混合动力学, 机器人控制, 四旋翼飞行

## 3 点简述
- 核心问题：现实物理模型精度有限，残余物理效应影响控制器合成，导致激进轨迹难以精确跟踪。
- 方法要点：通过自监督学习未知动态效应作为名义动力学残差，构建混合模型，并利用轨迹级数据和解析梯度进行学习。
- 实验或效果：以四旋翼敏捷飞行为例，优化器输出可精确跟踪的激进运动，验证了混合动力学的有效性。

## 摘要（原文）

> Real-world physics can only be analytically modeled with a certain level of precision for modern intricate robotic systems. As a result, tracking aggressive trajectories accurately could be challenging due to the existence of residual physics during controller synthesis. This paper presents a self-supervised residual learning and trajectory optimization framework to address the aforementioned challenges. At first, unknown dynamic effects on the closed-loop model are learned and treated as residuals of the nominal dynamics, jointly forming a hybrid model. We show that learning with analytic gradients can be achieved using only trajectory-level data while enjoying accurate long-horizon prediction with an arbitrary integration step size. Subsequently, a trajectory optimizer is developed to compute the optimal reference trajectory with the residual physics along it minimized. It ends up with trajectories that are friendly to the following control level. The agile flight of quadrotors illustrates that by utilizing the hybrid dynamics, the proposed optimizer outputs aggressive motions that can be precisely tracked.

