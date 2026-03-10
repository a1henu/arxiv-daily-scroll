---
layout: default
title: Context-free Self-Conditioned GAN for Trajectory Forecasting
---

# Context-free Self-Conditioned GAN for Trajectory Forecasting
**arXiv**：[2603.08658v1](https://arxiv.org/abs/2603.08658) · [PDF](https://arxiv.org/pdf/2603.08658.pdf)  
**作者**：Tiago Rodrigues de Almeida, Eduardo Gutierrez Maestro, Oscar Martinez Mozos  

**一句话要点**：提出基于自条件GAN的无上下文方法，用于轨迹预测以学习不同行为模式。

**关键词**：轨迹预测, 自条件GAN, 无上下文学习, 行为模式识别, 生成对抗网络

## 3 点简述
- 核心问题：轨迹预测中无上下文方法学习轨迹的不同行为模式。
- 方法要点：使用自条件GAN，在判别器特征空间区分行为模式，提出三种训练设置。
- 实验或效果：在人类运动和道路代理数据集上测试，优于先前无上下文方法，尤其在人类运动中表现突出。

## 摘要（原文）

> In this paper, we present a context-free unsupervised approach based on a self-conditioned GAN to learn different modes from 2D trajectories. Our intuition is that each mode indicates a different behavioral moving pattern in the discriminator's feature space. We apply this approach to the problem of trajectory forecasting. We present three different training settings based on self-conditioned GAN, which produce better forecasters. We test our method in two data sets: human motion and road agents. Experimental results show that our approach outperforms previous context-free methods in the least representative supervised labels while performing well in the remaining labels. In addition, our approach outperforms globally in human motion, while performing well in road agents.

