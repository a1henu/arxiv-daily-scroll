---
layout: default
title: MergeSlide: Continual Model Merging and Task-to-Class Prompt-Aligned Inference for Lifelong Learning on Whole Slide Images
---

# MergeSlide: Continual Model Merging and Task-to-Class Prompt-Aligned Inference for Lifelong Learning on Whole Slide Images
**arXiv**：[2511.13099v1](https://arxiv.org/abs/2511.13099) · [PDF](https://arxiv.org/pdf/2511.13099.pdf)  
**作者**：Doanh C. Bui, Ba Hung Ngo, Hoai Luan Pham, Khang Nguyen, Maï K. Nguyen, Yasuhiko Nakashima  

**一句话要点**：提出MergeSlide框架，通过模型合并和提示对齐推理解决全切片图像终身学习问题

**关键词**：终身学习, 全切片图像, 模型合并, 提示对齐, 灾难性遗忘, 视觉语言模型

## 3 点简述
- 核心问题：全切片图像终身学习中资源消耗大且易发生灾难性遗忘
- 方法要点：利用正交合并策略和任务到类提示对齐推理实现模型统一
- 实验或效果：在TCGA数据集上优于基于排练和零样本的基线方法

## 摘要（原文）

> Lifelong learning on Whole Slide Images (WSIs) aims to train or fine-tune a unified model sequentially on cancer-related tasks, reducing the resources and effort required for data transfer and processing, especially given the gigabyte-scale size of WSIs. In this paper, we introduce MergeSlide, a simple yet effective framework that treats lifelong learning as a model merging problem by leveraging a vision-language pathology foundation model. When a new task arrives, it is: 1) defined with class-aware prompts, 2) fine-tuned for a few epochs using an MLP-free backbone, and 3) merged into a unified model using an orthogonal continual merging strategy that preserves performance and mitigates catastrophic forgetting. For inference under the class-incremental learning (CLASS-IL) setting, where task identity is unknown, we introduce Task-to-Class Prompt-aligned (TCP) inference. Specifically, TCP first identifies the most relevant task using task-level prompts and then applies the corresponding class-aware prompts to generate predictions. To evaluate MergeSlide, we conduct experiments on a stream of six TCGA datasets. The results show that MergeSlide outperforms both rehearsal-based continual learning and vision-language zero-shot baselines. Code and data are available at https://github.com/caodoanh2001/MergeSlide.

