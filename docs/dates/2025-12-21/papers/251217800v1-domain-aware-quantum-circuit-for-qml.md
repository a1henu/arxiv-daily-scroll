---
layout: default
title: Domain-Aware Quantum Circuit for QML
---

# Domain-Aware Quantum Circuit for QML
**arXiv**：[2512.17800v1](https://arxiv.org/abs/2512.17800) · [PDF](https://arxiv.org/pdf/2512.17800.pdf)  
**作者**：Gurinder Singh, Thaddeus Pellegrini, Kenneth M. Merz,  

**一句话要点**：提出领域感知量子电路，利用图像先验提升噪声量子设备上的机器学习性能。

**关键词**：量子机器学习, 参数化量子电路, 图像分类, 噪声量子设备, 局部保持编码

## 3 点简述
- 核心问题：在噪声量子设备上设计表达力强、可训练且抗噪声的参数化量子电路。
- 方法要点：通过非重叠DCT式窗口引导局部保持编码和纠缠，采用交错编码-纠缠-训练循环。
- 实验或效果：在量子硬件上实现与强经典基线竞争的性能，优于量子电路搜索基线。

## 摘要（原文）

> Designing parameterized quantum circuits (PQCs) that are expressive, trainable, and robust to hardware noise is a central challenge for quantum machine learning (QML) on noisy intermediate-scale quantum (NISQ) devices. We present a Domain-Aware Quantum Circuit (DAQC) that leverages image priors to guide locality-preserving encoding and entanglement via non-overlapping DCT-style zigzag windows. The design employs interleaved encode-entangle-train cycles, where entanglement is applied among qubits hosting neighboring pixels, aligned to device connectivity. This staged, locality-preserving information flow expands the effective receptive field without deep global mixing, enabling efficient use of limited depth and qubits. The design concentrates representational capacity on short-range correlations, reduces long-range two-qubit operations, and encourages stable optimization, thereby mitigating depth-induced and globally entangled barren-plateau effects. We evaluate DAQC on MNIST, FashionMNIST, and PneumoniaMNIST datasets. On quantum hardware, DAQC achieves performance competitive with strong classical baselines (e.g., ResNet-18/50, DenseNet-121, EfficientNet-B0) and substantially outperforming Quantum Circuit Search (QCS) baselines. To the best of our knowledge, DAQC, which uses a quantum feature extractor with only a linear classical readout (no deep classical backbone), currently achieves the best reported performance on real quantum hardware for QML-based image classification tasks. Code and pretrained models are available at: https://github.com/gurinder-hub/DAQC.

