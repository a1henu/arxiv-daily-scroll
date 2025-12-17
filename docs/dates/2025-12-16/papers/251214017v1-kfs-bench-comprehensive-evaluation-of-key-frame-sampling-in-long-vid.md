---
layout: default
title: KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding
---

# KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding
**arXiv**：[2512.14017v1](https://arxiv.org/abs/2512.14017) · [PDF](https://arxiv.org/pdf/2512.14017.pdf)  
**作者**：Zongyao Li, Kengo Ishida, Satoshi Yamazaki, Xiaotong Ji, Jianquan Liu  

**一句话要点**：提出KFS-Bench基准以直接评估长视频问答中的关键帧采样策略

**关键词**：长视频理解, 关键帧采样, 视频问答, 基准评估, 多模态大语言模型

## 3 点简述
- 核心问题：长视频问答中关键帧采样缺乏直接评估基准，现有方法仅通过问答准确率间接衡量。
- 方法要点：设计多场景标注基准，引入采样质量指标，开发基于问题-视频相关性的自适应平衡采样方法。
- 实验或效果：基准支持全面分析采样方法，新方法在采样质量和问答性能上表现优异。

## 摘要（原文）

> We propose KFS-Bench, the first benchmark for key frame sampling in long video question answering (QA), featuring multi-scene annotations to enable direct and robust evaluation of sampling strategies. Key frame sampling is crucial for efficient long-form video understanding. In long video QA, selecting informative frames enables multimodal large language models (MLLMs) to improve both accuracy and efficiency. KFS-Bench addresses the limitation of prior works that only indirectly assess frame selection quality via QA accuracy. By providing ground-truth annotations of multiple disjoint scenes required per question, KFS-Bench allows us to directly analyze how different sampling approaches capture essential content across an entire long video. Using KFS-Bench, we conduct a comprehensive study of key frame sampling methods and identify that not only sampling precision but also scene coverage and sampling balance are the key factors influencing QA performance. Regarding all the factors, we design a novel sampling quality metric that correlates with QA accuracy. Furthermore, we develop a novel key frame sampling method that leverages question-video relevance to balance sampling diversity against question-frame similarity, thereby improving coverage of relevant scenes. Our adaptively balanced sampling approach achieves superior performance in both key frame sampling and QA performance. The benchmark is available at https://github.com/NEC-VID/KFS-Bench.

