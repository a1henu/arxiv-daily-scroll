---
layout: default
title: DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture
---

# DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture
**arXiv**：[2511.17354v1](https://arxiv.org/abs/2511.17354) · [PDF](https://arxiv.org/pdf/2511.17354.pdf)  
**作者**：Xiangteng He, Shunsuke Sakai, Kun Yuan, Nicolas Padoy, Tatsuhito Hasegawa, Leonid Sigal  

**一句话要点**：提出DSeq-JEPA以改进图像表示学习，通过顺序预测增强判别性。

**关键词**：自监督学习, 图像表示学习, 顺序预测, 判别性区域, 联合嵌入预测

## 3 点简述
- I-JEPA在预测掩码区域时缺乏顺序和判别性，导致表示学习不充分。
- DSeq-JEPA结合JEPA潜在预测与GPT顺序推理，按显著性顺序预测区域。
- 实验显示在分类、检测等任务中，DSeq-JEPA比I-JEPA变体更有效。

## 摘要（原文）

> Image-based Joint-Embedding Predictive Architecture (I-JEPA) learns visual representations by predicting latent embeddings of masked regions from visible context. However, it treats all regions uniformly and independently, lacking an explicit notion of where or in what order predictions should be made. Inspired by human visual perception, which deploys attention selectively and sequentially from the most informative to secondary regions, we propose DSeq-JEPA, a Discriminative Sequential Joint-Embedding Predictive Architecture that bridges predictive and autoregressive self-supervised learning, integrating JEPA-style latent prediction with GPT-style sequential reasoning. Specifically, DSeq-JEPA (i) first identifies primary discriminative regions based on a transformer-derived saliency map, emphasizing the distribution of visual importance, and then (ii) predicts subsequent regions in this discriminative order, progressively forming a curriculum-like semantic progression from primary to secondary cues -- a form of GPT-style pre-training. Extensive experiments across diverse tasks, including image classification (ImageNet), fine-grained visual categorization (iNaturalist21, CUB-200-2011, Stanford-Cars), detection and segmentation (MS-COCO, ADE20K), and low-level reasoning tasks (Clevr/Count, Clevr/Dist), demonstrate that DSeq-JEPA consistently focuses on more discriminative and generalizable representations than I-JEPA variants. Project page: https://github.com/SkyShunsuke/DSeq-JEPA.

