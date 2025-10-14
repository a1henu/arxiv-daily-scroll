---
layout: default
title: Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers
---

# Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers
**arXiv**：[2510.11538v1](https://arxiv.org/abs/2510.11538) · [PDF](https://arxiv.org/pdf/2510.11538.pdf)  
**作者**：Chaofan Gan, Zicheng Zhao, Yuanpeng Tu, Xi Chen, Ziran Qin, Tieyuan Chen, Mehrtash Harandi, Weiyao Lin  

**一句话要点**：提出细节引导策略以增强扩散变换器中的局部细节合成

**关键词**：扩散变换器, 大规模激活, 局部细节合成, 自引导策略, 训练免费方法

## 3 点简述
- 核心问题：扩散变换器内部特征图中的大规模激活功能未明，影响局部细节合成。
- 方法要点：基于大规模激活构建训练免费自引导策略，通过破坏激活生成细节缺陷模型进行指导。
- 实验或效果：在多种预训练扩散变换器上验证，细节质量一致提升，可与分类器自由引导结合。

## 摘要（原文）

> Diffusion Transformers (DiTs) have recently emerged as a powerful backbone
> for visual generation. Recent observations reveal \emph{Massive Activations}
> (MAs) in their internal feature maps, yet their function remains poorly
> understood. In this work, we systematically investigate these activations to
> elucidate their role in visual generation. We found that these massive
> activations occur across all spatial tokens, and their distribution is
> modulated by the input timestep embeddings. Importantly, our investigations
> further demonstrate that these massive activations play a key role in local
> detail synthesis, while having minimal impact on the overall semantic content
> of output. Building on these insights, we propose \textbf{D}etail
> \textbf{G}uidance (\textbf{DG}), a MAs-driven, training-free self-guidance
> strategy to explicitly enhance local detail fidelity for DiTs. Specifically, DG
> constructs a degraded ``detail-deficient'' model by disrupting MAs and
> leverages it to guide the original network toward higher-quality detail
> synthesis. Our DG can seamlessly integrate with Classifier-Free Guidance (CFG),
> enabling further refinements of fine-grained details. Extensive experiments
> demonstrate that our DG consistently improves fine-grained detail quality
> across various pre-trained DiTs (\eg, SD3, SD3.5, and Flux).

