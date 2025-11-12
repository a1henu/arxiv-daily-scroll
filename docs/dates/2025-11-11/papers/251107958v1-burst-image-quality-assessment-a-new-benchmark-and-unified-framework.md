---
layout: default
title: Burst Image Quality Assessment: A New Benchmark and Unified Framework for Multiple Downstream Tasks
---

# Burst Image Quality Assessment: A New Benchmark and Unified Framework for Multiple Downstream Tasks
**arXiv**：[2511.07958v1](https://arxiv.org/abs/2511.07958) · [PDF](https://arxiv.org/pdf/2511.07958.pdf)  
**作者**：Xiaoye Liang, Lai Jiang, Minglang Qiao, Yichen Guo, Yue Zhang, Xin Deng, Shengxi Li, Yufan Liu, Mai Xu  

**一句话要点**：提出突发图像质量评估任务与统一框架，以优化多下游任务性能。

**关键词**：突发图像质量评估, 任务驱动提示, 异构知识蒸馏, 下游任务优化, 基准数据集

## 3 点简述
- 突发图像冗余导致存储传输负担增加，下游任务效率降低。
- 开发任务驱动提示生成网络，结合异构知识蒸馏学习任务先验。
- 在10个下游场景中验证，提升去噪和超分辨率任务PSNR 0.33 dB。

## 摘要（原文）

> In recent years, the development of burst imaging technology has improved the capture and processing capabilities of visual data, enabling a wide range of applications. However, the redundancy in burst images leads to the increased storage and transmission demands, as well as reduced efficiency of downstream tasks. To address this, we propose a new task of Burst Image Quality Assessment (BuIQA), to evaluate the task-driven quality of each frame within a burst sequence, providing reasonable cues for burst image selection. Specifically, we establish the first benchmark dataset for BuIQA, consisting of $7,346$ burst sequences with $45,827$ images and $191,572$ annotated quality scores for multiple downstream scenarios. Inspired by the data analysis, a unified BuIQA framework is proposed to achieve an efficient adaption for BuIQA under diverse downstream scenarios. Specifically, a task-driven prompt generation network is developed with heterogeneous knowledge distillation, to learn the priors of the downstream task. Then, the task-aware quality assessment network is introduced to assess the burst image quality based on the task prompt. Extensive experiments across 10 downstream scenarios demonstrate the impressive BuIQA performance of the proposed approach, outperforming the state-of-the-art. Furthermore, it can achieve $0.33$ dB PSNR improvement in the downstream tasks of denoising and super-resolution, by applying our approach to select the high-quality burst frames.

