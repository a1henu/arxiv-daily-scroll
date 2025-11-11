---
layout: default
title: Beyond Boundaries: Leveraging Vision Foundation Models for Source-Free Object Detection
---

# Beyond Boundaries: Leveraging Vision Foundation Models for Source-Free Object Detection
**arXiv**：[2511.07301v1](https://arxiv.org/abs/2511.07301) · [PDF](https://arxiv.org/pdf/2511.07301.pdf)  
**作者**：Huizai Yao, Sicheng Zhao, Pengteng Li, Yi Cui, Shuo Lu, Weiyu Guo, Yunfan Lu, Yijie Xu, Hui Xiong  

**一句话要点**：提出基于视觉基础模型的源自由目标检测框架，以提升跨域泛化能力

**关键词**：源自由目标检测, 视觉基础模型, 特征对齐, 伪标签融合, 跨域泛化, 对比学习

## 3 点简述
- 源自由目标检测依赖源模型内部知识，导致跨域泛化受限和伪标签偏差
- 引入三个模块：全局特征对齐、实例特征对齐和伪标签融合，利用视觉基础模型增强特征与标签质量
- 在六个基准测试中实现最优性能，验证方法在提升迁移性和判别性方面的有效性

## 摘要（原文）

> Source-Free Object Detection (SFOD) aims to adapt a source-pretrained object
> detector to a target domain without access to source data. However, existing
> SFOD methods predominantly rely on internal knowledge from the source model,
> which limits their capacity to generalize across domains and often results in
> biased pseudo-labels, thereby hindering both transferability and
> discriminability. In contrast, Vision Foundation Models (VFMs), pretrained on
> massive and diverse data, exhibit strong perception capabilities and broad
> generalization, yet their potential remains largely untapped in the SFOD
> setting. In this paper, we propose a novel SFOD framework that leverages VFMs
> as external knowledge sources to jointly enhance feature alignment and label
> quality. Specifically, we design three VFM-based modules: (1) Patch-weighted
> Global Feature Alignment (PGFA) distills global features from VFMs using
> patch-similarity-based weighting to enhance global feature transferability; (2)
> Prototype-based Instance Feature Alignment (PIFA) performs instance-level
> contrastive learning guided by momentum-updated VFM prototypes; and (3)
> Dual-source Enhanced Pseudo-label Fusion (DEPF) fuses predictions from
> detection VFMs and teacher models via an entropy-aware strategy to yield more
> reliable supervision. Extensive experiments on six benchmarks demonstrate that
> our method achieves state-of-the-art SFOD performance, validating the
> effectiveness of integrating VFMs to simultaneously improve transferability and
> discriminability.

