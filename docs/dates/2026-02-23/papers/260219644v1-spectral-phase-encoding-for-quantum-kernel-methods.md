---
layout: default
title: Spectral Phase Encoding for Quantum Kernel Methods
---

# Spectral Phase Encoding for Quantum Kernel Methods
**arXiv**：[2602.19644v1](https://arxiv.org/abs/2602.19644) · [PDF](https://arxiv.org/pdf/2602.19644.pdf)  
**作者**：Pablo Herrero Gómez, Antonio Jimeno Morenilla, David Muñoz-Hernández, Higinio Mora Mora  

**一句话要点**：提出谱相位编码以增强量子核方法在噪声下的鲁棒性

**关键词**：量子核方法, 谱相位编码, 噪声鲁棒性, 离散傅里叶变换, 对角嵌入, NISQ机器学习

## 3 点简述
- 核心问题：量子核方法在数据损坏下的行为未充分理解，需分析噪声影响。
- 方法要点：引入谱相位编码，结合离散傅里叶变换前端与对角相位嵌入，对齐量子映射几何。
- 实验或效果：在真实数据集上验证，DFT预处理在量子变体中降解率最小，硬件实验显示可执行且数值稳定。

## 摘要（原文）

> Quantum kernel methods are promising for near-term quantum ma- chine learning, yet their behavior under data corruption remains insuf- ficiently understood. We analyze how quantum feature constructions degrade under controlled additive noise. We introduce Spectral Phase Encoding (SPE), a hybrid construc- tion combining a discrete Fourier transform (DFT) front-end with a diagonal phase-only embedding aligned with the geometry of diagonal quantum maps. Within a unified framework, we compare QK-DFT against alternative quantum variants (QK-PCA, QK-RP) and classi- cal SVM baselines under identical clean-data hyperparameter selection, quantifying robustness via dataset fixed-effects regression with wild cluster bootstrap inference across heterogeneous real-world datasets. Across the quantum family, DFT-based preprocessing yields the smallest degradation rate as noise increases, with statistically sup- ported slope differences relative to PCA and RP. Compared to classical baselines, QK-DFT shows degradation comparable to linear SVM and more stable than RBF SVM under matched tuning. Hardware exper- iments confirm that SPE remains executable and numerically stable for overlap estimation. These results indicate that robustness in quan- tum kernels depends critically on structure-aligned preprocessing and its interaction with diagonal embeddings, supporting a robustness-first perspective for NISQ-era quantum machine learning.

