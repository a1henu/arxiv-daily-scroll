---
layout: default
title: Using Legacy Polysomnography Data to Train a Radar System to Quantify Sleep in Older Adults and People living with Dementia
---

# Using Legacy Polysomnography Data to Train a Radar System to Quantify Sleep in Older Adults and People living with Dementia
**arXiv**：[2601.04057v1](https://arxiv.org/abs/2601.04057) · [PDF](https://arxiv.org/pdf/2601.04057.pdf)  
**作者**：M. Yin, K. G. Ravindran, C. Hadjipanayi, A. Bannon, A. Rapeaux, C. Della Monica, T. S. Lande, Derk-Jan Dijk, T. G. Constandinou  

**一句话要点**：提出基于对抗学习的深度迁移学习框架，利用多导睡眠图数据增强雷达睡眠分期性能

**关键词**：超宽带雷达, 睡眠分期, 迁移学习, 对抗学习, 多导睡眠图, 老年人健康监测

## 3 点简述
- 核心问题：雷达睡眠数据有限，难以构建泛化性强的模型。
- 方法要点：结合多导睡眠图与雷达数据，采用对抗学习进行领域适应。
- 实验或效果：在47名老年人雷达数据集上，四分类准确率达79.5%。

## 摘要（原文）

> Objective: Ultra-wideband radar technology offers a promising solution for unobtrusive and cost-effective in-home sleep monitoring. However, the limited availability of radar sleep data poses challenges in building robust models that generalize across diverse cohorts and environments. This study proposes a novel deep transfer learning framework to enhance sleep stage classification using radar data. Methods: An end-to-end neural network was developed to classify sleep stages based on nocturnal respiratory and motion signals. The network was trained using a combination of large-scale polysomnography (PSG) datasets and radar data. A domain adaptation approach employing adversarial learning was utilized to bridge the knowledge gap between PSG and radar signals. Validation was performed on a radar dataset of 47 older adults (mean age: 71.2), including 18 participants with prodromal or mild Alzheimer disease. Results: The proposed network structure achieves an accuracy of 79.5% with a Kappa value of 0.65 when classifying wakefulness, rapid eye movement, light sleep and deep sleep. Experimental results confirm that our deep transfer learning approach significantly enhances automatic sleep staging performance in the target domain. Conclusion: This method effectively addresses challenges associated with data variability and limited sample size, substantially improving the reliability of automatic sleep staging models, especially in contexts where radar data is limited. Significance: The findings underscore the viability of UWB radar as a nonintrusive, forward-looking sleep assessment tool that could significantly benefit care for older people and people with neurodegenerative disorders.

