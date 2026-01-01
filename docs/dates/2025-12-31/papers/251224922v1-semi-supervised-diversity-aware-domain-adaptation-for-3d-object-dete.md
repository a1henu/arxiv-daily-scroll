---
layout: default
title: Semi-Supervised Diversity-Aware Domain Adaptation for 3D Object detection
---

# Semi-Supervised Diversity-Aware Domain Adaptation for 3D Object detection
**arXiv**：[2512.24922v1](https://arxiv.org/abs/2512.24922) · [PDF](https://arxiv.org/pdf/2512.24922.pdf)  
**作者**：Bartłomiej Olber, Jakub Winter, Paweł Wawrzyński, Andrii Gamalii, Daniel Górniak, Marcin Łojek, Robert Nowak, Krystian Radlak  

**一句话要点**：提出基于神经元激活模式的半监督多样性感知域适应方法，以提升3D目标检测的跨域泛化能力。

**关键词**：3D目标检测, 域适应, 半监督学习, 神经元激活模式, 自动驾驶, 持续学习

## 3 点简述
- 核心问题：3D目标检测器在自动驾驶中跨域泛化差，如从美国到亚洲或欧洲性能下降。
- 方法要点：利用神经元激活模式选择目标域中少量代表性多样样本进行标注，结合持续学习技术防止权重漂移。
- 实验或效果：方法在少量标注预算下优于线性探测和现有域适应技术，实现先进性能。

## 摘要（原文）

> 3D object detectors are fundamental components of perception systems in autonomous vehicles. While these detectors achieve remarkable performance on standard autonomous driving benchmarks, they often struggle to generalize across different domains - for instance, a model trained in the U.S. may perform poorly in regions like Asia or Europe. This paper presents a novel lidar domain adaptation method based on neuron activation patterns, demonstrating that state-of-the-art performance can be achieved by annotating only a small, representative, and diverse subset of samples from the target domain if they are correctly selected. The proposed approach requires very small annotation budget and, when combined with post-training techniques inspired by continual learning prevent weight drift from the original model. Empirical evaluation shows that the proposed domain adaptation approach outperforms both linear probing and state-of-the-art domain adaptation techniques.

