---
layout: default
title: BLISSNet: Deep Operator Learning for Fast and Accurate Flow Reconstruction from Sparse Sensor Measurements
---

# BLISSNet: Deep Operator Learning for Fast and Accurate Flow Reconstruction from Sparse Sensor Measurements
**arXiv**：[2602.24228v1](https://arxiv.org/abs/2602.24228) · [PDF](https://arxiv.org/pdf/2602.24228.pdf)  
**作者**：Maksym Veremchuk, K. Andrea Scott, Zhao Pan  

**一句话要点**：提出BLISSNet以解决稀疏传感器测量下流体流动重建的精度与效率权衡问题

**关键词**：流体流动重建, 稀疏传感器测量, 深度算子学习, 零样本推理, 数据同化, 计算效率

## 3 点简述
- 核心问题：稀疏传感器测量难以准确重建复杂多尺度流体流动，现有方法在精度与计算效率间存在权衡
- 方法要点：采用DeepONet类架构，支持零样本推理和任意大小域，通过预计算网络组件降低推理成本
- 实验或效果：模型在精度上优于传统插值方法，推理速度更快，适用于大规模实时重建和数据同化

## 摘要（原文）

> Reconstructing fluid flows from sparse sensor measurements is a fundamental challenge in science and engineering. Widely separated measurements and complex, multiscale dynamics make accurate recovery of fine-scale structures difficult. In addition, existing methods face a persistent tradeoff: high-accuracy models are often computationally expensive, whereas faster approaches typically compromise fidelity. In this work, we introduce BLISSNet, a model that strikes a strong balance between reconstruction accuracy and computational efficiency for both flow reconstruction and nudging-based data assimilation. The model follows a DeepONet-like architecture, enabling zero-shot inference on domains of arbitrary size. After the first model call on a given domain, certain network components can be precomputed, leading to low inference cost for subsequent evaluations on large domains. Consequently, the model can achieve faster inference than classical interpolation methods such as radial basis function or bicubic interpolation. This combination of high accuracy, low cost, and zero-shot generalization makes BLISSNet well-suited for large-scale real-time flow reconstruction and data assimilation tasks.

