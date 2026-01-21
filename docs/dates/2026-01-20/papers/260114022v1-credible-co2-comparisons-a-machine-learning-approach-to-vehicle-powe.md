---
layout: default
title: Credible CO2 Comparisons: A Machine Learning Approach to Vehicle Powertrain Assessment
---

# Credible CO2 Comparisons: A Machine Learning Approach to Vehicle Powertrain Assessment
**arXiv**：[2601.14022v1](https://arxiv.org/abs/2601.14022) · [PDF](https://arxiv.org/pdf/2601.14022.pdf)  
**作者**：Rodrigo Pereira David, Luciano Araujo Dourado Filho, Daniel Marques da Silva, João Alfredo Cal-Braz  

**一句话要点**：提出基于机器学习的框架，在相同真实驾驶条件下公平评估内燃机与电动汽车的CO2排放。

**关键词**：车辆动力系统评估, CO2排放比较, 机器学习框架, 循环神经网络, 反事实分析, 真实驾驶条件

## 3 点简述
- 核心问题：道路运输脱碳需一致透明的方法比较不同车辆技术的CO2排放。
- 方法要点：使用循环神经网络独立建模，固定驾驶环境变量，构建反事实场景进行技术对比。
- 实验或效果：通过统一瞬时排放指标，实现可重复的公平评估，为数据驱动的碳性能分析提供基础。

## 摘要（原文）

> Decarbonizing road transport requires consistent and transparent methods for comparing CO2 emissions across vehicle technologies. This paper proposes a machine learning-based framework for like-for-like operational assessment of internal combustion engine vehicles (ICEVs) and electric vehicles (EVs) under identical, real-world driving conditions. The approach isolates technology-specific effects by holding the observed speed profile and environmental context fixed, enabling direct comparison of powertrain performance. Recurrent neural network models are trained independently for each domain to learn the mapping from contextual driving variables (speed, acceleration, temperature) to internal actuation variables (torque, throttle) and instantaneous CO2-equivalent emission rates. This structure allows the construction of counterfactual scenarios that answer: What emissions would an EV have generated if it had followed the same driving profile as an ICEV? By aligning both vehicle types on a unified instantaneous emissions metric, the framework enables fair and reproducible evaluation of powertrain technologies. It offers a scalable foundation for credible, data-driven assessments of vehicle carbon performance under real-world operating conditions.

