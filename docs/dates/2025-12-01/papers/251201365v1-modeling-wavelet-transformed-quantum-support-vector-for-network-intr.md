---
layout: default
title: Modeling Wavelet Transformed Quantum Support Vector for Network Intrusion Detection
---

# Modeling Wavelet Transformed Quantum Support Vector for Network Intrusion Detection
**arXiv**：[2512.01365v1](https://arxiv.org/abs/2512.01365) · [PDF](https://arxiv.org/pdf/2512.01365.pdf)  
**作者**：Swati Kumari, Shiva Raj Pokhrel, Swathi Chandrasekhar, Navneet Singh, Hridoy Sankar Dutta, Adnan Anwar, Sutharshan Rajasegarar, Robin Doss  

**一句话要点**：提出集成量子小波变换与量子支持向量机的混合框架，以提升物联网网络入侵检测的异常分类性能。

**关键词**：量子支持向量机, 量子小波变换, 网络入侵检测, 物联网安全, 混合量子-经典框架

## 3 点简述
- 核心问题：物联网环境下的网络流量异常检测面临复杂性和噪声挑战，需鲁棒解决方案。
- 方法要点：结合量子Haar小波包变换进行特征提取，使用保真度量子核的量子支持向量机进行分类，并通过混合训练优化。
- 实验或效果：在BoT-IoT和IoT-23数据集上分别达到96.67%和89.67%的准确率，优于量子自编码器方法。

## 摘要（原文）

> Network traffic anomaly detection is a critical cy- bersecurity challenge requiring robust solutions for complex Internet of Things (IoT) environments. We present a novel hybrid quantum-classical framework integrating an enhanced Quantum Support Vector Machine (QSVM) with the Quantum Haar Wavelet Packet Transform (QWPT) for superior anomaly classification under realistic noisy intermediate-scale Quantum conditions. Our methodology employs amplitude-encoded quan- tum state preparation, multi-level QWPT feature extraction, and behavioral analysis via Shannon Entropy profiling and Chi-square testing. Features are classified using QSVM with fidelity-based quantum kernels optimized through hybrid train- ing with simultaneous perturbation stochastic approximation (SPSA) optimizer. Evaluation under noiseless and depolarizing noise conditions demonstrates exceptional performance: 96.67% accuracy on BoT-IoT and 89.67% on IoT-23 datasets, surpassing quantum autoencoder approaches by over 7 percentage points.

