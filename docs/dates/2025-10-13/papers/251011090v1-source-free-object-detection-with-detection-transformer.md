---
layout: default
title: Source-Free Object Detection with Detection Transformer
---

# Source-Free Object Detection with Detection Transformer
**arXiv**：[2510.11090v1](https://arxiv.org/abs/2510.11090) · [PDF](https://arxiv.org/pdf/2510.11090.pdf)  
**作者**：Huizai Yao, Sicheng Zhao, Shuo Lu, Hui Chen, Yangyang Li, Guoping Liu, Tengfei Xing, Chenggang Yan, Jianhua Tao, Guiguang Ding  

**一句话要点**：提出FRANCK框架以解决源自由目标检测中DETR模型的适应问题

**关键词**：源自由目标检测, 检测变换器, 特征重加权, 对比学习, 查询融合蒸馏, 自训练优化

## 3 点简述
- 核心问题：源自由目标检测中DETR模型缺乏专门适配，导致性能受限。
- 方法要点：通过特征重加权、对比学习和查询融合蒸馏模块增强模型鲁棒性。
- 实验或效果：在多个基准测试中实现最先进性能，验证了方法的有效性。

## 摘要（原文）

> Source-Free Object Detection (SFOD) enables knowledge transfer from a source
> domain to an unsupervised target domain for object detection without access to
> source data. Most existing SFOD approaches are either confined to conventional
> object detection (OD) models like Faster R-CNN or designed as general solutions
> without tailored adaptations for novel OD architectures, especially Detection
> Transformer (DETR). In this paper, we introduce Feature Reweighting ANd
> Contrastive Learning NetworK (FRANCK), a novel SFOD framework specifically
> designed to perform query-centric feature enhancement for DETRs. FRANCK
> comprises four key components: (1) an Objectness Score-based Sample Reweighting
> (OSSR) module that computes attention-based objectness scores on multi-scale
> encoder feature maps, reweighting the detection loss to emphasize
> less-recognized regions; (2) a Contrastive Learning with Matching-based Memory
> Bank (CMMB) module that integrates multi-level features into memory banks,
> enhancing class-wise contrastive learning; (3) an Uncertainty-weighted
> Query-fused Feature Distillation (UQFD) module that improves feature
> distillation through prediction quality reweighting and query feature fusion;
> and (4) an improved self-training pipeline with a Dynamic Teacher Updating
> Interval (DTUI) that optimizes pseudo-label quality. By leveraging these
> components, FRANCK effectively adapts a source-pre-trained DETR model to a
> target domain with enhanced robustness and generalization. Extensive
> experiments on several widely used benchmarks demonstrate that our method
> achieves state-of-the-art performance, highlighting its effectiveness and
> compatibility with DETR-based SFOD models.

