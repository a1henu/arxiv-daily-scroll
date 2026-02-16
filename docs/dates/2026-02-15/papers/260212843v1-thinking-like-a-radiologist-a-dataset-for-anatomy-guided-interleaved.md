---
layout: default
title: Thinking Like a Radiologist: A Dataset for Anatomy-Guided Interleaved Vision Language Reasoning in Chest X-ray Interpretation
---

# Thinking Like a Radiologist: A Dataset for Anatomy-Guided Interleaved Vision Language Reasoning in Chest X-ray Interpretation
**arXiv**：[2602.12843v1](https://arxiv.org/abs/2602.12843) · [PDF](https://arxiv.org/pdf/2602.12843.pdf)  
**作者**：Yichen Zhao, Zelin Peng, Piao Yang, Xiaokang Yang, Wei Shen  

**一句话要点**：提出MMRad-IVL-22K数据集以解决医学大视觉语言模型在胸片诊断中视觉与语言推理脱节的问题。

**关键词**：医学视觉语言模型, 胸片诊断, 多模态推理, 数据集构建, 临床准确性, 放射学工作流程

## 3 点简述
- 核心问题：现有医学LVLMs依赖纯文本推理，易产生幻觉，缺乏视觉细节的持续交互。
- 方法要点：构建首个大规模数据集，模拟放射科医生视觉与语言交替推理的工作流程，覆盖35个解剖区域。
- 实验或效果：实验显示，多模态推理显著提升临床准确性和报告质量，微调模型优于通用和医学专用LVLMs。

## 摘要（原文）

> Radiological diagnosis is a perceptual process in which careful visual inspection and language reasoning are repeatedly interleaved. Most medical large vision language models (LVLMs) perform visual inspection only once and then rely on text-only chain-of-thought (CoT) reasoning, which operates purely in the linguistic space and is prone to hallucination. Recent methods attempt to mitigate this issue by introducing visually related coordinates, such as bounding boxes. However, these remain a pseudo-visual solution: coordinates are still text and fail to preserve rich visual details like texture and density. Motivated by the interleaved nature of radiological diagnosis, we introduce MMRad-IVL-22K, the first large-scale dataset designed for natively interleaved visual language reasoning in chest X-ray interpretation. MMRad-IVL-22K reflects a repeated cycle of reasoning and visual inspection workflow of radiologists, in which visual rationales complement textual descriptions and ground each step of the reasoning process. MMRad-IVL-22K comprises 21,994 diagnostic traces, enabling systematic scanning across 35 anatomical regions. Experimental results on advanced closed-source LVLMs demonstrate that report generation guided by multimodal CoT significantly outperforms that guided by text-only CoT in clinical accuracy and report quality (e.g., 6\% increase in the RadGraph metric), confirming that high-fidelity interleaved vision language evidence is a non-substitutable component of reliable medical AI. Furthermore, benchmarking across seven state-of-the-art open-source LVLMs demonstrates that models fine-tuned on MMRad-IVL-22K achieve superior reasoning consistency and report quality compared with both general-purpose and medical-specific LVLMs. The project page is available at https://github.com/qiuzyc/thinking_like_a_radiologist.

