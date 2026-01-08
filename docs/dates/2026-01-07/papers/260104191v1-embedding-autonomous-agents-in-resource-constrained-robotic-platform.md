---
layout: default
title: Embedding Autonomous Agents in Resource-Constrained Robotic Platforms
---

# Embedding Autonomous Agents in Resource-Constrained Robotic Platforms
**arXiv**：[2601.04191v1](https://arxiv.org/abs/2601.04191) · [PDF](https://arxiv.org/pdf/2601.04191.pdf)  
**作者**：Negar Halakou, Juan F. Gutierrez, Ye Sun, Han Jiang, Xueming Wu, Yilun Song, Andres Gomez  

**一句话要点**：在资源受限机器人平台中集成AgentSpeak自主代理以解决迷宫探索问题

**关键词**：自主代理, 资源受限系统, AgentSpeak, 机器人导航, 实时推理

## 3 点简述
- 核心问题：资源受限嵌入式设备在动态环境中需本地决策能力，以减少对外部控制的依赖。
- 方法要点：使用AgentSpeak编程自主代理，集成于双轮机器人，基于传感器数据自主决策探索迷宫。
- 实验或效果：代理在59秒内成功解决迷宫，使用287个推理周期，决策阶段耗时小于1毫秒，表明推理高效适合实时执行。

## 摘要（原文）

> Many embedded devices operate under resource constraints and in dynamic environments, requiring local decision-making capabilities. Enabling devices to make independent decisions in such environments can improve the responsiveness of the system and reduce the dependence on constant external control. In this work, we integrate an autonomous agent, programmed using AgentSpeak, with a small two-wheeled robot that explores a maze using its own decision-making and sensor data. Experimental results show that the agent successfully solved the maze in 59 seconds using 287 reasoning cycles, with decision phases taking less than one millisecond. These results indicate that the reasoning process is efficient enough for real-time execution on resource-constrained hardware. This integration demonstrates how high-level agent-based control can be applied to resource-constrained embedded systems for autonomous operation.

