---
layout: default
title: Enhanced Food Category Recognition under Illumination-Induced Domain Shift
---

# Enhanced Food Category Recognition under Illumination-Induced Domain Shift
**arXiv**：[2602.08491v1](https://arxiv.org/abs/2602.08491) · [PDF](https://arxiv.org/pdf/2602.08491.pdf)  
**作者**：Keonvin Park, Aditya Pal, Jin Hong Mok  

**一句话要点**：提出光照增强数据集以提升多类食品识别在光照变化下的鲁棒性

**关键词**：食品识别, 光照鲁棒性, 域偏移, 合成数据增强, 跨数据集评估

## 3 点简述
- 核心问题：光照变化导致食品识别系统在真实场景中性能显著下降，现有数据集缺乏光照标注
- 方法要点：通过系统改变光照温度和强度构建合成增强数据集，用于可控的鲁棒性分析
- 实验或效果：光照增强显著提高跨数据集评估的识别准确率，同时保持实时性能

## 摘要（原文）

> Visual food recognition systems deployed in real-world environments, such as automated conveyor-belt inspection, are highly sensitive to domain shifts caused by illumination changes. While recent studies have shown that lighting variations can significantly distort food perception by both humans and AI, existing works are often limited to single food categories or controlled settings, and most public food datasets lack explicit illumination annotations.
>   In this work, we investigate illumination-induced domain shift in multi-class food category recognition using two widely adopted datasets, Food-101 and Fruits-360. We demonstrate substantial accuracy degradation under cross-dataset evaluation due to mismatched visual conditions. To address this challenge, we construct synthetic illumination-augmented datasets by systematically varying light temperature and intensity, enabling controlled robustness analysis without additional labels.
>   We further evaluate cross-dataset transfer learning and domain generalization, with a focus on illumination-sensitive target categories such as apple-based classes. Experimental results show that illumination-aware augmentation significantly improves recognition robustness under domain shift while preserving real-time performance. Our findings highlight the importance of illumination robustness and provide practical insights for deploying reliable food recognition systems in real-world inspection scenarios.

