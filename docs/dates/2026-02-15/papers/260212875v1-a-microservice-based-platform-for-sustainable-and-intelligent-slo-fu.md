---
layout: default
title: A Microservice-Based Platform for Sustainable and Intelligent SLO Fulfilment and Service Management
---

# A Microservice-Based Platform for Sustainable and Intelligent SLO Fulfilment and Service Management
**arXiv**：[2602.12875v1](https://arxiv.org/abs/2602.12875) · [PDF](https://arxiv.org/pdf/2602.12875.pdf)  
**作者**：Juan Luis Herrera, Daniel Wang, Schahram Dustdar  

**一句话要点**：提出CASCA平台以解决计算连续体中微服务SLO与可持续性权衡的隐私保护问题

**关键词**：微服务架构, 服务级别目标, 计算连续体, 可持续计算, 隐私保护, 智能决策系统

## 3 点简述
- 核心问题：微服务在计算连续体中难以平衡性能与可持续性SLO，且需保护开发者隐私
- 方法要点：基于微服务架构的CASCA平台，支持运行时智能重配置服务以达成SLO
- 实验或效果：在真实测试床中，Bash、Rust和Python决策系统成功重配置媒体流服务，隐私得到维护

## 摘要（原文）

> The Microservices Architecture (MSA) design pattern has become a staple for modern applications, allowing functionalities to be divided across fine-grained microservices, fostering reusability, distribution, and interoperability. As MSA-based applications are deployed to the Computing Continuum (CC), meeting their Service Level Objectives (SLOs) becomes a challenge. Trading off performance and sustainability SLOs is especially challenging. This challenge can be addressed with intelligent decision systems, able to reconfigure the services during runtime to meet the SLOs. However, developing these agents while adhering to the MSA pattern is complex, especially because CC providers, who have key know-how and information to fulfill these SLOs, must comply with the privacy requirements of application developers. This work presents the Carbon-Aware SLO and Control plAtform (CASCA), an open-source MSA-based platform that allows CC providers to reconfigure services and fulfill their SLOs while maintaining the privacy of developers. CASCA is architected to be highly reusable, distributable, and easy to use, extend, and modify. CASCA has been evaluated in a real CC testbed for a media streaming service, where decision systems implemented in Bash, Rust, and Python successfully reconfigured the service, unaffected by upholding privacy.

