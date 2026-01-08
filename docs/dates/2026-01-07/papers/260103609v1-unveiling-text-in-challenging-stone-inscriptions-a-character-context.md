---
layout: default
title: Unveiling Text in Challenging Stone Inscriptions: A Character-Context-Aware Patching Strategy for Binarization
---

# Unveiling Text in Challenging Stone Inscriptions: A Character-Context-Aware Patching Strategy for Binarization
**arXiv**：[2601.03609v1](https://arxiv.org/abs/2601.03609) · [PDF](https://arxiv.org/pdf/2601.03609.pdf)  
**作者**：Pratyush Jena, Amal Joseph, Arnav Sharma, Ravi Kiran Sarvadevabhatla  

**一句话要点**：提出字符-上下文感知分块策略以解决石刻图像二值化难题

**关键词**：图像二值化, 石刻文本提取, 注意力机制, 分块策略, 零样本泛化

## 3 点简述
- 核心问题：石刻图像因对比度低、表面退化不均等导致现有二值化方法失效
- 方法要点：采用动态采样和分块选择训练注意力U-Net，聚焦细微结构线索
- 实验或效果：显著提升二值化性能，并展示跨脚本零样本泛化能力

## 摘要（原文）

> Binarization is a popular first step towards text extraction in historical artifacts. Stone inscription images pose severe challenges for binarization due to poor contrast between etched characters and the stone background, non-uniform surface degradation, distracting artifacts, and highly variable text density and layouts. These conditions frequently cause existing binarization techniques to fail and struggle to isolate coherent character regions. Many approaches sub-divide the image into patches to improve text fragment resolution and improve binarization performance. With this in mind, we present a robust and adaptive patching strategy to binarize challenging Indic inscriptions. The patches from our approach are used to train an Attention U-Net for binarization. The attention mechanism allows the model to focus on subtle structural cues, while our dynamic sampling and patch selection method ensures that the model learns to overcome surface noise and layout irregularities. We also introduce a carefully annotated, pixel-precise dataset of Indic stone inscriptions at the character-fragment level. We demonstrate that our novel patching mechanism significantly boosts binarization performance across classical and deep learning baselines. Despite training only on single script Indic dataset, our model exhibits strong zero-shot generalization to other Indic and non-indic scripts, highlighting its robustness and script-agnostic generalization capabilities. By producing clean, structured representations of inscription content, our method lays the foundation for downstream tasks such as script identification, OCR, and historical text analysis. Project page: https://ihdia.iiit.ac.in/shilalekhya-binarization/

