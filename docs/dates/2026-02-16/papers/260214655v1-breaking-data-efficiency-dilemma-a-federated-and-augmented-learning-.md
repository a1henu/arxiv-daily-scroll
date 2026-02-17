---
layout: default
title: Breaking Data Efficiency Dilemma: A Federated and Augmented Learning Framework For Alzheimer's Disease Detection via Speech
---

# Breaking Data Efficiency Dilemma: A Federated and Augmented Learning Framework For Alzheimer's Disease Detection via Speech
**arXiv**：[2602.14655v1](https://arxiv.org/abs/2602.14655) · [PDF](https://arxiv.org/pdf/2602.14655.pdf)  
**作者**：Xiao Wei, Bin Wen, Yuqin Lin, Kai Li, Mingyang gu, Xiaobao Wang, Longbiao Wang, Jianwu Dang  

**一句话要点**：提出FAL-AD框架，通过联邦学习与数据增强协同优化数据效率，用于阿尔茨海默病语音检测。

**关键词**：阿尔茨海默病检测, 语音分析, 联邦学习, 数据增强, 跨模态融合, 医疗AI

## 3 点简述
- 核心问题：AI语音检测面临医疗数据稀缺和隐私壁垒导致的数据效率困境。
- 方法要点：结合基于语音转换的数据增强、自适应联邦学习和注意力跨模态融合模型。
- 实验或效果：在ADReSSo数据集上实现91.52%的多模态准确率，优于集中式基线。

## 摘要（原文）

> Early diagnosis of Alzheimer's Disease (AD) is crucial for delaying its progression. While AI-based speech detection is non-invasive and cost-effective, it faces a critical data efficiency dilemma due to medical data scarcity and privacy barriers. Therefore, we propose FAL-AD, a novel framework that synergistically integrates federated learning with data augmentation to systematically optimize data efficiency. Our approach delivers three key breakthroughs: First, absolute efficiency improvement through voice conversion-based augmentation, which generates diverse pathological speech samples via cross-category voice-content recombination. Second, collaborative efficiency breakthrough via an adaptive federated learning paradigm, maximizing cross-institutional benefits under privacy constraints. Finally, representational efficiency optimization by an attentive cross-modal fusion model, which achieves fine-grained word-level alignment and acoustic-textual interaction. Evaluated on ADReSSo, FAL-AD achieves a state-of-the-art multi-modal accuracy of 91.52%, outperforming all centralized baselines and demonstrating a practical solution to the data efficiency dilemma. Our source code is publicly available at https://github.com/smileix/fal-ad.

