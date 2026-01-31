---
layout: default
title: When does predictive inverse dynamics outperform behavior cloning?
---

# When does predictive inverse dynamics outperform behavior cloning?
**arXiv**：[2601.21718v1](https://arxiv.org/abs/2601.21718) · [PDF](https://arxiv.org/pdf/2601.21718.pdf)  
**作者**：Lukas Schäfer, Pallavi Choudhury, Abdelhak Lemkhenter, Chris Lovett, Somjit Nath, Luis França, Matheus Ribeiro Furtado de Mendonça, Alex Lamb, Riashat Islam, Siddhartha Sen, John Langford, Katja Hofmann, Sergio Valcarcel Macua  

**一句话要点**：提出预测逆动力学模型以提升离线模仿学习在有限专家演示下的性能

**关键词**：离线模仿学习, 预测逆动力学模型, 偏差-方差权衡, 行为克隆, 样本效率, 高维视觉输入

## 3 点简述
- 核心问题：行为克隆在专家演示有限时性能不佳，预测逆动力学模型的优势原因不明
- 方法要点：预测逆动力学模型结合未来状态预测器和逆动力学模型，引入偏差-方差权衡
- 实验或效果：在2D导航任务中，预测逆动力学模型平均需演示量减少三倍；在3D游戏环境中，样本需求减少超66%

## 摘要（原文）

> Behavior cloning (BC) is a practical offline imitation learning method, but it often fails when expert demonstrations are limited. Recent works have introduced a class of architectures named predictive inverse dynamics models (PIDM) that combine a future state predictor with an inverse dynamics model (IDM). While PIDM often outperforms BC, the reasons behind its benefits remain unclear. In this paper, we provide a theoretical explanation: PIDM introduces a bias-variance tradeoff. While predicting the future state introduces bias, conditioning the IDM on the prediction can significantly reduce variance. We establish conditions on the state predictor bias for PIDM to achieve lower prediction error and higher sample efficiency than BC, with the gap widening when additional data sources are available. We validate the theoretical insights empirically in 2D navigation tasks, where BC requires up to five times (three times on average) more demonstrations than PIDM to reach comparable performance; and in a complex 3D environment in a modern video game with high-dimensional visual inputs and stochastic transitions, where BC requires over 66\% more samples than PIDM.

