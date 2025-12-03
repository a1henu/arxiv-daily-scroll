---
layout: default
title: OmniPerson: Unified Identity-Preserving Pedestrian Generation
---

# OmniPerson: Unified Identity-Preserving Pedestrian Generation
**arXiv**：[2512.02554v1](https://arxiv.org/abs/2512.02554) · [PDF](https://arxiv.org/pdf/2512.02554.pdf)  
**作者**：Changxiao Ma, Chao Yuan, Xincheng Shi, Yuzhuo Ma, Yongfei Zhang, Longkun Zhou, Yujia Zhang, Shangze Li, Yifan Xu  

**一句话要点**：提出OmniPerson统一身份保持行人生成管道，以解决行人重识别数据不足问题

**关键词**：行人重识别, 数据增强, 身份保持生成, 多模态生成, 行人数据集

## 3 点简述
- 行人重识别面临数据隐私和标注成本高导致训练数据缺乏的挑战
- OmniPerson提供全属性控制，支持多模态生成，并设计Multi-Refer Fuser确保身份一致性
- 实验显示OmniPerson在生成质量和身份一致性上达到先进水平，增强数据集能提升重识别模型性能

## 摘要（原文）

> Person re-identification (ReID) suffers from a lack of large-scale high-quality training data due to challenges in data privacy and annotation costs. While previous approaches have explored pedestrian generation for data augmentation, they often fail to ensure identity consistency and suffer from insufficient controllability, thereby limiting their effectiveness in dataset augmentation. To address this, We introduce OmniPerson, the first unified identity-preserving pedestrian generation pipeline for visible/infrared image/video ReID tasks. Our contributions are threefold: 1) We proposed OmniPerson, a unified generation model, offering holistic and fine-grained control over all key pedestrian attributes. Supporting RGB/IR modality image/video generation with any number of reference images, two kinds of person poses, and text. Also including RGB-to-IR transfer and image super-resolution abilities.2) We designed Multi-Refer Fuser for robust identity preservation with any number of reference images as input, making OmniPerson could distill a unified identity from a set of multi-view reference images, ensuring our generated pedestrians achieve high-fidelity pedestrian generation.3) We introduce PersonSyn, the first large-scale dataset for multi-reference, controllable pedestrian generation, and present its automated curation pipeline which transforms public, ID-only ReID benchmarks into a richly annotated resource with the dense, multi-modal supervision required for this task. Experimental results demonstrate that OmniPerson achieves SoTA in pedestrian generation, excelling in both visual fidelity and identity consistency. Furthermore, augmenting existing datasets with our generated data consistently improves the performance of ReID models. We will open-source the full codebase, pretrained model, and the PersonSyn dataset.

