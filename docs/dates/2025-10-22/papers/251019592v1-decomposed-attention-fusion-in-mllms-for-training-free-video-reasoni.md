---
layout: default
title: Decomposed Attention Fusion in MLLMs for Training-Free Video Reasoning Segmentation
---

# Decomposed Attention Fusion in MLLMs for Training-Free Video Reasoning Segmentation
**arXiv**：[2510.19592v1](https://arxiv.org/abs/2510.19592) · [PDF](https://arxiv.org/pdf/2510.19592.pdf)  
**作者**：Su Ho Han, Jeongseok Hyun, Pilhyeon Lee, Minho Shim, Dongyoon Wee, Seon Joo Kim  

**一句话要点**：提出Decomposed Attention Fusion方法，以训练免费方式实现视频推理分割。

**关键词**：多模态大语言模型, 视频推理分割, 注意力机制, 训练免费方法, 对象定位

## 3 点简述
- 核心问题：MLLM注意力图噪声大，与对象区域对齐差。
- 方法要点：通过对比对象-背景融合和互补视频帧融合精炼注意力图。
- 实验效果：在VOS基准上优于训练免费方法，性能接近训练方法。

## 摘要（原文）

> Multimodal large language models (MLLMs) demonstrate strong video
> understanding by attending to visual tokens relevant to textual queries. To
> directly adapt this for localization in a training-free manner, we cast video
> reasoning segmentation as a video QA task and extract attention maps via
> rollout mechanism. However, raw attention maps are noisy and poorly aligned
> with object regions. We propose Decomposed Attention Fusion (DecAF), which
> refines these maps through two mechanisms: (1) contrastive object-background
> fusion and (2) complementary video-frame fusion. This method suppresses
> irrelevant activations and enhances object-focused cues, enabling direct
> conversion of attention maps into coarse segmentation masks. In addition, we
> introduce attention-guided SAM2 prompting for obtaining fine-grained masks.
> Unlike existing methods that jointly train MLLMs with SAM, our method operates
> entirely without retraining. DecAF outperforms training-free methods and
> achieves performance comparable to training-based methods on both referring and
> reasoning VOS benchmarks. The code will be available at
> https://github.com/HYUNJS/DecAF.

