---
layout: default
title: TabFlash: Efficient Table Understanding with Progressive Question Conditioning and Token Focusing
---

# TabFlash: Efficient Table Understanding with Progressive Question Conditioning and Token Focusing
**arXiv**：[2511.13283v1](https://arxiv.org/abs/2511.13283) · [PDF](https://arxiv.org/pdf/2511.13283.pdf)  
**作者**：Jongha Kim, Minseong Bae, Sanghyeok Lee, Jinsung Yoon, Hyunwoo J. Kim  

**一句话要点**：提出TabFlash方法，通过渐进问题注入和令牌聚焦提升表格图像理解效率与效果

**关键词**：表格图像理解, 多模态大语言模型, 渐进问题注入, 令牌剪枝, 令牌聚焦训练, 效率优化

## 3 点简述
- 核心问题：表格图像存在冗余背景和问题无关区域，导致MLLM视觉特征冗余且低效
- 方法要点：采用渐进问题注入、令牌剪枝和令牌聚焦训练，生成紧凑且问题感知的视觉特征
- 实验效果：在表格理解任务中实现SOTA性能，FLOPs和内存使用分别减少27%和30%

## 摘要（原文）

> Table images present unique challenges for effective and efficient understanding due to the need for question-specific focus and the presence of redundant background regions. Existing Multimodal Large Language Model (MLLM) approaches often overlook these characteristics, resulting in uninformative and redundant visual representations. To address these issues, we aim to generate visual features that are both informative and compact to improve table understanding. We first propose progressive question conditioning, which injects the question into Vision Transformer layers with gradually increasing frequency, considering each layer's capacity to handle additional information, to generate question-aware visual features. To reduce redundancy, we introduce a pruning strategy that discards background tokens, thereby improving efficiency. To mitigate information loss from pruning, we further propose token focusing, a training strategy that encourages the model to concentrate essential information in the retained tokens. By combining these approaches, we present TabFlash, an efficient and effective MLLM for table understanding. TabFlash achieves state-of-the-art performance, outperforming both open-source and proprietary MLLMs, while requiring 27% less FLOPs and 30% less memory usage compared to the second-best MLLM.

