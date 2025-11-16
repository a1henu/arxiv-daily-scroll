---
layout: default
title: Decoupling Bias, Aligning Distributions: Synergistic Fairness Optimization for Deepfake Detection
---

# Decoupling Bias, Aligning Distributions: Synergistic Fairness Optimization for Deepfake Detection
**arXiv**：[2511.10150v1](https://arxiv.org/abs/2511.10150) · [PDF](https://arxiv.org/pdf/2511.10150.pdf)  
**作者**：Feng Ding, Wenhui Yi, Yunpeng Zhou, Xinan He, Hong Rao, Shu Hu  

**一句话要点**：提出双机制协同优化框架以提升深度伪造检测的公平性

**关键词**：深度伪造检测, 公平性优化, 结构解耦, 分布对齐, 数字身份安全

## 3 点简述
- 核心问题：深度伪造检测模型存在对性别和种族等人口群体的偏见，影响公平性。
- 方法要点：结合结构公平解耦和全局分布对齐，减少模型偏见并保持检测精度。
- 实验效果：在多个领域实验中，提升组间和组内公平性，同时维持总体检测准确率。

## 摘要（原文）

> Fairness is a core element in the trustworthy deployment of deepfake detection models, especially in the field of digital identity security. Biases in detection models toward different demographic groups, such as gender and race, may lead to systemic misjudgments, exacerbating the digital divide and social inequities. However, current fairness-enhanced detectors often improve fairness at the cost of detection accuracy. To address this challenge, we propose a dual-mechanism collaborative optimization framework. Our proposed method innovatively integrates structural fairness decoupling and global distribution alignment: decoupling channels sensitive to demographic groups at the model architectural level, and subsequently reducing the distance between the overall sample distribution and the distributions corresponding to each demographic group at the feature level. Experimental results demonstrate that, compared with other methods, our framework improves both inter-group and intra-group fairness while maintaining overall detection accuracy across domains.

