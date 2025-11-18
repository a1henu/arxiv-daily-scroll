---
layout: default
title: MedGEN-Bench: Contextually entangled benchmark for open-ended multimodal medical generation
---

# MedGEN-Bench: Contextually entangled benchmark for open-ended multimodal medical generation
**arXiv**：[2511.13135v1](https://arxiv.org/abs/2511.13135) · [PDF](https://arxiv.org/pdf/2511.13135.pdf)  
**作者**：Junjie Yang, Yuhao Yan, Gang Wu, Yuxuan Wang, Ruoyu Liang, Xinjie Jiang, Xiang Wan, Fenglei Fan, Yongquan Zhang, Feiwei Qin, Changmiao Wan  

**一句话要点**：提出MedGEN-Bench基准以解决医学多模态生成中上下文推理不足的问题

**关键词**：医学多模态生成, 上下文推理基准, 图像-文本对, 开放生成评估, 临床任务, 多模态模型

## 3 点简述
- 现有医学视觉基准存在查询模糊、推理简化及图像生成评估缺失等核心问题
- 方法要点包括构建专家验证的图像-文本对，并设计三种格式支持开放生成
- 实验评估了18个模型，采用像素级、语义和临床相关性三层评估框架

## 摘要（原文）

> As Vision-Language Models (VLMs) increasingly gain traction in medical applications, clinicians are progressively expecting AI systems not only to generate textual diagnoses but also to produce corresponding medical images that integrate seamlessly into authentic clinical workflows. Despite the growing interest, existing medical visual benchmarks present notable limitations. They often rely on ambiguous queries that lack sufficient relevance to image content, oversimplify complex diagnostic reasoning into closed-ended shortcuts, and adopt a text-centric evaluation paradigm that overlooks the importance of image generation capabilities. To address these challenges, we introduce \textsc{MedGEN-Bench}, a comprehensive multimodal benchmark designed to advance medical AI research. MedGEN-Bench comprises 6,422 expert-validated image-text pairs spanning six imaging modalities, 16 clinical tasks, and 28 subtasks. It is structured into three distinct formats: Visual Question Answering, Image Editing, and Contextual Multimodal Generation. What sets MedGEN-Bench apart is its focus on contextually intertwined instructions that necessitate sophisticated cross-modal reasoning and open-ended generative outputs, moving beyond the constraints of multiple-choice formats. To evaluate the performance of existing systems, we employ a novel three-tier assessment framework that integrates pixel-level metrics, semantic text analysis, and expert-guided clinical relevance scoring. Using this framework, we systematically assess 10 compositional frameworks, 3 unified models, and 5 VLMs.

