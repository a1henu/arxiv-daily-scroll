---
layout: default
title: Bio-inspired fine-tuning for selective transfer learning in image classification
---

# Bio-inspired fine-tuning for selective transfer learning in image classification
**arXiv**：[2601.11235v1](https://arxiv.org/abs/2601.11235) · [PDF](https://arxiv.org/pdf/2601.11235.pdf)  
**作者**：Ana Davila, Jacinto Colan, Yasuhisa Hasegawa  

**一句话要点**：提出BioTune自适应微调技术，以优化迁移学习在图像分类中的选择性层冻结与学习率调整。

**关键词**：迁移学习, 自适应微调, 进化优化, 图像分类, 层冻结, 学习率调整

## 3 点简述
- 核心问题：源域与目标域差异阻碍迁移学习效果，需高效微调策略。
- 方法要点：基于进化优化，自适应选择冻结层并调整未冻结层学习率，提升模型适应性。
- 实验或效果：在九个图像分类数据集上优于AutoRGN和LoRA，跨四种CNN架构表现稳定。

## 摘要（原文）

> Deep learning has significantly advanced image analysis across diverse domains but often depends on large, annotated datasets for success. Transfer learning addresses this challenge by utilizing pre-trained models to tackle new tasks with limited labeled data. However, discrepancies between source and target domains can hinder effective transfer learning. We introduce BioTune, a novel adaptive fine-tuning technique utilizing evolutionary optimization. BioTune enhances transfer learning by optimally choosing which layers to freeze and adjusting learning rates for unfrozen layers. Through extensive evaluation on nine image classification datasets, spanning natural and specialized domains such as medical imaging, BioTune demonstrates superior accuracy and efficiency over state-of-the-art fine-tuning methods, including AutoRGN and LoRA, highlighting its adaptability to various data characteristics and distribution changes. Additionally, BioTune consistently achieves top performance across four different CNN architectures, underscoring its flexibility. Ablation studies provide valuable insights into the impact of BioTune's key components on overall performance. The source code is available at https://github.com/davilac/BioTune.

