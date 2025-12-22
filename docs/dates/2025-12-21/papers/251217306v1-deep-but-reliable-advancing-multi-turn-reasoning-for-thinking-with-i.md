---
layout: default
title: Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images
---

# Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images
**arXiv**：[2512.17306v1](https://arxiv.org/abs/2512.17306) · [PDF](https://arxiv.org/pdf/2512.17306.pdf)  
**作者**：Wenhao Yang, Yu Xia, Jinlong Huang, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Yuanyu Wan, Lijun Zhang  

**一句话要点**：提出DRIM模型以解决视觉语言模型在多轮图像推理中自我反思与修正的不足

**关键词**：多轮视觉推理, 自我反思机制, 冗余惩罚优化, 视觉语言模型, 工具调用, 策略学习

## 3 点简述
- 现有视觉语言模型在多轮图像推理中难以自我反思和修正错误轨迹
- 通过数据构建、冷启动监督微调和冗余惩罚策略优化三阶段训练，促进深度可靠推理
- 实验显示DRIM在视觉理解基准上实现优越性能

## 摘要（原文）

> Recent advances in large Vision-Language Models (VLMs) have exhibited strong reasoning capabilities on complex visual tasks by thinking with images in their Chain-of-Thought (CoT), which is achieved by actively invoking tools to analyze visual inputs rather than merely perceiving them. However, existing models often struggle to reflect on and correct themselves when attempting incorrect reasoning trajectories. To address this limitation, we propose DRIM, a model that enables deep but reliable multi-turn reasoning when thinking with images in its multimodal CoT. Our pipeline comprises three stages: data construction, cold-start SFT and RL. Based on a high-resolution image dataset, we construct high-difficulty and verifiable visual question-answer pairs, where solving each task requires multi-turn tool calls to reach the correct answer. In the SFT stage, we collect tool trajectories as cold-start data, guiding a multi-turn reasoning pattern. In the RL stage, we introduce redundancy-penalized policy optimization, which incentivizes the model to develop a self-reflective reasoning pattern. The basic idea is to impose judgment on reasoning trajectories and penalize those that produce incorrect answers without sufficient multi-scale exploration. Extensive experiments demonstrate that DRIM achieves superior performance on visual understanding benchmarks.

