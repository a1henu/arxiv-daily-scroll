---
layout: default
title: Missing No More: Dictionary-Guided Cross-Modal Image Fusion under Missing Infrared
---

# Missing No More: Dictionary-Guided Cross-Modal Image Fusion under Missing Infrared
**arXiv**：[2603.08018v1](https://arxiv.org/abs/2603.08018) · [PDF](https://arxiv.org/pdf/2603.08018.pdf)  
**作者**：Yafei Zhang, Meng Ma, Huafeng Li, Yu Liu  

**一句话要点**：提出字典引导的跨模态图像融合框架，以解决红外缺失下的红外-可见光图像融合问题。

**关键词**：红外-可见光图像融合, 字典学习, 跨模态推断, 系数域表示, 缺失模态处理, 可解释性框架

## 3 点简述
- 核心问题：红外-可见光图像融合在红外模态缺失时，现有方法依赖像素空间生成，难以控制且缺乏可解释性。
- 方法要点：基于共享卷积字典，通过系数域表示学习、可见光引导的红外推断和自适应融合，实现编码-转移-融合-重建流程。
- 实验或效果：在红外缺失设置下，实验显示感知质量和下游检测性能一致提升，代码已开源。

## 摘要（原文）

> Infrared-visible (IR-VIS) image fusion is vital for perception and security, yet most methods rely on the availability of both modalities during training and inference. When the infrared modality is absent, pixel-space generative substitutes become hard to control and inherently lack interpretability. We address missing-IR fusion by proposing a dictionary-guided, coefficient-domain framework built upon a shared convolutional dictionary. The pipeline comprises three key components: (1) Joint Shared-dictionary Representation Learning (JSRL) learns a unified and interpretable atom space shared by both IR and VIS modalities; (2) VIS-Guided IR Inference (VGII) transfers VIS coefficients to pseudo-IR coefficients in the coefficient domain and performs a one-step closed-loop refinement guided by a frozen large language model as a weak semantic prior; and (3) Adaptive Fusion via Representation Inference (AFRI) merges VIS structures and inferred IR cues at the atom level through window attention and convolutional mixing, followed by reconstruction with the shared dictionary. This encode-transfer-fuse-reconstruct pipeline avoids uncontrolled pixel-space generation while ensuring prior preservation within interpretable dictionary-coefficient representation. Experiments under missing-IR settings demonstrate consistent improvements in perceptual quality and downstream detection performance. To our knowledge, this represents the first framework that jointly learns a shared dictionary and performs coefficient-domain inference-fusion to tackle missing-IR fusion. The source code is publicly available at https://github.com/harukiv/DCMIF.

