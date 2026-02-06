---
layout: default
title: RaBiT: Residual-Aware Binarization Training for Accurate and Efficient LLMs
---

# RaBiT: Residual-Aware Binarization Training for Accurate and Efficient LLMs
**arXiv**：[2602.05367v1](https://arxiv.org/abs/2602.05367) · [PDF](https://arxiv.org/pdf/2602.05367.pdf)  
**作者**：Youngcheon You, Banseok Lee, Minseop Choi, Seonyoung Kim, Hyochan Chong, Changdong Kim, Youngmin Kim, Dongkyu Kim  

**一句话要点**：提出RaBiT框架，通过残差层次化解决大语言模型二值化中的特征共适应问题，提升准确性与效率。

**关键词**：大语言模型量化, 残差二值化, 特征共适应, 量化感知训练, 高效推理, 硬件加速

## 3 点简述
- 核心问题：残差二值化训练中，并行路径学习冗余特征，导致误差补偿结构退化，限制模型表达能力。
- 方法要点：从单一全精度权重顺序推导每个二值路径，确保每个路径纠正前一个的误差，并通过稳健初始化稳定训练。
- 实验或效果：在2位量化中达到最先进性能，媲美硬件密集型向量量化方法，在RTX 4090上推理速度提升4.49倍。

## 摘要（原文）

> Efficient deployment of large language models (LLMs) requires extreme quantization, forcing a critical trade-off between low-bit efficiency and performance. Residual binarization enables hardware-friendly, matmul-free inference by stacking binary ($\pm$1) layers, but is plagued by pathological feature co-adaptation. We identify a key failure mode, which we term inter-path adaptation: during quantization-aware training (QAT), parallel residual binary paths learn redundant features, degrading the error-compensation structure and limiting the expressive capacity of the model. While prior work relies on heuristic workarounds (e.g., path freezing) that constrain the solution space, we propose RaBiT, a novel quantization framework that resolves co-adaptation by algorithmically enforcing a residual hierarchy. Its core mechanism sequentially derives each binary path from a single shared full-precision weight, which ensures that every path corrects the error of the preceding one. This process is stabilized by a robust initialization that prioritizes functional preservation over mere weight approximation. RaBiT redefines the 2-bit accuracy-efficiency frontier: it achieves state-of-the-art performance, rivals even hardware-intensive Vector Quantization (VQ) methods, and delivers a $4.49\times$ inference speed-up over full-precision models on an RTX 4090.

