---
layout: default
title: Safe-ROS: An Architecture for Autonomous Robots in Safety-Critical Domains
---

# Safe-ROS: An Architecture for Autonomous Robots in Safety-Critical Domains
**arXiv**：[2511.14433v1](https://arxiv.org/abs/2511.14433) · [PDF](https://arxiv.org/pdf/2511.14433.pdf)  
**作者**：Diana C. Benjumea, Marie Farrell, Louise A. Dennis  

**一句话要点**：提出Safe-ROS架构以在安全关键领域部署可验证安全的自主机器人

**关键词**：自主机器人, 安全关键系统, 形式化验证, ROS架构, 安全仪表功能

## 3 点简述
- 安全关键领域自主机器人需确保操作有效性和安全合规性
- 架构包含智能控制系统和安全系统，后者使用形式化可验证的安全仪表功能
- 在核环境机器人上验证SIF，通过仿真和测试展示架构有效性

## 摘要（原文）

> Deploying autonomous robots in safety-critical domains requires architectures that ensure operational effectiveness and safety compliance. In this paper, we contribute the Safe-ROS architecture for developing reliable and verifiable autonomous robots in such domains. It features two distinct subsystems: (1) an intelligent control system that is responsible for normal/routine operations, and (2) a Safety System consisting of Safety Instrumented Functions (SIFs) that provide formally verifiable independent oversight. We demonstrate Safe-ROS on an AgileX Scout Mini robot performing autonomous inspection in a nuclear environment. One safety requirement is selected and instantiated as a SIF. To support verification, we implement the SIF as a cognitive agent, programmed to stop the robot whenever it detects that it is too close to an obstacle. We verify that the agent meets the safety requirement and integrate it into the autonomous inspection. This integration is also verified, and the full deployment is validated in a Gazebo simulation, and lab testing. We evaluate this architecture in the context of the UK nuclear sector, where safety and regulation are crucial aspects of deployment. Success criteria include the development of a formal property from the safety requirement, implementation, and verification of the SIF, and the integration of the SIF into the operational robotic autonomous system. Our results demonstrate that the  Safe-ROS architecture can provide safety verifiable oversight while deploying autonomous robots in safety-critical domains, offering a robust framework that can be extended to additional requirements and various applications.

