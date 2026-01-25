---
layout: default
title: SAMTok: Representing Any Mask with Two Words
---

# SAMTok: Representing Any Mask with Two Words
**arXiv**：[2601.16093v1](https://arxiv.org/abs/2601.16093) · [PDF](https://arxiv.org/pdf/2601.16093.pdf)  
**作者**：Yikang Zhou, Tao Zhang, Dengxian Gong, Yuanzheng Wu, Ye Tian, Haochen Wang, Haobo Yuan, Jiacong Wang, Lu Qi, Hao Fei, Anran Wang, Zhuochen Wang, Yujing Wang, Cheng Chen, Shunping Ji, Xiangtai Li  

**一句话要点**：提出SAMTok将任意区域掩码编码为两个离散令牌，使多模态大语言模型通过标准训练获得像素级能力。

**关键词**：掩码令牌化, 像素级多模态大语言模型, 区域理解, 掩码生成, 强化学习, 离散表示

## 3 点简述
- 核心问题：像素级多模态大语言模型因复杂编码器、专用解码器和训练目标不兼容而难以扩展。
- 方法要点：基于SAM2训练掩码编码器和残差向量量化器，将掩码转换为两个信息丰富的离散令牌，作为新语言令牌集成。
- 实验或效果：在区域描述、视觉问答、指代分割等任务上达到先进或可比性能，并通过强化学习提升掩码生成效果。

## 摘要（原文）

> Pixel-wise capabilities are essential for building interactive intelligent systems. However, pixel-wise multi-modal LLMs (MLLMs) remain difficult to scale due to complex region-level encoders, specialized segmentation decoders, and incompatible training objectives. To address these challenges, we present SAMTok, a discrete mask tokenizer that converts any region mask into two special tokens and reconstructs the mask using these tokens with high fidelity. By treating masks as new language tokens, SAMTok enables base MLLMs (such as the QwenVL series) to learn pixel-wise capabilities through standard next-token prediction and simple reinforcement learning, without architectural modifications and specialized loss design. SAMTok builds on SAM2 and is trained on 209M diverse masks using a mask encoder and residual vector quantizer to produce discrete, compact, and information-rich tokens. With 5M SAMTok-formatted mask understanding and generation data samples, QwenVL-SAMTok attains state-of-the-art or comparable results on region captioning, region VQA, grounded conversation, referring segmentation, scene graph parsing, and multi-round interactive segmentation. We further introduce a textual answer-matching reward that enables efficient reinforcement learning for mask generation, delivering substantial improvements on GRES and GCG benchmarks. Our results demonstrate a scalable and straightforward paradigm for equipping MLLMs with strong pixel-wise capabilities. Our code and models are available.

