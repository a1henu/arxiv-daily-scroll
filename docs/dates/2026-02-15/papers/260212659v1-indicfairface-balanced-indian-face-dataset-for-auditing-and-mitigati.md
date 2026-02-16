---
layout: default
title: IndicFairFace: Balanced Indian Face Dataset for Auditing and Mitigating Geographical Bias in Vision-Language Models
---

# IndicFairFace: Balanced Indian Face Dataset for Auditing and Mitigating Geographical Bias in Vision-Language Models
**arXiv**：[2602.12659v1](https://arxiv.org/abs/2602.12659) · [PDF](https://arxiv.org/pdf/2602.12659.pdf)  
**作者**：Aarish Shah Mohsin, Mohammed Tayyab Ilyas Khan, Mohammad Nadeem, Shahab Saquib Sohail, Erik Cambria, Jiechao Gao  

**一句话要点**：提出IndicFairFace数据集以解决视觉语言模型中的印度地理偏见问题

**关键词**：视觉语言模型, 地理偏见, 公平数据集, 去偏方法, 印度人脸识别, 检索精度

## 3 点简述
- 现有公平数据集将印度视为单一类别，忽略其内部地理多样性，导致模型偏见。
- 构建平衡的印度人脸数据集，覆盖28个邦和8个中央直辖区，并采用后处理去偏方法。
- 量化并减少CLIP模型的地理偏见，去偏后检索精度下降小于1.5%，不影响现有嵌入空间。

## 摘要（原文）

> Vision-Language Models (VLMs) are known to inherit and amplify societal biases from their web-scale training data with Indian being particularly misrepresented. Existing fairness-aware datasets have significantly improved demographic balance across global race and gender groups, yet they continue to treat Indian as a single monolithic category. The oversimplification ignores the vast intra-national diversity across 28 states and 8 Union Territories of India and leads to representational and geographical bias. To address the limitation, we present IndicFairFace, a novel and balanced face dataset comprising 14,400 images representing geographical diversity of India. Images were sourced ethically from Wikimedia Commons and open-license web repositories and uniformly balanced across states and gender. Using IndicFairFace, we quantify intra-national geographical bias in prominent CLIP-based VLMs and reduce it using post-hoc Iterative Nullspace Projection debiasing approach. We also show that the adopted debiasing approach does not adversely impact the existing embedding space as the average drop in retrieval accuracy on benchmark datasets is less than 1.5 percent. Our work establishes IndicFairFace as the first benchmark to study geographical bias in VLMs for the Indian context.

