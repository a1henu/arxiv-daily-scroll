---
layout: default
title: Evaluating Federated Learning for Cross-Country Mood Inference from Smartphone Sensing Data
---

# Evaluating Federated Learning for Cross-Country Mood Inference from Smartphone Sensing Data
**arXiv**：[2602.15478v1](https://arxiv.org/abs/2602.15478) · [PDF](https://arxiv.org/pdf/2602.15478.pdf)  
**作者**：Sharmad Kalpande, Saurabh Shirke, Haroon R. Lone  

**一句话要点**：提出FedFAP框架，在跨国家联邦学习场景中解决基于智能手机感知的情绪推断问题。

**关键词**：联邦学习, 情绪推断, 智能手机感知, 个性化学习, 隐私保护, 跨国家分析

## 3 点简述
- 核心问题：传统情绪评估依赖不频繁的回顾性报告，难以捕捉情绪不稳定的连续性，且大规模部署面临隐私、感知可用性和行为模式变异等挑战。
- 方法要点：引入FedFAP，一种特征感知的个性化联邦框架，旨在适应不同地区的异构感知模态，支持各国作为独立客户端保留本地数据。
- 实验或效果：在跨地理和文化多样人群的评估中，FedFAP达到AUROC 0.744，优于集中式方法和现有个性化联邦基线，为情绪感知系统提供设计洞见。

## 摘要（原文）

> Mood instability is a key behavioral indicator of mental health, yet traditional assessments rely on infrequent and retrospective reports that fail to capture its continuous nature. Smartphone-based mobile sensing enables passive, in-the-wild mood inference from everyday behaviors; however, deploying such systems at scale remains challenging due to privacy constraints, uneven sensing availability, and substantial variability in behavioral patterns.
>   In this work, we study mood inference using smartphone sensing data in a cross-country federated learning setting, where each country participates as an independent client while retaining local data. We introduce FedFAP, a feature-aware personalized federated framework designed to accommodate heterogeneous sensing modalities across regions. Evaluations across geographically and culturally diverse populations show that FedFAP achieves an AUROC of 0.744, outperforming both centralized approaches and existing personalized federated baselines. Beyond inference, our results offer design insights for mood-aware systems, demonstrating how population-aware personalization and privacy-preserving learning can enable scalable and mood-aware mobile sensing technologies.

