---
layout: default
title: A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting
---

# A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting
**arXiv**：[2601.03200v1](https://arxiv.org/abs/2601.03200) · [PDF](https://arxiv.org/pdf/2601.03200.pdf)  
**作者**：Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  

**一句话要点**：提出基于3D高斯溅射的高保真数字孪生框架，以快速构建机器人操作场景并支持真实世界执行。

**关键词**：数字孪生, 3D高斯溅射, 机器人操作, 语义融合, 几何转换, 仿真到真实迁移

## 3 点简述
- 现有数字孪生方法重建慢、视觉保真度低，且难以将逼真模型转换为规划就绪的碰撞几何。
- 采用3D高斯溅射进行快速逼真重建，结合可见性感知语义融合和基于滤波的几何转换方法。
- 在Franka Emika Panda机器人拾放任务实验中，增强的几何精度有效支持了真实世界中的稳健操作。

## 摘要（原文）

> Developing high-fidelity, interactive digital twins is crucial for enabling closed-loop motion planning and reliable real-world robot execution, which are essential to advancing sim-to-real transfer. However, existing approaches often suffer from slow reconstruction, limited visual fidelity, and difficulties in converting photorealistic models into planning-ready collision geometry. We present a practical framework that constructs high-quality digital twins within minutes from sparse RGB inputs. Our system employs 3D Gaussian Splatting (3DGS) for fast, photorealistic reconstruction as a unified scene representation. We enhance 3DGS with visibility-aware semantic fusion for accurate 3D labelling and introduce an efficient, filter-based geometry conversion method to produce collision-ready models seamlessly integrated with a Unity-ROS2-MoveIt physics engine. In experiments with a Franka Emika Panda robot performing pick-and-place tasks, we demonstrate that this enhanced geometric accuracy effectively supports robust manipulation in real-world trials. These results demonstrate that 3DGS-based digital twins, enriched with semantic and geometric consistency, offer a fast, reliable, and scalable path from perception to manipulation in unstructured environments.

