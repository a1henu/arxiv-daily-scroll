---
layout: default
title: Design and Implementation of a High-Precision Wind-Estimation UAV with Onboard Sensors
---

# Design and Implementation of a High-Precision Wind-Estimation UAV with Onboard Sensors
**arXiv**：[2512.10428v1](https://arxiv.org/abs/2512.10428) · [PDF](https://arxiv.org/pdf/2512.10428.pdf)  
**作者**：Haowen Yu, Na Fan, Xing Liu, Ximin Lyu  

**一句话要点**：提出基于机载传感器的高精度风估计方法，用于无人机实时风向量估计。

**关键词**：无人机风估计, 扰动观测器, 薄板样条模型, 机载传感器, 气动增强, 实时估计

## 3 点简述
- 核心问题：传统风估计方法依赖外部传感器或简化动力学，限制在敏捷飞行或资源受限平台的应用。
- 方法要点：使用扰动观测器估计气动力，并通过薄板样条模型映射到风向量，结合定制风桶增强气动敏感性。
- 实验或效果：在风洞、室内外飞行实验中验证，速度RMSE低至0.06 m/s，方向RMSE低于7.3°，优于基线并提供垂直风估计。

## 摘要（原文）

> Accurate real-time wind vector estimation is essential for enhancing the safety, navigation accuracy, and energy efficiency of unmanned aerial vehicles (UAVs). Traditional approaches rely on external sensors or simplify vehicle dynamics, which limits their applicability during agile flight or in resource-constrained platforms. This paper proposes a real-time wind estimation method based solely on onboard sensors. The approach first estimates external aerodynamic forces using a disturbance observer (DOB), and then maps these forces to wind vectors using a thin-plate spline (TPS) model. A custom-designed wind barrel mounted on the UAV enhances aerodynamic sensitivity, further improving estimation accuracy. The system is validated through comprehensive experiments in wind tunnels, indoor and outdoor flights. Experimental results demonstrate that the proposed method achieves consistently high-accuracy wind estimation across controlled and real-world conditions, with speed RMSEs as low as \SI{0.06}{m/s} in wind tunnel tests, \SI{0.22}{m/s} during outdoor hover, and below \SI{0.38}{m/s} in indoor and outdoor dynamic flights, and direction RMSEs under \ang{7.3} across all scenarios, outperforming existing baselines. Moreover, the method provides vertical wind estimates -- unavailable in baselines -- with RMSEs below \SI{0.17}{m/s} even during fast indoor translations.

