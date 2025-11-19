---
layout: default
title: Is Your VLM for Autonomous Driving Safety-Ready? A Comprehensive Benchmark for Evaluating External and In-Cabin Risks
---

# Is Your VLM for Autonomous Driving Safety-Ready? A Comprehensive Benchmark for Evaluating External and In-Cabin Risks
**arXiv**：[2511.14592v1](https://arxiv.org/abs/2511.14592) · [PDF](https://arxiv.org/pdf/2511.14592.pdf)  
**作者**：Xianhui Meng, Yuchen Zhang, Zhijian Huang, Zheng Lu, Ziling Ji, Yaoyao Yin, Hongyuan Zhang, Guangfeng Jiang, Yandan Lin, Long Chen, Hangjun Ye, Li Zhang, Jun Liu, Xiaoshuai Hao  

**一句话要点**：提出DSBench基准以评估自动驾驶中视觉语言模型的安全风险

**关键词**：自动驾驶安全, 视觉语言模型, 安全基准, 风险评估, 数据集构建

## 3 点简述
- 核心问题：缺乏评估自动驾驶中外部环境和车内行为安全的综合基准
- 方法要点：构建DSBench基准，涵盖10大类28子类安全风险场景
- 实验或效果：评估显示模型性能下降，微调后安全性能显著提升

## 摘要（原文）

> Vision-Language Models (VLMs) show great promise for autonomous driving, but their suitability for safety-critical scenarios is largely unexplored, raising safety concerns. This issue arises from the lack of comprehensive benchmarks that assess both external environmental risks and in-cabin driving behavior safety simultaneously. To bridge this critical gap, we introduce DSBench, the first comprehensive Driving Safety Benchmark designed to assess a VLM's awareness of various safety risks in a unified manner. DSBench encompasses two major categories: external environmental risks and in-cabin driving behavior safety, divided into 10 key categories and a total of 28 sub-categories. This comprehensive evaluation covers a wide range of scenarios, ensuring a thorough assessment of VLMs' performance in safety-critical contexts. Extensive evaluations across various mainstream open-source and closed-source VLMs reveal significant performance degradation under complex safety-critical situations, highlighting urgent safety concerns. To address this, we constructed a large dataset of 98K instances focused on in-cabin and external safety scenarios, showing that fine-tuning on this dataset significantly enhances the safety performance of existing VLMs and paves the way for advancing autonomous driving technology. The benchmark toolkit, code, and model checkpoints will be publicly accessible.

