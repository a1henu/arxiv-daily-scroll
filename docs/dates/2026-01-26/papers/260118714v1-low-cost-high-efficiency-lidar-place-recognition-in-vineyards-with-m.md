---
layout: default
title: Low Cost, High Efficiency: LiDAR Place Recognition in Vineyards with Matryoshka Representation Learning
---

# Low Cost, High Efficiency: LiDAR Place Recognition in Vineyards with Matryoshka Representation Learning
**arXiv**：[2601.18714v1](https://arxiv.org/abs/2601.18714) · [PDF](https://arxiv.org/pdf/2601.18714.pdf)  
**作者**：Judith Vilella-Cantos, Mauro Martini, Marcello Chiaberge, Mónica Ballesta, David Valiente  

**一句话要点**：提出MinkUNeXt-VINE方法，以低成本稀疏LiDAR实现葡萄园高效地点识别。

**关键词**：地点识别, LiDAR感知, 表示学习, 农业机器人, 实时系统

## 3 点简述
- 核心问题：农业环境无结构且缺乏地标，地点识别对移动机器人具挑战性。
- 方法要点：采用预处理和Matryoshka表示学习多损失方法，优化低维输出与实时效率。
- 实验或效果：在长期葡萄园数据集上验证，优于现有方法，代码开源可复现。

## 摘要（原文）

> Localization in agricultural environments is challenging due to their unstructured nature and lack of distinctive landmarks. Although agricultural settings have been studied in the context of object classification and segmentation, the place recognition task for mobile robots is not trivial in the current state of the art. In this study, we propose MinkUNeXt-VINE, a lightweight, deep-learning-based method that surpasses state-of-the-art methods in vineyard environments thanks to its pre-processing and Matryoshka Representation Learning multi-loss approach. Our method prioritizes enhanced performance with low-cost, sparse LiDAR inputs and lower-dimensionality outputs to ensure high efficiency in real-time scenarios. Additionally, we present a comprehensive ablation study of the results on various evaluation cases and two extensive long-term vineyard datasets employing different LiDAR sensors. The results demonstrate the efficiency of the trade-off output produced by this approach, as well as its robust performance on low-cost and low-resolution input data. The code is publicly available for reproduction.

