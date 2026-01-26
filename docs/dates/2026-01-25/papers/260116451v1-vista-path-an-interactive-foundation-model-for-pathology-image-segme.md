---
layout: default
title: VISTA-PATH: An interactive foundation model for pathology image segmentation and quantitative analysis in computational pathology
---

# VISTA-PATH: An interactive foundation model for pathology image segmentation and quantitative analysis in computational pathology
**arXiv**：[2601.16451v1](https://arxiv.org/abs/2601.16451) · [PDF](https://arxiv.org/pdf/2601.16451.pdf)  
**作者**：Peixian Liang, Songhao Li, Shunsuke Koga, Yutong Li, Zahra Alipour, Yucheng Tang, Daguang Xu, Zhi Huang  

**一句话要点**：提出VISTA-PATH交互式基础模型，以解决病理图像分割在计算病理学中的静态预测问题。

**关键词**：病理图像分割, 交互式基础模型, 计算病理学, 组织微环境分析, 多类分割

## 3 点简述
- 核心问题：现有分割基础模型将分割视为静态视觉预测任务，与病理学需求对齐不佳。
- 方法要点：结合视觉上下文、语义组织描述和可选空间提示，实现交互式多类分割。
- 实验或效果：在多个基准测试中优于现有模型，支持人机交互细化，并提升组织微环境分析。

## 摘要（原文）

> Accurate semantic segmentation for histopathology image is crucial for quantitative tissue analysis and downstream clinical modeling. Recent segmentation foundation models have improved generalization through large-scale pretraining, yet remain poorly aligned with pathology because they treat segmentation as a static visual prediction task. Here we present VISTA-PATH, an interactive, class-aware pathology segmentation foundation model designed to resolve heterogeneous structures, incorporate expert feedback, and produce pixel-level segmentation that are directly meaningful for clinical interpretation. VISTA-PATH jointly conditions segmentation on visual context, semantic tissue descriptions, and optional expert-provided spatial prompts, enabling precise multi-class segmentation across heterogeneous pathology images. To support this paradigm, we curate VISTA-PATH Data, a large-scale pathology segmentation corpus comprising over 1.6 million image-mask-text triplets spanning 9 organs and 93 tissue classes. Across extensive held-out and external benchmarks, VISTA-PATH consistently outperforms existing segmentation foundation models. Importantly, VISTA-PATH supports dynamic human-in-the-loop refinement by propagating sparse, patch-level bounding-box annotation feedback into whole-slide segmentation. Finally, we show that the high-fidelity, class-aware segmentation produced by VISTA-PATH is a preferred model for computational pathology. It improve tissue microenvironment analysis through proposed Tumor Interaction Score (TIS), which exhibits strong and significant associations with patient survival. Together, these results establish VISTA-PATH as a foundation model that elevates pathology image segmentation from a static prediction to an interactive and clinically grounded representation for digital pathology. Source code and demo can be found at https://github.com/zhihuanglab/VISTA-PATH.

