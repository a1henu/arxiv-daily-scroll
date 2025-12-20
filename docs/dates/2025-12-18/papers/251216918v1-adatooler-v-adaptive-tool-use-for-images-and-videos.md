---
layout: default
title: AdaTooler-V: Adaptive Tool-Use for Images and Videos
---

# AdaTooler-V: Adaptive Tool-Use for Images and Videos
**arXiv**：[2512.16918v1](https://arxiv.org/abs/2512.16918) · [PDF](https://arxiv.org/pdf/2512.16918.pdf)  
**作者**：Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue  

**一句话要点**：提出AdaTooler-V以解决多模态大语言模型盲目调用视觉工具的问题

**关键词**：自适应工具调用, 多模态大语言模型, 强化学习, 视觉推理, 工具效益评估

## 3 点简述
- 现有开源模型在视觉推理中常盲目调用工具，增加开销并降低性能
- 引入AT-GRPO强化学习算法，基于工具效益分数自适应调整奖励，鼓励仅在必要时调用工具
- 在十二个基准测试中表现优异，AdaTooler-V-7B在V*基准上准确率达89.8%，超越GPT-4o和Gemini 1.5 Pro

## 摘要（原文）

> Recent advances have shown that multimodal large language models (MLLMs) benefit from multimodal interleaved chain-of-thought (CoT) with vision tool interactions. However, existing open-source models often exhibit blind tool-use reasoning patterns, invoking vision tools even when they are unnecessary, which significantly increases inference overhead and degrades model performance. To this end, we propose AdaTooler-V, an MLLM that performs adaptive tool-use by determining whether a visual problem truly requires tools. First, we introduce AT-GRPO, a reinforcement learning algorithm that adaptively adjusts reward scales based on the Tool Benefit Score of each sample, encouraging the model to invoke tools only when they provide genuine improvements. Moreover, we construct two datasets to support training: AdaTooler-V-CoT-100k for SFT cold start and AdaTooler-V-300k for RL with verifiable rewards across single-image, multi-image, and video data. Experiments across twelve benchmarks demonstrate the strong reasoning capability of AdaTooler-V, outperforming existing methods in diverse visual reasoning tasks. Notably, AdaTooler-V-7B achieves an accuracy of 89.8\% on the high-resolution benchmark V*, surpassing the commercial proprietary model GPT-4o and Gemini 1.5 Pro. All code, models, and data are released.

