---
layout: default
title: Now You See It, Now You Don't - Instant Concept Erasure for Safe Text-to-Image and Video Generation
---

# Now You See It, Now You Don't - Instant Concept Erasure for Safe Text-to-Image and Video Generation
**arXiv**：[2511.18684v1](https://arxiv.org/abs/2511.18684) · [PDF](https://arxiv.org/pdf/2511.18684.pdf)  
**作者**：Shristi Das Biswas, Arani Roy, Kaushik Roy  

**一句话要点**：提出ICE方法以解决文本到图像和视频生成中的概念安全擦除问题

**关键词**：概念擦除, 文本到图像生成, 文本到视频生成, 权重修改, 安全部署, 模态无关方法

## 3 点简述
- 现有概念擦除方法存在重训练成本高、推理开销大或易受攻击等问题
- ICE使用各向异性能量加权缩放和重叠投影器实现无训练、模态无关的权重修改
- 在多种目标移除任务中，ICE实现强擦除且保持生成能力，适用于T2I和T2V模型

## 摘要（原文）

> Robust concept removal for text-to-image (T2I) and text-to-video (T2V) models is essential for their safe deployment. Existing methods, however, suffer from costly retraining, inference overhead, or vulnerability to adversarial attacks. Crucially, they rarely model the latent semantic overlap between the target erase concept and surrounding content -- causing collateral damage post-erasure -- and even fewer methods work reliably across both T2I and T2V domains. We introduce Instant Concept Erasure (ICE), a training-free, modality-agnostic, one-shot weight modification approach that achieves precise, persistent unlearning with zero overhead. ICE defines erase and preserve subspaces using anisotropic energy-weighted scaling, then explicitly regularises against their intersection using a unique, closed-form overlap projector. We pose a convex and Lipschitz-bounded Spectral Unlearning Objective, balancing erasure fidelity and intersection preservation, that admits a stable and unique analytical solution. This solution defines a dissociation operator that is translated to the model's text-conditioning layers, making the edit permanent and runtime-free. Across targeted removals of artistic styles, objects, identities, and explicit content, ICE efficiently achieves strong erasure with improved robustness to red-teaming, all while causing only minimal degradation of original generative abilities in both T2I and T2V models.

