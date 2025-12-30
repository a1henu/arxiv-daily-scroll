---
layout: default
title: ECG-RAMBA: Zero-Shot ECG Generalization by Morphology-Rhythm Disentanglement and Long-Range Modeling
---

# ECG-RAMBA: Zero-Shot ECG Generalization by Morphology-Rhythm Disentanglement and Long-Range Modeling
**arXiv**：[2512.23347v1](https://arxiv.org/abs/2512.23347) · [PDF](https://arxiv.org/pdf/2512.23347.pdf)  
**作者**：Hai Duong Nguyen, Xuan-The Tran  

**一句话要点**：提出ECG-RAMBA框架，通过形态-节律解耦与长程建模实现零样本ECG泛化

**关键词**：心电图分类, 零样本泛化, 形态-节律解耦, 长程建模, Mamba架构, HRV特征

## 3 点简述
- 核心问题：ECG分类中形态与节律隐式纠缠导致泛化差，阻碍临床部署。
- 方法要点：分离形态与节律特征，使用MiniRocket提取形态、HRV描述节律，通过双向Mamba进行长程融合。
- 实验或效果：在Chapman–Shaoxing数据集上ROC-AUC约0.85，零样本迁移至CPSC-2021时PR-AUC为0.708，优于基线。

## 摘要（原文）

> Deep learning has achieved strong performance for electrocardiogram (ECG) classification within individual datasets, yet dependable generalization across heterogeneous acquisition settings remains a major obstacle to clinical deployment and longitudinal monitoring. A key limitation of many model architectures is the implicit entanglement of morphological waveform patterns and rhythm dynamics, which can promote shortcut learning and amplify sensitivity to distribution shifts. We propose ECG-RAMBA, a framework that separates morphology and rhythm and then re-integrates them through context-aware fusion. ECG-RAMBA combines: (i) deterministic morphological features extracted by MiniRocket, (ii) global rhythm descriptors computed from heart-rate variability (HRV), and (iii) long-range contextual modeling via a bi-directional Mamba backbone. To improve sensitivity to transient abnormalities under windowed inference, we introduce a numerically stable Power Mean pooling operator ($Q=3$) that emphasizes high-evidence segments while avoiding the brittleness of max pooling and the dilution of averaging. We evaluate under a protocol-faithful setting with subject-level cross-validation, a fixed decision threshold, and no test-time adaptation. On the Chapman--Shaoxing dataset, ECG-RAMBA achieves a macro ROC-AUC $\approx 0.85$. In zero-shot transfer, it attains PR-AUC $=0.708$ for atrial fibrillation detection on the external CPSC-2021 dataset, substantially outperforming a comparable raw-signal Mamba baseline, and shows consistent cross-dataset performance on PTB-XL. Ablation studies indicate that deterministic morphology provides a strong foundation, while explicit rhythm modeling and long-range context are critical drivers of cross-domain robustness.

