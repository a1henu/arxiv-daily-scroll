---
layout: default
title: Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation
---

# Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation
**arXiv**：[2603.04803v1](https://arxiv.org/abs/2603.04803) · [PDF](https://arxiv.org/pdf/2603.04803.pdf)  
**作者**：Boyu Han, Qianqian Xu, Shilong Bao, Zhiyong Yang, Ruochen Cui, Xilin Zhao, Qingming Huang  

**一句话要点**：提出扩散对比重建方法以平衡CLIP视觉编码器的判别与细节感知能力

**关键词**：对比学习, 扩散模型, 视觉表示学习, CLIP增强, 多模态模型

## 3 点简述
- 核心问题：CLIP视觉编码器在判别能力和细节感知能力上存在瓶颈，影响下游性能
- 方法要点：通过扩散模型重建图像，并注入基于重建图像的对比信号以统一优化目标
- 实验或效果：在多个基准测试和多模态大语言模型中验证了方法的有效性

## 摘要（原文）

> The limited understanding capacity of the visual encoder in Contrastive Language-Image Pre-training (CLIP) has become a key bottleneck for downstream performance. This capacity includes both Discriminative Ability (D-Ability), which reflects class separability, and Detail Perceptual Ability (P-Ability), which focuses on fine-grained visual cues. Recent solutions use diffusion models to enhance representations by conditioning image reconstruction on CLIP visual tokens. We argue that such paradigms may compromise D-Ability and therefore fail to effectively address CLIP's representation limitations. To address this, we integrate contrastive signals into diffusion-based reconstruction to pursue more comprehensive visual representations. We begin with a straightforward design that augments the diffusion process with contrastive learning on input images. However, empirical results show that the naive combination suffers from gradient conflict and yields suboptimal performance. To balance the optimization, we introduce the Diffusion Contrastive Reconstruction (DCR), which unifies the learning objective. The key idea is to inject contrastive signals derived from each reconstructed image, rather than from the original input, into the diffusion process. Our theoretical analysis shows that the DCR loss can jointly optimize D-Ability and P-Ability. Extensive experiments across various benchmarks and multi-modal large language models validate the effectiveness of our method. The code is available at https://github.com/boyuh/DCR.

