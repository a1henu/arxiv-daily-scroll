---
layout: default
title: Spatiotemporal Wildfire Prediction and Reinforcement Learning for Helitack Suppression
---

# Spatiotemporal Wildfire Prediction and Reinforcement Learning for Helitack Suppression
**arXiv**：[2601.14238v1](https://arxiv.org/abs/2601.14238) · [PDF](https://arxiv.org/pdf/2601.14238.pdf)  
**作者**：Shaurya Mathur, Shreyas Bellary Manjunath, Nitin Kulkarni, Alina Vereshchaka  

**一句话要点**：提出FireCastRL框架，结合时空预测与强化学习，用于野火主动抑制与资源优化。

**关键词**：野火预测, 时空建模, 强化学习, 直升机灭火, 物理模拟, 资源优化

## 3 点简述
- 核心问题：野火频发且传统管理被动，导致高成本与生态破坏。
- 方法要点：使用深度时空模型预测野火，并部署强化学习代理在物理模拟中执行直升机灭火战术。
- 实验或效果：公开大规模时空数据集，生成威胁评估报告以支持应急响应。

## 摘要（原文）

> Wildfires are growing in frequency and intensity, devastating ecosystems and communities while causing billions of dollars in suppression costs and economic damage annually in the U.S. Traditional wildfire management is mostly reactive, addressing fires only after they are detected. We introduce \textit{FireCastRL}, a proactive artificial intelligence (AI) framework that combines wildfire forecasting with intelligent suppression strategies. Our framework first uses a deep spatiotemporal model to predict wildfire ignition. For high-risk predictions, we deploy a pre-trained reinforcement learning (RL) agent to execute real-time suppression tactics with helitack units inside a physics-informed 3D simulation. The framework generates a threat assessment report to help emergency responders optimize resource allocation and planning. In addition, we are publicly releasing a large-scale, spatiotemporal dataset containing $\mathbf{9.5}$ million samples of environmental variables for wildfire prediction. Our work demonstrates how deep learning and RL can be combined to support both forecasting and tactical wildfire response. More details can be found at https://sites.google.com/view/firecastrl.

