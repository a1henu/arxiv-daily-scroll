---
layout: default
title: Ultrasound-Guided Real-Time Spinal Motion Visualization for Spinal Instability Assessment
---

# Ultrasound-Guided Real-Time Spinal Motion Visualization for Spinal Instability Assessment
**arXiv**：[2602.12917v1](https://arxiv.org/abs/2602.12917) · [PDF](https://arxiv.org/pdf/2602.12917.pdf)  
**作者**：Feng Li, Yuan Bi, Tianyu Song, Zhongliang Jiang, Nassir Navab  

**一句话要点**：提出机器人超声框架，用于实时三维脊柱运动可视化以评估脊柱不稳

**关键词**：脊柱不稳评估, 机器人超声, 三维运动可视化, 配准技术, 实时跟踪, 辐射减少

## 3 点简述
- 核心问题：脊柱不稳诊断依赖动态X射线，但缺乏实时三维运动信息且辐射暴露高。
- 方法要点：结合术前CBCT和机器人超声，通过运动学模型与ICP配准，实现中性至最大弯曲状态的实时运动插值。
- 实验或效果：在3D打印腰椎模型上评估，配准误差约1.94毫米，运动插值误差约2.01毫米。

## 摘要（原文）

> Purpose: Spinal instability is a widespread condition that causes pain, fatigue, and restricted mobility, profoundly affecting patients' quality of life. In clinical practice, the gold standard for diagnosis is dynamic X-ray imaging. However, X-ray provides only 2D motion information, while 3D modalities such as computed tomography (CT) or cone beam computed tomography (CBCT) cannot efficiently capture motion. Therefore, there is a need for a system capable of visualizing real-time 3D spinal motion while minimizing radiation exposure.
>   Methods: We propose ultrasound as an auxiliary modality for 3D spine visualization. Due to acoustic limitations, ultrasound captures only the superficial spinal surface. Therefore, the partially compounded ultrasound volume is registered to preoperative 3D imaging. In this study, CBCT provides the neutral spine configuration, while robotic ultrasound acquisition is performed at maximal spinal bending. A kinematic model is applied to the CBCT-derived spine model for coarse registration, followed by ICP for fine registration, with kinematic parameters optimized based on the registration results. Real-time ultrasound motion tracking is then used to estimate continuous 3D spinal motion by interpolating between the neutral and maximally bent states.
>   Results: The pipeline was evaluated on a bendable 3D-printed lumbar spine phantom. The registration error was $1.941 \pm 0.199$ mm and the interpolated spinal motion error was $2.01 \pm 0.309$ mm (median).
>   Conclusion: The proposed robotic ultrasound framework enables radiation-reduced, real-time 3D visualization of spinal motion, offering a promising 3D alternative to conventional dynamic X-ray imaging for assessing spinal instability.

