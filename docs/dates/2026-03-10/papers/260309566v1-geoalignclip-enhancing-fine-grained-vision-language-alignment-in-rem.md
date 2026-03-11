---
layout: default
title: GeoAlignCLIP: Enhancing Fine-Grained Vision-Language Alignment in Remote Sensing via Multi-Granular Consistency Learning
---

# GeoAlignCLIP: Enhancing Fine-Grained Vision-Language Alignment in Remote Sensing via Multi-Granular Consistency Learning
**arXiv**：[2603.09566v1](https://arxiv.org/abs/2603.09566) · [PDF](https://arxiv.org/pdf/2603.09566.pdf)  
**作者**：Xiao Yang, Ronghao Fu, Zhuoran Duan, Zhiwen Lin, Xueyan Liu, Bo Yang  

**一句话要点**：提出GeoAlignCLIP以解决遥感中细粒度视觉-语言对齐不足的问题

**关键词**：遥感视觉-语言对齐, 多粒度一致性学习, 细粒度语义对齐, RSFG-100k数据集, 区域级标注

## 3 点简述
- 现有方法依赖全局对齐，难以整合多粒度视觉与文本信息，限制细粒度任务性能。
- 通过多粒度语义对齐和模态内一致性学习，实现图像区域与文本概念的精确对齐。
- 构建RSFG-100k数据集，并在多个基准上验证模型优于现有方法，提升对齐鲁棒性。

## 摘要（原文）

> Vision-language pretraining models have made significant progress in bridging remote sensing imagery with natural language. However, existing approaches often fail to effectively integrate multi-granular visual and textual information, relying primarily on global image-text alignment. This limitation hinders the model's ability to accurately capture fine-grained details in images, thus restricting its performance in complex, fine-grained tasks. To address this, we propose GeoAlignCLIP, a unified framework that achieves fine-grained alignment in remote sensing tasks by learning multi-granular semantic alignments and incorporating intra-modal consistency, enabling more precise visual-semantic alignment between image regions and text concepts. Additionally, we construct RSFG-100k, a fine-granular remote sensing dataset containing scene descriptions, region-level annotations, and challenging hard-negative samples, providing hierarchical supervision for model training. Extensive experiments conducted on multiple public remote-sensing benchmarks demonstrate that GeoAlignCLIP consistently outperforms existing RS-specific methods across diverse tasks, exhibiting more robust and accurate fine-grained vision-language alignment.

