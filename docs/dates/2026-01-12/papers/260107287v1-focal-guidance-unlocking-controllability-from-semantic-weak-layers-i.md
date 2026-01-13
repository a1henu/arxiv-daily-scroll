---
layout: default
title: Focal Guidance: Unlocking Controllability from Semantic-Weak Layers in Video Diffusion Models
---

# Focal Guidance: Unlocking Controllability from Semantic-Weak Layers in Video Diffusion Models
**arXiv**：[2601.07287v1](https://arxiv.org/abs/2601.07287) · [PDF](https://arxiv.org/pdf/2601.07287.pdf)  
**作者**：Yuanyang Yin, Yufan Deng, Shenghai Yuan, Kaipeng Zhang, Xiao Yang, Feng Zhao  

**一句话要点**：提出Focal Guidance以增强基于DiT的图像到视频生成模型中对文本提示的遵循能力

**关键词**：图像到视频生成, 扩散变换器, 语义弱层, 可控性增强, 注意力机制, 基准评估

## 3 点简述
- 核心问题：现有I2V模型在去噪过程中存在语义弱层，导致文本指导与视觉约束耦合不足，影响对文本提示的遵循。
- 方法要点：引入Focal Guidance，包括细粒度语义指导和注意力缓存机制，以强化语义弱层的可控性。
- 实验或效果：在自建基准上验证，提升Wan2.1-I2V和HunyuanVideo-I2V的指令遵循分数，证明有效性和泛化性。

## 摘要（原文）

> The task of Image-to-Video (I2V) generation aims to synthesize a video from a reference image and a text prompt. This requires diffusion models to reconcile high-frequency visual constraints and low-frequency textual guidance during the denoising process. However, while existing I2V models prioritize visual consistency, how to effectively couple this dual guidance to ensure strong adherence to the text prompt remains underexplored. In this work, we observe that in Diffusion Transformer (DiT)-based I2V models, certain intermediate layers exhibit weak semantic responses (termed Semantic-Weak Layers), as indicated by a measurable drop in text-visual similarity. We attribute this to a phenomenon called Condition Isolation, where attention to visual features becomes partially detached from text guidance and overly relies on learned visual priors. To address this, we propose Focal Guidance (FG), which enhances the controllability from Semantic-Weak Layers. FG comprises two mechanisms: (1) Fine-grained Semantic Guidance (FSG) leverages CLIP to identify key regions in the reference frame and uses them as anchors to guide Semantic-Weak Layers. (2) Attention Cache transfers attention maps from semantically responsive layers to Semantic-Weak Layers, injecting explicit semantic signals and alleviating their over-reliance on the model's learned visual priors, thereby enhancing adherence to textual instructions. To further validate our approach and address the lack of evaluation in this direction, we introduce a benchmark for assessing instruction following in I2V models. On this benchmark, Focal Guidance proves its effectiveness and generalizability, raising the total score on Wan2.1-I2V to 0.7250 (+3.97\%) and boosting the MMDiT-based HunyuanVideo-I2V to 0.5571 (+7.44\%).

