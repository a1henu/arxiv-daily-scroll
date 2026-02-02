---
layout: default
title: Trackly: A Unified SaaS Platform for User Behavior Analytics and Real Time Rule Based Anomaly Detection
---

# Trackly: A Unified SaaS Platform for User Behavior Analytics and Real Time Rule Based Anomaly Detection
**arXiv**：[2601.22800v1](https://arxiv.org/abs/2601.22800) · [PDF](https://arxiv.org/pdf/2601.22800.pdf)  
**作者**：Md Zahurul Haque, Md. Hafizur Rahman, Yeahyea Sarker  

**一句话要点**：提出Trackly统一SaaS平台，整合用户行为分析与实时规则异常检测以解决产品与安全数据割裂问题。

**关键词**：用户行为分析, 实时异常检测, 规则引擎, SaaS平台, 微服务架构, 风险评分

## 3 点简述
- 核心问题：产品分析和安全监控分离导致数据碎片化和威胁检测延迟。
- 方法要点：通过轻量级SDK和REST API收集会话、地理位置、设备指纹等数据，基于可配置规则进行加权风险评分。
- 实验或效果：在合成数据集上实现98.1%准确率、97.7%精确率和2.25%误报率，证明对中小企业和电商有效。

## 摘要（原文）

> Understanding user behavior is essential for improving digital experiences, optimizing business conversions, and mitigating threats like account takeovers, fraud, and bot attacks. Most platforms separate product analytics and security, creating fragmented visibility and delayed threat detection. Trackly, a scalable SaaS platform, unifies comprehensive user behavior analytics with real time, rule based anomaly detection. It tracks sessions, IP based geo location, device browser fingerprints, and granular events such as page views, add to cart, and checkouts. Suspicious activities logins from new devices or locations, impossible travel (Haversine formula), rapid bot like actions, VPN proxy usage, or multiple accounts per IP are flagged via configurable rules with weighted risk scoring, enabling transparent, explainable decisions. A real time dashboard provides global session maps, DAU MAU, bounce rates, and session durations. Integration is simplified with a lightweight JavaScript SDK and secure REST APIs. Implemented on a multi tenant microservices stack (ASP.NET Core, MongoDB, RabbitMQ, Next.js), Trackly achieved 98.1% accuracy, 97.7% precision, and 2.25% false positives on synthetic datasets, proving its efficiency for SMEs and ecommerce.

