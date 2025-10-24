---
layout: default
title: EchoDistill: Bidirectional Concept Distillation for One-Step Diffusion Personalization
---

# EchoDistill: Bidirectional Concept Distillation for One-Step Diffusion Personalization
**arXiv**：[2510.20512v1](https://arxiv.org/abs/2510.20512) · [PDF](https://arxiv.org/pdf/2510.20512.pdf)  
**作者**：Yixiong Yang, Tao Wu, Senmao Li, Shiqi Yang, Yaxing Wang, Joost van de Weijer, Kai Wang  

**一句话要点**：提出双向概念蒸馏框架以解决一步扩散模型个性化难题

**关键词**：扩散模型, 概念蒸馏, 一步生成, 模型个性化, 对抗训练, 双向优化

## 3 点简述
- 核心问题：一步扩散模型难以有效捕捉新概念分布，限制个性化能力。
- 方法要点：教师与学生模型双向蒸馏，共享文本编码器并优化对抗与对齐损失。
- 实验效果：在一步扩散个性化设置中显著优于现有方法，提升生成质量。

## 摘要（原文）

> Recent advances in accelerating text-to-image (T2I) diffusion models have
> enabled the synthesis of high-fidelity images even in a single step. However,
> personalizing these models to incorporate novel concepts remains a challenge
> due to the limited capacity of one-step models to capture new concept
> distributions effectively. We propose a bidirectional concept distillation
> framework, EchoDistill, to enable one-step diffusion personalization (1-SDP).
> Our approach involves an end-to-end training process where a multi-step
> diffusion model (teacher) and a one-step diffusion model (student) are trained
> simultaneously. The concept is first distilled from the teacher model to the
> student, and then echoed back from the student to the teacher. During the
> EchoDistill, we share the text encoder between the two models to ensure
> consistent semantic understanding. Following this, the student model is
> optimized with adversarial losses to align with the real image distribution and
> with alignment losses to maintain consistency with the teacher's output.
> Furthermore, we introduce the bidirectional echoing refinement strategy,
> wherein the student model leverages its faster generation capability to
> feedback to the teacher model. This bidirectional concept distillation
> mechanism not only enhances the student ability to personalize novel concepts
> but also improves the generative quality of the teacher model. Our experiments
> demonstrate that this collaborative framework significantly outperforms
> existing personalization methods over the 1-SDP setup, establishing a novel
> paradigm for rapid and effective personalization in T2I diffusion models.

