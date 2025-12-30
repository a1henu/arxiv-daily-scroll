---
layout: default
title: MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?
---

# MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?
**arXiv**：[2512.23219v1](https://arxiv.org/abs/2512.23219) · [PDF](https://arxiv.org/pdf/2512.23219.pdf)  
**作者**：Shiqi Dai, Zizhi Ma, Zhicong Luo, Xuesong Yang, Yibin Huang, Wanyue Zhang, Chi Chen, Zonghao Guo, Wang Xu, Yufei Sun, Maosong Sun  

**一句话要点**：提出MM-UAVBench基准，系统评估多模态大语言模型在低空无人机场景下的感知、认知与规划能力。

**关键词**：多模态大语言模型, 无人机场景, 基准评估, 感知认知规划, 低空智能

## 3 点简述
- 核心问题：现有MLLM基准未覆盖低空无人机场景的独特挑战，缺乏对MLLM通用智能的统一评估。
- 方法要点：构建包含19个子任务、超5.7K人工标注问题的基准，基于真实无人机数据，涵盖感知、认知和规划三个维度。
- 实验或效果：在16个开源和专有MLLM上实验，发现模型难以适应低空场景的复杂视觉和认知需求，识别出空间偏见和多视角理解等瓶颈。

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have exhibited remarkable general intelligence across diverse domains, their potential in low-altitude applications dominated by Unmanned Aerial Vehicles (UAVs) remains largely underexplored. Existing MLLM benchmarks rarely cover the unique challenges of low-altitude scenarios, while UAV-related evaluations mainly focus on specific tasks such as localization or navigation, without a unified evaluation of MLLMs'general intelligence. To bridge this gap, we present MM-UAVBench, a comprehensive benchmark that systematically evaluates MLLMs across three core capability dimensions-perception, cognition, and planning-in low-altitude UAV scenarios. MM-UAVBench comprises 19 sub-tasks with over 5.7K manually annotated questions, all derived from real-world UAV data collected from public datasets. Extensive experiments on 16 open-source and proprietary MLLMs reveal that current models struggle to adapt to the complex visual and cognitive demands of low-altitude scenarios. Our analyses further uncover critical bottlenecks such as spatial bias and multi-view understanding that hinder the effective deployment of MLLMs in UAV scenarios. We hope MM-UAVBench will foster future research on robust and reliable MLLMs for real-world UAV intelligence.

