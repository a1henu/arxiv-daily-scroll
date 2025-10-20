---
layout: default
title: Improved Extended Kalman Filter-Based Disturbance Observers for Exoskeletons
---

# Improved Extended Kalman Filter-Based Disturbance Observers for Exoskeletons
**arXiv**：[2510.15533v1](https://arxiv.org/abs/2510.15533) · [PDF](https://arxiv.org/pdf/2510.15533.pdf)  
**作者**：Shilei Li, Dawei Shi, Makoto Iwasaki, Yan Ning, Hongpeng Zhou, Ling Shi  

**一句话要点**：提出两种改进EKF扰动观测器方法，提升外骨骼在时变交互力下的跟踪精度

**关键词**：扰动观测器, 扩展卡尔曼滤波, 外骨骼控制, 交互多模型, 多核相关熵, 跟踪精度

## 3 点简述
- 核心问题：未知扰动导致机械系统性能下降，且扰动动态未知时无法完美抑制
- 方法要点：引入交互多模型EKF和多核相关熵EKF，优化扰动估计的跟踪速度与不确定性权衡
- 实验效果：相比EKF扰动观测器，髋关节误差分别降低36.3%和16.2%，膝关节误差分别降低46.3%和24.4%

## 摘要（原文）

> The nominal performance of mechanical systems is often degraded by unknown
> disturbances. A two-degree-of-freedom control structure can decouple nominal
> performance from disturbance rejection. However, perfect disturbance rejection
> is unattainable when the disturbance dynamic is unknown. In this work, we
> reveal an inherent trade-off in disturbance estimation subject to tracking
> speed and tracking uncertainty. Then, we propose two novel methods to enhance
> disturbance estimation: an interacting multiple model extended Kalman
> filter-based disturbance observer and a multi-kernel correntropy extended
> Kalman filter-based disturbance observer. Experiments on an exoskeleton verify
> that the proposed two methods improve the tracking accuracy $36.3\%$ and
> $16.2\%$ in hip joint error, and $46.3\%$ and $24.4\%$ in knee joint error,
> respectively, compared to the extended Kalman filter-based disturbance
> observer, in a time-varying interaction force scenario, demonstrating the
> superiority of the proposed method.

