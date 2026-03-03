---
layout: default
title: ROSER: Few-Shot Robotic Sequence Retrieval for Scalable Robot Learning
---

# ROSER: Few-Shot Robotic Sequence Retrieval for Scalable Robot Learning
**arXiv**：[2603.01474v1](https://arxiv.org/abs/2603.01474) · [PDF](https://arxiv.org/pdf/2603.01474.pdf)  
**作者**：Zillur Rahman, Eddison Pham, Alejandro Daniel Noel, Cristian Meo  

**一句话要点**：提出ROSER框架以解决机器人学习中任务标记数据稀缺问题，通过少样本检索从无标签日志提取可重用轨迹。

**关键词**：少样本检索, 机器人序列检索, 度量学习, 数据利用, 时序窗口, 任务无关学习

## 3 点简述
- 核心问题：大规模机器人数据集多为连续日志，缺乏任务标记和分段，难以直接用于学习框架。
- 方法要点：ROSER学习任务无关的时序窗口度量空间，仅需3-5个参考示例即可准确检索，无需任务特定训练。
- 实验或效果：在多个数据集上超越现有方法，实现亚毫秒级推理和优越分布对齐，提升数据可用性。

## 摘要（原文）

> A critical bottleneck in robot learning is the scarcity of task-labeled, segmented training data, despite the abundance of large-scale robotic datasets recorded as long, continuous interaction logs. Existing datasets contain vast amounts of diverse behaviors, yet remain structurally incompatible with modern learning frameworks that require cleanly segmented, task-specific trajectories. We address this data utilization crisis by formalizing robotic sequence retrieval: the task of extracting reusable, task-centric segments from unlabeled logs using only a few reference examples. We introduce ROSER, a lightweight few-shot retrieval framework that learns task-agnostic metric spaces over temporal windows, enabling accurate retrieval with as few as 3-5 demonstrations, without any task-specific training required. To validate our approach, we establish comprehensive evaluation protocols and benchmark ROSER against classical alignment methods, learned embeddings, and language model baselines across three large-scale datasets (e.g., LIBERO, DROID, and nuScenes). Our experiments demonstrate that ROSER consistently outperforms all prior methods in both accuracy and efficiency, achieving sub-millisecond per-match inference while maintaining superior distributional alignment. By reframing data curation as few-shot retrieval, ROSER provides a practical pathway to unlock underutilized robotic datasets, fundamentally improving data availability for robot learning.

