---
layout: default
title: Prompt Reinjection: Alleviating Prompt Forgetting in Multimodal Diffusion Transformers
---

# Prompt Reinjection: Alleviating Prompt Forgetting in Multimodal Diffusion Transformers
**arXiv**：[2602.06886v1](https://arxiv.org/abs/2602.06886) · [PDF](https://arxiv.org/pdf/2602.06886.pdf)  
**作者**：Yuxuan Yao, Yuxuan Chen, Hui Li, Kaihui Cheng, Qipeng Guo, Yuwei Sun, Zilong Dong, Jingdong Wang, Siyu Zhu  

**一句话要点**：提出提示再注入方法以缓解多模态扩散变换器中的提示遗忘问题

**关键词**：多模态扩散变换器, 提示遗忘, 文本到图像生成, 提示再注入, 训练无关方法

## 3 点简述
- 核心问题：多模态扩散变换器在文本分支中随深度增加出现提示语义遗忘现象
- 方法要点：通过训练无关的提示再注入，将早期层提示表示重新注入后期层
- 实验或效果：在多个基准测试中提升指令跟随能力、偏好、美学和整体生成质量

## 摘要（原文）

> Multimodal Diffusion Transformers (MMDiTs) for text-to-image generation maintain separate text and image branches, with bidirectional information flow between text tokens and visual latents throughout denoising. In this setting, we observe a prompt forgetting phenomenon: the semantics of the prompt representation in the text branch is progressively forgotten as depth increases. We further verify this effect on three representative MMDiTs--SD3, SD3.5, and FLUX.1 by probing linguistic attributes of the representations over the layers in the text branch. Motivated by these findings, we introduce a training-free approach, prompt reinjection, which reinjects prompt representations from early layers into later layers to alleviate this forgetting. Experiments on GenEval, DPG, and T2I-CompBench++ show consistent gains in instruction-following capability, along with improvements on metrics capturing preference, aesthetics, and overall text--image generation quality.

