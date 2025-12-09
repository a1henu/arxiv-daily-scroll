---
layout: default
title: Spatiotemporal Calibration and Ground Truth Estimation for High-Precision SLAM Benchmarking in Extended Reality
---

# Spatiotemporal Calibration and Ground Truth Estimation for High-Precision SLAM Benchmarking in Extended Reality
**arXiv**：[2512.07221v1](https://arxiv.org/abs/2512.07221) · [PDF](https://arxiv.org/pdf/2512.07221.pdf)  
**作者**：Zichao Shu, Shitao Bei, Lijun Li, Zetao Chen  

**一句话要点**：提出连续时间最大似然估计器，结合IMU补偿运动捕捉抖动，实现XR中SLAM算法的高精度基准测试。

**关键词**：SLAM基准测试, 时空校准, 运动捕捉抖动补偿, 扩展现实, 连续时间估计, 多传感器融合

## 3 点简述
- 核心问题：运动捕捉系统存在时空校准误差和固有抖动，限制SLAM基准测试精度，影响XR沉浸体验。
- 方法要点：集成IMU数据补偿抖动，提出可变时间同步和基于螺旋同余约束的位姿残差，实现多传感器精确校准。
- 实验或效果：方法优于现有技术，验证了在XR设备和开源SLAM算法基准测试中的实用性和高精度。

## 摘要（原文）

> Simultaneous localization and mapping (SLAM) plays a fundamental role in extended reality (XR) applications. As the standards for immersion in XR continue to increase, the demands for SLAM benchmarking have become more stringent. Trajectory accuracy is the key metric, and marker-based optical motion capture (MoCap) systems are widely used to generate ground truth (GT) because of their drift-free and relatively accurate measurements. However, the precision of MoCap-based GT is limited by two factors: the spatiotemporal calibration with the device under test (DUT) and the inherent jitter in the MoCap measurements. These limitations hinder accurate SLAM benchmarking, particularly for key metrics like rotation error and inter-frame jitter, which are critical for immersive XR experiences. This paper presents a novel continuous-time maximum likelihood estimator to address these challenges. The proposed method integrates auxiliary inertial measurement unit (IMU) data to compensate for MoCap jitter. Additionally, a variable time synchronization method and a pose residual based on screw congruence constraints are proposed, enabling precise spatiotemporal calibration across multiple sensors and the DUT. Experimental results demonstrate that our approach outperforms existing methods, achieving the precision necessary for comprehensive benchmarking of state-of-the-art SLAM algorithms in XR applications. Furthermore, we thoroughly validate the practicality of our method by benchmarking several leading XR devices and open-source SLAM algorithms. The code is publicly available at https://github.com/ylab-xrpg/xr-hpgt.

