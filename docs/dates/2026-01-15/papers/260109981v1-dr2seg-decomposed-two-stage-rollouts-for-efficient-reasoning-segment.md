---
layout: default
title: DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models
---

# DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models
**arXiv**：[2601.09981v1](https://arxiv.org/abs/2601.09981) · [PDF](https://arxiv.org/pdf/2601.09981.pdf)  
**作者**：Yulin He, Wei Chen, Zhikang Jian, Tianhang Guo, Wenjuan Zhou, Minglong Li  

**一句话要点**：提出DR²Seg框架，通过分解两阶段推理提升多模态大语言模型中的推理分割效率与准确性。

**关键词**：推理分割, 多模态大语言模型, 两阶段推理, 自奖励框架, 对象定位

## 3 点简述
- 核心问题：现有方法在推理分割中因过度思考生成冗长推理链，干扰对象定位。
- 方法要点：采用两阶段策略，首阶段生成自包含描述，次阶段验证描述以抑制冗余推理。
- 实验或效果：在多种规模MLLMs和分割模型上验证，提升推理效率和分割性能。

## 摘要（原文）

> Reasoning segmentation is an emerging vision-language task that requires reasoning over intricate text queries to precisely segment objects. However, existing methods typically suffer from overthinking, generating verbose reasoning chains that interfere with object localization in multimodal large language models (MLLMs). To address this issue, we propose DR$^2$Seg, a self-rewarding framework that improves both reasoning efficiency and segmentation accuracy without requiring extra thinking supervision. DR$^2$Seg employs a two-stage rollout strategy that decomposes reasoning segmentation into multimodal reasoning and referring segmentation. In the first stage, the model generates a self-contained description that explicitly specifies the target object. In the second stage, this description replaces the original complex query to verify its self-containment. Based on this design, two self-rewards are introduced to strengthen goal-oriented reasoning and suppress redundant thinking. Extensive experiments across MLLMs of varying scales and segmentation models demonstrate that DR$^2$Seg consistently improves reasoning efficiency and overall segmentation performance.

