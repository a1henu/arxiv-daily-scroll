---
layout: default
title: LeafInst - Unified Instance Segmentation Network for Fine-Grained Forestry Leaf Phenotype Analysis: A New UAV based Benchmark
---

# LeafInst - Unified Instance Segmentation Network for Fine-Grained Forestry Leaf Phenotype Analysis: A New UAV based Benchmark
**arXiv**：[2603.03616v1](https://arxiv.org/abs/2603.03616) · [PDF](https://arxiv.org/pdf/2603.03616.pdf)  
**作者**：Taige Luo, Junru Xie, Chenyang Fan, Bingrong Liu, Ruisheng Wang, Yang Shao, Sheng Xu, Lin Cao  

**一句话要点**：提出LeafInst以解决开放环境中细粒度林业叶片实例分割问题

**关键词**：实例分割, 林业叶片分析, 无人机图像, 渐进特征金字塔网络, 动态非对称空间感知, 细粒度分割

## 3 点简述
- 核心问题：开放环境中细粒度林业叶片实例分割面临尺度变化、光照变化和不规则形态等挑战
- 方法要点：集成渐进特征金字塔网络、动态非对称空间感知模块和双残差动态异常回归头以提升性能
- 实验或效果：在Poplar-leaf数据集上达到68.4 mAP，优于YOLOv11和MaskDINO，并在PhenoBench基准上表现良好

## 摘要（原文）

> Intelligent forest tree breeding has advanced plant phenotyping, yet existing research largely focuses on large-leaf agricultural crops, with limited attention to fine-grained leaf analysis of sapling trees in open-field environments. Natural scenes introduce challenges including scale variation, illumination changes, and irregular leaf morphology. To address these issues, we collected UAV RGB imagery of field-grown saplings and constructed the Poplar-leaf dataset, containing 1,202 branches and 19,876 pixel-level annotated leaf instances. To our knowledge, this is the first instance segmentation dataset specifically designed for forestry leaves in open-field conditions. We propose LeafInst, a novel segmentation framework tailored for irregular and multi-scale leaf structures. The model integrates an Asymptotic Feature Pyramid Network (AFPN) for multi-scale perception, a Dynamic Asymmetric Spatial Perception (DASP) module for irregular shape modeling, and a dual-residual Dynamic Anomalous Regression Head (DARH) with Top-down Concatenation decoder Feature Fusion (TCFU) to improve detection and segmentation performance. On Poplar-leaf, LeafInst achieves 68.4 mAP, outperforming YOLOv11 by 7.1 percent and MaskDINO by 6.5 percent. On the public PhenoBench benchmark, it reaches 52.7 box mAP, exceeding MaskDINO by 3.4 percent. Additional experiments demonstrate strong generalization and practical utility for large-scale leaf phenotyping.

