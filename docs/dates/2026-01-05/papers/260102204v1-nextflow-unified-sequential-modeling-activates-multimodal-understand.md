---
layout: default
title: NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
---

# NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
**arXiv**：[2601.02204v1](https://arxiv.org/abs/2601.02204) · [PDF](https://arxiv.org/pdf/2601.02204.pdf)  
**作者**：Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen, Yangyang Song, Yongsheng Dong, Shikun Sun, Xian Li, Xu Wang, Yi Jiang, Hu Ye, Bo Chen, Yiming Gao, Peng Liu, Akide Liu, Zhipeng Yang, Qili Deng, Linjie Xing, Jiyang Liu, Zhao Wang, Yang Zhou, Mingcong Liu, Yi Zhang, Qian He, Xiwei Hu, Zhongqi Qi, Jie Shao, Zhiye Fu, Shuai Wang, Fangmin Chen, Xuezhi Chai, Zhihua Wu, Yitong Wang, Zehuan Yuan, Daniel K. Du, Xinglong Wu  

**一句话要点**：提出NextFlow统一自回归模型，通过多模态序列建模实现理解与生成任务。

**关键词**：多模态理解, 图像生成, 自回归模型, 统一序列建模, 视频生成, 强化学习

## 3 点简述
- 核心问题：传统方法难以统一处理文本和图像的序列与层次特性，导致多模态任务效率低。
- 方法要点：采用统一解码器架构，文本用下一词预测，图像用下一尺度预测，提升生成速度与稳定性。
- 实验或效果：在6万亿标记上训练，生成1024x1024图像仅需5秒，性能媲美专业扩散模型。

## 摘要（原文）

> We present NextFlow, a unified decoder-only autoregressive transformer trained on 6 trillion interleaved text-image discrete tokens. By leveraging a unified vision representation within a unified autoregressive architecture, NextFlow natively activates multimodal understanding and generation capabilities, unlocking abilities of image editing, interleaved content and video generation. Motivated by the distinct nature of modalities - where text is strictly sequential and images are inherently hierarchical - we retain next-token prediction for text but adopt next-scale prediction for visual generation. This departs from traditional raster-scan methods, enabling the generation of 1024x1024 images in just 5 seconds - orders of magnitude faster than comparable AR models. We address the instabilities of multi-scale generation through a robust training recipe. Furthermore, we introduce a prefix-tuning strategy for reinforcement learning. Experiments demonstrate that NextFlow achieves state-of-the-art performance among unified models and rivals specialized diffusion baselines in visual quality.

