---
layout: default
title: Quantum Topological Graph Neural Networks for Detecting Complex Fraud Patterns
---

# Quantum Topological Graph Neural Networks for Detecting Complex Fraud Patterns
**arXiv**：[2512.03696v1](https://arxiv.org/abs/2512.03696) · [PDF](https://arxiv.org/pdf/2512.03696.pdf)  
**作者**：Mohammad Doost, Mohammad Manthouri  

**一句话要点**：提出量子拓扑图神经网络QTGNN以检测大规模金融网络中的复杂欺诈模式

**关键词**：量子图神经网络, 金融欺诈检测, 拓扑数据分析, 混合量子-经典学习, 变分图卷积, NISQ设备优化

## 3 点简述
- 核心问题：检测金融交易网络中的复杂欺诈模式，涉及动态交易和结构异常。
- 方法要点：集成量子嵌入、变分图卷积和拓扑数据分析，包括量子纠缠增强和混合量子-经典学习。
- 实验或效果：在PaySim和Elliptic数据集上模拟，使用ROC-AUC等指标对比基准，进行消融研究评估组件贡献。

## 摘要（原文）

> We propose a novel QTGNN framework for detecting fraudulent transactions in large-scale financial networks. By integrating quantum embedding, variational graph convolutions, and topological data analysis, QTGNN captures complex transaction dynamics and structural anomalies indicative of fraud. The methodology includes quantum data embedding with entanglement enhancement, variational quantum graph convolutions with non-linear dynamics, extraction of higher-order topological invariants, hybrid quantum-classical anomaly learning with adaptive optimization, and interpretable decision-making via topological attribution. Rigorous convergence guarantees ensure stable training on noisy intermediate-scale quantum (NISQ) devices, while stability of topological signatures provides robust fraud detection. Optimized for NISQ hardware with circuit simplifications and graph sampling, the framework scales to large transaction networks. Simulations on financial datasets, such as PaySim and Elliptic, benchmark QTGNN against classical and quantum baselines, using metrics like ROC-AUC, precision, and false positive rate. An ablation study evaluates the contributions of quantum embeddings, topological features, non-linear channels, and hybrid learning. QTGNN offers a theoretically sound, interpretable, and practical solution for financial fraud detection, bridging quantum machine learning, graph theory, and topological analysis.

