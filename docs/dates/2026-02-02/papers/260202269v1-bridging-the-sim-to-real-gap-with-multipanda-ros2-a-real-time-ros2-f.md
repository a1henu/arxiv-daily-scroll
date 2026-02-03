---
layout: default
title: Bridging the Sim-to-Real Gap with multipanda ros2: A Real-Time ROS2 Framework for Multimanual Systems
---

# Bridging the Sim-to-Real Gap with multipanda ros2: A Real-Time ROS2 Framework for Multimanual Systems
**arXiv**：[2602.02269v1](https://arxiv.org/abs/2602.02269) · [PDF](https://arxiv.org/pdf/2602.02269.pdf)  
**作者**：Jon Škerlj, Seongjin Bien, Abdeldjallil Naceri, Sami Haddadin  

**一句话要点**：提出multipanda_ros2框架，通过实时控制与高保真仿真解决多机器人系统仿真到现实的差距问题。

**关键词**：多机器人控制, ROS2框架, 实时扭矩控制, 仿真到现实转换, 高保真仿真, 惯性参数识别

## 3 点简述
- 核心问题：多机器人系统在仿真到现实转换中面临实时控制、交互建模和仿真精度不足的挑战。
- 方法要点：基于ROS2开发开源架构，支持1kHz控制频率和≤2ms控制器切换延迟，集成MuJoCo仿真进行动态一致性评估。
- 实验或效果：展示惯性参数识别提升力/扭矩精度，为刚性双臂接触任务提供可复现平台，缩小仿真与现实差距。

## 摘要（原文）

> We present $multipanda\_ros2$, a novel open-source ROS2 architecture for multi-robot control of Franka Robotics robots. Leveraging ros2 control, this framework provides native ROS2 interfaces for controlling any number of robots from a single process. Our core contributions address key challenges in real-time torque control, including interaction control and robot-environment modeling. A central focus of this work is sustaining a 1kHz control frequency, a necessity for real-time control and a minimum frequency required by safety standards. Moreover, we introduce a controllet-feature design pattern that enables controller-switching delays of $\le 2$ ms, facilitating reproducible benchmarking and complex multi-robot interaction scenarios. To bridge the simulation-to-reality (sim2real) gap, we integrate a high-fidelity MuJoCo simulation with quantitative metrics for both kinematic accuracy and dynamic consistency (torques, forces, and control errors). Furthermore, we demonstrate that real-world inertial parameter identification can significantly improve force and torque accuracy, providing a methodology for iterative physics refinement. Our work extends approaches from soft robotics to rigid dual-arm, contact-rich tasks, showcasing a promising method to reduce the sim2real gap and providing a robust, reproducible platform for advanced robotics research.

