---
layout: default
title: Towards Unified Semantic and Controllable Image Fusion: A Diffusion Transformer Approach
---

# Towards Unified Semantic and Controllable Image Fusion: A Diffusion Transformer Approach
**arXiv**：[2512.07170v1](https://arxiv.org/abs/2512.07170) · [PDF](https://arxiv.org/pdf/2512.07170.pdf)  
**作者**：Jiayang Li, Chengjie Jiang, Junjun Jiang, Pengwei Liang, Jiayi Ma, Liqiang Nie  

**一句话要点**：提出DiTFuse扩散Transformer框架，实现语义可控的图像融合

**关键词**：图像融合, 扩散Transformer, 语义控制, 多模态对齐, 零样本泛化

## 3 点简述
- 现有图像融合方法在鲁棒性、适应性和可控性方面受限，缺乏用户意图整合能力
- DiTFuse通过联合编码图像与自然语言指令，在单一模型中实现端到端语义感知融合
- 实验在多个基准上显示优异性能，支持多级控制和零样本泛化

## 摘要（原文）

> Image fusion aims to blend complementary information from multiple sensing modalities, yet existing approaches remain limited in robustness, adaptability, and controllability. Most current fusion networks are tailored to specific tasks and lack the ability to flexibly incorporate user intent, especially in complex scenarios involving low-light degradation, color shifts, or exposure imbalance. Moreover, the absence of ground-truth fused images and the small scale of existing datasets make it difficult to train an end-to-end model that simultaneously understands high-level semantics and performs fine-grained multimodal alignment. We therefore present DiTFuse, instruction-driven Diffusion-Transformer (DiT) framework that performs end-to-end, semantics-aware fusion within a single model. By jointly encoding two images and natural-language instructions in a shared latent space, DiTFuse enables hierarchical and fine-grained control over fusion dynamics, overcoming the limitations of pre-fusion and post-fusion pipelines that struggle to inject high-level semantics. The training phase employs a multi-degradation masked-image modeling strategy, so the network jointly learns cross-modal alignment, modality-invariant restoration, and task-aware feature selection without relying on ground truth images. A curated, multi-granularity instruction dataset further equips the model with interactive fusion capabilities. DiTFuse unifies infrared-visible, multi-focus, and multi-exposure fusion-as well as text-controlled refinement and downstream tasks-within a single architecture. Experiments on public IVIF, MFF, and MEF benchmarks confirm superior quantitative and qualitative performance, sharper textures, and better semantic retention. The model also supports multi-level user control and zero-shot generalization to other multi-image fusion scenarios, including instruction-conditioned segmentation.

