---
layout: default
title: Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models
---

# Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models
**arXiv**：[2601.20367v1](https://arxiv.org/abs/2601.20367) · [PDF](https://arxiv.org/pdf/2601.20367.pdf)  
**作者**：Qing Lyu, Zhe Fu, Alexandre Bayen  

**一句话要点**：提出基于Transformer的无监督异常检测框架，以解决多智能体轨迹预测中的安全风险识别问题。

**关键词**：无监督异常检测, 多智能体轨迹预测, Transformer模型, 安全评估, 残差分析, 风险聚类

## 3 点简述
- 核心问题：自动驾驶中安全关键场景罕见，传统规则方法难以捕捉复杂交互风险，且缺乏验证异常与物理危险对齐的系统方法。
- 方法要点：使用多智能体Transformer建模正常驾驶，通过预测残差测量偏差，并引入双重评估方案检测稳定性和物理对齐。
- 实验或效果：在NGSIM数据集上验证，最大残差聚合器实现最高物理对齐，识别出388个被传统方法遗漏的异常，聚类为四类可解释风险。

## 摘要（原文）

> Identifying safety-critical scenarios is essential for autonomous driving, but the rarity of such events makes supervised labeling impractical. Traditional rule-based metrics like Time-to-Collision are too simplistic to capture complex interaction risks, and existing methods lack a systematic way to verify whether statistical anomalies truly reflect physical danger. To address this gap, we propose an unsupervised anomaly detection framework based on a multi-agent Transformer that models normal driving and measures deviations through prediction residuals. A dual evaluation scheme has been proposed to assess both detection stability and physical alignment: Stability is measured using standard ranking metrics in which Kendall Rank Correlation Coefficient captures rank agreement and Jaccard index captures the consistency of the top-K selected items; Physical alignment is assessed through correlations with established Surrogate Safety Measures (SSM). Experiments on the NGSIM dataset demonstrate our framework's effectiveness: We show that the maximum residual aggregator achieves the highest physical alignment while maintaining stability. Furthermore, our framework identifies 388 unique anomalies missed by Time-to-Collision and statistical baselines, capturing subtle multi-agent risks like reactive braking under lateral drift. The detected anomalies are further clustered into four interpretable risk types, offering actionable insights for simulation and testing.

