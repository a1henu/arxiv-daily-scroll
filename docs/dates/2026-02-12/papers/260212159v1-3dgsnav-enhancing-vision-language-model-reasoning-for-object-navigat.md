---
layout: default
title: 3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting
---

# 3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting
**arXiv**：[2602.12159v1](https://arxiv.org/abs/2602.12159) · [PDF](https://arxiv.org/pdf/2602.12159.pdf)  
**作者**：Wancai Zheng, Hao Chen, Xianlong Lu, Linlin Ou, Xinyi Yu  

**一句话要点**：提出3DGSNav框架，通过主动3D高斯溅射增强视觉语言模型在物体导航中的空间推理能力。

**关键词**：物体导航, 视觉语言模型, 3D高斯溅射, 主动感知, 零样本学习, 空间推理

## 3 点简述
- 现有零样本物体导航方法依赖场景抽象，导致高层决策受低层感知精度限制。
- 3DGSNav利用3D高斯溅射作为持久记忆，结合主动感知和结构化视觉提示提升模型推理。
- 在多个基准测试和四足机器人实验中，该方法展现出稳健且具竞争力的性能。

## 摘要（原文）

> Object navigation is a core capability of embodied intelligence, enabling an agent to locate target objects in unknown environments. Recent advances in vision-language models (VLMs) have facilitated zero-shot object navigation (ZSON). However, existing methods often rely on scene abstractions that convert environments into semantic maps or textual representations, causing high-level decision making to be constrained by the accuracy of low-level perception. In this work, we present 3DGSNav, a novel ZSON framework that embeds 3D Gaussian Splatting (3DGS) as persistent memory for VLMs to enhance spatial reasoning. Through active perception, 3DGSNav incrementally constructs a 3DGS representation of the environment, enabling trajectory-guided free-viewpoint rendering of frontier-aware first-person views. Moreover, we design structured visual prompts and integrate them with Chain-of-Thought (CoT) prompting to further improve VLM reasoning. During navigation, a real-time object detector filters potential targets, while VLM-driven active viewpoint switching performs target re-verification, ensuring efficient and reliable recognition. Extensive evaluations across multiple benchmarks and real-world experiments on a quadruped robot demonstrate that our method achieves robust and competitive performance against state-of-the-art approaches.The Project Page:https://aczheng-cai.github.io/3dgsnav.github.io/

