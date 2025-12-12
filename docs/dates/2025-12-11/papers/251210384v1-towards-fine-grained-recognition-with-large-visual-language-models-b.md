---
layout: default
title: Towards Fine-Grained Recognition with Large Visual Language Models: Benchmark and Optimization Strategies
---

# Towards Fine-Grained Recognition with Large Visual Language Models: Benchmark and Optimization Strategies
**arXiv**：[2512.10384v1](https://arxiv.org/abs/2512.10384) · [PDF](https://arxiv.org/pdf/2512.10384.pdf)  
**作者**：Cong Pang, Hongtao Yu, Zixuan Chen, Lewei Lu, Xin Lou  

**一句话要点**：提出FROW基准与优化策略以提升大视觉语言模型在细粒度识别任务中的性能

**关键词**：细粒度识别, 大视觉语言模型, 基准评估, 数据优化, 训练策略, 开放世界数据

## 3 点简述
- 现有基准忽视细粒度识别，影响实际应用；引入FROW基准评估LVLMs
- 从数据构建和训练过程提出优化策略，包括马赛克数据和开放世界数据
- 实验显示优化策略显著提升识别准确率，预训练加入细粒度数据可提高10%

## 摘要（原文）

> Large Vision Language Models (LVLMs) have made remarkable progress, enabling sophisticated vision-language interaction and dialogue applications. However, existing benchmarks primarily focus on reasoning tasks, often neglecting fine-grained recognition, which is crucial for practical application scenarios. To address this gap, we introduce the Fine-grained Recognition Open World (FROW) benchmark, designed for detailed evaluation of LVLMs with GPT-4o. On the basis of that, we propose a novel optimization strategy from two perspectives: \textit{data construction} and \textit{training process}, to improve the performance of LVLMs. Our dataset includes mosaic data, which combines multiple short-answer responses, and open-world data, generated from real-world questions and answers using GPT-4o, creating a comprehensive framework for evaluating fine-grained recognition in LVLMs. Experiments show that mosaic data improves category recognition accuracy by 1\% and open-world data boosts FROW benchmark accuracy by 10\%-20\% and content accuracy by 6\%-12\%. Meanwhile, incorporating fine-grained data into the pre-training phase can improve the model's category recognition accuracy by up to 10\%. The benchmark will be available at https://github.com/pc-inno/FROW.

