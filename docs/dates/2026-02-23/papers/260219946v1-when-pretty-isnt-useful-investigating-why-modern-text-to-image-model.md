---
layout: default
title: When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators
---

# When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators
**arXiv**：[2602.19946v1](https://arxiv.org/abs/2602.19946) · [PDF](https://arxiv.org/pdf/2602.19946.pdf)  
**作者**：Krzysztof Adamkiewicz, Brian Moser, Stanislav Frolov, Tobias Christian Nauen, Federico Raue, Andreas Dengel  

**一句话要点**：揭示现代文本到图像模型作为训练数据生成器时因美学中心分布导致性能下降

**关键词**：文本到图像模型, 合成数据生成, 分类器训练, 数据分布分析, 视觉真实感, 训练数据可靠性

## 3 点简述
- 核心问题：现代文本到图像模型生成合成数据时，视觉真实感提升但分类准确性在真实测试数据上下降
- 方法要点：使用2022至2025年先进模型生成大规模合成数据集，训练标准分类器并评估真实测试性能
- 实验或效果：分析显示模型分布窄化，美学中心化削弱多样性和标签-图像对齐，挑战生成真实感等同于数据真实感的假设

## 摘要（原文）

> Recent text-to-image (T2I) diffusion models produce visually stunning images and demonstrate excellent prompt following. But do they perform well as synthetic vision data generators? In this work, we revisit the promise of synthetic data as a scalable substitute for real training sets and uncover a surprising performance regression. We generate large-scale synthetic datasets using state-of-the-art T2I models released between 2022 and 2025, train standard classifiers solely on this synthetic data, and evaluate them on real test data. Despite observable advances in visual fidelity and prompt adherence, classification accuracy on real test data consistently declines with newer T2I models as training data generators. Our analysis reveals a hidden trend: These models collapse to a narrow, aesthetic-centric distribution that undermines diversity and label-image alignment. Overall, our findings challenge a growing assumption in vision research, namely that progress in generative realism implies progress in data realism. We thus highlight an urgent need to rethink the capabilities of modern T2I models as reliable training data generators.

