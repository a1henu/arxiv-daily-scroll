---
layout: default
title: Beyond Paired Data: Self-Supervised UAV Geo-Localization from Reference Imagery Alone
---

# Beyond Paired Data: Self-Supervised UAV Geo-Localization from Reference Imagery Alone
**arXiv**：[2512.02737v1](https://arxiv.org/abs/2512.02737) · [PDF](https://arxiv.org/pdf/2512.02737.pdf)  
**作者**：Tristan Amadei, Enric Meinhardt-Llopis, Benedicte Bascle, Corentin Abgrall, Gabriele Facciolo  

**一句话要点**：提出CAEVL模型，通过仅用卫星图像训练解决无人机无GNSS环境下的定位问题。

**关键词**：无人机定位, 自监督学习, 域适应, 图像匹配, 卫星图像, 无GNSS环境

## 3 点简述
- 核心问题：现有方法依赖配对无人机-卫星数据集，成本高且获取困难，限制应用。
- 方法要点：采用自监督训练范式，通过增强策略模拟卫星与无人机视图间的域偏移，无需无人机图像。
- 实验或效果：在ViLD数据集上验证，性能媲美配对数据训练方法，展示强泛化能力。

## 摘要（原文）

> Image-based localization in GNSS-denied environments is critical for UAV autonomy. Existing state-of-the-art approaches rely on matching UAV images to geo-referenced satellite images; however, they typically require large-scale, paired UAV-satellite datasets for training. Such data are costly to acquire and often unavailable, limiting their applicability. To address this challenge, we adopt a training paradigm that removes the need for UAV imagery during training by learning directly from satellite-view reference images. This is achieved through a dedicated augmentation strategy that simulates the visual domain shift between satellite and real-world UAV views. We introduce CAEVL, an efficient model designed to exploit this paradigm, and validate it on ViLD, a new and challenging dataset of real-world UAV images that we release to the community. Our method achieves competitive performance compared to approaches trained with paired data, demonstrating its effectiveness and strong generalization capabilities.

