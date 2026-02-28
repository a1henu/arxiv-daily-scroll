---
layout: default
title: Face Time Traveller : Travel Through Ages Without Losing Identity
---

# Face Time Traveller : Travel Through Ages Without Losing Identity
**arXiv**：[2602.22819v1](https://arxiv.org/abs/2602.22819) · [PDF](https://arxiv.org/pdf/2602.22819.pdf)  
**作者**：Purbayan Kar, Ayush Ghadiya, Vishal Chudasama, Pankaj Wasnik, C. V. Jawahar  

**一句话要点**：提出Face Time Traveller框架，通过扩散模型实现高保真、身份一致的人脸年龄变换。

**关键词**：人脸年龄变换, 扩散模型, 身份保持, 注意力控制, 提示细化, 背景一致性

## 3 点简述
- 核心问题：现有方法在宽年龄变换中身份保持不足，且扩散模型存在静态注意力和优化繁重问题。
- 方法要点：引入Face-Attribute-Aware Prompt Refinement编码内外老化线索，Adaptive Attention Control动态平衡注意力，Angular Inversion高效映射真实人脸。
- 实验或效果：在基准数据集和野外测试集上，FaceTT在身份保留、背景一致性和老化真实性方面优于SOTA方法。

## 摘要（原文）

> Face aging, an ill-posed problem shaped by environmental and genetic factors, is vital in entertainment, forensics, and digital archiving, where realistic age transformations must preserve both identity and visual realism. However, existing works relying on numerical age representations overlook the interplay of biological and contextual cues. Despite progress in recent face aging models, they struggle with identity preservation in wide age transformations, also static attention and optimization-heavy inversion in diffusion limit adaptability, fine-grained control and background consistency. To address these challenges, we propose Face Time Traveller (FaceTT), a diffusion-based framework that achieves high-fidelity, identity-consistent age transformation. Here, we introduce a Face-Attribute-Aware Prompt Refinement strategy that encodes intrinsic (biological) and extrinsic (environmental) aging cues for context-aware conditioning. A tuning-free Angular Inversion method is proposed that efficiently maps real faces into the diffusion latent space for fast and accurate reconstruction. Moreover, an Adaptive Attention Control mechanism is introduced that dynamically balances cross-attention for semantic aging cues and self-attention for structural and identity preservation. Extensive experiments on benchmark datasets and in-the-wild testset demonstrate that FaceTT achieves superior identity retention, background preservation and aging realism over state-of-the-art (SOTA) methods.

