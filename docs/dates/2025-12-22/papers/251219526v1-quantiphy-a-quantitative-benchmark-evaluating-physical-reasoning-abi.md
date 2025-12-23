---
layout: default
title: QuantiPhy: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models
---

# QuantiPhy: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models
**arXiv**：[2512.19526v1](https://arxiv.org/abs/2512.19526) · [PDF](https://arxiv.org/pdf/2512.19526.pdf)  
**作者**：Li Puyin, Tiange Xiang, Ella Mao, Shirley Wei, Xinye Chen, Adnan Masood, Li Fei-fei, Ehsan Adeli  

**一句话要点**：提出QuantiPhy基准以定量评估视觉语言模型的物理推理能力

**关键词**：物理推理评估, 定量基准, 视觉语言模型, 运动物体属性, 数值准确性

## 3 点简述
- 现有评估多为定性VQA，缺乏对模型定量推理运动物体属性的能力测试
- QuantiPhy包含3.3K视频文本实例，标准化提示和评分以评估数值准确性
- 实验显示先进模型依赖预训练知识而非输入参考，存在数值正确性差距

## 摘要（原文）

> Understanding the physical world is essential for generalist AI agents. However, it remains unclear whether state-of-the-art vision perception models (e.g., large VLMs) can reason physical properties quantitatively. Existing evaluations are predominantly VQA-based and qualitative, offering limited insight into whether these models can infer the kinematic quantities of moving objects from video observations. To address this, we present QuantiPhy, the first benchmark designed to quantitatively measure a VLM's physical reasoning ability. Comprising more than 3.3K video-text instances with numerical ground truth, QuantiPhy evaluates a VLM's performance on estimating an object's size, velocity, and acceleration at a given timestamp, using one of these properties as an input prior. The benchmark standardizes prompts and scoring to assess numerical accuracy, enabling fair comparisons across models. Our experiments on state-of-the-art VLMs reveal a consistent gap between their qualitative plausibility and actual numerical correctness. We further provide an in-depth analysis of key factors like background noise, counterfactual priors, and strategic prompting and find that state-of-the-art VLMs lean heavily on pre-trained world knowledge rather than faithfully using the provided visual and textual inputs as references when reasoning kinematic properties quantitatively. QuantiPhy offers the first rigorous, scalable testbed to move VLMs beyond mere verbal plausibility toward a numerically grounded physical understanding.

