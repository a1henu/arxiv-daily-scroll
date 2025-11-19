---
layout: default
title: Fusing Biomechanical and Spatio-Temporal Features for Fall Prediction: Characterizing and Mitigating the Simulation-to-Reality Gap
---

# Fusing Biomechanical and Spatio-Temporal Features for Fall Prediction: Characterizing and Mitigating the Simulation-to-Reality Gap
**arXiv**：[2511.14620v1](https://arxiv.org/abs/2511.14620) · [PDF](https://arxiv.org/pdf/2511.14620.pdf)  
**作者**：Md Fokhrul Islam, Sajeda Al-Hammouri, Christopher J. Arellano, Kavan Hazeli, Heman Shakeri  

**一句话要点**：提出BioST-GCN融合姿态与生物力学特征以预测老年人跌倒，并探讨模拟到现实的差距。

**关键词**：跌倒预测, 图卷积网络, 生物力学特征, 模拟到现实差距, 交叉注意力融合, 零样本泛化

## 3 点简述
- 核心问题：跌倒数据稀缺和模拟到现实差距阻碍基于视觉的跌倒预测系统开发。
- 方法要点：使用双流模型结合姿态和生物力学信息，通过交叉注意力机制融合特征。
- 实验或效果：在模拟数据上F1分数提升，但零样本泛化性能显著下降，需个性化策略。

## 摘要（原文）

> Falls are a leading cause of injury and loss of independence among older adults. Vision-based fall prediction systems offer a non-invasive solution to anticipate falls seconds before impact, but their development is hindered by the scarcity of available fall data. Contributing to these efforts, this study proposes the Biomechanical Spatio-Temporal Graph Convolutional Network (BioST-GCN), a dual-stream model that combines both pose and biomechanical information using a cross-attention fusion mechanism. Our model outperforms the vanilla ST-GCN baseline by 5.32% and 2.91% F1-score on the simulated MCF-UA stunt-actor and MUVIM datasets, respectively. The spatio-temporal attention mechanisms in the ST-GCN stream also provide interpretability by identifying critical joints and temporal phases. However, a critical simulation-reality gap persists. While our model achieves an 89.0% F1-score with full supervision on simulated data, zero-shot generalization to unseen subjects drops to 35.9%. This performance decline is likely due to biases in simulated data, such as `intent-to-fall' cues. For older adults, particularly those with diabetes or frailty, this gap is exacerbated by their unique kinematic profiles. To address this, we propose personalization strategies and advocate for privacy-preserving data pipelines to enable real-world validation. Our findings underscore the urgent need to bridge the gap between simulated and real-world data to develop effective fall prediction systems for vulnerable elderly populations.

