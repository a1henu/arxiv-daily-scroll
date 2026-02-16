---
layout: default
title: Power Interpretable Causal ODE Networks: A Unified Model for Explainable Anomaly Detection and Root Cause Analysis in Power Systems
---

# Power Interpretable Causal ODE Networks: A Unified Model for Explainable Anomaly Detection and Root Cause Analysis in Power Systems
**arXiv**：[2602.12592v1](https://arxiv.org/abs/2602.12592) · [PDF](https://arxiv.org/pdf/2602.12592.pdf)  
**作者**：Yue Sun, Likai Wang, Rick S. Blum, Parv Venkitasubramaniam  

**一句话要点**：提出PICODE网络以解决电力系统异常检测与根因分析的可解释性问题

**关键词**：异常检测, 根因分析, 可解释性, 因果图, 电力系统, 时间序列

## 3 点简述
- 现有时间序列异常检测模型多为黑盒，缺乏异常类型和起源的解释
- PICODE网络结合因果信息，统一进行异常检测、根因定位、类型分类和形状表征
- 实验显示PICODE在电力系统中检测性能竞争，可解释性提升且减少对标签或外部因果图的依赖

## 摘要（原文）

> Anomaly detection and root cause analysis (RCA) are critical for ensuring the safety and resilience of cyber-physical systems such as power grids. However, existing machine learning models for time series anomaly detection often operate as black boxes, offering only binary outputs without any explanation, such as identifying anomaly type and origin. To address this challenge, we propose Power Interpretable Causality Ordinary Differential Equation (PICODE) Networks, a unified, causality-informed architecture that jointly performs anomaly detection along with the explanation why it is detected as an anomaly, including root cause localization, anomaly type classification, and anomaly shape characterization. Experimental results in power systems demonstrate that PICODE achieves competitive detection performance while offering improved interpretability and reduced reliance on labeled data or external causal graphs. We provide theoretical results demonstrating the alignment between the shape of anomaly functions and the changes in the weights of the extracted causal graphs.

