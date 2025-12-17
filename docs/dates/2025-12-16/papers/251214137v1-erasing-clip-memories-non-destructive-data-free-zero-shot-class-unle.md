---
layout: default
title: Erasing CLIP Memories: Non-Destructive, Data-Free Zero-Shot class Unlearning in CLIP Models
---

# Erasing CLIP Memories: Non-Destructive, Data-Free Zero-Shot class Unlearning in CLIP Models
**arXiv**：[2512.14137v1](https://arxiv.org/abs/2512.14137) · [PDF](https://arxiv.org/pdf/2512.14137.pdf)  
**作者**：Ashish Mishra, Tarun Kumar, Gyanaranjan Nayak, Arpit Shah, Suparna Bhattacharya, Martin Foltin  

**一句话要点**：提出基于零空间投影的非破坏性数据无关零样本类别遗忘方法，用于CLIP模型选择性遗忘。

**关键词**：多模态模型, 选择性遗忘, 零空间投影, 零样本学习, 模型去污染, 隐私保护

## 3 点简述
- 针对CLIP等预训练多模态模型，解决选择性遗忘目标类别信息的问题，无需遗忘集图像或重训练。
- 利用目标文本嵌入的零空间投影，在最终投影层精确擦除类别信息，保持模型整体知识。
- 实验显示该方法能显著降低目标类零样本性能，平衡遗忘与信息保留，计算高效且精确。

## 摘要（原文）

> We introduce a novel, closed-form approach for selective unlearning in multimodal models, specifically targeting pretrained models such as CLIP. Our method leverages nullspace projection to erase the target class information embedded in the final projection layer, without requiring any retraining or the use of images from the forget set. By computing an orthonormal basis for the subspace spanned by target text embeddings and projecting these directions, we dramatically reduce the alignment between image features and undesired classes. Unlike traditional unlearning techniques that rely on iterative fine-tuning and extensive data curation, our approach is both computationally efficient and surgically precise. This leads to a pronounced drop in zero-shot performance for the target classes while preserving the overall multimodal knowledge of the model. Our experiments demonstrate that even a partial projection can balance between complete unlearning and retaining useful information, addressing key challenges in model decontamination and privacy preservation.

