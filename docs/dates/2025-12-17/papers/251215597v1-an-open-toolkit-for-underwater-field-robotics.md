---
layout: default
title: An Open Toolkit for Underwater Field Robotics
---

# An Open Toolkit for Underwater Field Robotics
**arXiv**：[2512.15597v1](https://arxiv.org/abs/2512.15597) · [PDF](https://arxiv.org/pdf/2512.15597.pdf)  
**作者**：Giacomo Picardi, Saverio Iacoponi, Matias Carandell, Jorge Aguirregomezcorta, Mrudul Chellapurath, Joaquin del Rio, Marcello Calisti, Iacopo Aguzzi  

**一句话要点**：提出开源水下机器人操作工具包以解决水下操纵系统开发成本高、模块化不足的问题

**关键词**：水下机器人, 开源硬件, 水下操纵, ROS2, 模块化设计, 现场测试

## 3 点简述
- 核心问题：水下机器人操作研究面临高成本、专有设计限制和模块化硬件缺乏，导致开发周期长、可重复性差
- 方法要点：提供深度额定水下机器人关节、紧凑电子控制和基于ROS2的软件栈，所有设计文件开源，支持本地制造和修改
- 实验或效果：经过实验室和现场测试，在40米深度可靠应用于多自由度机械臂、软抓取器和沉积物采样器，验证了鲁棒性和多功能性

## 摘要（原文）

> Underwater robotics is becoming increasingly important for marine science, environmental monitoring, and subsea industrial operations, yet the development of underwater manipulation and actuation systems remains restricted by high costs, proprietary designs, and limited access to modular, research-oriented hardware. While open-source initiatives have democratized vehicle construction and control software, a substantial gap persists for joint-actuated systems-particularly those requiring waterproof, feedback-enabled actuation suitable for manipulators, grippers, and bioinspired devices. As a result, many research groups face lengthy development cycles, limited reproducibility, and difficulty transitioning laboratory prototypes to field-ready platforms.
>   To address this gap, we introduce an open, cost-effective hardware and software toolkit for underwater manipulation research. The toolkit includes a depth-rated Underwater Robotic Joint (URJ) with early leakage detection, compact control and power management electronics, and a ROS2-based software stack for sensing and multi-mode actuation. All CAD models, fabrication files, PCB sources, firmware, and ROS2 packages are openly released, enabling local manufacturing, modification, and community-driven improvement.
>   The toolkit has undergone extensive laboratory testing and multiple field deployments, demonstrating reliable operation up to 40 m depth across diverse applications, including a 3-DoF underwater manipulator, a tendon-driven soft gripper, and an underactuated sediment sampler. These results validate the robustness, versatility, and reusability of the toolkit for real marine environments.
>   By providing a fully open, field-tested platform, this work aims to lower the barrier to entry for underwater manipulation research, improve reproducibility, and accelerate innovation in underwater field robotics.

