---
layout: default
title: Geometry-Free Conditional Diffusion Modeling for Solving the Inverse Electrocardiography Problem
---

# Geometry-Free Conditional Diffusion Modeling for Solving the Inverse Electrocardiography Problem
**arXiv**：[2601.18615v1](https://arxiv.org/abs/2601.18615) · [PDF](https://arxiv.org/pdf/2601.18615.pdf)  
**作者**：Ramiro Valdes Jara, Adam Meyers  

**一句话要点**：提出几何无关条件扩散模型以解决心电成像逆问题

**关键词**：心电成像逆问题, 条件扩散模型, 几何无关方法, 概率重建, 数据驱动模型, 非侵入性心脏成像

## 3 点简述
- 核心问题：解决心电成像逆问题，即从体表信号重建心表电位，具有非唯一性和欠定性。
- 方法要点：采用条件扩散模型学习概率映射，无需患者特定几何网格，实现多重建采样。
- 实验或效果：在真实数据集上评估，相比确定性基线模型，重建精度提升。

## 摘要（原文）

> This paper proposes a data-driven model for solving the inverse problem of electrocardiography, the mathematical problem that forms the basis of electrocardiographic imaging (ECGI). We present a conditional diffusion framework that learns a probabilistic mapping from noisy body surface signals to heart surface electric potentials. The proposed approach leverages the generative nature of diffusion models to capture the non-unique and underdetermined nature of the ECGI inverse problem, enabling probabilistic sampling of multiple reconstructions rather than a single deterministic estimate. Unlike traditional methods, the proposed framework is geometry-free and purely data-driven, alleviating the need for patient-specific mesh construction. We evaluate the method on a real ECGI dataset and compare it against strong deterministic baselines, including a convolutional neural network, long short-term memory network, and transformer-based model. The results demonstrate that the proposed diffusion approach achieves improved reconstruction accuracy, highlighting the potential of diffusion models as a robust tool for noninvasive cardiac electrophysiology imaging.

