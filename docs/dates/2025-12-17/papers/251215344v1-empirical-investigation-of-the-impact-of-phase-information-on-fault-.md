---
layout: default
title: Empirical Investigation of the Impact of Phase Information on Fault Diagnosis of Rotating Machinery
---

# Empirical Investigation of the Impact of Phase Information on Fault Diagnosis of Rotating Machinery
**arXiv**：[2512.15344v1](https://arxiv.org/abs/2512.15344) · [PDF](https://arxiv.org/pdf/2512.15344.pdf)  
**作者**：Hiroyoshi Nagahama, Katsufumi Inoue, Masayoshi Todorokihara, Michifumi Yoshioka  

**一句话要点**：提出两种相位感知预处理策略以解决旋转机械故障诊断中相位信息利用不足的问题。

**关键词**：旋转机械故障诊断, 相位感知预处理, 振动信号分析, 深度学习架构, 预测性维护

## 3 点简述
- 核心问题：现有方法在振动信号处理中常丢弃相位信息或未显式利用，影响故障诊断性能。
- 方法要点：引入三轴独立相位调整和单轴参考相位调整，分别处理随机相位变化和保持轴间关系。
- 实验或效果：在新转子数据集上评估六种深度学习架构，两种策略均提升准确率，单轴参考方法达96.2%。

## 摘要（原文）

> Predictive maintenance of rotating machinery increasingly relies on vibration signals, yet most learning-based approaches either discard phase during spectral feature extraction or use raw time-waveforms without explicitly leveraging phase information. This paper introduces two phase-aware preprocessing strategies to address random phase variations in multi-axis vibration data: (1) three-axis independent phase adjustment that aligns each axis individually to zero phase (2) single-axis reference phase adjustment that preserves inter-axis relationships by applying uniform time shifts. Using a newly constructed rotor dataset acquired with a synchronized three-axis sensor, we evaluate six deep learning architectures under a two-stage learning framework. Results demonstrate architecture-independent improvements: the three-axis independent method achieves consistent gains (+2.7\% for Transformer), while the single-axis reference approach delivers superior performance with up to 96.2\% accuracy (+5.4\%) by preserving spatial phase relationships. These findings establish both phase alignment strategies as practical and scalable enhancements for predictive maintenance systems.

