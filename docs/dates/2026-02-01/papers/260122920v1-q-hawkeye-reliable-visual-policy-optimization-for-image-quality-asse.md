---
layout: default
title: Q-Hawkeye: Reliable Visual Policy Optimization for Image Quality Assessment
---

# Q-Hawkeye: Reliable Visual Policy Optimization for Image Quality Assessment
**arXiv**：[2601.22920v1](https://arxiv.org/abs/2601.22920) · [PDF](https://arxiv.org/pdf/2601.22920.pdf)  
**作者**：Wulin Xie, Rui Dai, Ruidong Ding, Kaikui Liu, Xiangxiang Chu, Xinwen Hou, Jie Wen  

**一句话要点**：提出Q-Hawkeye框架，通过不确定性感知和感知优化提升基于强化学习的图像质量评估可靠性。

**关键词**：图像质量评估, 强化学习, 不确定性感知, 视觉感知优化, 可靠性提升, 泛化性能

## 3 点简述
- 核心问题：现有基于强化学习的IQA方法忽视预测稳定性差异和视觉感知能力，导致梯度更新噪声和可靠性不足。
- 方法要点：引入不确定性感知动态优化，根据预测方差重加权样本更新；设计感知感知优化，通过原始与退化图像对和隐式感知损失增强视觉证据基础。
- 实验或效果：在多个数据集上超越先进方法，表现出更好的泛化性能，代码和模型将开源。

## 摘要（原文）

> Image Quality Assessment (IQA) predicts perceptual quality scores consistent with human judgments. Recent RL-based IQA methods built on MLLMs focus on generating visual quality descriptions and scores, ignoring two key reliability limitations: (i) although the model's prediction stability varies significantly across training samples, existing GRPO-based methods apply uniform advantage weighting, thereby amplifying noisy signals from unstable samples in gradient updates; (ii) most works emphasize text-grounded reasoning over images while overlooking the model's visual perception ability of image content. In this paper, we propose Q-Hawkeye, an RL-based reliable visual policy optimization framework that redesigns the learning signal through unified Uncertainty-Aware Dynamic Optimization and Perception-Aware Optimization. Q-Hawkeye estimates predictive uncertainty using the variance of predicted scores across multiple rollouts and leverages this uncertainty to reweight each sample's update strength, stabilizing policy optimization. To strengthen perceptual reliability, we construct paired inputs of degraded images and their original images and introduce an Implicit Perception Loss that constrains the model to ground its quality judgments in genuine visual evidence. Extensive experiments demonstrate that Q-Hawkeye outperforms state-of-the-art methods and generalizes better across multiple datasets. The code and models will be made available.

