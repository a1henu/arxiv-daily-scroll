---
layout: default
title: Layer as Puzzle Pieces: Compressing Large Language Models through Layer Concatenation
---

# Layer as Puzzle Pieces: Compressing Large Language Models through Layer Concatenation
**arXiv**：[2510.15304v1](https://arxiv.org/abs/2510.15304) · [PDF](https://arxiv.org/pdf/2510.15304.pdf)  
**作者**：Fei Wang, Li Shen, Liang Ding, Chao Xue, Ye Liu, Changxing Ding  

**一句话要点**：提出CoMe方法，通过层拼接压缩大语言模型以降低计算存储需求

**关键词**：大语言模型压缩, 结构化剪枝, 层拼接合并, 分层蒸馏, 通道敏感度, 后训练恢复

## 3 点简述
- 核心问题：大语言模型尺寸大导致高计算存储成本，现有结构化剪枝方法忽略保留剪枝部分能力
- 方法要点：使用通道敏感度指标和层拼接合并技术，结合分层蒸馏后训练过程
- 实验或效果：在七个基准测试中，剪枝30%参数的LLaMA-2-7b模型保持83%原始平均准确率

## 摘要（原文）

> Large Language Models excel at natural language processing tasks, but their
> massive size leads to high computational and storage demands. Recent works have
> sought to reduce their model size through layer-wise structured pruning.
> However, they tend to ignore retaining the capabilities in the pruned part. In
> this work, we re-examine structured pruning paradigms and uncover several key
> limitations: 1) notable performance degradation due to direct layer removal, 2)
> incompetent linear weight layer aggregation, and 3) the lack of effective
> post-training recovery mechanisms. To address these limitations, we propose
> CoMe, including a progressive layer pruning framework with a
> Concatenation-based Merging technology and a hierarchical distillation
> post-training process. Specifically, we introduce a channel sensitivity metric
> that utilizes activation intensity and weight norms for fine-grained channel
> selection. Subsequently, we employ a concatenation-based layer merging method
> to fuse the most critical channels across adjacent layers, enabling progressive
> model size reduction. Finally, we propose a hierarchical distillation protocol
> that leverages the correspondences between the original and pruned model layers
> established during pruning, thereby enabling efficient knowledge transfer.
> Experiments on seven benchmarks show that CoMe achieves state-of-the-art
> performance; when pruning 30% of LLaMA-2-7b's parameters, the pruned model
> retains 83% of its original average accuracy. Our code is available at
> https://github.com/MPI-Lab/CoMe.

