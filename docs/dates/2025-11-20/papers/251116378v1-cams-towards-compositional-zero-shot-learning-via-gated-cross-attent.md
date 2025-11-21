---
layout: default
title: CAMS: Towards Compositional Zero-Shot Learning via Gated Cross-Attention and Multi-Space Disentanglement
---

# CAMS: Towards Compositional Zero-Shot Learning via Gated Cross-Attention and Multi-Space Disentanglement
**arXiv**：[2511.16378v1](https://arxiv.org/abs/2511.16378) · [PDF](https://arxiv.org/pdf/2511.16378.pdf)  
**作者**：Pan Yang, Cheng Deng, Jing Yang, Han Zhao, Yun Liu, Yuling Chen, Xiaoli Ruan, Yanping Chen  

**一句话要点**：提出CAMS方法以改进组合零样本学习中的语义解缠与泛化能力

**关键词**：组合零样本学习, 语义解缠, 门控交叉注意力, 多空间学习, CLIP模型

## 3 点简述
- 核心问题：CLIP全局语义表示在属性与对象解缠中能力有限，影响未见组合识别。
- 方法要点：设计门控交叉注意力提取细粒度语义，并在多空间进行语义解缠。
- 实验效果：在MIT-States等基准上，闭世界和开世界设置均达到最优性能。

## 摘要（原文）

> Compositional zero-shot learning (CZSL) aims to learn the concepts of attributes and objects in seen compositions and to recognize their unseen compositions. Most Contrastive Language-Image Pre-training (CLIP)-based CZSL methods focus on disentangling attributes and objects by leveraging the global semantic representation obtained from the image encoder. However, this representation has limited representational capacity and do not allow for complete disentanglement of the two. To this end, we propose CAMS, which aims to extract semantic features from visual features and perform semantic disentanglement in multidimensional spaces, thereby improving generalization over unseen attribute-object compositions. Specifically, CAMS designs a Gated Cross-Attention that captures fine-grained semantic features from the high-level image encoding blocks of CLIP through a set of latent units, while adaptively suppressing background and other irrelevant information. Subsequently, it conducts Multi-Space Disentanglement to achieve disentanglement of attribute and object semantics. Experiments on three popular benchmarks (MIT-States, UT-Zappos, and C-GQA) demonstrate that CAMS achieves state-of-the-art performance in both closed-world and open-world settings. The code is available at https://github.com/ybyangjing/CAMS.

