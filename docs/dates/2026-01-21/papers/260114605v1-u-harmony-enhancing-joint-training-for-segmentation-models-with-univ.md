---
layout: default
title: U-Harmony: Enhancing Joint Training for Segmentation Models with Universal Harmonization
---

# U-Harmony: Enhancing Joint Training for Segmentation Models with Universal Harmonization
**arXiv**：[2601.14605v1](https://arxiv.org/abs/2601.14605) · [PDF](https://arxiv.org/pdf/2601.14605.pdf)  
**作者**：Weiwei Ma, Xiaobing Yu, Peijie Qiu, Jin Yang, Pan Xiao, Xiaoqi Zhao, Xiaofeng Liu, Tomo Miyazaki, Shinichiro Omachi, Yongsong Huang  

**一句话要点**：提出U-Harmony方法以解决医学分割模型在异构数据集联合训练中的泛化与领域知识保留问题。

**关键词**：医学图像分割, 联合训练, 域适应, 特征归一化, 3D分割, 异构数据集

## 3 点简述
- 核心问题：医学分割数据集有限且异构，模型难以同时学习多领域数据，泛化与领域知识常冲突。
- 方法要点：通过域门控头和特征分布归一化-反归一化，减少领域差异并保留数据集特定知识。
- 实验或效果：在跨机构脑病变数据集上验证有效性，支持新模态和类别学习，提升模型鲁棒性和适应性。

## 摘要（原文）

> In clinical practice, medical segmentation datasets are often limited and heterogeneous, with variations in modalities, protocols, and anatomical targets across institutions. Existing deep learning models struggle to jointly learn from such diverse data, often sacrificing either generalization or domain-specific knowledge. To overcome these challenges, we propose a joint training method called Universal Harmonization (U-Harmony), which can be integrated into deep learning-based architectures with a domain-gated head, enabling a single segmentation model to learn from heterogeneous datasets simultaneously. By integrating U-Harmony, our approach sequentially normalizes and then denormalizes feature distributions to mitigate domain-specific variations while preserving original dataset-specific knowledge. More appealingly, our framework also supports universal modality adaptation, allowing the seamless learning of new imaging modalities and anatomical classes. Extensive experiments on cross-institutional brain lesion datasets demonstrate the effectiveness of our approach, establishing a new benchmark for robust and adaptable 3D medical image segmentation models in real-world clinical settings.

