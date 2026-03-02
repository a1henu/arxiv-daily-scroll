---
layout: default
title: Evaluating Accuracy of Vine Robot Shape Sensing with Distributed Inertial Measurement Units
---

# Evaluating Accuracy of Vine Robot Shape Sensing with Distributed Inertial Measurement Units
**arXiv**：[2602.24202v1](https://arxiv.org/abs/2602.24202) · [PDF](https://arxiv.org/pdf/2602.24202.pdf)  
**作者**：Alexis E. Laudenslager, Antonio Alvarez Valdivia, Nathaniel Hanson, Margaret McGuinness  

**一句话要点**：评估分布式IMU在藤蔓机器人主动转向下的形状感知精度，量化误差与影响因素。

**关键词**：藤蔓机器人, 形状感知, 分布式IMU, 主动转向, 传感器间距, 误差量化

## 3 点简述
- 核心问题：分布式IMU形状感知在主动转向、变长和不同传感器间距下的精度未系统量化。
- 方法要点：实验评估分布式IMU形状感知，测量IMU漂移和不同条件下的尖端位置误差。
- 实验或效果：被动转向误差11%长度，主动转向16%，生长实验误差8%，传感器间距影响误差最小化。

## 摘要（原文）

> Soft, tip-extending vine robots are well suited for navigating tight, debris-filled environments, making them ideal for urban search and rescue. Sensing the full shape of a vine robot's body is helpful both for localizing information from other sensors placed along the robot body and for determining the robot's configuration within the space being explored. Prior approaches have localized vine robot tips using a single inertial measurement unit (IMU) combined with force sensing or length estimation, while one method demonstrated full-body shape sensing using distributed IMUs on a passively steered robot in controlled maze environments. However, the accuracy of distributed IMU-based shape sensing under active steering, varying robot lengths, and different sensor spacings has not been systematically quantified. In this work, we experimentally evaluate the accuracy of vine robot shape sensing using distributed IMUs along the robot body. We quantify IMU drift, measuring an average orientation drift rate of 1.33 degrees/min across 15 sensors. For passive steering, mean tip position error was 11% of robot length. For active steering, mean tip position error increased to 16%. During growth experiments across lengths from 30-175 cm, mean tip error was 8%, with a positive trend with increasing length. We also analyze the influence of sensor spacing and observe that intermediate spacings can minimize error for single-curvature shapes. These results demonstrate the feasibility of distributed IMU-based shape sensing for vine robots while highlighting key limitations and opportunities for improved modeling and algorithmic integration for field deployment.

