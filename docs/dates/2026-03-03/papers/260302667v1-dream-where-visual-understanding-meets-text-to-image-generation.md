---
layout: default
title: DREAM: Where Visual Understanding Meets Text-to-Image Generation
---

# DREAM: Where Visual Understanding Meets Text-to-Image Generation
**arXiv**：[2603.02667v1](https://arxiv.org/abs/2603.02667) · [PDF](https://arxiv.org/pdf/2603.02667.pdf)  
**作者**：Chao Li, Tianhong Li, Sai Vidyaranya Nuthalapati, Hong-You Chen, Satya Narayan Shukla, Yonghuan Yang, Jun Xiao, Xiangjun Fan, Aashu Singh, Dina Katabi, Shlok Kumar Mishra  

**一句话要点**：提出DREAM统一框架，通过联合优化判别与生成目标，解决视觉理解与文本到图像生成的融合挑战。

**关键词**：统一多模态模型, 文本到图像生成, 视觉表示学习, 渐进掩码训练, 语义对齐解码, 判别生成协同

## 3 点简述
- 核心问题：统一视觉表示学习与文本到图像生成是跨模态学习的关键挑战。
- 方法要点：采用Masking Warmup渐进掩码和Semantically Aligned Decoding，提升训练稳定性和文本图像对齐。
- 实验或效果：在CC12M上训练，ImageNet线性探测准确率72.7%，FID 4.25，优于CLIP和FLUID。

## 摘要（原文）

> Unifying visual representation learning and text-to-image (T2I) generation within a single model remains a central challenge in multimodal learning. We introduce DREAM, a unified framework that jointly optimizes discriminative and generative objectives, while learning strong visual representations. DREAM is built on two key techniques: During training, Masking Warmup, a progressive masking schedule, begins with minimal masking to establish the contrastive alignment necessary for representation learning, then gradually transitions to full masking for stable generative training. At inference, DREAM employs Semantically Aligned Decoding to align partially masked image candidates with the target text and select the best one for further decoding, improving text-image fidelity (+6.3%) without external rerankers. Trained solely on CC12M, DREAM achieves 72.7% ImageNet linear-probing accuracy (+1.1% over CLIP) and an FID of 4.25 (+6.2% over FLUID), with consistent gains in few-shot classification, semantic segmentation, and depth estimation. These results demonstrate that discriminative and generative objectives can be synergistic, allowing unified multimodal models that excel at both visual understanding and generation.

