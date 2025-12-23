---
layout: default
title: Automatic Neuronal Activity Segmentation in Fast Four Dimensional Spatio-Temporal Fluorescence Imaging using Bayesian Approach
---

# Automatic Neuronal Activity Segmentation in Fast Four Dimensional Spatio-Temporal Fluorescence Imaging using Bayesian Approach
**arXiv**：[2512.19032v1](https://arxiv.org/abs/2512.19032) · [PDF](https://arxiv.org/pdf/2512.19032.pdf)  
**作者**：Ran Li, Pan Xiao, Kaushik Dutta, Youdong Guo  

**一句话要点**：提出贝叶斯深度学习框架以自动分割光片显微镜四维时空数据中的神经元活动

**关键词**：神经元活动分割, 贝叶斯深度学习, 四维时空成像, 光片显微镜, 不确定性建模

## 3 点简述
- 核心问题：荧光显微钙成像中神经元活动的手动分割耗时且泛化性差
- 方法要点：结合像素级相关性图与平均摘要图像，贝叶斯框架输出概率分割图并建模不确定性
- 实验或效果：在合成真值上平均Dice分数0.81，可重复性测试平均Dice分数0.79

## 摘要（原文）

> Fluorescence Microcopy Calcium Imaging is a fundamental tool to in-vivo record and analyze large scale neuronal activities simultaneously at a single cell resolution. Automatic and precise detection of behaviorally relevant neuron activity from the recordings is critical to study the mapping of brain activity in organisms. However a perpetual bottleneck to this problem is the manual segmentation which is time and labor intensive and lacks generalizability. To this end, we present a Bayesian Deep Learning Framework to detect neuronal activities in 4D spatio-temporal data obtained by light sheet microscopy. Our approach accounts for the use of temporal information by calculating pixel wise correlation maps and combines it with spatial information given by the mean summary image. The Bayesian framework not only produces probability segmentation maps but also models the uncertainty pertaining to active neuron detection. To evaluate the accuracy of our framework we implemented the test of reproducibility to assert the generalization of the network to detect neuron activity. The network achieved a mean Dice Score of 0.81 relative to the synthetic Ground Truth obtained by Otsu's method and a mean Dice Score of 0.79 between the first and second run for test of reproducibility. Our method successfully deployed can be used for rapid detection of active neuronal activities for behavioural studies.

