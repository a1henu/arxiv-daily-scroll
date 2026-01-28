---
layout: default
title: Neuromorphic BrailleNet: Accurate and Generalizable Braille Reading Beyond Single Characters through Event-Based Optical Tactile Sensing
---

# Neuromorphic BrailleNet: Accurate and Generalizable Braille Reading Beyond Single Characters through Event-Based Optical Tactile Sensing
**arXiv**：[2601.19079v1](https://arxiv.org/abs/2601.19079) · [PDF](https://arxiv.org/pdf/2601.19079.pdf)  
**作者**：Naqash Afzal, Niklas Funk, Erik Helmut, Jan Peters, Benjamin Ward-Cherrier  

**一句话要点**：提出基于事件触觉传感的连续盲文识别系统，以解决传统方法速度慢和鲁棒性差的问题。

**关键词**：事件触觉传感, 盲文识别, 连续滑动, 时空分割, 轻量分类器, 机器人辅助

## 3 点简述
- 传统盲文阅读器依赖逐字符扫描，限制速度和自然流程；视觉方法计算量大、延迟高且易受环境干扰。
- 使用开源事件触觉传感器EvTac，结合时空分割和轻量ResNet分类器处理稀疏事件流，模拟人类手指滑动。
- 在标准深度下达到≥98%字符准确率，多布局泛化强，快速扫描下保持高性能，日常词汇单词准确率超90%。

## 摘要（原文）

> Conventional robotic Braille readers typically rely on discrete, character-by-character scanning, limiting reading speed and disrupting natural flow. Vision-based alternatives often require substantial computation, introduce latency, and degrade in real-world conditions. In this work, we present a high accuracy, real-time pipeline for continuous Braille recognition using Evetac, an open-source neuromorphic event-based tactile sensor. Unlike frame-based vision systems, the neuromorphic tactile modality directly encodes dynamic contact events during continuous sliding, closely emulating human finger-scanning strategies. Our approach combines spatiotemporal segmentation with a lightweight ResNet-based classifier to process sparse event streams, enabling robust character recognition across varying indentation depths and scanning speeds. The proposed system achieves near-perfect accuracy (>=98%) at standard depths, generalizes across multiple Braille board layouts, and maintains strong performance under fast scanning. On a physical Braille board containing daily-living vocabulary, the system attains over 90% word-level accuracy, demonstrating robustness to temporal compression effects that challenge conventional methods. These results position neuromorphic tactile sensing as a scalable, low latency solution for robotic Braille reading, with broader implications for tactile perception in assistive and robotic applications.

