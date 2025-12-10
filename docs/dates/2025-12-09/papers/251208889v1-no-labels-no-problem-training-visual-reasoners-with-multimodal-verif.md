---
layout: default
title: No Labels, No Problem: Training Visual Reasoners with Multimodal Verifiers
---

# No Labels, No Problem: Training Visual Reasoners with Multimodal Verifiers
**arXiv**：[2512.08889v1](https://arxiv.org/abs/2512.08889) · [PDF](https://arxiv.org/pdf/2512.08889.pdf)  
**作者**：Damiano Marsili, Georgia Gkioxari  

**一句话要点**：提出无标注训练框架，结合多模态验证器提升视觉推理与定位能力

**关键词**：视觉推理, 无标注训练, 多模态验证器, 强化学习, 硬负样本挖掘, 空间关系理解

## 3 点简述
- 视觉推理需精确对象定位与复杂空间关系理解，现有方法依赖大规模标注或存在逻辑错误
- 框架使用LLM验证器通过强化学习优化推理，VLM验证器通过自动硬负样本挖掘增强视觉定位
- 在多样空间推理任务中评估，方法超越开源与专有模型，改进定位模型优于纯文本方法

## 摘要（原文）

> Visual reasoning is challenging, requiring both precise object grounding and understanding complex spatial relationships. Existing methods fall into two camps: language-only chain-of-thought approaches, which demand large-scale (image, query, answer) supervision, and program-synthesis approaches which use pre-trained models and avoid training, but suffer from flawed logic and erroneous grounding. We propose an annotation-free training framework that improves both reasoning and grounding. Our framework uses AI-powered verifiers: an LLM verifier refines LLM reasoning via reinforcement learning, while a VLM verifier strengthens visual grounding through automated hard-negative mining, eliminating the need for ground truth labels. This design combines the strengths of modern AI systems: advanced language-only reasoning models for decomposing spatial queries into simpler subtasks, and strong vision specialist models improved via performant VLM critics. We evaluate our approach across diverse spatial reasoning tasks, and show that our method improves visual reasoning and surpasses open-source and proprietary models, while with our improved visual grounding model we further outperform recent text-only visual reasoning methods. Project webpage: https://glab-caltech.github.io/valor/

