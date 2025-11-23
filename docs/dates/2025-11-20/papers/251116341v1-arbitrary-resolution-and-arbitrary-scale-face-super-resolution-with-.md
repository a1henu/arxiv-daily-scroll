---
layout: default
title: Arbitrary-Resolution and Arbitrary-Scale Face Super-Resolution with Implicit Representation Networks
---

# Arbitrary-Resolution and Arbitrary-Scale Face Super-Resolution with Implicit Representation Networks
**arXiv**：[2511.16341v1](https://arxiv.org/abs/2511.16341) · [PDF](https://arxiv.org/pdf/2511.16341.pdf)  
**作者**：Yi Ting Tsai, Yu Wei Chen, Hong-Han Shuai, Ching-Chun Huang  

**一句话要点**：提出ARASFSR方法，实现任意分辨率和尺度的面部超分辨率，提升鲁棒性。

**关键词**：面部超分辨率, 隐式表示网络, 任意尺度上采样, 局部频率估计, 全局坐标调制

## 3 点简述
- 现有面部超分辨率方法受限于固定上采样尺度和对输入尺寸变化的敏感性。
- 使用隐式表示网络结合局部频率估计和全局坐标调制，支持任意上采样。
- 实验显示ARASFSR在多种输入尺寸和上采样尺度下优于现有方法。

## 摘要（原文）

> Face super-resolution (FSR) is a critical technique for enhancing low-resolution facial images and has significant implications for face-related tasks. However, existing FSR methods are limited by fixed up-sampling scales and sensitivity to input size variations. To address these limitations, this paper introduces an Arbitrary-Resolution and Arbitrary-Scale FSR method with implicit representation networks (ARASFSR), featuring three novel designs. First, ARASFSR employs 2D deep features, local relative coordinates, and up-sampling scale ratios to predict RGB values for each target pixel, allowing super-resolution at any up-sampling scale. Second, a local frequency estimation module captures high-frequency facial texture information to reduce the spectral bias effect. Lastly, a global coordinate modulation module guides FSR to leverage prior facial structure knowledge and achieve resolution adaptation effectively. Quantitative and qualitative evaluations demonstrate the robustness of ARASFSR over existing state-of-the-art methods while super-resolving facial images across various input sizes and up-sampling scales.

