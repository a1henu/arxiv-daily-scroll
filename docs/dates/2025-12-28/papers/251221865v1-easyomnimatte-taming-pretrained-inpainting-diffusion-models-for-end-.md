---
layout: default
title: EasyOmnimatte: Taming Pretrained Inpainting Diffusion Models for End-to-End Video Layered Decomposition
---

# EasyOmnimatte: Taming Pretrained Inpainting Diffusion Models for End-to-End Video Layered Decomposition
**arXiv**：[2512.21865v1](https://arxiv.org/abs/2512.21865) · [PDF](https://arxiv.org/pdf/2512.21865.pdf)  
**作者**：Yihan Hu, Xuelin Chen, Xiaodong Cun  

**一句话要点**：提出EasyOmnimatte，通过双专家微调预训练视频修复扩散模型，实现端到端视频分层分解。

**关键词**：视频分层分解, 扩散模型微调, 双专家策略, 端到端学习, 视频修复, alpha遮罩

## 3 点简述
- 现有视频omnimatte方法依赖多阶段优化，未能充分利用生成先验，导致分解效果不佳。
- 核心方法：微调视频修复扩散模型，设计Effect Expert和Quality Expert双专家，分别捕获前景关联效果和优化alpha遮罩。
- 实验表明，EasyOmnimatte在质量和效率上优于基线，支持多种下游任务，验证了双专家策略的有效性。

## 摘要（原文）

> Existing video omnimatte methods typically rely on slow, multi-stage, or inference-time optimization pipelines that fail to fully exploit powerful generative priors, producing suboptimal decompositions. Our key insight is that, if a video inpainting model can be finetuned to remove the foreground-associated effects, then it must be inherently capable of perceiving these effects, and hence can also be finetuned for the complementary task: foreground layer decomposition with associated effects. However, although naïvely finetuning the inpainting model with LoRA applied to all blocks can produce high-quality alpha mattes, it fails to capture associated effects. Our systematic analysis reveals this arises because effect-related cues are primarily encoded in specific DiT blocks and become suppressed when LoRA is applied across all blocks. To address this, we introduce EasyOmnimatte, the first unified, end-to-end video omnimatte method. Concretely, we finetune a pretrained video inpainting diffusion model to learn dual complementary experts while keeping its original weights intact: an Effect Expert, where LoRA is applied only to effect-sensitive DiT blocks to capture the coarse structure of the foreground and associated effects, and a fully LoRA-finetuned Quality Expert learns to refine the alpha matte. During sampling, Effect Expert is used for denoising at early, high-noise steps, while Quality Expert takes over at later, low-noise steps. This design eliminates the need for two full diffusion passes, significantly reducing computational cost without compromising output quality. Ablation studies validate the effectiveness of this Dual-Expert strategy. Experiments demonstrate that EasyOmnimatte sets a new state-of-the-art for video omnimatte and enables various downstream tasks, significantly outperforming baselines in both quality and efficiency.

