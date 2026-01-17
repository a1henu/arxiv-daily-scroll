---
layout: default
title: How does downsampling affect needle electromyography signals? A generalisable workflow for understanding downsampling effects on high-frequency time series
---

# How does downsampling affect needle electromyography signals? A generalisable workflow for understanding downsampling effects on high-frequency time series
**arXiv**：[2601.10191v1](https://arxiv.org/abs/2601.10191) · [PDF](https://arxiv.org/pdf/2601.10191.pdf)  
**作者**：Mathieu Cherpitel, Janne Luijten, Thomas Bäck, Camiel Verhamme, Martijn Tannemaat, Anna Kononova  

**一句话要点**：提出评估下采样对高频时间序列影响的工作流，以优化针肌电信号分析的计算效率与诊断性能

**关键词**：针肌电信号分析, 下采样评估, 高频时间序列, 形状失真度量, 机器学习分类, 计算效率优化

## 3 点简述
- 核心问题：针肌电信号高采样率导致计算负担，下采样对诊断信息的影响未知
- 方法要点：结合形状失真度量和分类性能，系统评估下采样算法对波形完整性和预测效果的影响
- 实验或效果：通过三类神经肌肉疾病分类任务，验证工作流能识别保留诊断信息的下采样配置，降低计算负载

## 摘要（原文）

> Automated analysis of needle electromyography (nEMG) signals is emerging as a tool to support the detection of neuromuscular diseases (NMDs), yet the signals' high and heterogeneous sampling rates pose substantial computational challenges for feature-based machine-learning models, particularly for near real-time analysis. Downsampling offers a potential solution, but its impact on diagnostic signal content and classification performance remains insufficiently understood. This study presents a workflow for systematically evaluating information loss caused by downsampling in high-frequency time series. The workflow combines shape-based distortion metrics with classification outcomes from available feature-based machine learning models and feature space analysis to quantify how different downsampling algorithms and factors affect both waveform integrity and predictive performance. We use a three-class NMD classification task to experimentally evaluate the workflow. We demonstrate how the workflow identifies downsampling configurations that preserve diagnostic information while substantially reducing computational load. Analysis of shape-based distortion metrics showed that shape-aware downsampling algorithms outperform standard decimation, as they better preserve peak structure and overall signal morphology. The results provide practical guidance for selecting downsampling configurations that enable near real-time nEMG analysis and highlight a generalisable workflow that can be used to balance data reduction with model performance in other high-frequency time-series applications as well.

