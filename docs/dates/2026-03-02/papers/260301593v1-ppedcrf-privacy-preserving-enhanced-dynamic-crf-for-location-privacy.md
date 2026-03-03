---
layout: default
title: PPEDCRF: Privacy-Preserving Enhanced Dynamic CRF for Location-Privacy Protection for Sequence Videos with Minimal Detection Degradation
---

# PPEDCRF: Privacy-Preserving Enhanced Dynamic CRF for Location-Privacy Protection for Sequence Videos with Minimal Detection Degradation
**arXiv**：[2603.01593v1](https://arxiv.org/abs/2603.01593) · [PDF](https://arxiv.org/pdf/2603.01593.pdf)  
**作者**：Bo Ma, Jinsong Wu, Weiqi Yan, Catherine Shi, Minh Nguyen  

**一句话要点**：提出PPEDCRF框架，通过动态CRF和校准扰动保护行车记录视频位置隐私，同时最小化检测性能下降。

**关键词**：位置隐私保护, 动态条件随机场, 视频序列处理, 噪声注入, 目标检测, 隐私攻击防御

## 3 点简述
- 核心问题：行车记录视频即使移除GPS元数据，仍可通过背景视觉线索推断位置，存在隐私泄露风险。
- 方法要点：使用动态CRF发现和跟踪位置敏感区域，结合归一化控制惩罚分配扰动强度，并注入噪声以保留前景检测效用。
- 实验或效果：在公开驾驶数据集上，显著降低位置检索攻击成功率，同时保持与基线相当的检测和分割性能。

## 摘要（原文）

> Dashcam videos collected by autonomous or assisted-driving systems are increasingly shared for safety auditing and model improvement. Even when explicit GPS metadata are removed, an attacker can still infer the recording location by matching background visual cues (e.g., buildings and road layouts) against large-scale street-view imagery. This paper studies location-privacy leakage under a background-based retrieval attacker, and proposes PPEDCRF, a privacy-preserving enhanced dynamic conditional random field framework that injects calibrated perturbations only into inferred location-sensitive background regions while preserving foreground detection utility. PPEDCRF consists of three components: (i) a dynamic CRF that enforces temporal consistency to discover and track location sensitive regions across frames, (ii) a normalized control penalty (NCP) that allocates perturbation strength according to a hierarchical sensitivity model, and (iii) a utility-preserving noise injection module that minimizes interference to object detection and segmentation. Experiments on public driving datasets demonstrate that PPEDCRF significantly reduces location-retrieval attack success (e.g., Top-k retrieval accuracy) while maintaining competitive detection performance (e.g., mAP and segmentation metrics) compared with common baselines such as global noise, white-noise masking, and feature-based anonymization. The source code is in https://github.com/mabo1215/PPEDCRF.git

