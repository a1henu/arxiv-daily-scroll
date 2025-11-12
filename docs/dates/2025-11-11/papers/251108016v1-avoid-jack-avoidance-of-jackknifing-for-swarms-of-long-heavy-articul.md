---
layout: default
title: AVOID-JACK: Avoidance of Jackknifing for Swarms of Long Heavy Articulated Vehicles
---

# AVOID-JACK: Avoidance of Jackknifing for Swarms of Long Heavy Articulated Vehicles
**arXiv**：[2511.08016v1](https://arxiv.org/abs/2511.08016) · [PDF](https://arxiv.org/pdf/2511.08016.pdf)  
**作者**：Adrian Schönnagel, Michael Dubé, Christoph Steup, Felix Keppler, Sanaz Mostaghim  

**一句话要点**：提出去中心化群智方法以避免长重型铰接车辆的折叠与碰撞

**关键词**：群机器人学, 铰接车辆控制, 折叠避免, 去中心化控制, 反应式策略, 仿真验证

## 3 点简述
- 核心问题：长重型铰接车辆在群控中易折叠和相互碰撞，现有研究未解决
- 方法要点：采用纯反应式去中心化群智策略，专为长铰接车辆自动化设计
- 实验效果：单车辆折叠避免率达99.8%，多车辆交互中碰撞避免率达99.7%

## 摘要（原文）

> This paper presents a novel approach to avoiding jackknifing and mutual collisions in Heavy Articulated Vehicles (HAVs) by leveraging decentralized swarm intelligence. In contrast to typical swarm robotics research, our robots are elongated and exhibit complex kinematics, introducing unique challenges. Despite its relevance to real-world applications such as logistics automation, remote mining, airport baggage transport, and agricultural operations, this problem has not been addressed in the existing literature.
>   To tackle this new class of swarm robotics problems, we propose a purely reaction-based, decentralized swarm intelligence strategy tailored to automate elongated, articulated vehicles. The method presented in this paper prioritizes jackknifing avoidance and establishes a foundation for mutual collision avoidance. We validate our approach through extensive simulation experiments and provide a comprehensive analysis of its performance. For the experiments with a single HAV, we observe that for 99.8% jackknifing was successfully avoided and that 86.7% and 83.4% reach their first and second goals, respectively. With two HAVs interacting, we observe 98.9%, 79.4%, and 65.1%, respectively, while 99.7% of the HAVs do not experience mutual collisions.

