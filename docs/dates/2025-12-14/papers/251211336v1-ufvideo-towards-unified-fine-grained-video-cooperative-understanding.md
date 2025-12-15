---
layout: default
title: UFVideo: Towards Unified Fine-Grained Video Cooperative Understanding with Large Language Models
---

# UFVideo: Towards Unified Fine-Grained Video Cooperative Understanding with Large Language Models
**arXiv**：[2512.11336v1](https://arxiv.org/abs/2512.11336) · [PDF](https://arxiv.org/pdf/2512.11336.pdf)  
**作者**：Hewen Pan, Cong Wei, Dashuang Liang, Zepeng Huang, Pengfei Gao, Ziqi Zhou, Lulu Xue, Pengfei Yan, Xiaoming Wei, Minghui Li, Shengshan Hu  

**一句话要点**：提出UFVideo，首个统一多粒度协同理解的视频大语言模型，以解决现有模型局限于专项任务的问题。

**关键词**：视频大语言模型, 多粒度协同理解, 统一视觉-语言对齐, 视频理解基准, 时间定位, 掩码生成

## 3 点简述
- 现有视频大语言模型局限于专项理解任务，缺乏全面多粒度感知能力。
- 设计统一视觉-语言引导对齐方法，在单一模型中灵活处理全局、像素和时间尺度视频理解。
- 构建UFVideo-Bench评估多粒度协同任务，并在9个公共基准上验证模型有效性，优于GPT-4o。

## 摘要（原文）

> With the advancement of multi-modal Large Language Models (LLMs), Video LLMs have been further developed to perform on holistic and specialized video understanding. However, existing works are limited to specialized video understanding tasks, failing to achieve a comprehensive and multi-grained video perception. To bridge this gap, we introduce UFVideo, the first Video LLM with unified multi-grained cooperative understanding capabilities. Specifically, we design unified visual-language guided alignment to flexibly handle video understanding across global, pixel and temporal scales within a single model. UFVideo dynamically encodes the visual and text inputs of different tasks and generates the textual response, temporal localization, or grounded mask. Additionally, to evaluate challenging multi-grained video understanding tasks, we construct the UFVideo-Bench consisting of three distinct collaborative tasks within the scales, which demonstrates UFVideo's flexibility and advantages over GPT-4o. Furthermore, we validate the effectiveness of our model across 9 public benchmarks covering various common video understanding tasks, providing valuable insights for future Video LLMs.

