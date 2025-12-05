---
layout: default
title: Visual Reasoning Tracer: Object-Level Grounded Reasoning Benchmark
---

# Visual Reasoning Tracer: Object-Level Grounded Reasoning Benchmark
**arXiv**：[2512.05091v1](https://arxiv.org/abs/2512.05091) · [PDF](https://arxiv.org/pdf/2512.05091.pdf)  
**作者**：Haobo Yuan, Yueyi Sun, Yanwei Li, Tao Zhang, Xueqing Deng, Henghui Ding, Lu Qi, Anran Wang, Xiangtai Li, Ming-Hsuan Yang  

**一句话要点**：提出Visual Reasoning Tracer任务与基准，以解决多模态大语言模型推理过程不透明的问题。

**关键词**：视觉推理, 多模态大语言模型, 基准评测, 数据集构建, 对象级定位

## 3 点简述
- 核心问题：多模态大语言模型推理过程不透明，缺乏中间步骤和细粒度证据。
- 方法要点：引入VRT任务，要求模型定位目标对象并预测中间推理路径对象。
- 实验或效果：基于VRT-80k数据集训练的模型在推理路径追踪上显著提升。

## 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have significantly improved performance on tasks such as visual grounding and visual question answering. However, the reasoning processes of these models remain largely opaque; they typically output only final predictions without revealing the intermediate steps or fine-grained evidence (e.g., pixels, locations) that lead to the result. This contrasts with human intelligence, which naturally operates through a chain of visual reasoning. To address this limitation, we introduce the Visual Reasoning Tracer (VRT) task, which requires models to not only localize the target object but also explicitly predict the intermediate objects that form the reasoning path. To advance research in this area, we contribute: (1) VRT-Bench, a human-annotated benchmark for evaluating visual reasoning; (2) a new metric for assessing the quality of reasoning traces; and (3) VRT-80k, a large-scale dataset for reasoning model training. Our experiments reveal that while existing models often produce the correct final output, they struggle to ground their intermediate reasoning. In contrast, models trained on VRT-80k achieve substantial improvements in tracing the reasoning path.

