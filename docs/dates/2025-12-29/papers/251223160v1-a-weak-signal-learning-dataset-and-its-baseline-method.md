---
layout: default
title: A Weak Signal Learning Dataset and Its Baseline Method
---

# A Weak Signal Learning Dataset and Its Baseline Method
**arXiv**：[2512.23160v1](https://arxiv.org/abs/2512.23160) · [PDF](https://arxiv.org/pdf/2512.23160.pdf)  
**作者**：Xianqi Liu, Xiangru Li, Lefeng He, Ziyu Fang  

**一句话要点**：提出首个弱信号学习专用数据集及PDVFN模型，以解决低信噪比和极端类别不平衡场景下的特征提取问题。

**关键词**：弱信号学习, 低信噪比, 类别不平衡, 双视图表示, PDVFN模型, 天文光谱学

## 3 点简述
- 核心问题：弱信号学习中关键信息常被噪声掩盖，且缺乏专用数据集，制约了模型性能提升。
- 方法要点：构建包含13,158个光谱样本的数据集，提出双视图表示和PDVFN模型，并行提取局部序列和全局频域特征。
- 实验或效果：PDVFN在低信噪比和极端类别不平衡场景下表现出更高的准确性和鲁棒性，为天文光谱学等任务提供新方案。

## 摘要（原文）

> Weak signal learning (WSL) is a common challenge in many fields like fault diagnosis, medical imaging, and autonomous driving, where critical information is often masked by noise and interference, making feature identification difficult. Even in tasks with abundant strong signals, the key to improving model performance often lies in effectively extracting weak signals. However, the lack of dedicated datasets has long constrained research. To address this, we construct the first specialized dataset for weak signal feature learning, containing 13,158 spectral samples. It features low SNR dominance (over 55% samples with SNR below 50) and extreme class imbalance (class ratio up to 29:1), providing a challenging benchmark for classification and regression in weak signal scenarios. We also propose a dual-view representation (vector + time-frequency map) and a PDVFN model tailored to low SNR, distribution skew, and dual imbalance. PDVFN extracts local sequential features and global frequency-domain structures in parallel, following principles of local enhancement, sequential modeling, noise suppression, multi-scale capture, frequency extraction, and global perception. This multi-source complementarity enhances representation for low-SNR and imbalanced data, offering a novel solution for WSL tasks like astronomical spectroscopy. Experiments show our method achieves higher accuracy and robustness in handling weak signals, high noise, and extreme class imbalance, especially in low SNR and imbalanced scenarios. This study provides a dedicated dataset, a baseline model, and establishes a foundation for future WSL research.

