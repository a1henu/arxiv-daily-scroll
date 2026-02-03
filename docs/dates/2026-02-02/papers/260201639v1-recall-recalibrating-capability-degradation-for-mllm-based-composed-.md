---
layout: default
title: ReCALL: Recalibrating Capability Degradation for MLLM-based Composed Image Retrieval
---

# ReCALL: Recalibrating Capability Degradation for MLLM-based Composed Image Retrieval
**arXiv**：[2602.01639v1](https://arxiv.org/abs/2602.01639) · [PDF](https://arxiv.org/pdf/2602.01639.pdf)  
**作者**：Tianyu Yang, ChenWei He, Xiangzhao Hao, Tianyue Wang, Jiarui Guo, Haiyun Guo, Leigang Qu, Jinqiao Wang, Tat-Seng Chua  

**一句话要点**：提出ReCALL框架以解决MLLM适配检索任务时的能力退化问题

**关键词**：组合图像检索, 多模态大语言模型, 能力退化, 对比学习, 指令生成, 细粒度推理

## 3 点简述
- 核心问题：生成式MLLM适配为判别式检索器导致细粒度推理能力退化
- 方法要点：通过诊断-生成-精炼流程，利用自引导挖掘和CoT提示生成校正数据
- 实验或效果：在CIRR和FashionIQ数据集上实现SOTA性能，有效校准退化能力

## 摘要（原文）

> Composed Image Retrieval (CIR) aims to retrieve target images based on a hybrid query comprising a reference image and a modification text. Early dual-tower Vision-Language Models (VLMs) struggle with cross-modality compositional reasoning required for this task. Recently, adapting generative Multimodal Large Language Models (MLLMs) for retrieval offers a promising direction. However, we identify that this adaptation strategy overlooks a fundamental issue: adapting a generative MLLM into a single-embedding discriminative retriever triggers a paradigm conflict, which leads to Capability Degradation - the deterioration of native fine-grained reasoning after retrieval adaptation. To address this challenge, we propose ReCALL (Recalibrating Capability Degradation), a model-agnostic framework that follows a diagnose-generate-refine pipeline: Firstly, we diagnose cognitive blind spots of the retriever via self-guided informative instance mining. Next, we generate corrective instructions and triplets by CoT prompting the foundation MLLM and conduct quality control with VQA-based consistency filtering. Finally, we refine the retriever through continual training on these triplets with a grouped contrastive scheme, thereby internalizing fine-grained visual-semantic distinctions and realigning the discriminative embedding space of retriever with intrinsic compositional reasoning within the MLLM. Extensive experiments on CIRR and FashionIQ show that ReCALL consistently recalibrates degraded capabilities and achieves state-of-the-art performance. Code will be released soon.

