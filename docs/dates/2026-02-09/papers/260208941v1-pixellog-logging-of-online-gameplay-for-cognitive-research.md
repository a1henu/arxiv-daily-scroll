---
layout: default
title: pixelLOG: Logging of Online Gameplay for Cognitive Research
---

# pixelLOG: Logging of Online Gameplay for Cognitive Research
**arXiv**：[2602.08941v1](https://arxiv.org/abs/2602.08941) · [PDF](https://arxiv.org/pdf/2602.08941.pdf)  
**作者**：Zeyu Lu, Dennis L. Barbour  

**一句话要点**：提出pixelLOG框架，用于在Minecraft服务器中收集高分辨率行为数据以支持基于过程的认知研究。

**关键词**：认知研究框架, 行为数据采集, Minecraft服务器, 多代理环境, 高分辨率追踪

## 3 点简述
- 传统认知评估常依赖孤立输出测量，难以捕捉自然情境下的认知复杂性。
- pixelLOG通过主动轮询和被动事件监控，在Spigot服务器上实现高达20+次/秒的数据采集。
- 该框架支持人类和多代理行为追踪，输出结构化JSON，增强生态效度。

## 摘要（原文）

> Traditional cognitive assessments often rely on isolated, output-focused measurements that may fail to capture the complexity of human cognition in naturalistic settings. We present pixelLOG, a high-performance data collection framework for Spigot-based Minecraft servers designed specifically for process-based cognitive research. Unlike existing frameworks tailored only for artificial intelligence agents, pixelLOG also enables human behavioral tracking in multi-player/multi-agent environments. Operating at configurable frequencies up to and exceeding 20 updates per second, the system captures comprehensive behavioral data through a hybrid approach of active state polling and passive event monitoring. By leveraging Spigot's extensible API, pixelLOG facilitates robust session isolation and produces structured JSON outputs integrable with standard analytical pipelines. This framework bridges the gap between decontextualized laboratory assessments and richer, more ecologically valid tasks, enabling high-resolution analysis of cognitive processes as they unfold in complex, virtual environments.

