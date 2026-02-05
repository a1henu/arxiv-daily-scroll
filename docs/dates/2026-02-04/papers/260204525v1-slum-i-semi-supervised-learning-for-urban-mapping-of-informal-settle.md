---
layout: default
title: SLUM-i: Semi-supervised Learning for Urban Mapping of Informal Settlements and Data Quality Benchmarking
---

# SLUM-i: Semi-supervised Learning for Urban Mapping of Informal Settlements and Data Quality Benchmarking
**arXiv**：[2602.04525v1](https://arxiv.org/abs/2602.04525) · [PDF](https://arxiv.org/pdf/2602.04525.pdf)  
**作者**：Muhammad Taha Mukhtar, Syed Musa Ali Kazmi, Khola Naseem, Muhammad Ali Chattha, Andreas Dengel, Sheraz Ahmed, Muhammad Naseer Bajwa, Muhammad Imran Malik  

**一句话要点**：提出半监督分割框架SLUM-i，用于解决城市非正规住区映射中的数据稀缺与质量挑战。

**关键词**：半监督学习, 城市映射, 非正规住区, 数据质量评估, 语义分割, 域迁移

## 3 点简述
- 核心问题：城市非正规住区映射受限于标注稀缺、光谱模糊和标注噪声。
- 方法要点：集成类感知自适应阈值和原型库系统，缓解类别不平衡和特征退化。
- 实验或效果：在三大洲八城市验证，模型在10%源标签下达到0.461 mIoU，优于全监督零样本泛化。

## 摘要（原文）

> Rapid urban expansion has fueled the growth of informal settlements in major cities of low- and middle-income countries, with Lahore and Karachi in Pakistan and Mumbai in India serving as prominent examples. However, large-scale mapping of these settlements is severely constrained not only by the scarcity of annotations but by inherent data quality challenges, specifically high spectral ambiguity between formal and informal structures and significant annotation noise. We address this by introducing a benchmark dataset for Lahore, constructed from scratch, along with companion datasets for Karachi and Mumbai, which were derived from verified administrative boundaries, totaling 1,869 $\text{km}^2$ of area. To evaluate the global robustness of our framework, we extend our experiments to five additional established benchmarks, encompassing eight cities across three continents, and provide comprehensive data quality assessments of all datasets. We also propose a new semi-supervised segmentation framework designed to mitigate the class imbalance and feature degradation inherent in standard semi-supervised learning pipelines. Our method integrates a Class-Aware Adaptive Thresholding mechanism that dynamically adjusts confidence thresholds to prevent minority class suppression and a Prototype Bank System that enforces semantic consistency by anchoring predictions to historically learned high-fidelity feature representations. Extensive experiments across a total of eight cities spanning three continents demonstrate that our approach outperforms state-of-the-art semi-supervised baselines. Most notably, our method demonstrates superior domain transfer capability whereby a model trained on only 10% of source labels reaches a 0.461 mIoU on unseen geographies and outperforms the zero-shot generalization of fully supervised models.

