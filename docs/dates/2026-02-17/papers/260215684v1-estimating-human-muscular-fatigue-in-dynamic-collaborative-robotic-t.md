---
layout: default
title: Estimating Human Muscular Fatigue in Dynamic Collaborative Robotic Tasks with Learning-Based Models
---

# Estimating Human Muscular Fatigue in Dynamic Collaborative Robotic Tasks with Learning-Based Models
**arXiv**：[2602.15684v1](https://arxiv.org/abs/2602.15684) · [PDF](https://arxiv.org/pdf/2602.15684.pdf)  
**作者**：Feras Kiki, Pouya P. Niaz, Alireza Madani, Cagatay Basdogan  

**一句话要点**：提出基于学习模型的框架，通过sEMG估计动态人机协作任务中的人类肌肉疲劳，以优化安全与性能。

**关键词**：人机协作, 肌肉疲劳估计, 表面肌电图, 机器学习回归, 卷积神经网络, 疲劳自适应控制

## 3 点简述
- 核心问题：评估动态人机协作中的人类肌肉疲劳，以提升操作者安全和系统性能。
- 方法要点：使用臂戴sEMG，结合频域和时域特征，通过机器学习回归模型和CNN预测疲劳周期分数。
- 实验或效果：在十名参与者实验中，CNN平均RMSE最低为20.8%，模型在未训练运动模式中表现出良好泛化能力。

## 摘要（原文）

> Assessing human muscle fatigue is critical for optimizing performance and safety in physical human-robot interaction(pHRI). This work presents a data-driven framework to estimate fatigue in dynamic, cyclic pHRI using arm-mounted surface electromyography(sEMG). Subject-specific machine-learning regression models(Random Forest, XGBoost, and Linear Regression predict the fraction of cycles to fatigue(FCF) from three frequency-domain and one time-domain EMG features, and are benchmarked against a convolutional neural network(CNN) that ingests spectrograms of filtered EMG. Framing fatigue estimation as regression (rather than classification) captures continuous progression toward fatigue, supporting earlier detection, timely intervention, and adaptive robot control. In experiments with ten participants, a collaborative robot under admittance control guided repetitive lateral (left-right) end-effector motions until muscular fatigue. Average FCF RMSE across participants was 20.8+/-4.3% for the CNN, 23.3+/-3.8% for Random Forest, 24.8+/-4.5% for XGBoost, and 26.9+/-6.1% for Linear Regression. To probe cross-task generalization, one participant additionally performed unseen vertical (up-down) and circular repetitions; models trained only on lateral data were tested directly and largely retained accuracy, indicating robustness to changes in movement direction, arm kinematics, and muscle recruitment, while Linear Regression deteriorated. Overall, the study shows that both feature-based ML and spectrogram-based DL can estimate remaining work capacity during repetitive pHRI, with the CNN delivering the lowest error and the tree-based models close behind. The reported transfer to new motion patterns suggests potential for practical fatigue monitoring without retraining for every task, improving operator protection and enabling fatigue-aware shared autonomy, for safer fatigue-adaptive pHRI control.

