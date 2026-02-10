---
layout: default
title: Bridging Academia and Industry: A Comprehensive Benchmark for Attributed Graph Clustering
---

# Bridging Academia and Industry: A Comprehensive Benchmark for Attributed Graph Clustering
**arXiv**：[2602.08519v1](https://arxiv.org/abs/2602.08519) · [PDF](https://arxiv.org/pdf/2602.08519.pdf)  
**作者**：Yunhui Liu, Pengyu Qiu, Yu Xing, Yongchao Liu, Peng Du, Chuntao Hong, Jiajun Zheng, Tao Zheng, Tieke He  

**一句话要点**：提出PyAGC基准以解决属性图聚类在学术与工业应用间的差距

**关键词**：属性图聚类, 工业基准, 无监督学习, 图神经网络, 可扩展算法, 异质性图

## 3 点简述
- 属性图聚类在工业应用中面临数据集小、同质性高、评估指标不切实际的问题
- PyAGC提供模块化框架、内存高效的小批量实现和12个多样化数据集
- 在Ant Group工业流程中验证，强调无监督结构指标和效率分析

## 摘要（原文）

> Attributed Graph Clustering (AGC) is a fundamental unsupervised task that integrates structural topology and node attributes to uncover latent patterns in graph-structured data. Despite its significance in industrial applications such as fraud detection and user segmentation, a significant chasm persists between academic research and real-world deployment. Current evaluation protocols suffer from the small-scale, high-homophily citation datasets, non-scalable full-batch training paradigms, and a reliance on supervised metrics that fail to reflect performance in label-scarce environments. To bridge these gaps, we present PyAGC, a comprehensive, production-ready benchmark and library designed to stress-test AGC methods across diverse scales and structural properties. We unify existing methodologies into a modular Encode-Cluster-Optimize framework and, for the first time, provide memory-efficient, mini-batch implementations for a wide array of state-of-the-art AGC algorithms. Our benchmark curates 12 diverse datasets, ranging from 2.7K to 111M nodes, specifically incorporating industrial graphs with complex tabular features and low homophily. Furthermore, we advocate for a holistic evaluation protocol that mandates unsupervised structural metrics and efficiency profiling alongside traditional supervised metrics. Battle-tested in high-stakes industrial workflows at Ant Group, this benchmark offers the community a robust, reproducible, and scalable platform to advance AGC research towards realistic deployment. The code and resources are publicly available via GitHub (https://github.com/Cloudy1225/PyAGC), PyPI (https://pypi.org/project/pyagc), and Documentation (https://pyagc.readthedocs.io).

