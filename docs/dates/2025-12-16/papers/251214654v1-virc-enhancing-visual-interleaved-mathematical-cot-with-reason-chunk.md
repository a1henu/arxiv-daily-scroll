---
layout: default
title: ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking
---

# ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking
**arXiv**：[2512.14654v1](https://arxiv.org/abs/2512.14654) · [PDF](https://arxiv.org/pdf/2512.14654.pdf)  
**作者**：Lihong Wang, Liangqi Li, Weiwei Feng, Jiamin Wu, Changtao Miao, Tieru Wu, Rui Ma, Bo Zhang, Zhe Li  

**一句话要点**：提出ViRC框架，通过Reason Chunking机制增强多模态数学任务中的视觉交错推理能力。

**关键词**：多模态推理, 数学任务, Reason Chunking, Critical Reasoning Units, 渐进训练, 视觉交错

## 3 点简述
- 核心问题：现有MLLMs在数学任务中依赖静态图像，缺乏动态视觉获取和结构化推理，导致多模态推理能力受限。
- 方法要点：引入Reason Chunking机制，将推理过程分解为Critical Reasoning Units，模拟人类逐步验证命题和整合视觉信息的模式。
- 实验或效果：基于CRUX数据集进行渐进训练，ViRC-7B模型在多个数学基准上平均提升18.8%，代码已开源。

## 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

