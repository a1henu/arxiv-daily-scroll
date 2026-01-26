---
layout: default
title: Learning Successive Interference Cancellation for Low-Complexity Soft-Output MIMO Detection
---

# Learning Successive Interference Cancellation for Low-Complexity Soft-Output MIMO Detection
**arXiv**：[2601.16586v1](https://arxiv.org/abs/2601.16586) · [PDF](https://arxiv.org/pdf/2601.16586.pdf)  
**作者**：Benedikt Fesl, Fatih Capar  

**一句话要点**：提出recurSIC框架，以低复杂度实现MIMO软输出检测，适用于边缘设备

**关键词**：MIMO检测, 连续干扰消除, 软输出, 低复杂度, 边缘计算, 机器学习

## 3 点简述
- 核心问题：低复杂度MIMO检测在5G RedCap和IoT设备中面临挑战，需平衡机器学习部署与计算内存限制
- 方法要点：基于连续干扰消除结构，融入学习处理阶段，通过多路径假设跟踪生成可靠软信息
- 实验或效果：在现实无线场景中，recurSIC以极低复杂度实现强硬的硬检测和软检测性能

## 摘要（原文）

> Low-complexity multiple-input multiple-output (MIMO) detection remains a key challenge in modern wireless systems, particularly for 5G reduced capability (RedCap) and internet-of-things (IoT) devices. In this context, the growing interest in deploying machine learning on edge devices must be balanced against stringent constraints on computational complexity and memory while supporting high-order modulation. Beyond accurate hard detection, reliable soft information is equally critical, as modern receivers rely on soft-input channel decoding, imposing additional requirements on the detector design. In this work, we propose recurSIC, a lightweight learning-based MIMO detection framework that is structurally inspired by successive interference cancellation (SIC) and incorporates learned processing stages. It generates reliable soft information via multi-path hypothesis tracking with a tunable complexity parameter while requiring only a single forward pass and a minimal parameter count. Numerical results in realistic wireless scenarios show that recurSIC achieves strong hard- and soft-detection performance at very low complexity, making it well suited for edge-constrained MIMO receivers.

