---
layout: default
title: POSEIDON: Physics-Optimized Seismic Energy Inference and Detection Operating Network
---

# POSEIDON: Physics-Optimized Seismic Energy Inference and Detection Operating Network
**arXiv**：[2601.02264v1](https://arxiv.org/abs/2601.02264) · [PDF](https://arxiv.org/pdf/2601.02264.pdf)  
**作者**：Boris Kriuk, Fedor Kriuk  

**一句话要点**：提出物理信息能量模型POSEIDON以解决地震预测中忽视物理定律的黑盒问题

**关键词**：物理信息机器学习, 地震预测, 能量模型, 多任务学习, 可解释AI, 地震数据集

## 3 点简述
- 核心问题：地震预测和灾害评估中现有机器学习方法常忽略物理定律，缺乏可解释性
- 方法要点：嵌入Gutenberg-Richter和Omori-Utsu定律作为可学习约束，统一处理余震识别、海啸潜力和前震检测
- 实验或效果：在Poseidon数据集上实现最先进性能，物理参数收敛至科学可解释值，提升预测准确性

## 摘要（原文）

> Earthquake prediction and seismic hazard assessment remain fundamental challenges in geophysics, with existing machine learning approaches often operating as black boxes that ignore established physical laws. We introduce POSEIDON (Physics-Optimized Seismic Energy Inference and Detection Operating Network), a physics-informed energy-based model for unified multi-task seismic event prediction, alongside the Poseidon dataset -- the largest open-source global earthquake catalog comprising 2.8 million events spanning 30 years. POSEIDON embeds fundamental seismological principles, including the Gutenberg-Richter magnitude-frequency relationship and Omori-Utsu aftershock decay law, as learnable constraints within an energy-based modeling framework. The architecture simultaneously addresses three interconnected prediction tasks: aftershock sequence identification, tsunami generation potential, and foreshock detection. Extensive experiments demonstrate that POSEIDON achieves state-of-the-art performance across all tasks, outperforming gradient boosting, random forest, and CNN baselines with the highest average F1 score among all compared methods. Crucially, the learned physics parameters converge to scientifically interpretable values -- Gutenberg-Richter b-value of 0.752 and Omori-Utsu parameters p=0.835, c=0.1948 days -- falling within established seismological ranges while enhancing rather than compromising predictive accuracy. The Poseidon dataset is publicly available at https://huggingface.co/datasets/BorisKriuk/Poseidon, providing pre-computed energy features, spatial grid indices, and standardized quality metrics to advance physics-informed seismic research.

