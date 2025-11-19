---
layout: default
title: Vision Large Language Models Are Good Noise Handlers in Engagement Analysis
---

# Vision Large Language Models Are Good Noise Handlers in Engagement Analysis
**arXiv**：[2511.14749v1](https://arxiv.org/abs/2511.14749) · [PDF](https://arxiv.org/pdf/2511.14749.pdf)  
**作者**：Alexander Vedernikov, Puneet Kumar, Haoyu Chen, Tapio Seppänen, Xiaobai Li  

**一句话要点**：提出基于视觉大语言模型的框架以解决视频参与度分析中的标签噪声问题

**关键词**：视频参与度分析, 视觉大语言模型, 标签噪声处理, 课程学习, 软标签优化

## 3 点简述
- 核心问题：视频参与度识别受主观和噪声标签限制，影响模型性能。
- 方法要点：利用VLMs通过问卷提取行为线索，划分数据并采用课程学习和软标签优化策略。
- 实验或效果：在EngageNet等基准上超越先前方法，F1分数最高提升+1.21%。

## 摘要（原文）

> Engagement recognition in video datasets, unlike traditional image classification tasks, is particularly challenged by subjective labels and noise limiting model performance. To overcome the challenges of subjective and noisy engagement labels, we propose a framework leveraging Vision Large Language Models (VLMs) to refine annotations and guide the training process. Our framework uses a questionnaire to extract behavioral cues and split data into high- and low-reliability subsets. We also introduce a training strategy combining curriculum learning with soft label refinement, gradually incorporating ambiguous samples while adjusting supervision to reflect uncertainty. We demonstrate that classical computer vision models trained on refined high-reliability subsets and enhanced with our curriculum strategy show improvements, highlighting benefits of addressing label subjectivity with VLMs. This method surpasses prior state of the art across engagement benchmarks such as EngageNet (three of six feature settings, maximum improvement of +1.21%), and DREAMS / PAFE with F1 gains of +0.22 / +0.06.

