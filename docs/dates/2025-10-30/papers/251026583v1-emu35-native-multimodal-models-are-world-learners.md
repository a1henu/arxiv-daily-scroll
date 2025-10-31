---
layout: default
title: Emu3.5: Native Multimodal Models are World Learners
---

# Emu3.5: Native Multimodal Models are World Learners
**arXiv**：[2510.26583v1](https://arxiv.org/abs/2510.26583) · [PDF](https://arxiv.org/pdf/2510.26583.pdf)  
**作者**：Yufeng Cui, Honghao Chen, Haoge Deng, Xu Huang, Xinghang Li, Jirong Liu, Yang Liu, Zhuoyan Luo, Jinsheng Wang, Wenxuan Wang, Yueze Wang, Chengyuan Wang, Fan Zhang, Yingli Zhao, Ting Pan, Xianduo Li, Zecheng Hao, Wenxuan Ma, Zhuo Chen, Yulong Ao, Tiejun Huang, Zhongyuan Wang, Xinlong Wang  

**一句话要点**：提出Emu3.5原生多模态世界模型，实现跨视觉语言的状态预测与生成。

**关键词**：多模态世界模型, 视觉语言交织生成, 离散扩散适应, 强化学习后训练, 开源模型

## 3 点简述
- 核心问题：构建能原生处理视觉语言交织输入输出的多模态模型。
- 方法要点：端到端预训练与强化学习后训练，结合DiDA提升推理效率。
- 实验或效果：在图像生成与编辑任务中媲美Gemini 2.5 Flash，开源支持研究。

## 摘要（原文）

> We introduce Emu3.5, a large-scale multimodal world model that natively
> predicts the next state across vision and language. Emu3.5 is pre-trained
> end-to-end with a unified next-token prediction objective on a corpus of
> vision-language interleaved data containing over 10 trillion tokens, primarily
> derived from sequential frames and transcripts of internet videos. The model
> naturally accepts interleaved vision-language inputs and generates interleaved
> vision-language outputs. Emu3.5 is further post-trained with large-scale
> reinforcement learning to enhance multimodal reasoning and generation. To
> improve inference efficiency, we propose Discrete Diffusion Adaptation (DiDA),
> which converts token-by-token decoding into bidirectional parallel prediction,
> accelerating per-image inference by about 20x without sacrificing performance.
> Emu3.5 exhibits strong native multimodal capabilities, including long-horizon
> vision-language generation, any-to-image (X2I) generation, and complex
> text-rich image generation. It also exhibits generalizable world-modeling
> abilities, enabling spatiotemporally consistent world exploration and
> open-world embodied manipulation across diverse scenarios and tasks. For
> comparison, Emu3.5 achieves performance comparable to Gemini 2.5 Flash Image
> (Nano Banana) on image generation and editing tasks and demonstrates superior
> results on a suite of interleaved generation tasks. We open-source Emu3.5 at
> https://github.com/baaivision/Emu3.5 to support community research.

