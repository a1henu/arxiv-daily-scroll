---
layout: default
title: MOVA: Towards Scalable and Synchronized Video-Audio Generation
---

# MOVA: Towards Scalable and Synchronized Video-Audio Generation
**arXiv**：[2602.08794v1](https://arxiv.org/abs/2602.08794) · [PDF](https://arxiv.org/pdf/2602.08794.pdf)  
**作者**：SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  

**一句话要点**：提出MOVA开源模型以解决音视频同步生成的可扩展性和质量问题

**关键词**：音视频同步生成, 混合专家架构, 开源模型, 图像-文本到音视频生成, 高效推理

## 3 点简述
- 核心问题：现有音视频生成依赖级联管道，导致成本高、误差累积和质量下降
- 方法要点：采用混合专家架构，共320亿参数，支持图像-文本到音视频的生成任务
- 实验或效果：生成高质量同步音视频内容，包括唇语同步、环境音效和内容对齐音乐

## 摘要（原文）

> Audio is indispensable for real-world video, yet generation models have largely overlooked audio components. Current approaches to producing audio-visual content often rely on cascaded pipelines, which increase cost, accumulate errors, and degrade overall quality. While systems such as Veo 3 and Sora 2 emphasize the value of simultaneous generation, joint multimodal modeling introduces unique challenges in architecture, data, and training. Moreover, the closed-source nature of existing systems limits progress in the field. In this work, we introduce MOVA (MOSS Video and Audio), an open-source model capable of generating high-quality, synchronized audio-visual content, including realistic lip-synced speech, environment-aware sound effects, and content-aligned music. MOVA employs a Mixture-of-Experts (MoE) architecture, with a total of 32B parameters, of which 18B are active during inference. It supports IT2VA (Image-Text to Video-Audio) generation task. By releasing the model weights and code, we aim to advance research and foster a vibrant community of creators. The released codebase features comprehensive support for efficient inference, LoRA fine-tuning, and prompt enhancement.

