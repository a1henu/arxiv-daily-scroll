---
layout: default
title: LTX-2: Efficient Joint Audio-Visual Foundation Model
---

# LTX-2: Efficient Joint Audio-Visual Foundation Model
**arXiv**：[2601.03233v1](https://arxiv.org/abs/2601.03233) · [PDF](https://arxiv.org/pdf/2601.03233.pdf)  
**作者**：Yoav HaCohen, Benny Brazowski, Nisan Chiprut, Yaki Bitterman, Andrew Kvochko, Avishai Berkowitz, Daniel Shalem, Daphna Lifschitz, Dudu Moshe, Eitan Porat, Eitan Richardson, Guy Shiran, Itay Chachy, Jonathan Chetboun, Michael Finkelson, Michael Kupchick, Nir Zabari, Nitzan Guetta, Noa Kotler, Ofir Bibi, Ori Gordon, Poriya Panet, Roi Benita, Shahar Armon, Victor Kulikov, Yaron Inger, Yonatan Shiftan, Zeev Melumian, Zeev Farbman  

**一句话要点**：提出LTX-2联合音视频基础模型，以高效生成高质量同步音视频内容。

**关键词**：音视频生成, 联合基础模型, 非对称Transformer, 跨模态注意力, 模态感知引导, 开源模型

## 3 点简述
- 核心问题：现有文本到视频扩散模型缺乏音频，缺失语义和情感线索。
- 方法要点：采用非对称双流Transformer，结合双向跨注意力与模态感知分类器自由引导。
- 实验或效果：在开源系统中达到领先音视频质量和提示遵循，计算成本低。

## 摘要（原文）

> Recent text-to-video diffusion models can generate compelling video sequences, yet they remain silent -- missing the semantic, emotional, and atmospheric cues that audio provides. We introduce LTX-2, an open-source foundational model capable of generating high-quality, temporally synchronized audiovisual content in a unified manner. LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning. This architecture enables efficient training and inference of a unified audiovisual model while allocating more capacity for video generation than audio generation. We employ a multilingual text encoder for broader prompt understanding and introduce a modality-aware classifier-free guidance (modality-CFG) mechanism for improved audiovisual alignment and controllability. Beyond generating speech, LTX-2 produces rich, coherent audio tracks that follow the characters, environment, style, and emotion of each scene -- complete with natural background and foley elements. In our evaluations, the model achieves state-of-the-art audiovisual quality and prompt adherence among open-source systems, while delivering results comparable to proprietary models at a fraction of their computational cost and inference time. All model weights and code are publicly released.

