---
layout: default
title: Finetuning-Free Personalization of Text to Image Generation via Hypernetworks
---

# Finetuning-Free Personalization of Text to Image Generation via Hypernetworks
**arXiv**：[2511.03156v1](https://arxiv.org/abs/2511.03156) · [PDF](https://arxiv.org/pdf/2511.03156.pdf)  
**作者**：Sagar Shrestha, Gopal Sharma, Luowei Zhou, Suren Kumar  

**一句话要点**：提出基于超网络的免微调个性化文本到图像生成方法，以解决计算成本高和推理慢的问题。

**关键词**：文本到图像生成, 超网络, 免微调个性化, LoRA权重预测, 扩散模型

## 3 点简述
- 核心问题：传统个性化方法依赖主题特定微调，计算昂贵且推理慢。
- 方法要点：使用超网络从主题图像直接预测LoRA权重，无需测试时优化。
- 实验或效果：在CelebA-HQ等数据集上验证，实现强个性化性能。

## 摘要（原文）

> Personalizing text-to-image diffusion models has traditionally relied on
> subject-specific fine-tuning approaches such as
> DreamBooth~\cite{ruiz2023dreambooth}, which are computationally expensive and
> slow at inference. Recent adapter- and encoder-based methods attempt to reduce
> this overhead but still depend on additional fine-tuning or large backbone
> models for satisfactory results. In this work, we revisit an orthogonal
> direction: fine-tuning-free personalization via Hypernetworks that predict
> LoRA-adapted weights directly from subject images. Prior hypernetwork-based
> approaches, however, suffer from costly data generation or unstable attempts to
> mimic base model optimization trajectories. We address these limitations with
> an end-to-end training objective, stabilized by a simple output regularization,
> yielding reliable and effective hypernetworks. Our method removes the need for
> per-subject optimization at test time while preserving both subject fidelity
> and prompt alignment. To further enhance compositional generalization at
> inference time, we introduce Hybrid-Model Classifier-Free Guidance (HM-CFG),
> which combines the compositional strengths of the base diffusion model with the
> subject fidelity of personalized models during sampling. Extensive experiments
> on CelebA-HQ, AFHQ-v2, and DreamBench demonstrate that our approach achieves
> strong personalization performance and highlights the promise of hypernetworks
> as a scalable and effective direction for open-category personalization.

