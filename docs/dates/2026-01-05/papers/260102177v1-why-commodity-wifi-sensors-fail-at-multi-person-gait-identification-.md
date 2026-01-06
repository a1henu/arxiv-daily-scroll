---
layout: default
title: Why Commodity WiFi Sensors Fail at Multi-Person Gait Identification: A Systematic Analysis Using ESP32
---

# Why Commodity WiFi Sensors Fail at Multi-Person Gait Identification: A Systematic Analysis Using ESP32
**arXiv**：[2601.02177v1](https://arxiv.org/abs/2601.02177) · [PDF](https://arxiv.org/pdf/2601.02177.pdf)  
**作者**：Oliver Custance, Saad Khan, Simon Parkinson  

**一句话要点**：系统分析ESP32传感器在多人员步态识别中的性能限制，揭示硬件约束导致信号质量不足

**关键词**：WiFi信道状态信息, 多人员步态识别, 信号分离方法, ESP32传感器, 性能分析

## 3 点简述
- 核心问题：探究商品WiFi传感器在多人员步态识别中性能差是算法限制还是硬件约束
- 方法要点：使用ESP32传感器，评估六种信号分离方法在1-10人场景下的表现
- 实验或效果：所有方法准确率低（45-56%），显示高主体内变异性和低主体间区分度

## 摘要（原文）

> WiFi Channel State Information (CSI) has shown promise for single-person gait identification, with numerous studies reporting high accuracy. However, multi-person identification remains largely unexplored, with the limited existing work relying on complex, expensive setups requiring modified firmware. A critical question remains unanswered: is poor multi-person performance an algorithmic limitation or a fundamental hardware constraint? We systematically evaluate six diverse signal separation methods (FastICA, SOBI, PCA, NMF, Wavelet, Tensor Decomposition) across seven scenarios with 1-10 people using commodity ESP32 WiFi sensors--a simple, low-cost, off-the-shelf solution. Through novel diagnostic metrics (intra-subject variability, inter-subject distinguishability, performance degradation rate), we reveal that all methods achieve similarly low accuracy (45-56\%, $σ$=3.74\%) with statistically insignificant differences (p $>$ 0.05). Even the best-performing method, NMF, achieves only 56\% accuracy. Our analysis reveals high intra-subject variability, low inter-subject distinguishability, and severe performance degradation as person count increases, indicating that commodity ESP32 sensors cannot provide sufficient signal quality for reliable multi-person separation.

