---
layout: default
title: CAM-LDS: Cyber Attack Manifestations for Automatic Interpretation of System Logs and Security Alerts
---

# CAM-LDS: Cyber Attack Manifestations for Automatic Interpretation of System Logs and Security Alerts
**arXiv**：[2603.04186v1](https://arxiv.org/abs/2603.04186) · [PDF](https://arxiv.org/pdf/2603.04186.pdf)  
**作者**：Max Landauer, Wolfgang Hotwagner, Thorina Boenke, Florian Skopik, Markus Wurzenberger  

**一句话要点**：提出CAM-LDS数据集以支持基于大语言模型的系统日志与安全警报自动解释

**关键词**：日志分析, 网络安全, 大语言模型, 攻击数据集, 自动解释

## 3 点简述
- 核心问题：现有日志分析方法依赖专家规则，缺乏语义理解，且公开标注数据集稀缺。
- 方法要点：构建开源可复现的测试环境，涵盖81种攻击技术，提取攻击执行产生的日志事件。
- 实验或效果：案例研究表明，大语言模型能完美预测约三分之一攻击步骤，展示数据集实用潜力。

## 摘要（原文）

> Log data are essential for intrusion detection and forensic investigations. However, manual log analysis is tedious due to high data volumes, heterogeneous event formats, and unstructured messages. Even though many automated methods for log analysis exist, they usually still rely on domain-specific configurations such as expert-defined detection rules, handcrafted log parsers, or manual feature-engineering. Crucially, the level of automation of conventional methods is limited due to their inability to semantically understand logs and explain their underlying causes. In contrast, Large Language Models enable domain- and format-agnostic interpretation of system logs and security alerts. Unfortunately, research on this topic remains challenging, because publicly available and labeled data sets covering a broad range of attack techniques are scarce. To address this gap, we introduce the Cyber Attack Manifestation Log Data Set (CAM-LDS), comprising seven attack scenarios that cover 81 distinct techniques across 13 tactics and collected from 18 distinct sources within a fully open-source and reproducible test environment. We extract log events that directly result from attack executions to facilitate analysis of manifestations concerning command observability, event frequencies, performance metrics, and intrusion detection alerts. We further present an illustrative case study utilizing an LLM to process the CAM-LDS. The results indicate that correct attack techniques are predicted perfectly for approximately one third of attack steps and adequately for another third, highlighting the potential of LLM-based log interpretation and utility of our data set.

