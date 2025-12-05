---
layout: default
title: Deep infant brain segmentation from multi-contrast MRI
---

# Deep infant brain segmentation from multi-contrast MRI
**arXiv**：[2512.05114v1](https://arxiv.org/abs/2512.05114) · [PDF](https://arxiv.org/pdf/2512.05114.pdf)  
**作者**：Malte Hoffmann, Lilla Zöllei, Adrian V. Dalca  

**一句话要点**：提出BabySeg深度学习框架，以解决婴儿脑MRI分割中协议多样性和数据稀缺问题。

**关键词**：婴儿脑分割, 多对比MRI, 领域随机化, 深度学习框架, 医学图像分析

## 3 点简述
- 核心问题：婴儿脑MRI分割因发育差异、成像限制和运动伪影而困难，现有模型常局限于特定图像类型或年龄组。
- 方法要点：基于领域随机化技术合成训练图像，增强模型对数据集偏移的鲁棒性，并支持灵活处理任意数量输入扫描。
- 实验或效果：在多种年龄组和输入配置下，单模型实现最先进性能，运行时间显著低于现有工具。

## 摘要（原文）

> Segmentation of magnetic resonance images (MRI) facilitates analysis of human brain development by delineating anatomical structures. However, in infants and young children, accurate segmentation is challenging due to development and imaging constraints. Pediatric brain MRI is notoriously difficult to acquire, with inconsistent availability of imaging modalities, substantial non-head anatomy in the field of view, and frequent motion artifacts. This has led to specialized segmentation models that are often limited to specific image types or narrow age groups, or that are fragile for more variable images such as those acquired clinically. We address this method fragmentation with BabySeg, a deep learning brain segmentation framework for infants and young children that supports diverse MRI protocols, including repeat scans and image types unavailable during training. Our approach builds on recent domain randomization techniques, which synthesize training images far beyond realistic bounds to promote dataset shift invariance. We also describe a mechanism that enables models to flexibly pool and interact features from any number of input scans. We demonstrate state-of-the-art performance that matches or exceeds the accuracy of several existing methods for various age cohorts and input configurations using a single model, in a fraction of the runtime required by many existing tools.

