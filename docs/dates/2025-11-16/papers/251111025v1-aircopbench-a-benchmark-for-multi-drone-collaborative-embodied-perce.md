---
layout: default
title: AirCopBench: A Benchmark for Multi-drone Collaborative Embodied Perception and Reasoning
---

# AirCopBench: A Benchmark for Multi-drone Collaborative Embodied Perception and Reasoning
**arXiv**：[2511.11025v1](https://arxiv.org/abs/2511.11025) · [PDF](https://arxiv.org/pdf/2511.11025.pdf)  
**作者**：Jirong Zha, Yuxuan Fan, Tianyu Zhang, Geng Chen, Yingfeng Chen, Chen Gao, Xinlei Chen  

**一句话要点**：提出AirCopBench基准以评估多无人机在退化感知条件下的协作感知与推理

**关键词**：多无人机协作, 多模态大模型评估, 退化感知场景, 协作感知基准, 仿真到真实迁移

## 3 点简述
- 多模态大模型在单智能体视觉任务中表现良好，但缺乏多智能体协作感知的评估基准
- 构建包含14.6k+问题的基准，涵盖场景理解、物体理解、感知评估和协作决策等任务维度
- 评估40个模型显示协作感知任务存在显著性能差距，最佳模型平均落后人类24.38%

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown promise in single-agent vision tasks, yet benchmarks for evaluating multi-agent collaborative perception remain scarce. This gap is critical, as multi-drone systems provide enhanced coverage, robustness, and collaboration compared to single-sensor setups. Existing multi-image benchmarks mainly target basic perception tasks using high-quality single-agent images, thus failing to evaluate MLLMs in more complex, egocentric collaborative scenarios, especially under real-world degraded perception conditions.To address these challenges, we introduce AirCopBench, the first comprehensive benchmark designed to evaluate MLLMs in embodied aerial collaborative perception under challenging perceptual conditions. AirCopBench includes 14.6k+ questions derived from both simulator and real-world data, spanning four key task dimensions: Scene Understanding, Object Understanding, Perception Assessment, and Collaborative Decision, across 14 task types. We construct the benchmark using data from challenging degraded-perception scenarios with annotated collaborative events, generating large-scale questions through model-, rule-, and human-based methods under rigorous quality control. Evaluations on 40 MLLMs show significant performance gaps in collaborative perception tasks, with the best model trailing humans by 24.38% on average and exhibiting inconsistent results across tasks. Fine-tuning experiments further confirm the feasibility of sim-to-real transfer in aerial collaborative perception and reasoning.

