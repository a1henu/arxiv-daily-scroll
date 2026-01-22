---
layout: default
title: PROGRESSLM: Towards Progress Reasoning in Vision-Language Models
---

# PROGRESSLM: Towards Progress Reasoning in Vision-Language Models
**arXiv**：[2601.15224v1](https://arxiv.org/abs/2601.15224) · [PDF](https://arxiv.org/pdf/2601.15224.pdf)  
**作者**：Jianshu Zhang, Chengxuan Qian, Haosen Sun, Haoran Lu, Dingcheng Wang, Letian Xue, Han Liu  

**一句话要点**：提出ProgressLM以提升视觉语言模型在任务进度推理上的能力，通过基准测试与两阶段推理方法。

**关键词**：任务进度推理, 视觉语言模型, 长时动态理解, 基准测试, 两阶段推理, 数据集构建

## 3 点简述
- 核心问题：视觉语言模型难以从部分观察中推断任务进度，需长时动态推理而非静态视觉识别。
- 方法要点：引入Progress-Bench基准，探索基于提示和训练的两阶段进度推理范式，包括ProgressLM-45K数据集。
- 实验或效果：测试14个模型显示多数表现不佳，ProgressLM-3B在任务无关训练下实现一致改进，分析错误模式。

## 摘要（原文）

> Estimating task progress requires reasoning over long-horizon dynamics rather than recognizing static visual content. While modern Vision-Language Models (VLMs) excel at describing what is visible, it remains unclear whether they can infer how far a task has progressed from partial observations. To this end, we introduce Progress-Bench, a benchmark for systematically evaluating progress reasoning in VLMs. Beyond benchmarking, we further explore a human-inspired two-stage progress reasoning paradigm through both training-free prompting and training-based approach based on curated dataset ProgressLM-45K. Experiments on 14 VLMs show that most models are not yet ready for task progress estimation, exhibiting sensitivity to demonstration modality and viewpoint changes, as well as poor handling of unanswerable cases. While training-free prompting that enforces structured progress reasoning yields limited and model-dependent gains, the training-based ProgressLM-3B achieves consistent improvements even at a small model scale, despite being trained on a task set fully disjoint from the evaluation tasks. Further analyses reveal characteristic error patterns and clarify when and why progress reasoning succeeds or fails.

