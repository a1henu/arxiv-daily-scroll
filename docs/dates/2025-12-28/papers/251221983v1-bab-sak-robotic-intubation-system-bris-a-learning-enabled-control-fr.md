---
layout: default
title: Bab_Sak Robotic Intubation System (BRIS): A Learning-Enabled Control Framework for Safe Fiberoptic Endotracheal Intubation
---

# Bab_Sak Robotic Intubation System (BRIS): A Learning-Enabled Control Framework for Safe Fiberoptic Endotracheal Intubation
**arXiv**：[2512.21983v1](https://arxiv.org/abs/2512.21983) · [PDF](https://arxiv.org/pdf/2512.21983.pdf)  
**作者**：Saksham Gupta, Sarthak Mishra, Arshad Ayub, Kamran Farooque, Spandan Roy, Babita Gupta  

**一句话要点**：提出BRIS机器人插管系统，通过学习控制框架实现安全光纤引导气管插管。

**关键词**：机器人插管系统, 学习控制框架, 光纤支气管镜, 深度估计, 气道导航, 临床兼容性

## 3 点简述
- 核心问题：现有机器人插管系统缺乏气管导管推进集成控制和基于隆突的客观深度验证。
- 方法要点：集成四向可操纵光纤支气管镜、独立导管推进机制和摄像头增强口器，采用学习闭环控制框架和单目内窥镜深度估计。
- 实验或效果：在高保真气道模型上验证，展示可靠导航和可控导管放置，支持标准及困难气道配置。

## 摘要（原文）

> Endotracheal intubation is a critical yet technically demanding procedure, with failure or improper tube placement leading to severe complications. Existing robotic and teleoperated intubation systems primarily focus on airway navigation and do not provide integrated control of endotracheal tube advancement or objective verification of tube depth relative to the carina. This paper presents the Robotic Intubation System (BRIS), a compact, human-in-the-loop platform designed to assist fiberoptic-guided intubation while enabling real-time, objective depth awareness. BRIS integrates a four-way steerable fiberoptic bronchoscope, an independent endotracheal tube advancement mechanism, and a camera-augmented mouthpiece compatible with standard clinical workflows. A learning-enabled closed-loop control framework leverages real-time shape sensing to map joystick inputs to distal bronchoscope tip motion in Cartesian space, providing stable and intuitive teleoperation under tendon nonlinearities and airway contact. Monocular endoscopic depth estimation is used to classify airway regions and provide interpretable, anatomy-aware guidance for safe tube positioning relative to the carina. The system is validated on high-fidelity airway mannequins under standard and difficult airway configurations, demonstrating reliable navigation and controlled tube placement. These results highlight BRIS as a step toward safer, more consistent, and clinically compatible robotic airway management.

