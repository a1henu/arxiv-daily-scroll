---
layout: default
title: Contingency Model-based Control (CMC) for Communicationless Cooperative Collision Avoidance in Robot Swarms
---

# Contingency Model-based Control (CMC) for Communicationless Cooperative Collision Avoidance in Robot Swarms
**arXiv**：[2512.20391v1](https://arxiv.org/abs/2512.20391) · [PDF](https://arxiv.org/pdf/2512.20391.pdf)  
**作者**：Georg Schildbach  

**一句话要点**：提出基于应急模型的通信无感控制方法，以解决机器人集群中的协同避碰问题。

**关键词**：机器人集群, 协同避碰, 通信无感控制, 应急模型, 隐式合作, 即插即用

## 3 点简述
- 核心问题：去中心化机器人集群中，无线通信脆弱性（如延迟、丢包）影响协同避碰可靠性。
- 方法要点：采用隐式合作范式，基于离线共识规则定义应急轨迹和互避约束，确保递归可行性和避碰。
- 实验或效果：数值模拟验证避碰保证有效，集群运行平滑，并支持即插即用新机器人加入。

## 摘要（原文）

> Cooperative collision avoidance between robots in swarm operations remains an open challenge. Assuming a decentralized architecture, each robot is responsible for making its own control decisions, including motion planning. To this end, most existing approaches mostly rely some form of (wireless) communication between the agents of the swarm. In reality, however, communication is brittle. It may be affected by latency, further delays and packet losses, transmission faults, and is subject to adversarial attacks, such as jamming or spoofing. This paper proposes Contingency Model-based Control (CMC) as a communicationless alternative. It follows the implicit cooperation paradigm, under which the design of the robots is based on consensual (offline) rules, similar to traffic rules. They include the definition of a contingency trajectory for each robot, and a method for construction of mutual collision avoidance constraints. The setup is shown to guarantee the recursive feasibility and collision avoidance between all swarm members in closed-loop operation. Moreover, CMC naturally satisfies the Plug \& Play paradigm, i.e., for new robots entering the swarm. Two numerical examples demonstrate that the collision avoidance guarantee is intact and that the robot swarm operates smoothly under the CMC regime.

