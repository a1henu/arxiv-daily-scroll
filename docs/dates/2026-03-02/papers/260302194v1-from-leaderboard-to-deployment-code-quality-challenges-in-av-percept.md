---
layout: default
title: From Leaderboard to Deployment: Code Quality Challenges in AV Perception Repositories
---

# From Leaderboard to Deployment: Code Quality Challenges in AV Perception Repositories
**arXiv**：[2603.02194v1](https://arxiv.org/abs/2603.02194) · [PDF](https://arxiv.org/pdf/2603.02194.pdf)  
**作者**：Mateus Karvat, Bram Adams, Sidney Givigi  

**一句话要点**：提出首个大规模实证研究，分析自动驾驶感知代码质量以弥合研究到部署的差距

**关键词**：自动驾驶感知, 代码质量分析, 静态分析, 生产就绪性, 安全漏洞, 持续集成

## 3 点简述
- 核心问题：自动驾驶感知模型仅关注基准性能，忽视代码质量、生产就绪性和长期维护性，导致研究卓越与安全关键部署间存在显著差距。
- 方法要点：使用静态分析工具（Pylint、Bandit、Radon）系统评估178个KITTI和NuScenes 3D目标检测模型，分析代码错误、安全漏洞、可维护性和开发实践。
- 实验或效果：仅7.3%仓库满足基本生产就绪标准，安全漏洞高度集中，持续集成/持续部署管道与更好代码可维护性相关，提出可操作指南以改进质量与安全。

## 摘要（原文）

> Autonomous vehicle (AV) perception models are typically evaluated solely on benchmark performance metrics, with limited attention to code quality, production readiness and long-term maintainability. This creates a significant gap between research excellence and real-world deployment in safety-critical systems subject to international safety standards. To address this gap, we present the first large-scale empirical study of software quality in AV perception repositories, systematically analyzing 178 unique models from the KITTI and NuScenes 3D Object Detection leaderboards. Using static analysis tools (Pylint, Bandit, and Radon), we evaluated code errors, security vulnerabilities, maintainability, and development practices. Our findings revealed that only 7.3% of the studied repositories meet basic production-readiness criteria, defined as having zero critical errors and no high-severity security vulnerabilities. Security issues are highly concentrated, with the top five issues responsible for almost 80% of occurrences, which prompted us to develop a set of actionable guidelines to prevent them. Additionally, the adoption of Continuous Integration/Continuous Deployment pipelines was correlated with better code maintainability. Our findings highlight that leaderboard performance does not reflect production readiness and that targeted interventions could substantially improve the quality and safety of AV perception code.

