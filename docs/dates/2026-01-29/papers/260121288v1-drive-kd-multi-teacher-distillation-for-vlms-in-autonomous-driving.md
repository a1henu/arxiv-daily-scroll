---
layout: default
title: Drive-KD: Multi-Teacher Distillation for VLMs in Autonomous Driving
---

# Drive-KD: Multi-Teacher Distillation for VLMs in Autonomous Driving
**arXiv**：[2601.21288v1](https://arxiv.org/abs/2601.21288) · [PDF](https://arxiv.org/pdf/2601.21288.pdf)  
**作者**：Weitong Lian, Zecong Tang, Haoran Li, Tianjian Gao, Yifei Wang, Zixu Wang, Lingyi Meng, Tengju Ru, Zhejun Cui, Yichen Zhu, Hangshuo Cao, Qi Kang, Tianxing Chen, Yusen Qin, Kaixuan Wang, Yu Zhang  

**一句话要点**：提出Drive-KD多教师蒸馏框架，以提升自动驾驶视觉语言模型效率与性能。

**关键词**：自动驾驶, 视觉语言模型, 知识蒸馏, 多教师学习, 推理规划

## 3 点简述
- 核心问题：大型模型在自动驾驶中内存消耗高、推理延迟大，小模型能力不足。
- 方法要点：分解为感知-推理-规划三元组，利用层特定注意力进行知识蒸馏，引入非对称梯度投影缓解冲突。
- 实验或效果：蒸馏后模型内存减少42倍，吞吐提升11.4倍，在DriveBench上超越预训练大模型，规划维度优于GPT-5.1。

## 摘要（原文）

> Autonomous driving is an important and safety-critical task, and recent advances in LLMs/VLMs have opened new possibilities for reasoning and planning in this domain. However, large models demand substantial GPU memory and exhibit high inference latency, while conventional supervised fine-tuning (SFT) often struggles to bridge the capability gaps of small models. To address these limitations, we propose Drive-KD, a framework that decomposes autonomous driving into a "perception-reasoning-planning" triad and transfers these capabilities via knowledge distillation. We identify layer-specific attention as the distillation signal to construct capability-specific single-teacher models that outperform baselines. Moreover, we unify these single-teacher settings into a multi-teacher distillation framework and introduce asymmetric gradient projection to mitigate cross-capability gradient conflicts. Extensive evaluations validate the generalization of our method across diverse model families and scales. Experiments show that our distilled InternVL3-1B model, with ~42 times less GPU memory and ~11.4 times higher throughput, achieves better overall performance than the pretrained 78B model from the same family on DriveBench, and surpasses GPT-5.1 on the planning dimension, providing insights toward efficient autonomous driving VLMs.

