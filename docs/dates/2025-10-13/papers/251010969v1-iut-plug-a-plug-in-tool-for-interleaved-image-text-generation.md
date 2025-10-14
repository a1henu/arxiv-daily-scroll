---
layout: default
title: IUT-Plug: A Plug-in tool for Interleaved Image-Text Generation
---

# IUT-Plug: A Plug-in tool for Interleaved Image-Text Generation
**arXiv**：[2510.10969v1](https://arxiv.org/abs/2510.10969) · [PDF](https://arxiv.org/pdf/2510.10969.pdf)  
**作者**：Zeteng Lin, Xingxing Li, Wen You, Xiaoyang Li, Zehan Lu, Yujun Cai, Jing Tang  

**一句话要点**：提出IUT-Plug模块以解决多模态图像-文本生成中的逻辑、实体和风格漂移问题

**关键词**：图像理解树, 多模态生成, 上下文漂移, 结构化推理, 跨模态一致性, 问答基准

## 3 点简述
- 现有视觉语言模型在复杂图像-文本场景中难以保持逻辑、对象身份和风格一致性
- 基于图像理解树构建动态提取和协调机制，增强结构化推理和跨模态一致性
- 实验显示在多样化多模态问答场景中有效缓解上下文漂移并提升准确性

## 摘要（原文）

> Existing vision language models (VLMs), including GPT-4 and DALL-E, often
> struggle to preserve logic, object identity, and style in multimodal image-text
> generation. This limitation significantly hinders the generalization capability
> of VLMs in complex image-text input-output scenarios. To address this issue, we
> propose IUT-Plug, a module grounded in an Image Understanding Tree (IUT), which
> enhances existing interleaved VLMs through explicit structured reasoning,
> thereby mitigating context drift in logic, entity identity, and style. The
> proposed framework operates in two stages. (1) A dynamic IUT-Plug extraction
> module parses visual scenes into hierarchical symbolic structures. (2) A
> coordinated narrative-flow and image synthesis mechanism ensures cross-modal
> consistency. To evaluate our approach, we construct a novel benchmark based on
> 3,000 real human-generated question-answer pairs over fine-tuned large models,
> introducing a dynamic evaluation protocol for quantifying context drift in
> interleaved VLMs. Experimental results demonstrate that IUT-Plug not only
> improves accuracy on established benchmarks but also effectively alleviates the
> three critical forms of context drift across diverse multimodal question
> answering (QA) scenarios.

