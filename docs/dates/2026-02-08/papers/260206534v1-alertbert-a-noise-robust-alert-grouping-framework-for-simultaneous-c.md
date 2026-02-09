---
layout: default
title: AlertBERT: A noise-robust alert grouping framework for simultaneous cyber attacks
---

# AlertBERT: A noise-robust alert grouping framework for simultaneous cyber attacks
**arXiv**：[2602.06534v1](https://arxiv.org/abs/2602.06534) · [PDF](https://arxiv.org/pdf/2602.06534.pdf)  
**作者**：Lukas Karner, Max Landauer, Markus Wurzenberger, Florian Skopik  

**一句话要点**：提出AlertBERT框架以解决噪声环境下同时性网络攻击的警报分组问题

**关键词**：警报分组, 自监督学习, 掩码语言模型, 基于密度聚类, 网络攻击检测, 噪声鲁棒性

## 3 点简述
- 核心问题：传统基于时间的警报分组方法在高误报和同时攻击的大规模网络中效果不佳
- 方法要点：利用掩码语言模型和基于密度的聚类进行自监督学习，支持实时或取证操作
- 实验或效果：通过数据增强方法评估，AlertBERT在识别正确警报组方面优于传统技术

## 摘要（原文）

> Automated detection of cyber attacks is a critical capability to counteract the growing volume and sophistication of cyber attacks. However, the high numbers of security alerts issued by intrusion detection systems lead to alert fatigue among analysts working in security operations centres (SOC), which in turn causes slow reaction time and incorrect decision making. Alert grouping, which refers to clustering of security alerts according to their underlying causes, can significantly reduce the number of distinct items analysts have to consider. Unfortunately, conventional time-based alert grouping solutions are unsuitable for large scale computer networks characterised by high levels of false positive alerts and simultaneously occurring attacks. To address these limitations, we propose AlertBERT, a self-supervised framework designed to group alerts from isolated or concurrent attacks in noisy environments. Thereby, our open-source implementation of AlertBERT leverages masked-language-models and density-based clustering to support both real-time or forensic operation. To evaluate our framework, we further introduce a novel data augmentation method that enables flexible control over noise levels and simulates concurrent attack occurrences. Based on the data sets generated through this method, we demonstrate that AlertBERT consistently outperforms conventional time-based grouping techniques, achieving superior accuracy in identifying correct alert groups.

