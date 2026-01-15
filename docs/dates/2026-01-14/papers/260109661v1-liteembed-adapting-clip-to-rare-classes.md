---
layout: default
title: LiteEmbed: Adapting CLIP to Rare Classes
---

# LiteEmbed: Adapting CLIP to Rare Classes
**arXiv**：[2601.09661v1](https://arxiv.org/abs/2601.09661) · [PDF](https://arxiv.org/pdf/2601.09661.pdf)  
**作者**：Aishwarya Agarwal, Srikrishna Karanam, Vineet Gandhi  

**一句话要点**：提出LiteEmbed框架，通过子空间优化文本嵌入，以解决CLIP在罕见类别上的零样本识别问题。

**关键词**：零样本学习, 文本嵌入优化, 罕见类别适应, CLIP个性化, 子空间分解

## 3 点简述
- 核心问题：CLIP在预训练中罕见或新兴类别上表现不佳，影响零样本识别能力。
- 方法要点：基于PCA分解，通过粗对齐和细分离目标优化文本嵌入，无需重训练编码器。
- 实验或效果：在分类、检索等任务中显著优于先前方法，提升罕见类别的适应性和可区分性。

## 摘要（原文）

> Large-scale vision-language models such as CLIP achieve strong zero-shot recognition but struggle with classes that are rarely seen during pretraining, including newly emerging entities and culturally specific categories. We introduce LiteEmbed, a lightweight framework for few-shot personalization of CLIP that enables new classes to be added without retraining its encoders. LiteEmbed performs subspace-guided optimization of text embeddings within CLIP's vocabulary, leveraging a PCA-based decomposition that disentangles coarse semantic directions from fine-grained variations. Two complementary objectives, coarse alignment and fine separation, jointly preserve global semantic consistency while enhancing discriminability among visually similar classes. Once optimized, the embeddings are plug-and-play, seamlessly substituting CLIP's original text features across classification, retrieval, segmentation, and detection tasks. Extensive experiments demonstrate substantial gains over prior methods, establishing LiteEmbed as an effective approach for adapting CLIP to underrepresented, rare, or unseen classes.

