---
layout: default
title: e5-omni: Explicit Cross-modal Alignment for Omni-modal Embeddings
---

# e5-omni: Explicit Cross-modal Alignment for Omni-modal Embeddings
**arXiv**：[2601.03666v1](https://arxiv.org/abs/2601.03666) · [PDF](https://arxiv.org/pdf/2601.03666.pdf)  
**作者**：Haonan Chen, Sicheng Gao, Radu Timofte, Tetsuya Sakai, Zhicheng Dou  

**一句话要点**：提出e5-omni方法，通过显式对齐解决多模态嵌入中的尺度不一致和负样本效率问题。

**关键词**：全模态嵌入, 显式对齐, 温度校准, 负样本课程学习, 批量白化, 多模态检索

## 3 点简述
- 核心问题：现有全模态嵌入依赖预训练视觉语言模型的隐式对齐，导致相似度尺度不一致、负样本效率低和统计特性不匹配。
- 方法要点：引入模态感知温度校准、可控负样本课程学习和批量白化，以显式对齐多模态嵌入。
- 实验或效果：在MMEB-V2和AudioCaps数据集上优于基线，方法可迁移至其他视觉语言模型骨干。

## 摘要（原文）

> Modern information systems often involve different types of items, e.g., a text query, an image, a video clip, or an audio segment. This motivates omni-modal embedding models that map heterogeneous modalities into a shared space for direct comparison. However, most recent omni-modal embeddings still rely heavily on implicit alignment inherited from pretrained vision-language model (VLM) backbones. In practice, this causes three common issues: (i) similarity logits have modality-dependent sharpness, so scores are not on a consistent scale; (ii) in-batch negatives become less effective over time because mixed-modality batches create an imbalanced hardness distribution; as a result, many negatives quickly become trivial and contribute little gradient; and (iii) embeddings across modalities show mismatched first- and second-order statistics, which makes rankings less stable. To tackle these problems, we propose e5-omni, a lightweight explicit alignment recipe that adapts off-the-shelf VLMs into robust omni-modal embedding models. e5-omni combines three simple components: (1) modality-aware temperature calibration to align similarity scales, (2) a controllable negative curriculum with debiasing to focus on confusing negatives while reducing the impact of false negatives, and (3) batch whitening with covariance regularization to better match cross-modal geometry in the shared embedding space. Experiments on MMEB-V2 and AudioCaps show consistent gains over strong bi-modal and omni-modal baselines, and the same recipe also transfers well to other VLM backbones. We release our model checkpoint at https://huggingface.co/Haon-Chen/e5-omni-7B.

