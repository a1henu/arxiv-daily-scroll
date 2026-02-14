---
layout: default
title: Self-Supervised Learning via Flow-Guided Neural Operator on Time-Series Data
---

# Self-Supervised Learning via Flow-Guided Neural Operator on Time-Series Data
**arXiv**：[2602.12267v1](https://arxiv.org/abs/2602.12267) · [PDF](https://arxiv.org/pdf/2602.12267.pdf)  
**作者**：Duy Nguyen, Jiachen Yao, Jiayun Wang, Julius Berner, Animashree Anandkumar  

**一句话要点**：提出流引导神经算子框架，通过动态噪声水平增强自监督学习在时间序列数据中的表示能力。

**关键词**：自监督学习, 时间序列分析, 神经算子, 流匹配, 生物医学信号处理, 特征提取

## 3 点简述
- 核心问题：传统自监督学习方法如掩码自编码器使用固定掩码比，限制了表示学习的灵活性和性能。
- 方法要点：结合算子学习与流匹配，利用短时傅里叶变换统一时间分辨率，通过不同噪声强度提取多层次特征。
- 实验或效果：在生物医学领域评估中，FGNO在神经信号解码、皮肤温度预测和睡眠数据分类任务上显著优于基线方法。

## 摘要（原文）

> Self-supervised learning (SSL) is a powerful paradigm for learning from unlabeled time-series data. However, popular methods such as masked autoencoders (MAEs) rely on reconstructing inputs from a fixed, predetermined masking ratio. Instead of this static design, we propose treating the corruption level as a new degree of freedom for representation learning, enhancing flexibility and performance. To achieve this, we introduce the Flow-Guided Neural Operator (FGNO), a novel framework combining operator learning with flow matching for SSL training. FGNO learns mappings in functional spaces by using Short-Time Fourier Transform to unify different time resolutions. We extract a rich hierarchy of features by tapping into different network layers and flow times that apply varying strengths of noise to the input data. This enables the extraction of versatile representations, from low-level patterns to high-level global features, using a single model adaptable to specific tasks. Unlike prior generative SSL methods that use noisy inputs during inference, we propose using clean inputs for representation extraction while learning representations with noise; this eliminates randomness and boosts accuracy. We evaluate FGNO across three biomedical domains, where it consistently outperforms established baselines. Our method yields up to 35% AUROC gains in neural signal decoding (BrainTreeBank), 16% RMSE reductions in skin temperature prediction (DREAMT), and over 20% improvement in accuracy and macro-F1 on SleepEDF under low-data regimes. These results highlight FGNO's robustness to data scarcity and its superior capacity to learn expressive representations for diverse time series.

