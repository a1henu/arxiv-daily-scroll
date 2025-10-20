---
layout: default
title: OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM
---

# OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM
**arXiv**：[2510.15870v1](https://arxiv.org/abs/2510.15870) · [PDF](https://arxiv.org/pdf/2510.15870.pdf)  
**作者**：Hanrong Ye, Chao-Han Huck Yang, Arushi Goel, Wei Huang, Ligeng Zhu, Yuanhang Su, Sean Lin, An-Chieh Cheng, Zhen Wan, Jinchuan Tian, Yuming Lou, Dong Yang, Zhijian Liu, Yukang Chen, Ambrish Dantrey, Ehsan Jahangiri, Sreyan Ghosh, Daguang Xu, Ehsan Hosseini-Asl, Danial Mohseni Taheri, Vidya Murali, Sifei Liu, Jason Lu, Oluwatobi Olabiyi, Frank Wang, Rafael Valle, Bryan Catanzaro, Andrew Tao, Song Han, Jan Kautz, Hongxu Yin, Pavlo Molchanov  

**一句话要点**：提出OmniVinci架构与数据增强方法，提升多模态理解能力

**关键词**：多模态理解, 模型架构优化, 数据合成, 跨模态对齐, 时间嵌入, 开源LLM

## 3 点简述
- 核心问题：机器需跨模态感知，如人类多感官融合。
- 方法要点：引入OmniAlignNet、Temporal Embedding Grouping和Constrained Rotary Time Embedding。
- 实验或效果：在多个基准上超越Qwen2.5-Omni，训练数据减少6倍。

## 摘要（原文）

> Advancing machine intelligence requires developing the ability to perceive
> across multiple modalities, much as humans sense the world. We introduce
> OmniVinci, an initiative to build a strong, open-source, omni-modal LLM. We
> carefully study the design choices across model architecture and data curation.
> For model architecture, we present three key innovations: (i) OmniAlignNet for
> strengthening alignment between vision and audio embeddings in a shared
> omni-modal latent space; (ii) Temporal Embedding Grouping for capturing
> relative temporal alignment between vision and audio signals; and (iii)
> Constrained Rotary Time Embedding for encoding absolute temporal information in
> omni-modal embeddings. We introduce a curation and synthesis pipeline that
> generates 24M single-modal and omni-modal conversations. We find that
> modalities reinforce one another in both perception and reasoning. Our model,
> OmniVinci, outperforms Qwen2.5-Omni with +19.05 on DailyOmni (cross-modal
> understanding), +1.7 on MMAR (audio), and +3.9 on Video-MME (vision), while
> using just 0.2T training tokens - a 6 times reduction compared to
> Qwen2.5-Omni's 1.2T. We finally demonstrate omni-modal advantages in downstream
> applications spanning robotics, medical AI, and smart factory.

