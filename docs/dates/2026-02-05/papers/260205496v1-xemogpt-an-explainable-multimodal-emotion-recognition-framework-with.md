---
layout: default
title: XEmoGPT: An Explainable Multimodal Emotion Recognition Framework with Cue-Level Perception and Reasoning
---

# XEmoGPT: An Explainable Multimodal Emotion Recognition Framework with Cue-Level Perception and Reasoning
**arXiv**：[2602.05496v1](https://arxiv.org/abs/2602.05496) · [PDF](https://arxiv.org/pdf/2602.05496.pdf)  
**作者**：Hanwen Zhang, Yao Liu, Peiyuan Jiang, Lang Junjie, Xie Jun, Yihui He, Yajiao Deng, Siyu Du, Qiao Liu  

**一句话要点**：提出XEmoGPT框架以解决多模态情感识别中线索级感知与推理的挑战

**关键词**：多模态情感识别, 线索级感知, 可解释人工智能, 情感线索推理, 视频音频编码, 数据集构建

## 3 点简述
- 核心问题：现有方法因通用编码器对细粒度情感线索不敏感及数据集标注质量与规模权衡，导致线索级感知与推理受限
- 方法要点：引入VECB和AECB模块增强视频和音频编码器，并构建EmoCue数据集支持线索级推理
- 实验或效果：XEmoGPT在情感线索感知和推理上表现优异，并发布EmoCue-360指标和EmoCue-Eval基准

## 摘要（原文）

> Explainable Multimodal Emotion Recognition plays a crucial role in applications such as human-computer interaction and social media analytics. However, current approaches struggle with cue-level perception and reasoning due to two main challenges: 1) general-purpose modality encoders are pretrained to capture global structures and general semantics rather than fine-grained emotional cues, resulting in limited sensitivity to emotional signals; and 2) available datasets usually involve a trade-off between annotation quality and scale, which leads to insufficient supervision for emotional cues and ultimately limits cue-level reasoning. Moreover, existing evaluation metrics are inadequate for assessing cue-level reasoning performance. To address these challenges, we propose eXplainable Emotion GPT (XEmoGPT), a novel EMER framework capable of both perceiving and reasoning over emotional cues. It incorporates two specialized modules: the Video Emotional Cue Bridge (VECB) and the Audio Emotional Cue Bridge (AECB), which enhance the video and audio encoders through carefully designed tasks for fine-grained emotional cue perception. To further support cue-level reasoning, we construct a large-scale dataset, EmoCue, designed to teach XEmoGPT how to reason over multimodal emotional cues. In addition, we introduce EmoCue-360, an automated metric that extracts and matches emotional cues using semantic similarity, and release EmoCue-Eval, a benchmark of 400 expert-annotated samples covering diverse emotional scenarios. Experimental results show that XEmoGPT achieves strong performance in both emotional cue perception and reasoning.

