---
layout: default
title: RISE: Interactive Visual Diagnosis of Fairness in Machine Learning Models
---

# RISE: Interactive Visual Diagnosis of Fairness in Machine Learning Models
**arXiv**：[2602.04339v1](https://arxiv.org/abs/2602.04339) · [PDF](https://arxiv.org/pdf/2602.04339.pdf)  
**作者**：Ray Chen, Christan Grant  

**一句话要点**：提出RISE交互可视化工具，通过排序残差诊断机器学习模型在域偏移下的公平性问题。

**关键词**：公平性诊断, 交互可视化, 域偏移, 残差分析, 模型评估

## 3 点简述
- 核心问题：域偏移下公平性评估困难，标量指标常掩盖差异细节。
- 方法要点：将排序残差转换为可解释模式，连接曲线结构与公平性概念。
- 实验或效果：支持局部差异诊断、跨环境子群比较，揭示隐藏公平问题与权衡。

## 摘要（原文）

> Evaluating fairness under domain shift is challenging because scalar metrics often obscure exactly where and how disparities arise. We introduce \textit{RISE} (Residual Inspection through Sorted Evaluation), an interactive visualization tool that converts sorted residuals into interpretable patterns. By connecting residual curve structures to formal fairness notions, RISE enables localized disparity diagnosis, subgroup comparison across environments, and the detection of hidden fairness issues. Through post-hoc analysis, RISE exposes accuracy-fairness trade-offs that aggregate statistics miss, supporting more informed model selection.

