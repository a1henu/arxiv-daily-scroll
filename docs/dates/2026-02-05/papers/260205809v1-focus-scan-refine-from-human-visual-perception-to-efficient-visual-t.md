---
layout: default
title: Focus-Scan-Refine: From Human Visual Perception to Efficient Visual Token Pruning
---

# Focus-Scan-Refine: From Human Visual Perception to Efficient Visual Token Pruning
**arXiv**：[2602.05809v1](https://arxiv.org/abs/2602.05809) · [PDF](https://arxiv.org/pdf/2602.05809.pdf)  
**作者**：Enwei Tong, Yuanchao Bai, Yao Zhu, Junjun Jiang, Xianming Liu  

**一句话要点**：提出Focus-Scan-Refine框架以解决视觉语言模型中视觉令牌剪枝的准确性与效率平衡问题

**关键词**：视觉语言模型, 令牌剪枝, 训练无关剪枝, 视觉感知启发, 推理效率优化, 上下文聚合

## 3 点简述
- 核心问题：视觉语言模型生成大量视觉令牌导致推理延迟和内存占用高，现有剪枝方法在激进压缩下难以平衡局部证据与全局上下文。
- 方法要点：模仿人类视觉感知，通过聚焦关键证据、扫描补充上下文和精炼聚合细节的三步框架进行训练无关的令牌剪枝。
- 实验或效果：在多个视觉语言模型和基准测试中，FSR在准确性与效率权衡上优于现有最先进剪枝方法。

## 摘要（原文）

> Vision-language models (VLMs) often generate massive visual tokens that greatly increase inference latency and memory footprint; while training-free token pruning offers a practical remedy, existing methods still struggle to balance local evidence and global context under aggressive compression. We propose Focus-Scan-Refine (FSR), a human-inspired, plug-and-play pruning framework that mimics how humans answer visual questions: focus on key evidence, then scan globally if needed, and refine the scanned context by aggregating relevant details. FSR first focuses on key evidence by combining visual importance with instruction relevance, avoiding the bias toward visually salient but query-irrelevant regions. It then scans for complementary context conditioned on the focused set, selecting tokens that are most different from the focused evidence. Finally, FSR refines the scanned context by aggregating nearby informative tokens into the scan anchors via similarity-based assignment and score-weighted merging, without increasing the token budget. Extensive experiments across multiple VLM backbones and vision-language benchmarks show that FSR consistently improves the accuracy-efficiency trade-off over existing state-of-the-art pruning methods. The source codes can be found at https://github.com/ILOT-code/FSR

