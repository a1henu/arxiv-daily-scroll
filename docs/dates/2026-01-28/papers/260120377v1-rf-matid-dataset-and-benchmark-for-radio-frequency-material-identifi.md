---
layout: default
title: RF-MatID: Dataset and Benchmark for Radio Frequency Material Identification
---

# RF-MatID: Dataset and Benchmark for Radio Frequency Material Identification
**arXiv**：[2601.20377v1](https://arxiv.org/abs/2601.20377) · [PDF](https://arxiv.org/pdf/2601.20377.pdf)  
**作者**：Xinyan Chen, Qinchun Li, Ruiqin Ma, Jiaqi Bai, Li Yi, Jianfei Yang  

**一句话要点**：提出RF-MatID数据集与基准以解决射频材料识别中缺乏大规模公开数据的问题

**关键词**：射频材料识别, 大规模数据集, 深度学习基准, 几何扰动, 宽频带射频, 分布外鲁棒性

## 3 点简述
- 核心问题：射频材料识别缺乏大规模公开数据集，限制了学习方法的基准评估
- 方法要点：构建首个开源、大规模、宽频带、几何多样的射频数据集，包含16个细粒度类别
- 实验或效果：建立多设置基准，评估深度学习模型在分布内性能和跨角度、跨距离的分布外鲁棒性

## 摘要（原文）

> Accurate material identification plays a crucial role in embodied AI systems, enabling a wide range of applications. However, current vision-based solutions are limited by the inherent constraints of optical sensors, while radio-frequency (RF) approaches, which can reveal intrinsic material properties, have received growing attention. Despite this progress, RF-based material identification remains hindered by the lack of large-scale public datasets and the limited benchmarking of learning-based approaches. In this work, we present RF-MatID, the first open-source, large-scale, wide-band, and geometry-diverse RF dataset for fine-grained material identification. RF-MatID includes 16 fine-grained categories grouped into 5 superclasses, spanning a broad frequency range from 4 to 43.5 GHz, and comprises 142k samples in both frequency- and time-domain representations. The dataset systematically incorporates controlled geometry perturbations, including variations in incidence angle and stand-off distance. We further establish a multi-setting, multi-protocol benchmark by evaluating state-of-the-art deep learning models, assessing both in-distribution performance and out-of-distribution robustness under cross-angle and cross-distance shifts. The 5 frequency-allocation protocols enable systematic frequency- and region-level analysis, thereby facilitating real-world deployment. RF-MatID aims to enable reproducible research, accelerate algorithmic advancement, foster cross-domain robustness, and support the development of real-world application in RF-based material identification.

