---
layout: default
title: OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security
---

# OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security
**arXiv**：[2603.08566v1](https://arxiv.org/abs/2603.08566) · [PDF](https://arxiv.org/pdf/2603.08566.pdf)  
**作者**：Andrew Chin, Dongkwan Kim, Yu-Fu Fu, Fabian Fleischer, Youngjoon Kim, HyungSeok Han, Cen Zhang, Brian Junekyu Lee, Hanqing Zhao, Taesoo Kim  

**一句话要点**：提出OSS-CRS框架，以解决开源网络推理系统在现实世界部署中的可用性问题。

**关键词**：网络推理系统, 开源安全, 本地部署框架, 漏洞发现, 资源管理, AIxCC竞赛

## 3 点简述
- 核心问题：现有AIxCC竞赛开源网络推理系统依赖已不存在的云基础设施，难以在外部部署使用。
- 方法要点：开发开放、本地可部署框架，支持预算感知资源管理，整合多种网络推理技术。
- 实验或效果：移植冠军系统Atlantis，在8个OSS-Fuzz项目中发现了10个未知漏洞，包括3个高严重性漏洞。

## 摘要（原文）

> DARPA's AI Cyber Challenge (AIxCC) showed that cyber reasoning systems (CRSs) can go beyond vulnerability discovery to autonomously confirm and patch bugs: seven teams built such systems and open-sourced them after the competition. Yet all seven open-sourced CRSs remain largely unusable outside their original teams, each bound to the competition cloud infrastructure that no longer exists. We present OSS-CRS, an open, locally deployable framework for running and combining CRS techniques against real-world open-source projects, with budget-aware resource management. We ported the first-place system (Atlantis) and discovered 10 previously unknown bugs (three of high severity) across 8 OSS-Fuzz projects. OSS-CRS is publicly available.

