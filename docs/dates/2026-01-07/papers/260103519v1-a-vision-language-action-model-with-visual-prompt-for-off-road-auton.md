---
layout: default
title: A Vision-Language-Action Model with Visual Prompt for OFF-Road Autonomous Driving
---

# A Vision-Language-Action Model with Visual Prompt for OFF-Road Autonomous Driving
**arXiv**：[2601.03519v1](https://arxiv.org/abs/2601.03519) · [PDF](https://arxiv.org/pdf/2601.03519.pdf)  
**作者**：Liangdong Zhang, Yiming Nie, Haoyang Li, Fanjie Kong, Baobao Zhang, Shunxin Huang, Kai Fu, Chen Min, Liang Xiao  

**一句话要点**：提出OFF-EMMA视觉-语言-动作模型，通过视觉提示和链式一致性推理提升越野自动驾驶轨迹规划性能。

**关键词**：越野自动驾驶, 视觉-语言-动作模型, 视觉提示, 链式一致性推理, 轨迹规划, 端到端框架

## 3 点简述
- 核心问题：越野环境中轨迹规划面临空间感知不足和推理不稳定的挑战，传统方法适应性有限。
- 方法要点：设计视觉提示块增强空间理解，引入链式一致性推理策略提高规划准确性和鲁棒性。
- 实验或效果：在RELLIS-3D数据集上显著优于现有方法，降低平均L2误差和失败率。

## 摘要（原文）

> Efficient trajectory planning in off-road terrains presents a formidable challenge for autonomous vehicles, often necessitating complex multi-step pipelines. However, traditional approaches exhibit limited adaptability in dynamic environments. To address these limitations, this paper proposes OFF-EMMA, a novel end-to-end multimodal framework designed to overcome the deficiencies of insufficient spatial perception and unstable reasoning in visual-language-action (VLA) models for off-road autonomous driving scenarios. The framework explicitly annotates input images through the design of a visual prompt block and introduces a chain-of-thought with self-consistency (COT-SC) reasoning strategy to enhance the accuracy and robustness of trajectory planning. The visual prompt block utilizes semantic segmentation masks as visual prompts, enhancing the spatial understanding ability of pre-trained visual-language models for complex terrains. The COT- SC strategy effectively mitigates the error impact of outliers on planning performance through a multi-path reasoning mechanism. Experimental results on the RELLIS-3D off-road dataset demonstrate that OFF-EMMA significantly outperforms existing methods, reducing the average L2 error of the Qwen backbone model by 13.3% and decreasing the failure rate from 16.52% to 6.56%.

