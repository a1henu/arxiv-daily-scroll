---
layout: default
title: Feature Matching-Based Gait Phase Prediction for Obstacle Crossing Control of Powered Transfemoral Prosthesis
---

# Feature Matching-Based Gait Phase Prediction for Obstacle Crossing Control of Powered Transfemoral Prosthesis
**arXiv**：[2510.24676v1](https://arxiv.org/abs/2510.24676) · [PDF](https://arxiv.org/pdf/2510.24676.pdf)  
**作者**：Jiaxuan Zhang, Yuquan Leng, Yixuan Guo, Chenglong Fu  

**一句话要点**：提出基于特征匹配的步态相位预测方法，用于动力大腿假肢的越障控制

**关键词**：步态相位预测, 动力假肢控制, 遗传算法优化, 惯性传感器, 关节角度预测

## 3 点简述
- 核心问题：动力大腿假肢用户在复杂地形越障时面临挑战
- 方法要点：使用遗传算法优化神经网络结构，预测大腿和膝关节角度
- 实验或效果：在噪声标准差小于1时，步态相位估计准确率达100%，关节角度预测误差低于9%

## 摘要（原文）

> For amputees with powered transfemoral prosthetics, navigating obstacles or
> complex terrain remains challenging. This study addresses this issue by using
> an inertial sensor on the sound ankle to guide obstacle-crossing movements. A
> genetic algorithm computes the optimal neural network structure to predict the
> required angles of the thigh and knee joints. A gait progression prediction
> algorithm determines the actuation angle index for the prosthetic knee motor,
> ultimately defining the necessary thigh and knee angles and gait progression.
> Results show that when the standard deviation of Gaussian noise added to the
> thigh angle data is less than 1, the method can effectively eliminate noise
> interference, achieving 100\% accuracy in gait phase estimation under 150 Hz,
> with thigh angle prediction error being 8.71\% and knee angle prediction error
> being 6.78\%. These findings demonstrate the method's ability to accurately
> predict gait progression and joint angles, offering significant practical value
> for obstacle negotiation in powered transfemoral prosthetics.

