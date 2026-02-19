---
layout: default
title: Machine Learning Driven Prediction of the Behavior of Biohybrid Actuators
---

# Machine Learning Driven Prediction of the Behavior of Biohybrid Actuators
**arXiv**：[2602.16330v1](https://arxiv.org/abs/2602.16330) · [PDF](https://arxiv.org/pdf/2602.16330.pdf)  
**作者**：Michail-Antisthenis Tsompanas, Marco Perez Hernandez, Faisal Abdul-Fattah, Karim Elhakim, Mostafa Ibrahim, Judith Fuentes, Florencia Lezcano, Riccardo Collu, Massimo Barbaro, Stefano Lai, Samuel Sanchez, Andrew Adamatzky  

**一句话要点**：提出基于监督学习的静态与动态模型，以预测生物混合执行器的行为，解决其生物变异性和非线性挑战。

**关键词**：生物混合执行器, 监督学习, 随机森林, 神经网络, 长短期记忆网络, 数字孪生

## 3 点简述
- 核心问题：生物混合执行器（如骨骼肌环）存在生物变异性和非线性，导致可控性和可预测性差。
- 方法要点：采用随机森林和神经网络进行静态预测，以及长短期记忆网络进行动态建模，作为数字孪生。
- 实验或效果：静态模型R²达0.9425，动态模型R²达0.9956，支持性能优化和自适应控制策略开发。

## 摘要（原文）

> Skeletal muscle-based biohybrid actuators have proved to be a promising component in soft robotics, offering efficient movement. However, their intrinsic biological variability and nonlinearity pose significant challenges for controllability and predictability. To address these issues, this study investigates the application of supervised learning, a form of machine learning, to model and predict the behavior of biohybrid machines (BHMs), focusing on a muscle ring anchored on flexible polymer pillars. First, static prediction models (i.e., random forest and neural network regressors) are trained to estimate the maximum exerted force achieved from input variables such as muscle sample, electrical stimulation parameters, and baseline exerted force. Second, a dynamic modeling framework, based on Long Short-Term Memory networks, is developed to serve as a digital twin, replicating the time series of exerted forces observed in response to electrical stimulation. Both modeling approaches demonstrate high predictive accuracy. The best performance of the static models is characterized by R2 of 0.9425, whereas the dynamic model achieves R2 of 0.9956. The static models can enable optimization of muscle actuator performance for targeted applications and required force outcomes, while the dynamic model provides a foundation for developing robustly adaptive control strategies in future biohybrid robotic systems.

