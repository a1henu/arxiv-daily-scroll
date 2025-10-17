---
layout: default
title: OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression
---

# OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression
**arXiv**：[2510.14954v1](https://arxiv.org/abs/2510.14954) · [PDF](https://arxiv.org/pdf/2510.14954.pdf)  
**作者**：Zhe Li, Weihao Yuan, Weichao Shen, Siyu Zhu, Zilong Dong, Chang Xu  

**一句话要点**：提出连续掩码自回归运动变换器以解决多模态人体运动生成问题

**关键词**：人体运动生成, 多模态融合, 自回归变换器, 连续掩码建模, 扩散模型

## 3 点简述
- 核心问题：全身多模态运动生成需有效机制与多模态融合，如文本、语音和音乐。
- 方法要点：采用连续掩码自回归变换器，结合门控线性注意力和RMSNorm模块。
- 实验效果：在文本到运动、语音到手势和音乐到舞蹈任务中优于现有方法。

## 摘要（原文）

> Whole-body multi-modal human motion generation poses two primary challenges:
> creating an effective motion generation mechanism and integrating various
> modalities, such as text, speech, and music, into a cohesive framework. Unlike
> previous methods that usually employ discrete masked modeling or autoregressive
> modeling, we develop a continuous masked autoregressive motion transformer,
> where a causal attention is performed considering the sequential nature within
> the human motion. Within this transformer, we introduce a gated linear
> attention and an RMSNorm module, which drive the transformer to pay attention
> to the key actions and suppress the instability caused by either the abnormal
> movements or the heterogeneous distributions within multi-modalities. To
> further enhance both the motion generation and the multimodal generalization,
> we employ the DiT structure to diffuse the conditions from the transformer
> towards the targets. To fuse different modalities, AdaLN and cross-attention
> are leveraged to inject the text, speech, and music signals. Experimental
> results demonstrate that our framework outperforms previous methods across all
> modalities, including text-to-motion, speech-to-gesture, and music-to-dance.
> The code of our method will be made public.

