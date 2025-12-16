---
layout: default
title: Sharpness-aware Dynamic Anchor Selection for Generalized Category Discovery
---

# Sharpness-aware Dynamic Anchor Selection for Generalized Category Discovery
**arXiv**：[2512.12925v1](https://arxiv.org/abs/2512.12925) · [PDF](https://arxiv.org/pdf/2512.12925.pdf)  
**作者**：Zhimao Peng, Enguang Wang, Fei Yang, Xialei Liu, Ming-Ming Cheng  

**一句话要点**：提出Sharpness-aware Dynamic Anchor Selection以解决广义类别发现中伪标签噪声问题

**关键词**：广义类别发现, 伪标签噪声, 损失锐度惩罚, 动态锚点选择, 开放世界学习

## 3 点简述
- 核心问题：大预训练模型偏好特定视觉模式，导致未标记数据编码伪相关和生成噪声伪标签。
- 方法要点：引入损失锐度惩罚增强模型鲁棒性，动态锚点选择基于KNN密度和类概率选取未知类代表样本。
- 实验或效果：在多个GCD基准测试中实现最先进结果，有效减轻伪标签噪声。

## 摘要（原文）

> Generalized category discovery (GCD) is an important and challenging task in open-world learning. Specifically, given some labeled data of known classes, GCD aims to cluster unlabeled data that contain both known and unknown classes. Current GCD methods based on parametric classification adopt the DINO-like pseudo-labeling strategy, where the sharpened probability output of one view is used as supervision information for the other view. However, large pre-trained models have a preference for some specific visual patterns, resulting in encoding spurious correlation for unlabeled data and generating noisy pseudo-labels. To address this issue, we propose a novel method, which contains two modules: Loss Sharpness Penalty (LSP) and Dynamic Anchor Selection (DAS). LSP enhances the robustness of model parameters to small perturbations by minimizing the worst-case loss sharpness of the model, which suppressing the encoding of trivial features, thereby reducing overfitting of noise samples and improving the quality of pseudo-labels. Meanwhile, DAS selects representative samples for the unknown classes based on KNN density and class probability during the model training and assigns hard pseudo-labels to them, which not only alleviates the confidence difference between known and unknown classes but also enables the model to quickly learn more accurate feature distribution for the unknown classes, thus further improving the clustering accuracy. Extensive experiments demonstrate that the proposed method can effectively mitigate the noise of pseudo-labels, and achieve state-of-the-art results on multiple GCD benchmarks.

