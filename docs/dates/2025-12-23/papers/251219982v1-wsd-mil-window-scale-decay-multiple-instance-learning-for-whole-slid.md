---
layout: default
title: WSD-MIL: Window Scale Decay Multiple Instance Learning for Whole Slide Image Classification
---

# WSD-MIL: Window Scale Decay Multiple Instance Learning for Whole Slide Image Classification
**arXiv**：[2512.19982v1](https://arxiv.org/abs/2512.19982) · [PDF](https://arxiv.org/pdf/2512.19982.pdf)  
**作者**：Le Feng, Li Xiao  

**一句话要点**：提出WSD-MIL以解决全切片图像分类中实例关系建模与计算效率问题

**关键词**：全切片图像分类, 多实例学习, 窗口尺度衰减注意力, 计算病理学, Transformer优化

## 3 点简述
- 现有MIL方法忽视全切片图像内实例的复杂语义关系，Transformer方法计算复杂度高且难以处理肿瘤区域尺度变化
- WSD-MIL包含基于窗口尺度衰减的注意力模块和基于挤压激励的区域门模块，以捕获多尺度局部关系并增强全局建模
- 在CAMELYON16和TCGA-BRCA数据集上实现最优性能，计算内存减少62%

## 摘要（原文）

> In recent years, the integration of pre-trained foundational models with multiple instance learning (MIL) has improved diagnostic accuracy in computational pathology. However, existing MIL methods focus on optimizing feature extractors and aggregation strategies while overlooking the complex semantic relationships among instances within whole slide image (WSI). Although Transformer-based MIL approaches aiming to model instance dependencies, the quadratic computational complexity limits their scalability to large-scale WSIs. Moreover, due to the pronounced variations in tumor region scales across different WSIs, existing Transformer-based methods employing fixed-scale attention mechanisms face significant challenges in precisely capturing local instance correlations and fail to account for the distance-based decay effect of patch relevance. To address these challenges, we propose window scale decay MIL (WSD-MIL), designed to enhance the capacity to model tumor regions of varying scales while improving computational efficiency. WSD-MIL comprises: 1) a window scale decay based attention module, which employs a cluster-based sampling strategy to reduce computational costs while progressively decaying attention window-scale to capture local instance relationships at varying scales; and 2) a squeeze-and-excitation based region gate module, which dynamically adjusts window weights to enhance global information modeling. Experimental results demonstrate that WSD-MIL achieves state-of-the-art performance on the CAMELYON16 and TCGA-BRCA datasets while reducing 62% of the computational memory. The code will be publicly available.

