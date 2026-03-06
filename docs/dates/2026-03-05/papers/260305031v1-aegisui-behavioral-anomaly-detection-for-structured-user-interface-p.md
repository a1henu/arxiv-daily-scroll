---
layout: default
title: AegisUI: Behavioral Anomaly Detection for Structured User Interface Protocols in AI Agent Systems
---

# AegisUI: Behavioral Anomaly Detection for Structured User Interface Protocols in AI Agent Systems
**arXiv**：[2603.05031v1](https://arxiv.org/abs/2603.05031) · [PDF](https://arxiv.org/pdf/2603.05031.pdf)  
**作者**：Mohd Safwan Uddin, Saba Hajira  

**一句话要点**：提出AegisUI框架以检测AI代理系统中结构化UI协议的行为异常

**关键词**：行为异常检测, 结构化UI协议, AI代理系统, 随机森林, 自编码器, 安全框架

## 3 点简述
- 核心问题：AI代理动态构建UI时，结构化协议负载可能通过语法检查但隐藏恶意行为，如钓鱼界面或数据泄露。
- 方法要点：框架生成UI负载、注入攻击、提取18个特征，并比较三种异常检测器（随机森林、自编码器、隔离森林）。
- 实验或效果：在4000个标记负载上，随机森林表现最佳（准确率0.931，F1分数0.843），自编码器无需恶意标签训练，适用于新系统部署。

## 摘要（原文）

> AI agents that build user interfaces on the fly assembling buttons, forms, and data displays from structured protocol payloads are becoming common in production systems. The trouble is that a payload can pass every schema check and still trick a user: a button might say "View invoice" while its hidden action wipes an account, or a display widget might quietly bind to an internal salary field. Current defenses stop at syntax; they were never built to catch this kind of behavioral mismatch.
>   We built AegisUI to study exactly this gap. The framework generates structured UI payloads, injects realistic attacks into them, extracts numeric features, and benchmarks anomaly detectors end-to-end. We produced 4000 labeled payloads (3000 benign, 1000 malicious) spanning five application domains and five attack families: phishing interfaces, data leakage, layout abuse, manipulative UI, and workflow anomalies.
>   From each payload we extracted 18 features covering structural, semantic, binding, and session dimensions, then compared three detectors: Isolation Forest (unsupervised), a benign-trained autoencoder (semi-supervised), and Random Forest (supervised). On a stratified 80/20 split, Random Forest scored best overall (accuracy 0.931, precision 0.980, recall 0.740, F1 0.843, ROC-AUC 0.952). The autoencoder came second (F1 0.762, ROC-AUC 0.863) and needs no malicious labels at training time, which matters when deploying a new system that lacks attack history. Per-attack-type analysis showed that layout abuse is easiest to catch while manipulative UI payloads are hardest. All code, data, and configurations are released for full reproducibility.

