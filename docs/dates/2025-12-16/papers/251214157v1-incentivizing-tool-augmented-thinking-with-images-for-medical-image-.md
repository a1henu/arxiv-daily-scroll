---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
**arXiv**：[2512.14157v1](https://arxiv.org/abs/2512.14157) · [PDF](https://arxiv.org/pdf/2512.14157.pdf)  
**作者**：Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen  

**一句话要点**：提出Ophiuchus框架，通过工具增强推理解决医学图像分析中复杂任务的动态聚焦问题。

**关键词**：医学图像分析, 工具增强推理, 多模态思维链, 自反思微调, 强化学习, 视觉问答

## 3 点简述
- 核心问题：现有医学MLLMs在需要动态迭代聚焦细粒度视觉区域的任务中表现不足。
- 方法要点：采用三阶段训练策略，结合模型内在能力与外部工具，实现工具选择、自反思和强化学习。
- 实验或效果：在多个医学基准测试中优于现有SOTA方法，包括VQA、检测和基于推理的分割。

## 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

