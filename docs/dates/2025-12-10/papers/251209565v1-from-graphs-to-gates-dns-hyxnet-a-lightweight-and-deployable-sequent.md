---
layout: default
title: From Graphs to Gates: DNS-HyXNet, A Lightweight and Deployable Sequential Model for Real-Time DNS Tunnel Detection
---

# From Graphs to Gates: DNS-HyXNet, A Lightweight and Deployable Sequential Model for Real-Time DNS Tunnel Detection
**arXiv**：[2512.09565v1](https://arxiv.org/abs/2512.09565) · [PDF](https://arxiv.org/pdf/2512.09565.pdf)  
**作者**：Faraz Ali, Muhammad Afaq, Mahmood Niazi, Muzammil Behzad  

**一句话要点**：提出DNS-HyXNet，一种基于xLSTM的轻量级序列模型，用于实时DNS隧道检测

**关键词**：DNS隧道检测, 序列建模, xLSTM, 实时系统, 轻量级网络, 网络安全

## 3 点简述
- 核心问题：DNS隧道作为隐蔽通信通道，现有图方法如GraphTunnel延迟高，不适合实时部署。
- 方法要点：集成令牌化域名嵌入和数值特征，通过双层xLSTM直接学习序列依赖，避免图重建，实现单阶段多分类。
- 实验或效果：在公开数据集上达到99.99%准确率，检测延迟仅0.041毫秒，验证了实时性和可部署性。

## 摘要（原文）

> Domain Name System (DNS) tunneling remains a covert channel for data exfiltration and command-and-control communication. Although graph-based methods such as GraphTunnel achieve strong accuracy, they introduce significant latency and computational overhead due to recursive parsing and graph construction, limiting their suitability for real-time deployment. This work presents DNS-HyXNet, a lightweight extended Long Short-Term Memory (xLSTM) hybrid framework designed for efficient sequence-based DNS tunnel detection. DNS-HyXNet integrates tokenized domain embeddings with normalized numerical DNS features and processes them through a two-layer xLSTM network that directly learns temporal dependencies from packet sequences, eliminating the need for graph reconstruction and enabling single-stage multi-class classification. The model was trained and evaluated on two public benchmark datasets with carefully tuned hyperparameters to ensure low memory consumption and fast inference. Across all experimental splits of the DNS-Tunnel-Datasets, DNS-HyXNet achieved up to 99.99% accuracy, with macro-averaged precision, recall, and F1-scores exceeding 99.96%, and demonstrated a per-sample detection latency of just 0.041 ms, confirming its scalability and real-time readiness. These results show that sequential modeling with xLSTM can effectively replace computationally expensive recursive graph generation, offering a deployable and energy-efficient alternative for real-time DNS tunnel detection on commodity hardware.

