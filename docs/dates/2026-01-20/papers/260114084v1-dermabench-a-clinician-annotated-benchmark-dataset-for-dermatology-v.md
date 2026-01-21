---
layout: default
title: DermaBench: A Clinician-Annotated Benchmark Dataset for Dermatology Visual Question Answering and Reasoning
---

# DermaBench: A Clinician-Annotated Benchmark Dataset for Dermatology Visual Question Answering and Reasoning
**arXiv**：[2601.14084v1](https://arxiv.org/abs/2601.14084) · [PDF](https://arxiv.org/pdf/2601.14084.pdf)  
**作者**：Abdurrahim Yilmaz, Ozan Erdem, Ece Gokyayla, Ayda Acar, Burc Bugra Dagtas, Dilara Ilhan Erdil, Gulsum Gencoglan, Burak Temelkuran  

**一句话要点**：提出DermaBench基准数据集以评估皮肤病学视觉问答和推理能力

**关键词**：皮肤病学视觉问答, 多模态模型评估, 临床推理基准, 专家标注数据集, 视觉语言模型

## 3 点简述
- 核心问题：现有数据集局限于图像分类，无法评估多模态模型在皮肤病学中的视觉理解和临床推理能力。
- 方法要点：基于DDI数据集，由皮肤科专家标注656张临床图像，涵盖22个主要问题类型，生成约14,474个VQA注释。
- 实验或效果：发布为元数据数据集，支持评估模型对皮肤病图像的细粒度形态分析和描述生成。

## 摘要（原文）

> Vision-language models (VLMs) are increasingly important in medical applications; however, their evaluation in dermatology remains limited by datasets that focus primarily on image-level classification tasks such as lesion recognition. While valuable for recognition, such datasets cannot assess the full visual understanding, language grounding, and clinical reasoning capabilities of multimodal models. Visual question answering (VQA) benchmarks are required to evaluate how models interpret dermatological images, reason over fine-grained morphology, and generate clinically meaningful descriptions. We introduce DermaBench, a clinician-annotated dermatology VQA benchmark built on the Diverse Dermatology Images (DDI) dataset. DermaBench comprises 656 clinical images from 570 unique patients spanning Fitzpatrick skin types I-VI. Using a hierarchical annotation schema with 22 main questions (single-choice, multi-choice, and open-ended), expert dermatologists annotated each image for diagnosis, anatomic site, lesion morphology, distribution, surface features, color, and image quality, together with open-ended narrative descriptions and summaries, yielding approximately 14.474 VQA-style annotations. DermaBench is released as a metadata-only dataset to respect upstream licensing and is publicly available at Harvard Dataverse.

