---
layout: default
title: Representation Space Constrained Learning with Modality Decoupling for Multimodal Object Detection
---

# Representation Space Constrained Learning with Modality Decoupling for Multimodal Object Detection
**arXiv**：[2511.15433v1](https://arxiv.org/abs/2511.15433) · [PDF](https://arxiv.org/pdf/2511.15433.pdf)  
**作者**：YiKang Shao, Tao Shi  

**一句话要点**：提出RSC-MD方法以解决多模态目标检测中的融合退化问题

**关键词**：多模态目标检测, 融合退化, 梯度抑制, 模态解耦, 表示空间约束学习

## 3 点简述
- 核心问题：多模态检测中梯度抑制导致单模态分支欠优化和模态学习不平衡
- 方法要点：通过RSC和MD模块放大梯度并消除模态耦合与不平衡
- 实验或效果：在多个数据集上实现SOTA性能，有效缓解融合退化

## 摘要（原文）

> Multimodal object detection has attracted significant attention in both academia and industry for its enhanced robustness. Although numerous studies have focused on improving modality fusion strategies, most neglect fusion degradation, and none provide a theoretical analysis of its underlying causes. To fill this gap, this paper presents a systematic theoretical investigation of fusion degradation in multimodal detection and identifies two key optimization deficiencies: (1) the gradients of unimodal branch backbones are severely suppressed under multimodal architectures, resulting in under-optimization of the unimodal branches; (2) disparities in modality quality cause weaker modalities to experience stronger gradient suppression, which in turn results in imbalanced modality learning. To address these issues, this paper proposes a Representation Space Constrained Learning with Modality Decoupling (RSC-MD) method, which consists of two modules. The RSC module and the MD module are designed to respectively amplify the suppressed gradients and eliminate inter-modality coupling interference as well as modality imbalance, thereby enabling the comprehensive optimization of each modality-specific backbone. Extensive experiments conducted on the FLIR, LLVIP, M3FD, and MFAD datasets demonstrate that the proposed method effectively alleviates fusion degradation and achieves state-of-the-art performance across multiple benchmarks. The code and training procedures will be released at https://github.com/yikangshao/RSC-MD.

