---
layout: default
title: Boosting Segment Anything Model to Generalize Visually Non-Salient Scenarios
---

# Boosting Segment Anything Model to Generalize Visually Non-Salient Scenarios
**arXiv**：[2601.00537v1](https://arxiv.org/abs/2601.00537) · [PDF](https://arxiv.org/pdf/2601.00537.pdf)  
**作者**：Guangqian Guo, Pengfei Chen, Yong Guo, Huafeng Chen, Boqiang Zhang, Shan Gao  

**一句话要点**：提出VNS-SAM以增强SAM在视觉非显著场景下的分割性能

**关键词**：视觉非显著分割, 零样本分割, SAM增强, 特征挖掘, 数据集构建

## 3 点简述
- 核心问题：SAM在视觉非显著场景（前景与背景对比度低）中分割性能受限
- 方法要点：通过Mask-Edge Token Interactive解码器和Non-Salient Feature Mining模块利用SAM低层特征
- 实验或效果：在VNS-SEG数据集上验证，零样本设置下性能优越，参数增量小且训练快速

## 摘要（原文）

> Segment Anything Model (SAM), known for its remarkable zero-shot segmentation capabilities, has garnered significant attention in the community. Nevertheless, its performance is challenged when dealing with what we refer to as visually non-salient scenarios, where there is low contrast between the foreground and background. In these cases, existing methods often cannot capture accurate contours and fail to produce promising segmentation results. In this paper, we propose Visually Non-Salient SAM (VNS-SAM), aiming to enhance SAM's perception of visually non-salient scenarios while preserving its original zero-shot generalizability. We achieve this by effectively exploiting SAM's low-level features through two designs: Mask-Edge Token Interactive decoder and Non-Salient Feature Mining module. These designs help the SAM decoder gain a deeper understanding of non-salient characteristics with only marginal parameter increments and computational requirements. The additional parameters of VNS-SAM can be optimized within 4 hours, demonstrating its feasibility and practicality. In terms of data, we established VNS-SEG, a unified dataset for various VNS scenarios, with more than 35K images, in contrast to previous single-task adaptations. It is designed to make the model learn more robust VNS features and comprehensively benchmark the model's segmentation performance and generalizability on VNS scenarios. Extensive experiments across various VNS segmentation tasks demonstrate the superior performance of VNS-SAM, particularly under zero-shot settings, highlighting its potential for broad real-world applications. Codes and datasets are publicly available at https://guangqian-guo.github.io/VNS-SAM.

