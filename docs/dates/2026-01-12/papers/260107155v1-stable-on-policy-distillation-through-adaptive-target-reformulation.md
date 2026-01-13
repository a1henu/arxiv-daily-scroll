---
layout: default
title: Stable On-Policy Distillation through Adaptive Target Reformulation
---

# Stable On-Policy Distillation through Adaptive Target Reformulation
**arXiv**：[2601.07155v1](https://arxiv.org/abs/2601.07155) · [PDF](https://arxiv.org/pdf/2601.07155.pdf)  
**作者**：Ijun Jang, Jewon Yeom, Juan Yeo, Hyunggu Lim, Taesup Kim  

**一句话要点**：提出Veto方法以解决策略蒸馏中的训练不稳定问题

**关键词**：知识蒸馏, 策略蒸馏, 训练稳定性, 梯度优化, 语言模型压缩

## 3 点简述
- 核心问题：策略蒸馏因师生分布差距大导致训练不稳定，如梯度异常或多样性崩溃
- 方法要点：在logit空间构建几何桥，通过可调参数抑制有害梯度并平衡性能与多样性
- 实验或效果：在多种推理和生成任务中优于监督微调和现有策略基线

## 摘要（原文）

> Knowledge distillation (KD) is a widely adopted technique for transferring knowledge from large language models to smaller student models; however, conventional supervised KD often suffers from a distribution mismatch between training and inference. While on-policy KD approaches attempt to mitigate this issue by learning directly from student-generated outputs, they frequently encounter training instabilities because the distributional gap between the novice student and the expert teacher is often too wide to bridge directly. These challenges manifest as pathological gradients in forward KL objectives or diversity collapse in reverse KL regimes. To address these limitations, we propose Veto, an objective-level reformulation that constructs a geometric bridge in the logit space. Unlike prior methods that mix data samples, Veto creates an intermediate target distribution that promotes alignment between the teacher and the student. By introducing a tunable parameter beta, Veto serves as an Adaptive Gradient Veto that stabilizes optimization by suppressing harmful gradients on low-confidence tokens, while simultaneously acting as a Decisiveness Knob to balance reward-driven performance with output diversity. Extensive experiments across various reasoning and generation tasks demonstrate that Veto consistently outperforms supervised fine-tuning and existing on-policy baselines.

