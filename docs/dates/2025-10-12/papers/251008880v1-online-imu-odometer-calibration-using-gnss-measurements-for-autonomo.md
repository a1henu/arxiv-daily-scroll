---
layout: default
title: Online IMU-odometer Calibration using GNSS Measurements for Autonomous Ground Vehicle Localization
---

# Online IMU-odometer Calibration using GNSS Measurements for Autonomous Ground Vehicle Localization
**arXiv**：[2510.08880v1](https://arxiv.org/abs/2510.08880) · [PDF](https://arxiv.org/pdf/2510.08880.pdf)  
**作者**：Baoshan Song, Xiao Xia, Penggao Yan, Yihan Zhong, Weisong Wen, Li-Ta Hsu  

**一句话要点**：提出在线IMU-里程计标定方法，融合GNSS测量以提升自主地面车辆定位精度

**关键词**：自主车辆定位, 传感器标定, 因子图优化, GNSS融合, 在线校准

## 3 点简述
- 核心问题：IMU-里程计内外参标定不准确，影响自主车辆定位精度。
- 方法要点：在可扩展因子图优化框架中，融合IMU、里程计和原始GNSS测量。
- 实验效果：标定后定位最大误差降至17.75米，比松散耦合方法提升71.14%。

## 摘要（原文）

> Accurate calibration of intrinsic (odometer scaling factors) and extrinsic
> parameters (IMU-odometer translation and rotation) is essential for autonomous
> ground vehicle localization. Existing GNSS-aided approaches often rely on
> positioning results or raw measurements without ambiguity resolution, and their
> observability properties remain underexplored. This paper proposes a tightly
> coupled online calibration method that fuses IMU, odometer, and raw GNSS
> measurements (pseudo-range, carrier-phase, and Doppler) within an extendable
> factor graph optimization (FGO) framework, incorporating outlier mitigation and
> ambiguity resolution. Observability analysis reveals that two horizontal
> translation and three rotation parameters are observable under general motion,
> while vertical translation remains unobservable. Simulation and real-world
> experiments demonstrate superior calibration and localization performance over
> state-of-the-art loosely coupled methods. Specifically, the IMU-odometer
> positioning using our calibrated parameters achieves the absolute maximum error
> of 17.75 m while the one of LC method is 61.51 m, achieving up to 71.14 percent
> improvement. To foster further research, we also release the first open-source
> dataset that combines IMU, 2D odometer, and raw GNSS measurements from both
> rover and base stations.

