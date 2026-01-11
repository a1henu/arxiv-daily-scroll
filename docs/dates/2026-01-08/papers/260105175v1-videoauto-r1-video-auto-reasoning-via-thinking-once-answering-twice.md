---
layout: default
title: VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice
---

# VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice
**arXiv**：[2601.05175v1](https://arxiv.org/abs/2601.05175) · [PDF](https://arxiv.org/pdf/2601.05175.pdf)  
**作者**：Shuming Liu, Mingchen Zhuge, Changsheng Zhao, Jun Chen, Lemeng Wu, Zechun Liu, Chenchen Zhu, Zhipeng Cai, Chong Zhou, Haozhe Liu, Ernie Chang, Saksham Suri, Hongyu Xu, Qi Qian, Wei Wen, Balakrishnan Varadarajan, Zhuang Liu, Hu Xu, Florian Bordes, Raghuraman Krishnamoorthi, Bernard Ghanem, Vikas Chandra, Yunyang Xiong  

**一句话要点**：提出VideoAuto-R1框架，通过按需推理策略提升视频理解效率与准确性。

**关键词**：视频理解, 链式思维推理, 按需推理, 效率优化, 视频问答

## 3 点简述
- 核心问题：链式思维推理在视频理解中是否必要，其计算成本高但优势未明。
- 方法要点：采用“思考一次，回答两次”训练范式，基于初始答案置信度决定推理激活。
- 实验或效果：在视频QA和定位基准上实现SOTA精度，平均响应长度减少约3.3倍。

## 摘要（原文）

> Chain-of-thought (CoT) reasoning has emerged as a powerful tool for multimodal large language models on video understanding tasks. However, its necessity and advantages over direct answering remain underexplored. In this paper, we first demonstrate that for RL-trained video models, direct answering often matches or even surpasses CoT performance, despite CoT producing step-by-step analyses at a higher computational cost. Motivated by this, we propose VideoAuto-R1, a video understanding framework that adopts a reason-when-necessary strategy. During training, our approach follows a Thinking Once, Answering Twice paradigm: the model first generates an initial answer, then performs reasoning, and finally outputs a reviewed answer. Both answers are supervised via verifiable rewards. During inference, the model uses the confidence score of the initial answer to determine whether to proceed with reasoning. Across video QA and grounding benchmarks, VideoAuto-R1 achieves state-of-the-art accuracy with significantly improved efficiency, reducing the average response length by ~3.3x, e.g., from 149 to just 44 tokens. Moreover, we observe a low rate of thinking-mode activation on perception-oriented tasks, but a higher rate on reasoning-intensive tasks. This suggests that explicit language-based reasoning is generally beneficial but not always necessary.

