---
layout: default
title: Acoustic Drone Package Delivery Detection
---

# Acoustic Drone Package Delivery Detection
**arXiv**：[2602.09991v1](https://arxiv.org/abs/2602.09991) · [PDF](https://arxiv.org/pdf/2602.09991.pdf)  
**作者**：François Marcoux, François Grondin  

**一句话要点**：提出基于声学特征的无人机包裹投递检测算法，用于限制区域安全监控。

**关键词**：无人机检测, 声学信号处理, 包裹投递识别, 麦克风阵列, 深度神经网络, 安全监控

## 3 点简述
- 核心问题：无人机在监狱等限制区域非法投递包裹的安全挑战，现有研究缺乏投递事件识别。
- 方法要点：使用地面麦克风阵列，通过深度神经网络从梅尔频谱图估计螺旋桨转速，分析转速突变检测投递时刻。
- 实验或效果：在150米内螺旋桨转速估计平均绝对误差16 Hz，无人机存在检测准确率97%，投递事件识别率96%，假阳性率8%。

## 摘要（原文）

> In recent years, the illicit use of unmanned aerial vehicles (UAVs) for deliveries in restricted area such as prisons became a significant security challenge. While numerous studies have focused on UAV detection or localization, little attention has been given to delivery events identification. This study presents the first acoustic package delivery detection algorithm using a ground-based microphone array. The proposed method estimates both the drone's propeller speed and the delivery event using solely acoustic features. A deep neural network detects the presence of a drone and estimates the propeller's rotation speed or blade passing frequency (BPF) from a mel spectrogram. The algorithm analyzes the BPFs to identify probable delivery moments based on sudden changes before and after a specific time. Results demonstrate a mean absolute error of the blade passing frequency estimator of 16 Hz when the drone is less than 150 meters away from the microphone array. The drone presence detection estimator has a accuracy of 97%. The delivery detection algorithm correctly identifies 96% of events with a false positive rate of 8%. This study shows that deliveries can be identified using acoustic signals up to a range of 100 meters.

