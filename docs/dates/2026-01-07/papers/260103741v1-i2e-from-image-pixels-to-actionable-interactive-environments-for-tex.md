---
layout: default
title: I2E: From Image Pixels to Actionable Interactive Environments for Text-Guided Image Editing
---

# I2E: From Image Pixels to Actionable Interactive Environments for Text-Guided Image Editing
**arXiv**：[2601.03741v1](https://arxiv.org/abs/2601.03741) · [PDF](https://arxiv.org/pdf/2601.03741.pdf)  
**作者**：Jinghan Yu, Junhao Xiao, Chenyu Zhu, Jiaming Li, Jia Li, HanMing Deng, Xirui Wang, Guoli Jia, Jianjun Li, Zhiyuan Ma, Xiang Bai, Bowen Zhou  

**一句话要点**：提出I2E范式以解决文本引导图像编辑中复杂组合任务的控制难题

**关键词**：文本引导图像编辑, 组合编辑, 对象层分解, 思维链推理, 物理感知代理, 多实例空间推理

## 3 点简述
- 现有方法在组合编辑任务中面临规划与执行耦合、对象级控制不足和像素中心建模的局限
- I2E采用分解-行动范式，将图像转换为可操作对象层，并通过思维链推理解析指令为原子动作
- 在I2E-Bench和公开基准上，I2E在复杂指令处理、物理合理性和多轮编辑稳定性方面显著优于现有方法

## 摘要（原文）

> Existing text-guided image editing methods primarily rely on end-to-end pixel-level inpainting paradigm. Despite its success in simple scenarios, this paradigm still significantly struggles with compositional editing tasks that require precise local control and complex multi-object spatial reasoning. This paradigm is severely limited by 1) the implicit coupling of planning and execution, 2) the lack of object-level control granularity, and 3) the reliance on unstructured, pixel-centric modeling. To address these limitations, we propose I2E, a novel "Decompose-then-Action" paradigm that revisits image editing as an actionable interaction process within a structured environment. I2E utilizes a Decomposer to transform unstructured images into discrete, manipulable object layers and then introduces a physics-aware Vision-Language-Action Agent to parse complex instructions into a series of atomic actions via Chain-of-Thought reasoning. Further, we also construct I2E-Bench, a benchmark designed for multi-instance spatial reasoning and high-precision editing. Experimental results on I2E-Bench and multiple public benchmarks demonstrate that I2E significantly outperforms state-of-the-art methods in handling complex compositional instructions, maintaining physical plausibility, and ensuring multi-turn editing stability.

