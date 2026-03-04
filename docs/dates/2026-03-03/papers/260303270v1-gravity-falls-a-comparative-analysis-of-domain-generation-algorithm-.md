---
layout: default
title: Gravity Falls: A Comparative Analysis of Domain-Generation Algorithm (DGA) Detection Methods for Mobile Device Spearphishing
---

# Gravity Falls: A Comparative Analysis of Domain-Generation Algorithm (DGA) Detection Methods for Mobile Device Spearphishing
**arXiv**：[2603.03270v1](https://arxiv.org/abs/2603.03270) · [PDF](https://arxiv.org/pdf/2603.03270.pdf)  
**作者**：Adam Dorian Wong, John D. Hastings  

**一句话要点**：提出Gravity Falls数据集以评估DGA检测方法在移动设备鱼叉式短信钓鱼中的泛化能力

**关键词**：域名生成算法检测, 移动设备安全, 短信钓鱼, 机器学习评估, 威胁演化分析, 半合成数据集

## 3 点简述
- 核心问题：现有DGA检测研究多关注恶意软件C2和邮件钓鱼，缺乏对移动设备短信钓鱼中DGA战术泛化性的评估。
- 方法要点：构建半合成数据集Gravity Falls，涵盖2022至2025年短信钓鱼链接，分析威胁演员从随机字符串到字典拼接和主题组合抢注的演变。
- 实验或效果：评估传统启发式和机器学习检测器，结果显示性能高度依赖战术，随机字符串检测效果最佳，但其他战术召回率低，现有方法不适应持续演变的DGA战术。

## 摘要（原文）

> Mobile devices are frequent targets of eCrime threat actors through SMS spearphishing (smishing) links that leverage Domain Generation Algorithms (DGA) to rotate hostile infrastructure. Despite this, DGA research and evaluation largely emphasize malware C2 and email phishing datasets, leaving limited evidence on how well detectors generalize to smishing-driven domain tactics outside enterprise perimeters. This work addresses that gap by evaluating traditional and machine-learning DGA detectors against Gravity Falls, a new semi-synthetic dataset derived from smishing links delivered between 2022 and 2025. Gravity Falls captures a single threat actor's evolution across four technique clusters, shifting from short randomized strings to dictionary concatenation and themed combo-squatting variants used for credential theft and fee/fine fraud. Two string-analysis approaches (Shannon entropy and Exp0se) and two ML-based detectors (an LSTM classifier and COSSAS DGAD) are assessed using Top-1M domains as benign baselines. Results are strongly tactic-dependent: performance is highest on randomized-string domains but drops on dictionary concatenation and themed combo-squatting, with low recall across multiple tool/cluster pairings. Overall, both traditional heuristics and recent ML detectors are ill-suited for consistently evolving DGA tactics observed in Gravity Falls, motivating more context-aware approaches and providing a reproducible benchmark for future evaluation.

