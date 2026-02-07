---
layout: default
title: ShapePuri: Shape Guided and Appearance Generalized Adversarial Purification
---

# ShapePuri: Shape Guided and Appearance Generalized Adversarial Purification
**arXiv**：[2602.05175v1](https://arxiv.org/abs/2602.05175) · [PDF](https://arxiv.org/pdf/2602.05175.pdf)  
**作者**：Zhe Li, Bernhard Kainz  

**一句话要点**：提出ShapePuri框架，通过形状引导和外观去偏增强对抗鲁棒性

**关键词**：对抗防御, 形状引导, 外观去偏, 鲁棒性增强, 深度学习安全

## 3 点简述
- 核心问题：现有对抗防御方法如扩散净化计算成本高且信息损失大
- 方法要点：集成形状编码模块提供几何指导，全局外观去偏模块减少外观偏差
- 实验或效果：在AutoAttack协议下实现84.06%干净准确率和81.64%鲁棒准确率

## 摘要（原文）

> Deep neural networks demonstrate impressive performance in visual recognition, but they remain vulnerable to adversarial attacks that is imperceptible to the human. Although existing defense strategies such as adversarial training and purification have achieved progress, diffusion-based purification often involves high computational costs and information loss. To address these challenges, we introduce Shape Guided Purification (ShapePuri), a novel defense framework enhances robustness by aligning model representations with stable structural invariants. ShapePuri integrates two components: a Shape Encoding Module (SEM) that provides dense geometric guidance through Signed Distance Functions (SDF), and a Global Appearance Debiasing (GAD) module that mitigates appearance bias via stochastic transformations. In our experiments, ShapePuri achieves $84.06\%$ clean accuracy and $81.64\%$ robust accuracy under the AutoAttack protocol, representing the first defense framework to surpass the $80\%$ threshold on this benchmark. Our approach provides a scalable and efficient adversarial defense that preserves prediction stability during inference without requiring auxiliary modules or additional computational cost.

