---
layout: default
title: Predicting Time Pressure of Powered Two-Wheeler Riders for Proactive Safety Interventions
---

# Predicting Time Pressure of Powered Two-Wheeler Riders for Proactive Safety Interventions
**arXiv**：[2601.03173v1](https://arxiv.org/abs/2601.03173) · [PDF](https://arxiv.org/pdf/2601.03173.pdf)  
**作者**：Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil, Subasish Das  

**一句话要点**：提出MotoTimePressure模型预测两轮车骑手时间压力，以支持主动安全干预

**关键词**：时间压力预测, 两轮车安全, 深度学习模型, 多变量时间序列, 主动安全干预, 智能交通系统

## 3 点简述
- 核心问题：时间压力影响两轮车骑手风险行为，但实时预测在智能交通系统中研究不足。
- 方法要点：构建大规模多变量时间序列数据集，结合卷积预处理、双阶段时间注意力和Squeeze-and-Excitation特征重校准的深度学习模型。
- 实验或效果：模型准确率达91.53%，ROC AUC为98.93%，提升碰撞预测性能，支持自适应警报等主动干预措施。

## 摘要（原文）

> Time pressure critically influences risky maneuvers and crash proneness among powered two-wheeler riders, yet its prediction remains underexplored in intelligent transportation systems. We present a large-scale dataset of 129,000+ labeled multivariate time-series sequences from 153 rides by 51 participants under No, Low, and High Time Pressure conditions. Each sequence captures 63 features spanning vehicle kinematics, control inputs, behavioral violations, and environmental context. Our empirical analysis shows High Time Pressure induces 48% higher speeds, 36.4% greater speed variability, 58% more risky turns at intersections, 36% more sudden braking, and 50% higher rear brake forces versus No Time Pressure. To benchmark this dataset, we propose MotoTimePressure, a deep learning model combining convolutional preprocessing, dual-stage temporal attention, and Squeeze-and-Excitation feature recalibration, achieving 91.53% accuracy and 98.93% ROC AUC, outperforming eight baselines. Since time pressure cannot be directly measured in real time, we demonstrate its utility in collision prediction and threshold determination. Using MTPS-predicted time pressure as features, improves Informer-based collision risk accuracy from 91.25% to 93.51%, approaching oracle performance (93.72%). Thresholded time pressure states capture rider cognitive stress and enable proactive ITS interventions, including adaptive alerts, haptic feedback, V2I signaling, and speed guidance, supporting safer two-wheeler mobility under the Safe System Approach.

