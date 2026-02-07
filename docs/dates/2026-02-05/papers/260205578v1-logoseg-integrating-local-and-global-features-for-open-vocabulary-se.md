---
layout: default
title: LoGoSeg: Integrating Local and Global Features for Open-Vocabulary Semantic Segmentation
---

# LoGoSeg: Integrating Local and Global Features for Open-Vocabulary Semantic Segmentation
**arXiv**：[2602.05578v1](https://arxiv.org/abs/2602.05578) · [PDF](https://arxiv.org/pdf/2602.05578.pdf)  
**作者**：Junyang Chen, Xiangbo Lv, Zhiqiang Kou, Xingdong Sheng, Ning Xu, Yiguo Qiao  

**一句话要点**：提出LoGoSeg框架，通过整合局部与全局特征解决开放词汇语义分割中的空间对齐和物体幻觉问题。

**关键词**：开放词汇语义分割, 视觉语言模型, 局部全局特征融合, 物体存在先验, 区域感知对齐, 单阶段框架

## 3 点简述
- 核心问题：现有方法依赖图像级预训练，导致空间对齐不精确，在模糊或杂乱场景中产生分割不匹配和物体幻觉。
- 方法要点：引入物体存在先验、区域感知对齐模块和双流融合机制，无需外部掩码提议或额外数据集，提升效率和精度。
- 实验或效果：在六个基准测试中展示竞争性性能和强泛化能力，验证了在开放词汇设置下的有效性。

## 摘要（原文）

> Open-vocabulary semantic segmentation (OVSS) extends traditional closed-set segmentation by enabling pixel-wise annotation for both seen and unseen categories using arbitrary textual descriptions. While existing methods leverage vision-language models (VLMs) like CLIP, their reliance on image-level pretraining often results in imprecise spatial alignment, leading to mismatched segmentations in ambiguous or cluttered scenes. However, most existing approaches lack strong object priors and region-level constraints, which can lead to object hallucination or missed detections, further degrading performance. To address these challenges, we propose LoGoSeg, an efficient single-stage framework that integrates three key innovations: (i) an object existence prior that dynamically weights relevant categories through global image-text similarity, effectively reducing hallucinations; (ii) a region-aware alignment module that establishes precise region-level visual-textual correspondences; and (iii) a dual-stream fusion mechanism that optimally combines local structural information with global semantic context. Unlike prior works, LoGoSeg eliminates the need for external mask proposals, additional backbones, or extra datasets, ensuring efficiency. Extensive experiments on six benchmarks (A-847, PC-459, A-150, PC-59, PAS-20, and PAS-20b) demonstrate its competitive performance and strong generalization in open-vocabulary settings.

