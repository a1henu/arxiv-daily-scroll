---
layout: default
title: Reclaiming Lost Text Layers for Source-Free Cross-Domain Few-Shot Learning
---

# Reclaiming Lost Text Layers for Source-Free Cross-Domain Few-Shot Learning
**arXiv**：[2603.05235v1](https://arxiv.org/abs/2603.05235) · [PDF](https://arxiv.org/pdf/2603.05235.pdf)  
**作者**：Zhenyu Zhang, Guangyao Chen, Yixiong Zou, Yuhua Li, Ruixuan Li  

**一句话要点**：提出重利用文本编码器丢失层的方法，以提升源自由跨域少样本学习性能。

**关键词**：源自由跨域少样本学习, 文本编码器优化, 视觉-语言模型, 域适应, 少样本学习

## 3 点简述
- 核心问题：CLIP文本编码器中某些中间层在跨域少样本学习中被视为冗余，但实际包含有益信息未被充分利用。
- 方法要点：通过层和编码器级别重利用丢失层信息，指导视觉分支在域偏移下重新学习。
- 实验或效果：在多种设置、骨干网络和任务上验证了方法的有效性，代码已开源。

## 摘要（原文）

> Source-Free Cross-Domain Few-Shot Learning (SF-CDFSL) focuses on fine-tuning with limited training data from target domains (e.g., medical or satellite images), where CLIP has recently shown promising results due to its generalizability to downstream tasks. Current works indicate CLIP's text encoder is more suitable for cross-domain tasks, however, we find that \textbf{removing certain middle layers of the text encoder can effectively improve performance in SF-CDFSL}, which we call the Lost Layers. In this paper, we delve into this phenomenon for a deeper understanding. We discover that instead of being harmful for the SF-CDFSL task, the information in these layers is actually beneficial, but visual gaps prevent this useful information from being fully utilized, making these layers seem redundant. Based on this understanding, unlike current works that simply remove these layers, we propose a method to teachs the model to \textbf{re-utilize} information in these lost layers at both the layer and encoder levels, guiding the re-learning of the visual branch under domain shifts. Our approach effectively addresses the issue of underutilized information in the text encoder. Extensive experiments across various settings, backbones (CLIP, SigLip, PE-Core), and tasks (4 CDFSL datasets and 10 Meta-dataset datasets) demonstrate the effectiveness of our method. Code is available at https://github.com/zhenyuZ-HUST/CVPR26-VtT.

