---
layout: default
title: MedSAM3: Delving into Segment Anything with Medical Concepts
---

# MedSAM3: Delving into Segment Anything with Medical Concepts
**arXiv**：[2511.19046v1](https://arxiv.org/abs/2511.19046) · [PDF](https://arxiv.org/pdf/2511.19046.pdf)  
**作者**：Anglin Liu, Rundong Xue, Xu R. Cao, Yifan Shen, Yi Lu, Xiang Li, Qianqian Chen, Jintai Chen  

**一句话要点**：提出MedSAM-3模型，通过文本提示实现医学图像分割，解决泛化性不足问题。

**关键词**：医学图像分割, 文本提示分割, 多模态大语言模型, 开放词汇, 代理框架

## 3 点简述
- 医学图像分割泛化性差，需大量手动标注。
- 基于SAM-3微调，支持开放词汇文本提示分割。
- 在多种模态实验中，性能优于现有模型。

## 摘要（原文）

> Medical image segmentation is fundamental for biomedical discovery. Existing methods lack generalizability and demand extensive, time-consuming manual annotation for new clinical application. Here, we propose MedSAM-3, a text promptable medical segmentation model for medical image and video segmentation. By fine-tuning the Segment Anything Model (SAM) 3 architecture on medical images paired with semantic conceptual labels, our MedSAM-3 enables medical Promptable Concept Segmentation (PCS), allowing precise targeting of anatomical structures via open-vocabulary text descriptions rather than solely geometric prompts. We further introduce the MedSAM-3 Agent, a framework that integrates Multimodal Large Language Models (MLLMs) to perform complex reasoning and iterative refinement in an agent-in-the-loop workflow. Comprehensive experiments across diverse medical imaging modalities, including X-ray, MRI, Ultrasound, CT, and video, demonstrate that our approach significantly outperforms existing specialist and foundation models. We will release our code and model at https://github.com/Joey-S-Liu/MedSAM3.

