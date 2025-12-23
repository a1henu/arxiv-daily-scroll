---
layout: default
title: A Flexible Field-Based Policy Learning Framework for Diverse Robotic Systems and Sensors
---

# A Flexible Field-Based Policy Learning Framework for Diverse Robotic Systems and Sensors
**arXiv**：[2512.19148v1](https://arxiv.org/abs/2512.19148) · [PDF](https://arxiv.org/pdf/2512.19148.pdf)  
**作者**：Jose Gustavo Buenaventura Carreon, Floris Erich, Roman Mykhailyshyn, Tomohiro Motoda, Ryo Hanai, Yukiyasu Domae  

**一句话要点**：提出基于扩散策略和3D语义场景的跨机器人视觉运动学习框架，实现类别级泛化操作。

**关键词**：扩散策略, 3D语义场景表示, 跨机器人泛化, 视觉运动学习, 模块化设计

## 3 点简述
- 核心问题：跨机器人系统与传感器配置的视觉运动学习泛化能力不足。
- 方法要点：结合扩散策略控制与D3Fields的3D语义场景表示，支持模块化设计和统一配置层。
- 实验或效果：在抓取和提升积木任务中，仅100次演示后达到80%成功率，展示平台间技能迁移。

## 摘要（原文）

> We present a cross robot visuomotor learning framework that integrates diffusion policy based control with 3D semantic scene representations from D3Fields to enable category level generalization in manipulation. Its modular design supports diverse robot camera configurations including UR5 arms with Microsoft Azure Kinect arrays and bimanual manipulators with Intel RealSense sensors through a low latency control stack and intuitive teleoperation. A unified configuration layer enables seamless switching between setups for flexible data collection training and evaluation. In a grasp and lift block task the framework achieved an 80 percent success rate after only 100 demonstration episodes demonstrating robust skill transfer between platforms and sensing modalities. This design paves the way for scalable real world studies in cross robotic generalization.

