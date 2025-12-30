---
layout: default
title: Same or Not? Enhancing Visual Perception in Vision-Language Models
---

# Same or Not? Enhancing Visual Perception in Vision-Language Models
**arXiv**：[2512.23592v1](https://arxiv.org/abs/2512.23592) · [PDF](https://arxiv.org/pdf/2512.23592.pdf)  
**作者**：Damiano Marsili, Aditya Mehta, Ryan Y. Lin, Georgia Gkioxari  

**一句话要点**：提出TWIN数据集以增强视觉语言模型的细粒度感知能力

**关键词**：视觉语言模型, 细粒度感知, 数据集构建, 图像对任务, 基准评估

## 3 点简述
- 视觉语言模型存在细粒度感知不足和视觉偏见问题
- 引入TWIN数据集，通过图像对任务训练模型关注细微视觉线索
- 在FGVQA基准上提升达19.3%，且不影响通用VQA性能

## 摘要（原文）

> Vision-language models (VLMs) excel at broad visual understanding but remain coarse-grained, exhibit visual biases, and miss subtle visual details. Existing training corpora reinforce this limitation by emphasizing general recognition ("Is it a cat or a dog?") over fine-grained perception. To address this, we introduce a new training corpus and task designed to enhance the perceptual abilities of VLMs. TWIN is a large-scale dataset of 561,000 image-pair queries that task models to determine whether two visually similar images depict the same object, encouraging attention to nuanced visual cues. The dataset spans a diverse range of everyday objects across contexts, viewpoints, and appearances. Fine-tuning VLMs on TWIN yields notable gains in fine-grained recognition, even on unseen domains such as art, animals, plants, and landmarks. To quantify these gains, we introduce FGVQA, a benchmark suite of 12,000 queries that repurposes fine-grained recognition and retrieval datasets from multiple domains. While existing VLMs struggle on FGVQA, when fine-tuned on TWIN they improve by up to 19.3%, without compromising performance on general VQA benchmarks. Finally, our TWIN dataset scales favorably with object annotations, and our analysis shows that scale is key to performance. We envision TWIN as a drop-in addition to open-source VLM training corpora, advancing perceptual precision of future models. Project webpage: https://glab-caltech.github.io/twin/

