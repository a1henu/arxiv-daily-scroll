---
layout: default
title: AnyAD: Unified Any-Modality Anomaly Detection in Incomplete Multi-Sequence MRI
---

# AnyAD: Unified Any-Modality Anomaly Detection in Incomplete Multi-Sequence MRI
**arXiv**：[2512.21264v1](https://arxiv.org/abs/2512.21264) · [PDF](https://arxiv.org/pdf/2512.21264.pdf)  
**作者**：Changwei Wu, Yifei Chen, Yuxin Du, Mingxuan Liu, Jinying Zong, Beining Wu, Jie Dong, Feiwei Qin, Yunkang Cao, Qiyuan Tian  

**一句话要点**：提出AnyAD框架以解决脑MRI中任意模态组合下的异常检测问题

**关键词**：多模态异常检测, 脑MRI分析, 特征分布对齐, 正常原型提取, 任意模态推理, 医学图像处理

## 3 点简述
- 核心问题：脑MRI异常检测面临标注稀缺和模态缺失的挑战，现有方法难以泛化到未见模态组合
- 方法要点：采用双路径DINOv2编码器与特征分布对齐机制，结合正常原型提取器和引导解码器，支持任意模态推理
- 实验或效果：在多个数据集上超越先进基线，在7种模态组合中实现优越泛化性能

## 摘要（原文）

> Reliable anomaly detection in brain MRI remains challenging due to the scarcity of annotated abnormal cases and the frequent absence of key imaging modalities in real clinical workflows. Existing single-class or multi-class anomaly detection (AD) models typically rely on fixed modality configurations, require repetitive training, or fail to generalize to unseen modality combinations, limiting their clinical scalability. In this work, we present a unified Any-Modality AD framework that performs robust anomaly detection and localization under arbitrary MRI modality availability. The framework integrates a dual-pathway DINOv2 encoder with a feature distribution alignment mechanism that statistically aligns incomplete-modality features with full-modality representations, enabling stable inference even with severe modality dropout. To further enhance semantic consistency, we introduce an Intrinsic Normal Prototypes (INPs) extractor and an INP-guided decoder that reconstruct only normal anatomical patterns while naturally amplifying abnormal deviations. Through randomized modality masking and indirect feature completion during training, the model learns to adapt to all modality configurations without re-training. Extensive experiments on BraTS2018, MU-Glioma-Post, and Pretreat-MetsToBrain-Masks demonstrate that our approach consistently surpasses state-of-the-art industrial and medical AD baselines across 7 modality combinations, achieving superior generalization. This study establishes a scalable paradigm for multimodal medical AD under real-world, imperfect modality conditions. Our source code is available at https://github.com/wuchangw/AnyAD.

