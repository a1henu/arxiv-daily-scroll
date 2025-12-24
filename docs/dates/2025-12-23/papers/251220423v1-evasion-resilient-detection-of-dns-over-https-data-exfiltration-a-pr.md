---
layout: default
title: Evasion-Resilient Detection of DNS-over-HTTPS Data Exfiltration: A Practical Evaluation and Toolkit
---

# Evasion-Resilient Detection of DNS-over-HTTPS Data Exfiltration: A Practical Evaluation and Toolkit
**arXiv**：[2512.20423v1](https://arxiv.org/abs/2512.20423) · [PDF](https://arxiv.org/pdf/2512.20423.pdf)  
**作者**：Adam Elaoumari  

**一句话要点**：提出容器化工具包以评估DNS-over-HTTPS数据外泄检测的规避策略与性能

**关键词**：DNS-over-HTTPS检测, 数据外泄评估, 机器学习分类, 容器化工具包, 规避策略分析

## 3 点简述
- 核心问题：评估DNS-over-HTTPS文件外泄的检测能力及攻击者规避策略的有效性
- 方法要点：构建端到端容器化管道，支持可配置外泄生成与特征提取，集成机器学习与阈值检测对比
- 实验或效果：在公开数据集上训练分类器，并在规避场景下进行基准测试，提供可复现工具包

## 摘要（原文）

> The purpose of this project is to assess how well defenders can detect DNS-over-HTTPS (DoH) file exfiltration, and which evasion strategies can be used by attackers. While providing a reproducible toolkit to generate, intercept and analyze DoH exfiltration, and comparing Machine Learning vs threshold-based detection under adversarial scenarios. The originality of this project is the introduction of an end-to-end, containerized pipeline that generates configurable file exfiltration over DoH using several parameters (e.g., chunking, encoding, padding, resolver rotation). It allows for file reconstruction at the resolver side, while extracting flow-level features using a fork of DoHLyzer. The pipeline contains a prediction side, which allows the training of machine learning models based on public labelled datasets and then evaluates them side-by-side with threshold-based detection methods against malicious and evasive DNS-Over-HTTPS traffic. We train Random Forest, Gradient Boosting and Logistic Regression classifiers on a public DoH dataset and benchmark them against evasive DoH exfiltration scenarios. The toolkit orchestrates traffic generation, file capture, feature extraction, model training and analysis. The toolkit is then encapsulated into several Docker containers for easy setup and full reproducibility regardless of the platform it is run on. Future research regarding this project is directed at validating the results on mixed enterprise traffic, extending the protocol coverage to HTTP/3/QUIC request, adding a benign traffic generation, and working on real-time traffic evaluation. A key objective is to quantify when stealth constraints make DoH exfiltration uneconomical and unworthy for the attacker.

