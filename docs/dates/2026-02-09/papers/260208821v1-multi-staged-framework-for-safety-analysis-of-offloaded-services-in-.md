---
layout: default
title: Multi-Staged Framework for Safety Analysis of Offloaded Services in Distributed Intelligent Transportation Systems
---

# Multi-Staged Framework for Safety Analysis of Offloaded Services in Distributed Intelligent Transportation Systems
**arXiv**：[2602.08821v1](https://arxiv.org/abs/2602.08821) · [PDF](https://arxiv.org/pdf/2602.08821.pdf)  
**作者**：Robin Dehler, Oliver Schumann, Jona Ruof, Michael Buchholz  

**一句话要点**：提出多阶段安全分析框架以解决分布式智能交通系统中卸载服务的安全性问题

**关键词**：分布式智能交通系统, 服务卸载, 安全分析框架, 面向服务架构, 计算复杂度优化

## 3 点简述
- 核心问题：远程服务数据易受攻击或传输干扰，需确保安全可靠性
- 方法要点：基于面向服务架构，设计多阶段框架验证远程服务与本地数据
- 实验或效果：评估框架性能，比较计算复杂度和检测腐败数据能力

## 摘要（原文）

> The integration of service-oriented architectures (SOA) with function offloading for distributed, intelligent transportation systems (ITS) offers the opportunity for connected autonomous vehicles (CAVs) to extend their locally available services. One major goal of offloading a subset of functions in the processing chain of a CAV to remote devices is to reduce the overall computational complexity on the CAV. The extension of using remote services, however, requires careful safety analysis, since the remotely created data are corrupted more easily, e.g., through an attacker on the remote device or by intercepting the wireless transmission. To tackle this problem, we first analyze the concept of SOA for distributed environments. From this, we derive a safety framework that validates the reliability of remote services and the data received locally. Since it is possible for the autonomous driving task to offload multiple different services, we propose a specific multi-staged framework for safety analysis dependent on the service composition of local and remote services. For efficiency reasons, we directly include the multi-staged framework for safety analysis in our service-oriented function offloading framework (SOFOF) that we have proposed in earlier work. The evaluation compares the performance of the extended framework considering computational complexity, with energy savings being a major motivation for function offloading, and its capability to detect data from corrupted remote services.

