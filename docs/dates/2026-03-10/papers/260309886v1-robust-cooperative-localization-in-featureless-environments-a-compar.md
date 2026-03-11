---
layout: default
title: Robust Cooperative Localization in Featureless Environments: A Comparative Study of DCL, StCL, CCL, CI, and Standard-CL
---

# Robust Cooperative Localization in Featureless Environments: A Comparative Study of DCL, StCL, CCL, CI, and Standard-CL
**arXiv**：[2603.09886v1](https://arxiv.org/abs/2603.09886) · [PDF](https://arxiv.org/pdf/2603.09886.pdf)  
**作者**：Nivand Khosravi, Meysam Basiri, Rodrigo Ventura  

**一句话要点**：比较五种协同定位方法在无特征环境中的鲁棒性，揭示权衡与适用性

**关键词**：协同定位, 多机器人系统, 鲁棒性分析, 蒙特卡洛模拟, 滤波器一致性

## 3 点简述
- 核心问题：在GPS拒止的无特征环境中，多机器人协同定位的鲁棒性与精度权衡
- 方法要点：评估DCL、StCL、CCL、CI和Standard-CL五种方法，基于ROS实现与蒙特卡洛模拟
- 实验或效果：StCL和Standard-CL精度高但一致性差，DCL稳定，CI平衡，CCL最优但敏感于异常值

## 摘要（原文）

> Cooperative localization (CL) enables accurate position estimation in multi-robot systems operating in GPS-denied environments. This paper presents a comparative study of five CL approaches: Centralized Cooperative Localization (CCL), Decentralized Cooperative Localization (DCL), Sequential Cooperative Localization (StCL), Covariance Intersection (CI), and Standard Cooperative Localization (Standard-CL). All methods are implemented in ROS and evaluated through Monte Carlo simulations under two conditions: weak data association and robust detection. Our analysis reveals fundamental trade-offs among the methods. StCL and Standard-CL achieve the lowest position errors but exhibit severe filter inconsistency, making them unsuitable for safety-critical applications. DCL demonstrates remarkable stability under challenging conditions due to its measurement stride mechanism, which provides implicit regularization against outliers. CI emerges as the most balanced approach, achieving near-optimal consistency while maintaining competitive accuracy. CCL provides theoretically optimal estimation but shows sensitivity to measurement outliers. These findings offer practical guidance for selecting CL algorithms based on application requirements.

