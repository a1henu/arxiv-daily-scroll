---
layout: default
title: Towards Autonomous Robotic Kidney Ultrasound: Spatial-Efficient Volumetric Imaging via Template Guided Optimal Pivoting
---

# Towards Autonomous Robotic Kidney Ultrasound: Spatial-Efficient Volumetric Imaging via Template Guided Optimal Pivoting
**arXiv**：[2602.16641v1](https://arxiv.org/abs/2602.16641) · [PDF](https://arxiv.org/pdf/2602.16641.pdf)  
**作者**：Xihan Ma, Haichong Zhang  

**一句话要点**：提出模板引导最优枢轴扫描方法，以实现机器人肾脏超声的高效三维成像

**关键词**：机器人超声, 肾脏成像, 三维定位, 模板引导, 最优枢轴扫描, 空间效率

## 3 点简述
- 核心问题：传统自由手超声成像存在操作依赖性和三维定位缺失，机器人系统缺乏高效成像窗口确定方法。
- 方法要点：通过探索性成像注册肾脏模板定位器官，执行固定点枢轴扫描对齐长轴以最小化探头移动。
- 实验或效果：仿真和活体验证显示，60%探索比优化平衡，活体定位精度达7.36毫米和13.84度，探头足迹缩短约75毫米。

## 摘要（原文）

> Medical ultrasound (US) imaging is a frontline tool for the diagnosis of kidney diseases. However, traditional freehand imaging procedure suffers from inconsistent, operator-dependent outcomes, lack of 3D localization information, and risks of work-related musculoskeletal disorders. While robotic ultrasound (RUS) systems offer the potential for standardized, operator-independent 3D kidney data acquisition, the existing scanning methods lack the ability to determine the optimal imaging window for efficient imaging. As a result, the scan is often blindly performed with excessive probe footprint, which frequently leads to acoustic shadowing and incomplete organ coverage. Consequently, there is a critical need for a spatially efficient imaging technique that can maximize the kidney coverage through minimum probe footprint. Here, we propose an autonomous workflow to achieve efficient kidney imaging via template-guided optimal pivoting. The system first performs an explorative imaging to generate partial observations of the kidney. This data is then registered to a kidney template to estimate the organ pose. With the kidney localized, the robot executes a fixed-point pivoting sweep where the imaging plane is aligned with the kidney long axis to minimize the probe translation. The proposed method was validated in simulation and in-vivo. Simulation results indicate that a 60% exploration ratio provides optimal balance between kidney localization accuracy and scanning efficiency. In-vivo evaluation on two male subjects demonstrates a kidney localization accuracy up to 7.36 mm and 13.84 degrees. Moreover, the optimal pivoting approach shortened the probe footprint by around 75 mm when compared with the baselines. These results valid our approach of leveraging anatomical templates to align the probe optimally for volumetric sweep.

