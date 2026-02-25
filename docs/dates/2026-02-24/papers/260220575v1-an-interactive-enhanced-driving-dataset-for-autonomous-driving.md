---
layout: default
title: An interactive enhanced driving dataset for autonomous driving
---

# An interactive enhanced driving dataset for autonomous driving
**arXiv**：[2602.20575v1](https://arxiv.org/abs/2602.20575) · [PDF](https://arxiv.org/pdf/2602.20575.pdf)  
**作者**：Haojie Feng, Peizhi Zhang, Mengjie Tian, Xinrui Zhang, Zhuoren Li, Junpeng Huang, Xiurong Wang, Junfan Zhu, Jianzhou Wang, Dongxiao Yin, Lu Xiong  

**一句话要点**：提出交互增强驾驶数据集以解决自动驾驶中交互场景稀疏和多模态对齐不足的问题

**关键词**：自动驾驶数据集, 交互场景挖掘, 多模态对齐, 视觉语言模型评估, 鸟瞰视频合成, 推理能力微调

## 3 点简述
- 核心问题：自动驾驶全自动化需强交互能力，但现有数据交互场景稀疏且多模态对齐不足
- 方法要点：基于交互轨迹从自然驾驶数据挖掘百万级交互片段，并构建合成鸟瞰视频严格对齐语义动作与结构化语言
- 实验或效果：提供基准测试评估十种主流视觉语言模型，展示数据集在评估和微调自动驾驶模型推理能力中的重用价值

## 摘要（原文）

> The evolution of autonomous driving towards full automation demands robust interactive capabilities; however, the development of Vision-Language-Action (VLA) models is constrained by the sparsity of interactive scenarios and inadequate multimodal alignment in existing data. To this end, this paper proposes the Interactive Enhanced Driving Dataset (IEDD). We develop a scalable pipeline to mine million-level interactive segments from naturalistic driving data based on interactive trajectories, and design metrics to quantify the interaction processes. Furthermore, the IEDD-VQA dataset is constructed by generating synthetic Bird's Eye View (BEV) videos where semantic actions are strictly aligned with structured language. Benchmark results evaluating ten mainstream Vision Language Models (VLMs) are provided to demonstrate the dataset's reuse value in assessing and fine-tuning the reasoning capabilities of autonomous driving models.

