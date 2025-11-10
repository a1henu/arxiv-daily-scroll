---
layout: default
title: Role-SynthCLIP: A Role Play Driven Diverse Synthetic Data Approach
---

# Role-SynthCLIP: A Role Play Driven Diverse Synthetic Data Approach
**arXiv**：[2511.05057v1](https://arxiv.org/abs/2511.05057) · [PDF](https://arxiv.org/pdf/2511.05057.pdf)  
**作者**：Yuanxiang Huangfu, Chaochao Wang, Weilei Wang  

**一句话要点**：提出Role-SynthCLIP，通过多视角角色扮演提示增强合成数据语义多样性以改进CLIP模型训练。

**关键词**：对比学习预训练, 合成数据生成, 多模态大语言模型, 语义多样性, 图像-文本对齐

## 3 点简述
- 现有合成数据方法强调数据量，但语义多样性有限且标题冗余浅显。
- 利用多视角角色扮演提示引导MLLMs生成多样化标题，提升图像-文本对齐。
- 实验显示，仅用100万对数据训练CLIP-B/16，在MS COCO上Recall@1达64.1%，优于现有基线。

## 摘要（原文）

> The effectiveness of Contrastive Language-Image Pre-training (CLIP) models
> critically depends on the semantic diversity and quality of their training
> data. However, while existing synthetic data generation methods primarily focus
> on increasing data volume, such emphasis often leads to limited semantic
> diversity and redundant or shallow captions. To address this limitation, we
> propose Role-SynthCLIP, a novel data synthesis framework that leverages
> multi-perspective role-playing prompts (e.g., a compositional analyst, an
> interpreter of image context) to guide Multimodal Large Language Models (MLLMs)
> in generating semantically diverse captions from distinct viewpoints. This
> mechanism enhances the semantic diversity and fine-grained image-text alignment
> of synthetic pairs, thereby improving caption expressiveness and accuracy while
> keeping the total number of image-text pairs unchanged. Experimental results
> demonstrate the effectiveness and efficiency of our method. A CLIP-B/16 model
> trained on only 1 million Role-SynthCLIP pairs achieves a Recall@1 of 64.1% on
> the MS COCO validation set, surpassing the best existing synthetic data
> baseline (trained on 5M pairs) by 2.8 percentage points. The code and trained
> models are released at https://github.com/huangfu170/Role-SynthCLIP.

