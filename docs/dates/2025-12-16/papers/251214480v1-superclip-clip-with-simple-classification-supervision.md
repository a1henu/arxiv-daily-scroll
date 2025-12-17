---
layout: default
title: SuperCLIP: CLIP with Simple Classification Supervision
---

# SuperCLIP: CLIP with Simple Classification Supervision
**arXiv**：[2512.14480v1](https://arxiv.org/abs/2512.14480) · [PDF](https://arxiv.org/pdf/2512.14480.pdf)  
**作者**：Weiheng Zhao, Zilong Huang, Jiashi Feng, Xinggang Wang  

**一句话要点**：提出SuperCLIP，通过分类监督增强对比学习以解决CLIP细粒度语义利用不足问题。

**关键词**：视觉-语言对齐, 对比学习, 分类监督, 细粒度语义, 零样本学习, 图像-文本检索

## 3 点简述
- CLIP模型因仅优化全局相似性而忽视词级监督，导致细粒度视觉-文本对齐能力受限。
- SuperCLIP在视觉编码器上添加轻量线性层，利用词级线索增强对齐，总FLOPs仅增0.077%。
- 实验表明SuperCLIP在零样本分类、图像-文本检索和纯视觉任务上均提升性能，且缓解小批次性能下降。

## 摘要（原文）

> Contrastive Language-Image Pretraining (CLIP) achieves strong generalization in vision-language tasks by aligning images and texts in a shared embedding space. However, recent findings show that CLIP-like models still underutilize fine-grained semantic signals in text, and this issue becomes even more pronounced when dealing with long and detailed captions. This stems from CLIP's training objective, which optimizes only global image-text similarity and overlooks token-level supervision - limiting its ability to achieve fine-grained visual-text alignment. To address this, we propose SuperCLIP, a simple yet effective framework that augments contrastive learning with classification-based supervision. By adding only a lightweight linear layer to the vision encoder, SuperCLIP leverages token-level cues to enhance visual-textual alignment - with just a 0.077% increase in total FLOPs, and no need for additional annotated data. Experiments show that SuperCLIP consistently improves zero-shot classification, image-text retrieval, and purely visual tasks. These gains hold regardless of whether the model is trained on original web data or rich re-captioned data, demonstrating SuperCLIP's ability to recover textual supervision in both cases. Furthermore, SuperCLIP alleviates CLIP's small-batch performance drop through classification-based supervision that avoids reliance on large batch sizes. Code and models will be made open source.

