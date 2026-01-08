---
layout: default
title: FLNet: Flood-Induced Agriculture Damage Assessment using Super Resolution of Satellite Images
---

# FLNet: Flood-Induced Agriculture Damage Assessment using Super Resolution of Satellite Images
**arXiv**：[2601.03884v1](https://arxiv.org/abs/2601.03884) · [PDF](https://arxiv.org/pdf/2601.03884.pdf)  
**作者**：Sanidhya Ghosal, Anurag Sharma, Sushil Ghildiyal, Mukesh Saini  

**一句话要点**：提出FLNet，通过超分辨率增强卫星图像以解决洪水后农作物损害评估问题。

**关键词**：洪水损害评估, 卫星图像超分辨率, 深度学习分类, 农作物监测, 灾害管理

## 3 点简述
- 核心问题：洪水后农作物损害评估依赖传统方法慢且偏，卫星方法受云层和低分辨率限制。
- 方法要点：使用深度学习架构FLNet，将Sentinel-2图像从10米超分辨率至3米后分类损害。
- 实验或效果：在BFCD-22数据集上测试，全损害F1分数从0.83提升至0.89，接近商业高分辨率图像。

## 摘要（原文）

> Distributing government relief efforts after a flood is challenging. In India, the crops are widely affected by floods; therefore, making rapid and accurate crop damage assessment is crucial for effective post-disaster agricultural management. Traditional manual surveys are slow and biased, while current satellite-based methods face challenges like cloud cover and low spatial resolution. Therefore, to bridge this gap, this paper introduced FLNet, a novel deep learning based architecture that used super-resolution to enhance the 10 m spatial resolution of Sentinel-2 satellite images into 3 m resolution before classifying damage. We tested our model on the Bihar Flood Impacted Croplands Dataset (BFCD-22), and the results showed an improved critical "Full Damage" F1-score from 0.83 to 0.89, nearly matching the 0.89 score of commercial high-resolution imagery. This work presented a cost-effective and scalable solution, paving the way for a nationwide shift from manual to automated, high-fidelity damage assessment.

