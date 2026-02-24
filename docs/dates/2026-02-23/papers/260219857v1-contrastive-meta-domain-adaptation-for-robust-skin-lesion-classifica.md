---
layout: default
title: Contrastive meta-domain adaptation for robust skin lesion classification across clinical and acquisition conditions
---

# Contrastive meta-domain adaptation for robust skin lesion classification across clinical and acquisition conditions
**arXiv**：[2602.19857v1](https://arxiv.org/abs/2602.19857) · [PDF](https://arxiv.org/pdf/2602.19857.pdf)  
**作者**：Rodrigo Mota, Kelvin Cunha, Emanoel dos Santos, Fábio Papais, Francisco Filho, Thales Bezerra, Erico Medeiros, Paulo Borba, Tsang Ing Ren  

**一句话要点**：提出基于视觉元域对比的适应策略，以提升皮肤病变分类在临床与采集条件下的鲁棒性。

**关键词**：皮肤病变分类, 领域适应, 视觉元域, 对比学习, 鲁棒性提升

## 3 点简述
- 核心问题：深度学习模型对皮肤图像采集变异性与领域特异性敏感，导致临床部署性能下降。
- 方法要点：利用视觉元域概念，从大尺度皮肤镜数据集迁移视觉表示至临床图像领域。
- 实验或效果：多数据集实验显示分类性能提升，皮肤镜与临床图像间性能差距减小。

## 摘要（原文）

> Deep learning models for dermatological image analysis remain sensitive to acquisition variability and domain-specific visual characteristics, leading to performance degradation when deployed in clinical settings. We investigate how visual artifacts and domain shifts affect deep learning-based skin lesion classification. We propose an adaptation strategy, grounded in the idea of visual meta-domains, that transfers visual representations from larger dermoscopic datasets into clinical image domains, thereby improving generalization robustness. Experiments across multiple dermatology datasets show consistent gains in classification performance and reduced gaps between dermoscopic and clinical images. These results emphasize the importance of domain-aware training for deployable systems.

