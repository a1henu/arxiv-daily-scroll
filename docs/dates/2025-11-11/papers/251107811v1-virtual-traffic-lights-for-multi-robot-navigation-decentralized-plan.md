---
layout: default
title: Virtual Traffic Lights for Multi-Robot Navigation: Decentralized Planning with Centralized Conflict Resolution
---

# Virtual Traffic Lights for Multi-Robot Navigation: Decentralized Planning with Centralized Conflict Resolution
**arXiv**：[2511.07811v1](https://arxiv.org/abs/2511.07811) · [PDF](https://arxiv.org/pdf/2511.07811.pdf)  
**作者**：Sagar Gupta, Thanh Vinh Nguyen, Thieu Long Phan, Vidul Attri, Archit Gupta, Niroshinie Fernando, Kevin Lee, Seng W. Loke, Ronny Kutadinata, Benjamin Champion, Akansel Cosgun  

**一句话要点**：提出混合多机器人协调框架，结合分散路径规划与集中冲突解决以提高导航成功率

**关键词**：多机器人导航, 分散规划, 集中冲突解决, 虚拟交通灯, 死锁避免

## 3 点简述
- 核心问题：多机器人导航中潜在冲突导致死锁和效率低下
- 方法要点：机器人自主规划路径，集中系统检测冲突并发出停止指令
- 实验或效果：仿真和真实实验显示成功率高、死锁减少

## 摘要（原文）

> We present a hybrid multi-robot coordination framework that combines decentralized path planning with centralized conflict resolution. In our approach, each robot autonomously plans its path and shares this information with a centralized node. The centralized system detects potential conflicts and allows only one of the conflicting robots to proceed at a time, instructing others to stop outside the conflicting area to avoid deadlocks. Unlike traditional centralized planning methods, our system does not dictate robot paths but instead provides stop commands, functioning as a virtual traffic light. In simulation experiments with multiple robots, our approach increased the success rate of robots reaching their goals while reducing deadlocks. Furthermore, we successfully validated the system in real-world experiments with two quadruped robots and separately with wheeled Duckiebots.

