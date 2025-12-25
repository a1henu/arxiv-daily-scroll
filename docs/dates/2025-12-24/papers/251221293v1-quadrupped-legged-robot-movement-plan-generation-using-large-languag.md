---
layout: default
title: Quadrupped-Legged Robot Movement Plan Generation using Large Language Model
---

# Quadrupped-Legged Robot Movement Plan Generation using Large Language Model
**arXiv**：[2512.21293v1](https://arxiv.org/abs/2512.21293) · [PDF](https://arxiv.org/pdf/2512.21293.pdf)  
**作者**：Muhtadin, Vincentius Gusti Putu A. B. M., Ahmad Zaini, Mauridhi Hery Purnomo, I Ketut Eddy Purnama, Chastine Fatichah  

**一句话要点**：提出基于大语言模型的分布式控制框架，以自然语言指令实现四足机器人导航

**关键词**：四足机器人控制, 大语言模型应用, 分布式架构, 传感器融合, ROS导航

## 3 点简述
- 传统四足机器人控制需专业知识，操作门槛高
- 采用分布式架构，将高层指令处理卸载至外部服务器，结合传感器融合生成ROS命令
- 在结构化室内环境中验证，跨场景成功率超90%

## 摘要（原文）

> Traditional control interfaces for quadruped robots often impose a high barrier to entry, requiring specialized technical knowledge for effective operation. To address this, this paper presents a novel control framework that integrates Large Language Models (LLMs) to enable intuitive, natural language-based navigation. We propose a distributed architecture where high-level instruction processing is offloaded to an external server to overcome the onboard computational constraints of the DeepRobotics Jueying Lite 3 platform. The system grounds LLM-generated plans into executable ROS navigation commands using real-time sensor fusion (LiDAR, IMU, and Odometry). Experimental validation was conducted in a structured indoor environment across four distinct scenarios, ranging from single-room tasks to complex cross-zone navigation. The results demonstrate the system's robustness, achieving an aggregate success rate of over 90\% across all scenarios, validating the feasibility of offloaded LLM-based planning for autonomous quadruped deployment in real-world settings.

