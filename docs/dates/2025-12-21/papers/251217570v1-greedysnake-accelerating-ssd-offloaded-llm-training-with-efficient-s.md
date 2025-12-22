---
layout: default
title: GreedySnake: Accelerating SSD-Offloaded LLM Training with Efficient Scheduling and Optimizer Step Overlapping
---

# GreedySnake: Accelerating SSD-Offloaded LLM Training with Efficient Scheduling and Optimizer Step Overlapping
**arXiv**：[2512.17570v1](https://arxiv.org/abs/2512.17570) · [PDF](https://arxiv.org/pdf/2512.17570.pdf)  
**作者**：Yikang Yue, Yishu Yin, Xuehai Qian  

**一句话要点**：提出GreedySnake系统，通过垂直调度和优化步骤重叠加速SSD卸载的LLM训练。

**关键词**：SSD卸载训练, 大语言模型训练, 垂直调度, 优化步骤重叠, 训练吞吐量提升

## 3 点简述
- 核心问题：SSD卸载训练中I/O瓶颈限制训练吞吐量，尤其在较小批次下。
- 方法要点：采用垂直调度，先执行层内所有微批次再进入下一层，并重叠优化步骤与前向传递。
- 实验效果：在GPT-65B和GPT-175B上，相比ZeRO-Infinity实现最高2.53倍吞吐量提升。

## 摘要（原文）

> SSD-offloaded training offers a practical and promising approach to making LLM training cost-effective. Building on gradient accumulation with micro-batches, this paper introduces GreedySnake, a new SSD-offloaded training system that employs vertical scheduling, which executes all microbatches of a layer before proceeding to the next. Compared to existing systems that use horizontal scheduling (i.e., executing micro-batches sequentially), GreedySnake achieves higher training throughput with smaller batch sizes, bringing the system much closer to the ideal scenario predicted by the roofline model. To further mitigate the I/O bottleneck, GreedySnake overlaps part of the optimization step with the forward pass of the next iteration. Experimental results on A100 GPUs show that GreedySnake achieves saturated training throughput improvements over ZeRO-Infinity: 1.96x on 1 GPU and 1.93x on 4 GPUs for GPT-65B, and 2.53x on 1 GPU for GPT-175B. The code is open-sourced at https://github.com/npz7yyk/GreedySnake

