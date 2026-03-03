---
layout: default
title: Generative Visual Chain-of-Thought for Image Editing
---

# Generative Visual Chain-of-Thought for Image Editing
**arXiv**：[2603.01893v1](https://arxiv.org/abs/2603.01893) · [PDF](https://arxiv.org/pdf/2603.01893.pdf)  
**作者**：Zijin Yin, Tiankai Hang, Yiji Cheng, Shiyi Zhang, Runze He, Yu Xu, Chunyu Wang, Bing Li, Zheng Chang, Kongming Liang, Qinglin Lu, Zhanyu Ma  

**一句话要点**：提出生成式视觉思维链以解决复杂场景下图像编辑的定位难题

**关键词**：图像编辑, 视觉推理, 思维链, 端到端学习, 空间定位

## 3 点简述
- 现有方法在复杂场景和精细空间指令下难以感知编辑区域
- GVCoT通过端到端联合优化视觉令牌，生成空间线索定位并执行编辑
- 实验表明GVCoT在SREdit-Bench和ImgEdit上优于先进模型

## 摘要（原文）

> Existing image editing methods struggle to perceive where to edit, especially under complex scenes and nuanced spatial instructions. To address this issue, we propose Generative Visual Chain-of-Thought (GVCoT), a unified framework that performs native visual reasoning by first generating spatial cues to localize the target region and then executing the edit. Unlike prior text-only CoT or tool-dependent visual CoT paradigms, GVCoT jointly optimizes visual tokens generated during the reasoning and editing phases in an end-to-end manner. This way fosters the emergence of innate spatial reasoning ability and enables more effective utilization of visual-domain cues. The main challenge of training GCVoT lies in the scarcity of large-scale editing data with precise edit region annotations; to this end, we construct GVCoT-Edit-Instruct, a dataset of 1.8M high-quality samples spanning 19 tasks. We adopt a progressive training strategy: supervised fine-tuning to build foundational localization ability in reasoning trace before final editing, followed by reinforcement learning to further improve reasoning and editing quality. Finally, we introduce SREdit-Bench, a new benchmark designed to comprehensively stress-test models under sophisticated scenes and fine-grained referring expressions. Experiments demonstrate that GVCoT consistently outperforms state-of-the-art models on SREdit-Bench and ImgEdit. We hope our GVCoT will inspire future research toward interpretable and precise image editing.

