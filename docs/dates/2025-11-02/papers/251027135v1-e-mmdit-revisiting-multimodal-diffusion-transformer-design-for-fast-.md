---
layout: default
title: E-MMDiT: Revisiting Multimodal Diffusion Transformer Design for Fast Image Synthesis under Limited Resources
---

# E-MMDiT: Revisiting Multimodal Diffusion Transformer Design for Fast Image Synthesis under Limited Resources
**arXiv**：[2510.27135v1](https://arxiv.org/abs/2510.27135) · [PDF](https://arxiv.org/pdf/2510.27135.pdf)  
**作者**：Tong Shen, Jingai Yu, Dong Zhou, Dong Li, Emad Barsoum  

**一句话要点**：提出E-MMDiT以在有限资源下实现快速图像合成

**关键词**：多模态扩散模型, 令牌压缩, 轻量级架构, 快速图像合成, 有限资源训练

## 3 点简述
- 核心问题：扩散模型训练资源需求高、延迟大，难以在有限计算条件下部署。
- 方法要点：采用令牌压缩、位置强化和交替子区域注意力，降低计算成本。
- 实验或效果：在512px生成任务中，使用25M数据训练1.5天，GenEval得分0.66。

## 摘要（原文）

> Diffusion models have shown strong capabilities in generating high-quality
> images from text prompts. However, these models often require large-scale
> training data and significant computational resources to train, or suffer from
> heavy structure with high latency. To this end, we propose Efficient Multimodal
> Diffusion Transformer (E-MMDiT), an efficient and lightweight multimodal
> diffusion model with only 304M parameters for fast image synthesis requiring
> low training resources. We provide an easily reproducible baseline with
> competitive results. Our model for 512px generation, trained with only 25M
> public data in 1.5 days on a single node of 8 AMD MI300X GPUs, achieves 0.66 on
> GenEval and easily reaches to 0.72 with some post-training techniques such as
> GRPO. Our design philosophy centers on token reduction as the computational
> cost scales significantly with the token count. We adopt a highly compressive
> visual tokenizer to produce a more compact representation and propose a novel
> multi-path compression module for further compression of tokens. To enhance our
> design, we introduce Position Reinforcement, which strengthens positional
> information to maintain spatial coherence, and Alternating Subregion Attention
> (ASA), which performs attention within subregions to further reduce
> computational cost. In addition, we propose AdaLN-affine, an efficient
> lightweight module for computing modulation parameters in transformer blocks.
> Our code is available at https://github.com/AMD-AGI/Nitro-E and we hope E-MMDiT
> serves as a strong and practical baseline for future research and contributes
> to democratization of generative AI models.

