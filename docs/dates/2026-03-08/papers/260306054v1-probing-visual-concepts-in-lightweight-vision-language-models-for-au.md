---
layout: default
title: Probing Visual Concepts in Lightweight Vision-Language Models for Automated Driving
---

# Probing Visual Concepts in Lightweight Vision-Language Models for Automated Driving
**arXiv**：[2603.06054v1](https://arxiv.org/abs/2603.06054) · [PDF](https://arxiv.org/pdf/2603.06054.pdf)  
**作者**：Nikos Theodoridis, Reenu Mohandas, Ganesh Sistu, Anthony Scanlan, Ciarán Eising, Tim Brophy  

**一句话要点**：探究轻量级视觉语言模型在自动驾驶中的视觉概念编码，识别感知与认知失败模式

**关键词**：视觉语言模型, 自动驾驶, 线性探针, 视觉概念编码, 失败模式分析

## 3 点简述
- 核心问题：视觉语言模型在自动驾驶相关简单视觉任务中失败原因不明，需理解视觉信息流动瓶颈
- 方法要点：通过反事实图像集和线性探针分析模型激活，评估视觉概念的线性编码程度
- 实验或效果：发现对象存在等概念线性编码，而方向等空间概念仅隐式编码，并识别感知与认知失败模式

## 摘要（原文）

> The use of Vision-Language Models (VLMs) in automated driving applications is becoming increasingly common, with the aim of leveraging their reasoning and generalisation capabilities to handle long tail scenarios. However, these models often fail on simple visual questions that are highly relevant to automated driving, and the reasons behind these failures remain poorly understood. In this work, we examine the intermediate activations of VLMs and assess the extent to which specific visual concepts are linearly encoded, with the goal of identifying bottlenecks in the flow of visual information. Specifically, we create counterfactual image sets that differ only in a targeted visual concept and then train linear probes to distinguish between them using the activations of four state-of-the-art (SOTA) VLMs. Our results show that concepts such as the presence of an object or agent in a scene are explicitly and linearly encoded, whereas other spatial visual concepts, such as the orientation of an object or agent, are only implicitly encoded by the spatial structure retained by the vision encoder. In parallel, we observe that in certain cases, even when a concept is linearly encoded in the model's activations, the model still fails to answer correctly. This leads us to identify two failure modes. The first is perceptual failure, where the visual information required to answer a question is not linearly encoded in the model's activations. The second is cognitive failure, where the visual information is present but the model fails to align it correctly with language semantics. Finally, we show that increasing the distance of the object in question quickly degrades the linear separability of the corresponding visual concept. Overall, our findings improve our understanding of failure cases in VLMs on simple visual tasks that are highly relevant to automated driving.

