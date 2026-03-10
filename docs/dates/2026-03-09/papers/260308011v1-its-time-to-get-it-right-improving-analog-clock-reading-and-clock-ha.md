---
layout: default
title: It's Time to Get It Right: Improving Analog Clock Reading and Clock-Hand Spatial Reasoning in Vision-Language Models
---

# It's Time to Get It Right: Improving Analog Clock Reading and Clock-Hand Spatial Reasoning in Vision-Language Models
**arXiv**：[2603.08011v1](https://arxiv.org/abs/2603.08011) · [PDF](https://arxiv.org/pdf/2603.08011.pdf)  
**作者**：Jaeha Choi, Jin Won Lee, Siwoo You, Jangho Lee  

**一句话要点**：提出TickTockVQA数据集与Swap-DPO框架以提升视觉语言模型在真实场景中的模拟时钟读取能力

**关键词**：模拟时钟读取, 视觉语言模型, 时空推理, 数据集构建, 直接偏好优化, 真实场景理解

## 3 点简述
- 现有模拟时钟数据集多为合成或平面数据，缺乏真实场景多样性，导致视觉语言模型在时钟读取中时空推理能力弱
- 引入TickTockVQA数据集，包含多样真实场景模拟时钟，提供小时和分钟标注及可推断的AM/PM标签
- 提出Swap-DPO基于直接偏好优化的微调框架，实验显示该方法显著提高时钟读取准确性和鲁棒性

## 摘要（原文）

> Advances in vision-language models (VLMs) have achieved remarkable success on complex multimodal reasoning tasks, leading to the assumption that they should also excel at reading analog clocks. However, contrary to this expectation, our study reveals that reading analog clocks in real-world environments remains a significant challenge for state-of-the-art VLMs. Existing analog clock datasets are largely synthetic or planar with limited stylistic diversity and minimal background context, failing to capture the visual variability of real-world scenes. As a result, VLMs trained on such data exhibit weak spatial-temporal reasoning, frequently confusing the hour and minute hands and struggling under common visual conditions such as occlusion, lighting variation, and cluttered backgrounds. To address this issue, we introduce TickTockVQA, a human-annotated dataset containing analog clocks in diverse real-world scenarios. TickTockVQA provides explicit hour and minute annotations, and includes an AM/PM tag when it is inferable from the visual context. Furthermore, we propose Swap-DPO, a direct preference optimization based fine-tuning framework to align model reasoning toward accurate time interpretation. Experimental results demonstrate that our approach substantially enhances clock reading accuracy and robustness under real-world conditions, establishing a foundation for future research on spatial-temporal reasoning and visual understanding in VLMs.

