---
layout: default
title: Towards Training-free Multimodal Hate Localisation with Large Language Models
---

# Towards Training-free Multimodal Hate Localisation with Large Language Models
**arXiv**：[2602.09637v1](https://arxiv.org/abs/2602.09637) · [PDF](https://arxiv.org/pdf/2602.09637.pdf)  
**作者**：Yueming Sun, Long Yang, Jianbo Jiao, Zeyu Fu  

**一句话要点**：提出训练无关的LLM框架LELA，用于视频仇恨内容检测与定位

**关键词**：多模态视频理解, 仇恨内容检测, 训练无关方法, 大语言模型应用, 时序定位

## 3 点简述
- 在线视频仇恨内容检测依赖大量标注且缺乏细粒度定位能力
- LELA通过多模态分解与多阶段提示实现训练无关的细粒度仇恨评分
- 在HateMM和MultiHateClip基准上显著优于现有训练无关方法

## 摘要（原文）

> The proliferation of hateful content in online videos poses severe threats to individual well-being and societal harmony. However, existing solutions for video hate detection either rely heavily on large-scale human annotations or lack fine-grained temporal precision. In this work, we propose LELA, the first training-free Large Language Model (LLM) based framework for hate video localization. Distinct from state-of-the-art models that depend on supervised pipelines, LELA leverages LLMs and modality-specific captioning to detect and temporally localize hateful content in a training-free manner. Our method decomposes a video into five modalities, including image, speech, OCR, music, and video context, and uses a multi-stage prompting scheme to compute fine-grained hateful scores for each frame. We further introduce a composition matching mechanism to enhance cross-modal reasoning. Experiments on two challenging benchmarks, HateMM and MultiHateClip, demonstrate that LELA outperforms all existing training-free baselines by a large margin. We also provide extensive ablations and qualitative visualizations, establishing LELA as a strong foundation for scalable and interpretable hate video localization.

